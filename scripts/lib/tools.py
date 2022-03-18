import string
import re
import requests
import json

from lib.rules import cconj, relation_NP, relation_IP, relation_CP, abbr_map
from lib.reader import IndexedCorpusTree


def determine_relations(mod_tag, mod_func, head_tag, head_func, node):

    if mod_tag == "S":
        if mod_func in {"MAIN", "QUE", "HEADING"} and head_tag == "S0":
            return "conj"
        elif mod_func == "PREFIX":
            if "(st " in str(node):
                return "cc"
            return "VANTAR_LIÐ_S_PREFIX"  # TODO
        elif mod_func == "HEADING":
            return "VANTAR_LIÐ_S_HEADING"  # TODO
        elif mod_func == "EXPLAIN" and head_tag == "NP" and head_func == "OBJ":
            return "acl"
        elif mod_func == "EXPLAIN" and head_tag == "S0":  # interjected clauses
            return "parataxis"
    elif mod_tag == "NP":
        return relation_NP.get(mod_func, "VANTAR_LIÐ")
    elif mod_tag in {
        "no",
        "person",
        "sérnafn",
        "entity",
        "fyrirtæki",
        "gata",
    } and head_tag in {
        "NP",
        "ADJP",
        "PP",
    }:  # seinna no. í nafnlið fær 'conj' og er háð fyrra no.
        return "conj"
    # elif head_tag == "ADJP":
    #    return "amod"
    # elif mod_tag == "ES":      # ATH. hvernig eru leppir merktir í GC?
    #    return "expl"  # expletive
    elif mod_tag in {"fn", "abfn", "pfn"}:
        return "nmod"
    elif mod_tag == "gr":  # áður: "D", "WD", "ONE", "ONES", "OTHER", "OTHERS", "SUCH"
        return "det"
    elif mod_tag in {"ADJP", "lo", "raðnr"}:
        return "amod"
    elif mod_tag in {"PP", "no"}:
        # -DIR, -LOC
        return "obl"  # NP sem er haus PP fær obl nominal  #TODO: haus CP-ADV (sem er PP) á að vera merktur advcl
    elif mod_tag in {"P", "fs"}:
        return "case"
    elif mod_tag == "ADVP" and mod_func == "PCL":
        return "compound:prt"
    elif mod_tag in {"ao", "eo", "ADVP", "abbrev"}:
        return "advmod"
    if mod_tag == "IP":
        if head_tag == "CP" and head_func == "REL":
            return "acl:relcl"
        if mod_func is None:
            if head_tag in {"S", "S0", "CP"} and head_func in {
                "MAIN",
                "X",
                "QUOTE",
                "SOURCE",
            }:
                return "conj"
            elif head_tag == "CP":
                if head_func in {"THT-OBJ", "QUE", "QUE-SUBJ"}:
                    return "ccomp/xcomp"
                elif head_func == "ADV-TEMP":
                    return "advcl"
            elif "_nh_" in str(node) and head_tag == "VP" and head_func is None:
                return "ccomp/xcomp"
        return relation_IP.get(mod_func, "VANTAR_LIÐ")
    if mod_tag == "VP":
        if head_tag == "VP" and head_func == "AUX":
            return "aux"
        elif mod_func == "AUX":
            return "aux"
        elif mod_func is None:
            if (
                "+lemma+vera" in str(node)
                or "+lemma+er" in str(node)
                or "+lemma+verða" in str(node)
                or "+lemma+mæla" in str(node)
                or "+lemma+þykja" in str(node)
                and head_tag == "VP"
                and head_func is None
            ):
                return "cop"  # copula, the phrase's head is a predicate
            elif (
                mod_func is None
                and head_tag in {"IP"}
                and head_func in {None, "INF", "INF-OBJ"}
            ):
                return "conj"
            elif head_tag == "VP" and head_func is None:
                # and "so_0 " in str(node)
                # or "_sagnb_" in str(node):
                return "conj"
            elif "_nh_" in str(node) and head_tag == "VP" and head_func is None:
                return "ccomp/xcomp"
            elif "lhþt" in str(node) and head_tag == "VP" and head_func is None:
                return "ccomp/xcomp"
            elif head_tag == "PP":
                return "case??"  # TODO
        return "VANTAR_LIÐ_VP_None"
    elif mod_tag == "so":
        if head_tag == "CP":
            return "ccomp"
        elif (
            mod_func is not None
            and "_lhnt" in mod_func
            and head_tag == "NP"
            and head_func is None
        ):
            return "amod"
    # elif head_tag == "IP" and head_func == "INF-PRP":  # ??
    #    return "advcl"
    elif (
        head_tag == "NP" and mod_tag is not None and "lhþt" in mod_tag
    ):  # passive participle
        return "HALLÓ_LHÞT"  # Á ekki við um neitt í testset
    elif mod_tag is not None and "lhþt" in mod_tag:
        return "ccomp/xcomp"  # Á ekki við um neitt í testset eða devset    # TODO, taka út ef kemur ekki fyrir
    # elif mod_tag in [
    #    "VAN",
    #    "DAN",
    #    "HAN",
    #    "BAN",
    #    "RAN",
    # ]:  # passive participle
    #    return "VAN_DAN_HAN"
    #    return "aux"       # á líklega bara við um IcePaHC
    elif mod_func is not None and "lhþt" in mod_func:
        if head_func and "=" in head_func:  # TODO: ??
            return "conj"
        else:
            return "VANTAR_LIÐ_" + mod_tag + mod_func
    elif head_tag == "VP" and head_func == "AUX":  # TODO: ??
        return "aux"
    # elif (
    #    mod_tag[:2] == "BE" or mod_tag == "BAN"
    # ):  # ATH. cop ekki merkt sérstaklega í GC - hvernig á að höndla cop?
    #    return "BAN_BAN"
    #    return "cop"  # á líklega bara við um IcePaHC
    elif (
        mod_func is not None and "_lh_" in mod_func
    ):  # á bara að vera lh.nt., er þetta rétt?     # TODO
        return "amod"
    elif mod_tag == "CP" and mod_func == "REL" and head_tag == "ADVP":
        return "advcl"
    elif mod_tag == "CP":
        return relation_CP.get(mod_func, "VANTAR_LIÐ")
    elif mod_tag == "st":
        return "cc"
    elif mod_tag in {
        "C",
        "CP",
        "TO",
    }:  # infinitival marker with marker relation
        if (
            "st og+lemma+og" in str(node)
            or "st eða+lemma+eða" in str(node)
            or "st en+lemma+en" in str(node)
            or "st heldur+lemma+heldur" in str(node)
            or "st enda+lemma+enda" in str(node)
            or "st ellegar+lemma+ellegar" in str(node)
            or "st bæði+lemma+bæði" in str(node)
            or "st hvorki+lemma+hvorki" in str(node)
            or "st annaðhvort+lemma+annaðhvort" in str(node)
            or "st hvort+lemma+hvort" in str(node)
            or "st ýmist+lemma+ýmist" in str(node)
        ):  # coordinating conjunction
            return "cc"
        return "mark"
    elif mod_tag in {"stt", "nhm"}:
        return "mark"
    elif mod_tag in {"to", "töl", "tala", "tími", "ártal", "prósenta"}:
        return "nummod"
    elif mod_tag in string.punctuation or mod_tag == "grm":
        return "punct"
    elif (
        mod_tag == "abbrev"
        and head_tag == "NP"
        or head_tag == "CP"
        and head_func == "EXPLAIN"
    ):
        return "flat:name"
    elif mod_tag in {"foreign", "FOREIGN"} or head_tag == "foreign":
        return "flat:foreign"
    elif mod_tag == "uh":
        return "discourse"
    elif mod_tag == "x":
        return "dep"  # the token could not be analyzed, leads to unknown dependency

    return "HALLÓ_" + mod_tag, mod_func, head_tag, head_func  # "VANTAR_LIÐ"


def decode_escaped(string, lemma=False):
    """
    Fixes various punctuations (-, /, ') that are escaped in corpus data
    Also fixes most abbrevations in corpus data using abbrevations rules dictionar
    """
    if re.search(r"[<>]", string):
        """Tokens processed"""
        if re.search(r"</?dash/?>", string):
            string = re.sub(r"</?dash/?>", "-", string)
        if re.search(r"</?slash/?>", string):
            string = re.sub(r"</?slash/?>", "/", string)
        if re.search(r"</?apostrophe/?>", string):
            string = re.sub(r"</?apostrophe/?>", "'", string)
        return string
    if string in abbr_map.keys():
        string = re.sub(abbr_map[string][0], abbr_map[string][1], string)

        return string
    else:
        return string

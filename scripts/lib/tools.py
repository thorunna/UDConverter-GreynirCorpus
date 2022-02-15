import string
import re
import requests
import json

from lib.rules import relation_NP, relation_IP, relation_CP, abbr_map
from lib.reader import IndexedCorpusTree


def determine_relations(mod_tag, mod_func, head_tag, head_func):

    if mod_tag == "NP":
        # return mod_tag, mod_func, head_tag, head_func
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
    elif head_tag == "ADJP":
        return "amod"
    # elif mod_tag == "ES":      # ATH. hvernig eru leppir merktir í GC?
    #    return "expl"  # expletive
    elif mod_tag in {"fn", "abfn", "pfn"}:
        return "nmod"
    elif mod_tag == "gr":  # áður: "D", "WD", "ONE", "ONES", "OTHER", "OTHERS", "SUCH"
        return "det"
    elif mod_tag == "lo":
        return "amod"
    elif mod_tag == "PP":
        # -BY, -PRN
        return "obl"  # NP sem er haus PP fær obl nominal  #TODO: haus CP-ADV (sem er PP) á að vera merktur advcl
    elif mod_tag in {"P", "fs"}:
        return "case"
    elif mod_tag == "ADVP" and mod_func == "PCL":
        return "compound:prt"
    elif mod_tag in {
        "ao",
        "eo",
        "ADVP",
    }:
        return "advmod"
    elif mod_tag == "IP" and head_tag == "CP" and head_func == "REL":
        return "acl:relcl"
    elif mod_tag in ["IP", "VP"]:
        return relation_IP.get(mod_func, "VANTAR_LIÐ")
    elif mod_tag == "so" and head_tag == "CP":
        return "ccomp"
    # elif head_tag == "IP" and head_func == "INF-PRP":  # ??
    #    return "advcl"
    elif head_tag == "NP" and mod_tag == "VAN":  # passive participle
        return "amod"
    elif mod_tag in {"VAN", "DAN"} or mod_tag[:2] == "DO":
        return "ccomp/xcomp"
    elif mod_tag in ["VAN", "DAN", "HAN", "BAN", "RAN"]:  # passive participle
        return "aux"
    elif mod_func is not None and "lhþt" in mod_func:
        if head_func and "=" in head_func:
            return "conj"
        else:
            return "VANTAR_LIÐ"
    # elif mod_tag[:2] in ['VB', 'DO', 'HV', 'RD', 'MD']: #todo
    elif head_tag == "VP" and head_func == "AUX":
        return "aux"
    elif (
        mod_tag[:2] == "BE" or mod_tag == "BAN"
    ):  # ATH. cop ekki merkt sérstaklega í GC - hvernig á að höndla cop?
        return "cop"
    elif (
        mod_func is not None and "_lh_" in mod_func
    ):  # á bara að vera lh.nt., er þetta rétt?
        return "amod"
    elif mod_tag == "st":
        return "cc"
    # elif mod_tag == "CONJP" and head_tag == "IP":
    #    return relation_IP.get(head_func, "VANTAR_LIÐ")
    # elif mod_tag == "CONJP":
    #    return "conj"
    elif mod_tag == "CP" and mod_func == "REL" and head_tag == "ADVP":
        return "advcl"
    elif mod_tag == "CP":
        return relation_CP.get(mod_func, "VANTAR_LIÐ")
    elif mod_tag in {
        "C",
        "CP",
        "TO",
    }:  # infinitival marker with marker relation   # ATH. tekur líka samtengingar með
        return "mark"
    elif mod_tag in {"to", "töl", "tala"}:
        return "nummod"
    # elif mod_tag == "FRAG":
    #    return "xcomp"
    elif mod_tag in string.punctuation or mod_tag == "grm":
        return "punct"
    # elif mod_tag in ["INTJ", "INTJP"] or head_tag == "INTJP":
    #    return "discourse"
    elif mod_tag == "foreign" or head_tag == "foreign":
        return "flat:foreign"

    return "HALLÓ_" + mod_tag, mod_func  # "VANTAR_LIÐ"


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

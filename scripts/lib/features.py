"""

A script for converting various token information into UD features, both for Icelandic and 
Faroese text, for the respective token.
The conversion builds on information from existing tags if a third-party tagger (such as ABLTagger) 
is not used. If so, the tagger's output is converted to the proper format.

"""
import os
import re
import json
import string
import requests

from collections import defaultdict

from lib.rules import cconj, GC_UD_map, Greynir_map
from lib import fo_rules
from lib.tools import decode_escaped


class G_Features:
    """
    Class for extracting UD features from the original tags
    """

    def __init__(self, tag, token=None):
        self.tag = tag
        self.token = token
        self.features = defaultdict(list)

    def _nominal_features(self, tag):
        if len(tag) == 1:
            self.features["Definite"] = Greynir_map["Definite"]["ind"]
        elif tag[0] == "entity":
            if len(tag) > 2:
                if tag[1] in {"nf", "þf", "þgf", "ef"}:
                    self.features["Case"] = Greynir_map["Case"][tag[1]]
                elif tag[1] in {"et", "ft"}:
                    self.features["Number"] = Greynir_map["Number"][tag[1]]
                if tag[2] in {"nf", "þf", "þgf", "ef"}:
                    self.features["Case"] = Greynir_map["Case"][tag[2]]
                elif tag[2] in {"et", "ft"}:
                    self.features["Number"] = Greynir_map["Number"][tag[2]]
                elif tag[2] in {"kk", "kvk", "hk"}:
                    self.features["Gender"] = Greynir_map["Gender"][tag[2]]
            else:
                self.features["Case"] = Greynir_map["Case"][tag[1]]
        else:
            if len(tag) == 4:
                self.features["Number"] = Greynir_map["Number"][tag[1]]
                self.features["Case"] = Greynir_map["Case"][tag[2]]
                self.features["Gender"] = Greynir_map["Gender"][tag[3]]
            elif len(tag) < 4:
                if len(tag) == 2 and tag[1] in {"et", "ft"}:
                    self.features["Number"] = Greynir_map["Number"][tag[1]]
                elif len(tag) == 2 and tag[1] in {"nf", "þf", "þgf", "ef"}:
                    self.features["Case"] = Greynir_map["Case"][tag[1]]
                else:
                    if tag[1] in {"nf", "þf", "þgf", "ef"}:
                        self.features["Case"] = Greynir_map["Case"][tag[1]]
                    elif tag[1] in {"et", "ft"}:
                        self.features["Number"] = Greynir_map["Number"][tag[1]]
                    if tag[2] in {"nf", "þf", "þgf", "ef"}:
                        self.features["Case"] = Greynir_map["Case"][tag[2]]
                    elif tag[2] in {"kk", "kvk", "hk"}:
                        self.features["Gender"] = Greynir_map["Gender"][tag[2]]
            elif len(tag) > 4:
                if tag[4].startswith("gr"):
                    self.features["Definite"] = Greynir_map["Definite"][tag[4]]
                elif tag[2].startswith("gr"):
                    self.features["Definite"] = Greynir_map["Definite"][tag[2]]
            else:
                self.features["Definite"] = Greynir_map["Definite"]["ind"]

        return self.features

    def _adjective_features(self, tag):
        if len(tag) > 1:
            if tag[1] in {"nf", "þf", "þgf", "ef"}:
                self.features["Case"] = Greynir_map["Case"][tag[1]]
                if len(tag) == 3:
                    self.features["Gender"] = Greynir_map["Gender"][tag[2]]
            else:
                self.features["Number"] = Greynir_map["Number"][tag[1]]
                if len(tag) > 2:
                    self.features["Case"] = Greynir_map["Case"][tag[2]]
                    self.features["Gender"] = Greynir_map["Gender"][tag[3]]
            if len(tag) > 5 and tag[4] != "sb":
                self.features["Degree"] = Greynir_map["Degree"][tag[4]]
                ## tag[5] == sterk beyging/veik beyging
            else:
                self.features["Degree"] = Greynir_map["Degree"]["fst"]
            ## tag[4] == sterk beyging/veik beyging

        ## definite??

        return self.features

    def _pronoun_features(self, tag):
        if tag[0] != "fn":
            self.features["PronType"] = Greynir_map["PronType"][tag[0]]
        if len(tag) > 1:
            if tag[0] != "abfn":
                self.features["Number"] = Greynir_map["Number"][tag[1]]
                self.features["Case"] = Greynir_map["Case"][tag[2]]
                if tag[0] == "fn":
                    self.features["Gender"] = Greynir_map["Gender"][tag[3]]
                elif tag[0] == "pfn":
                    if len(tag) == 4:
                        if tag[3].startswith("p"):
                            self.features["Person"] = Greynir_map["Person"][tag[3]]
                        else:
                            self.features["Gender"] = Greynir_map["Gender"][tag[3]]
                    elif len(tag) == 5:
                        if tag[4].startswith("p"):
                            self.features["Person"] = Greynir_map["Person"][tag[4]]
                        else:
                            self.features["Person"] = Greynir_map["Person"][tag[3]]
                            self.features["Gender"] = Greynir_map["Gender"][tag[4]]
        elif tag[0] == "abfn":
            if len(tag) > 1:
                self.features["Case"] = Greynir_map["Case"][tag[1]]

        return self.features

    def _determiner_features(self, tag):
        """
        Ekki notað í GreynirCorpus - hægt að nota??
        """

    def _numeral_features(self, tag):
        if len(tag) > 1:
            if len(tag) == 2:
                self.features["Case"] = Greynir_map["Case"][tag[1]]
            elif len(tag) == 3:
                self.features["Case"] = Greynir_map["Case"][tag[1]]
                self.features["Gender"] = Greynir_map["Gender"][tag[2]]
            else:
                self.features["Number"] = Greynir_map["Number"][tag[1]]
                self.features["Case"] = Greynir_map["Case"][tag[2]]
                self.features["Gender"] = Greynir_map["Gender"][tag[3]]

        return self.features

    def _verb_features(self, tag):
        if tag[1] == "1":
            del tag[2]
        elif tag[1] == "2":
            del tag[2:4]
        if len(tag) > 2:
            if tag[2] in {"bh", "fh", "vh"}:
                self.features["Mood"] = Greynir_map["Mood"][tag[2]]
            elif tag[2] in {"lh", "lhþt", "sagnb", "nh"}:
                self.features["VerbForm"] = Greynir_map["VerbForm"][tag[2]]
                if tag[2] == "lhþt":
                    self.features["Tense"] = "Past"
                    if len(tag) > 3:
                        self.features["Number"] = Greynir_map["Number"][tag[3]]
                elif tag[2] == "lh":
                    self.features["Tense"] = "Pres"
                    self.features["Number"] = Greynir_map["Number"][tag[3]]
            if len(tag) > 4:
                if tag[3].startswith("p"):
                    self.features["Person"] = Greynir_map["Person"][tag[3]]
                elif tag[3] in {"et", "ft"}:
                    self.features["Number"] = Greynir_map["Number"][tag[3]]
                if tag[4] in {"et", "ft"}:
                    self.features["Number"] = Greynir_map["Number"][tag[4]]
                if len(tag) > 5:
                    if tag[5] in {"nt", "þt"}:
                        self.features["Tense"] = Greynir_map["Tense"][tag[5]]
                    if tag[5] in {"lh", "lhþt", "sagnb", "nh"}:
                        self.features["VerbForm"] = Greynir_map["VerbForm"][tag[5]]
        if tag[-1] in {"gm", "mm"}:
            self.features["Voice"] = Greynir_map["Voice"][tag[-1]]

        return self.features

    def _adverb_features(self, tag):
        if len(tag) > 1:
            self.features["Degree"] = Greynir_map["Degree"][tag[1]]

        return self.features

    def _other_features(self, tag):
        return self.features

    def get_features(self):
        if self.tag is None:
            return None
        tag_sp = self.tag.split("_")
        word = tag_sp[0]

        if word in {"no", "person", "sérnafn", "entity", "fyrirtæki", "gata"}:
            return self._nominal_features(tag_sp)
        elif word == "so":
            return self._verb_features(tag_sp)
        elif word == "lo":
            return self._adjective_features(tag_sp)
        elif word in {"gr", "fn", "pfn", "abfn"}:
            return self._pronoun_features(tag_sp)
        elif word in {"ao", "eo"}:
            return self._adverb_features(tag_sp)
        elif word in {"to", "tala"}:
            ## if töl (óbeygjanlegt): ??
            return self._numeral_features(tag_sp)

        else:
            return self._other_features(self.tag)

    def get_UD_tag(self):
        """ """

        if self.tag is not None and "_" in self.tag:
            tag = self.tag.split("_")[0]
        else:
            tag = self.tag
        if tag == "st" and self.token in cconj:
            return "CCONJ"
        try:
            tag = GC_UD_map[tag]
            return tag
        except:
            # raise
            if self.tag is not None and tag in string.punctuation:
                tag = "PUNCT"
                return tag
            elif self.tag is not None:
                tag = GC_UD_map.get(tag[0], "X")
                return tag
            else:
                return None


class FeatureExtractionError(Exception):
    """docstring for ."""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "FeatureExtractionError: {0}".format(self.message)
        else:
            return "FeatureExtractionError has been raised"


if __name__ == "__main__":

    in_dir = "testing/CoNLLU_output/"
    # in_path = 'testing/CoNLLU_output/1985.sagan.nar-fic.conllu'

    for filename in os.listdir(in_dir)[1:]:
        # filename = os.path.basename(in_path)
        in_path = os.path.join(in_dir, filename)
        # OTB_path = os.path.join('taggers','tagged', re.sub('conllu', 'txt.tagged', filename))
        # OTB_path = 'taggers/tagged/2008.mamma.nar-fic.txt.tagged'
        out_path = in_path + ".tmp"

        CoNLLU_file = open(in_path, "r")
        # OTB_file = open(OTB_path, 'r')

        CoNLLU_lines = [line.split("\t") for line in list(CoNLLU_file.readlines())]
        line_indexes = [i for i in range(len(CoNLLU_lines))]
        self.OTB_tagDict = getTagDict(filename)

        word_index = 1
        try:
            for i in line_indexes:
                f = Features(CoNLLU_lines, self.OTB_tagDict, i, word_index)
                f.get_UD_tag()
                f.get_OTB_tag()
                # print(f.index, f.IcePaHC_tag, f.UD_tag)
                # if f.OTB_token == 'Placeholder':
                #     print(f.word_index, f.token, f.OTB_token, f.OTB_tag, f.IcePaHC_tag, f.UD_tag)
                if f.OTB_tag:
                    word_index += 1
                    # print(f.word_index, f.token, f.OTB_token, f.OTB_tag, f.IcePaHC_tag, f.UD_tag)
                    # print(f.curr_line)
        except RecursionError:
            print("Recursion error!!!!")
            # print(f.curr_line)
            print(f.token, f.IcePaHC_tag)
            break
        print("You have just finished", filename)
        # input()

        CoNLLU_file.close()
        # OTB_file.close()

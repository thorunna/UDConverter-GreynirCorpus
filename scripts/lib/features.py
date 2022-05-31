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

    def get_features(self):
        if self.tag is None:
            return "_"
        tag_sp = self.tag.split("_")

        for feature in tag_sp:
            if feature in Greynir_map:
                value = Greynir_map[feature]
                if value[1] is None:
                    return "_"
                self.features[value[0]] = value[1]

        if len(self.features) == 0:
            return "_"

        return self.features

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

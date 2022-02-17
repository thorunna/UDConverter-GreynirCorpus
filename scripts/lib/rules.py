cconj = {
    "og",
    "eða",
    "en",
    "heldur",
    "enda",
    "ellegar",
    "bæði",
    "hvorki",
    "annaðhvort",
    "hvort",
    "ýmist",
}

GC_UD_map = {
    "no": "NOUN",  # generalized nouns tagged as NOUN
    "abbrev": "NOUN",
    "so": "VERB",
    "lo": "ADJ",
    "fs": "ADP",
    "nhm": "PART",
    "gr": "DET",
    "uh": "INTJ",
    "ao": "ADV",
    "eo": "ADV",
    "st": "CONJ",  # TODO: ath. mun á conj og sconj miðað við st og stt
    "stt": "CONJ",
    "fn": "PRON",
    "pfn": "PRON",
    "abfn": "PRON",
    "person": "PROPN",
    "sérnafn": "PROPN",
    "entity": "PROPN",
    "fyrirtæki": "PROPN",
    "gata": "PROPN",
    "to": "NUM",
    "töl": "NUM",
    "tala": "NUM",
    "tími": "NUM",
    "ártal": "NUM",
    "raðnr": "ADJ",
    "grm": "PUNCT",
    "foreign": "X",
    # "D": "DET",  # generalized determiners tagged as DET (determiner)
    # "ONE": "DET",  # ath. áður taggað sem NUM
    # "ONES": "DET",
    "P": "ADP",  # generalized prepositions tagged as ADP
    "RP": "ADP",  # specifiers of P/complements of P - Ath. flokka sem eitthvað annað?
    "RPX": "ADP",
    "FOR": "ADP",
    "Q": "DET",  # quantifiers tagged as DET - áður: quantifiers tagged as ADJ - ATH ÞETTA ÞARF AÐ ENDURSKOÐA
    "C": "SCONJ",  # complimentizer tagged as SCONJ (subordinate conjunction)
    "V": "VERB",
    "DO": "VERB",  #'gera', do, tagged as verb
    "HV": "AUX",  #'have' tagged as auxiliary verb
    "MD": "AUX",  # modal verbs tagged as auxiliary
    "RD": "VERB",  #'verða', become, tagged as verb
    "W": "DET",  # WH-determiner tagged as DET (determiner)
    "so": "VERB",  # All forms of "verða" tagged as VERB
    "TO": "PART",  # Infinitive marker tagged as PART (particle)
    "FP": "PART",  # focus particles marked as PART
    "NPR": "PROPN",  # proper nouns tagged as PROPN
    "NPRS": "PROPN",
    "PRO": "PRON",
    # 'WQ' : 'PRON',  #interrogative pronoun
    "WQ": "SCONJ",
    "WPRO": "PRON",  # wh-pronouns
    "SUCH": "PRON",
    "ES": "PRON",  # expletive tagged as PRON
    "MAN": "PRON",
    "MANS": "PRON",
    "NUM": "NUM",
    "ADJ": "ADJ",  # Adjectives tagged as ADV
    "ADJR": "ADJ",  # Comparative adjectives tagged as ADV
    "ADJS": "ADJ",  # Superlative adjectives tagged as ADV
    "WADJ": "ADJ",
    "ADV": "ADV",  # Adverbs tagged as ADV
    "WADV": "ADV",  # TODO: ath. betur - bara spor?
    "NEG": "ADV",
    "ADVR": "ADV",  # Comparative adverbs tagged as ADV
    "ADVS": "ADV",  # Superlative adverbs tagged as ADV
    "ALSO": "ADV",
    "OTHER": "PRON",
    "OTHERS": "PRON",
    "INTJ": "INTJ",  # interjection
    "FW": "X",
    "LS": "NUM",  # list marker tagged as numeral
    "X": "X",
}

Greynir_map = {
    "Gender": {"kk": "Masc", "kvk": "Fem", "hk": "Neut", "x": None},
    "Number": {
        "ft": "Plur",
        "et": "Sing",
    },  # noun, plural number  # noun singular number
    "PronType": {
        "pfn": "Prs",  # personal
        # "e": "Prs",  # posessive (tagged as personal)
        # 'a' : 'Rcp',   #reciprocal
        # "s": "Int",  # interrogative
        # "t": "Rel",  # relative
        # "a": "Dem",  # demonstrative
        # "b": "Dem",
        # "o": "Ind",  # indefinite
        "abfn": "Prs",  # reflexive, categorized as personal/possessive in UD
        "gr": "Art",
    },
    "Tense": {"nt": "Pres", "þt": "Past"},  # present tense  # past tense
    "Person": {"p1": "1", "p2": "2", "p3": "3"},
    "Case": {
        "nf": "Nom",  # nominative case
        "þf": "Acc",  # accusative case
        "þgf": "Dat",  # dative case
        "ef": "Gen",  # dative case
        None: "Nom",
    },
    "Mood": {
        "bh": "Imp",  # imperative
        "fh": "Ind",  # indicative
        "vh": "Sub",  # subjunctive
    },
    "VerbForm": {
        "lh": "Part",  # present participle
        "lhþt": "Part",  # past participle
        "sagnb": "Sup",
        "nh": "Inf",  # infinitive
    },
    "Voice": {
        "gm": "Act",  # active voice
        "mm": "Mid",  # middle voice
        # "pass": "Pass",  # passive voice
    },
    "Definite": {
        "ind": "Ind",  # adjectives
        "gr": "Def",  # definite
        #    "g": "Def",  # nouns
        #    "o": None,  # 'ÓBEYGT', TODO: check if output 100% correct
        None: "Ind",
    },
    "Degree": {  # adjectives  # adjectives  # nouns
        "fst": "Pos",  # positive, default case
        "mst": "Cmp",  # comparative
        "est": "Sup",  # superlative
        "esb": "Sup",  # superlative, indefinite
        "evb": "Sup",  # superlative, definite
    },
    "NumType": {
        "tala": "Card",  # cardinal number
        "raðnr": "Ord",  # ordinal number
    },
}

head_rules = {
    "S0": {"dir": "r", "rules": [("S-MAIN|S-QUOTE|S-QUE")]},
    "S0-X": {"dir": "r", "rules": [("S-MAIN|S-QUOTE|S-QUE")]},
    "S-MAIN": {"dir": "r", "rules": ["IP"]},
    "S-HEADING": {"dir": "r", "rules": ["IP", "VP", "NP", "NP-OBJ", "NP-SUBJ", "NP.*"]},
    "S-PREFIX": {"dir": "r", "rules": ["IP", "NP.*"]},
    "S-QUE": {"dir": "r", "rules": ["IP"]},
    "CP-ADV": {"dir": "r", "rules": ["IP-SUB.*"]},  # TODO: aldrei bara CP-ADV?
    "CP-ADV-ACK": {"dir": "r", "rules": ["IP"]},
    "CP-ADV-CAUSE": {"dir": "r", "rules": ["IP"]},
    "CP-ADV-COND": {"dir": "r", "rules": ["IP"]},
    "CP-ADV-CONS": {"dir": "r", "rules": ["IP"]},
    "CP-ADV-PURP": {"dir": "r", "rules": ["IP"]},
    "CP-ADV-TEMP": {"dir": "r", "rules": ["IP"]},
    "CP-ADV-CMP": {"dir": "r", "rules": ["NP"]},
    "CP-EXPLAIN": {"dir": "r", "rules": ["abbrev"]},
    "CP-QUE": {"dir": "r", "rules": ["IP", "CP-QUE.*"]},  # question
    "CP-REL": {"dir": "r", "rules": ["IP"]},  # relative
    "CP-THT": {"dir": "r", "rules": ["IP", ".*"]},  # að
    "CP-QUOTE": {"dir": "r", "rules": ["IP"]},
    "IP": {"dir": "r", "rules": ["VP"]},
    "IP-INF": {
        "dir": "r",
        "rules": [
            "VP",
            "IP-INF",
            "NP-PRD",
            "NP-OBJ",
            "PP",
        ],
    },
    "IP-INF-PRD": {"dir": "r", "rules": ["VP"]},
    "IP-INF-OBJ": {"dir": "r", "rules": ["VP"]},
    "NP": {
        "dir": "r",
        "rules": [
            "CP-FRL",
            (
                "no(_\w\w)?_nf.*|person(_\w\w)?_nf.*|entity(_\w\w)?_nf.*|fyrirtæki(_\w\w)?_nf.*|gata(_\w\w)?_nf.*"
            ),
            ("no.*|sérnafn.*|person.*|entity.*|fyrirtæki.*|gata.*|prósenta.*"),
            ("fn(_\w\w)?_nf.*|pfn(_\w\w)?_nf.*|abfn(_\w\w)?_nf.*"),
            ("fn.*|pfn.*|abfn.*"),
            "RRC",
            "IP-INF-PRP",
            "NP.*",
            "Q.*",
            "lo.*",
            "IP-SUB",
        ],
    },
    "NP-SUBJ": {
        "dir": "r",
        "rules": [
            (
                "no(_\w\w)?_nf.*|person(_\w\w)?_nf.*|entity(_\w\w)?_nf.*|fyrirtæki(_\w\w)?_nf.*|gata(_\w\w)?_nf.*|prósenta(_\w\w)?_nf.*"
            ),
            ("no.*|sérnafn.*|person.*|entity.*|fyrirtæki.*|gata.*"),
            ("fn(_\w\w)?_nf.*|pfn(_\w\w)?_nf.*|abfn(_\w\w)?_nf.*"),
            ("fn.*|pfn.*|abfn.*"),
            "NP.*",
            "lo_\w\w_nf.*",
        ],
    },
    "NP-IOBJ": {
        "dir": "r",
        "rules": [
            ("no.*|sérnafn.*|person.*|entity.*|fyrirtæki.*|gata.*"),
            ("fn.*|pfn.*|abfn.*"),
            "NP.*",
        ],
    },
    "NP-OBJ": {
        "dir": "r",
        "rules": [
            ("no.*|sérnafn.*|person.*|entity.*|fyrirtæki.*|gata.*"),
            "NP",
            "NP-.+",
            ("fn.*|pfn.*|abfn.*"),
        ],
    },
    "NP-PRD": {
        "dir": "r",
        "rules": [
            ("no.*|sérnafn.*|person.*|entity.*|fyrirtæki.*|gata.*"),
            ("fn.*|pfn.*|abfn.*"),
            "lo_\w\w_nf.*",
            "NP.*",
            "lo.*",
            "gr.",
            ("tala.*|to.*|töl.*"),
        ],
    },  # predicate
    "NP-ADP": {
        "dir": "r",
        "rules": ["so.*", "no.*", "lo.*", "VP", "abfn.*"],
    },
    "NP-POSS": {
        "dir": "r",
        "rules": [
            ("no.*|sérnafn.*|person.*|entity.*|fyrirtæki.*|gata.*"),
            "prósenta.*",
            "NP",
            ("fn.*|pfn.*"),
        ],
    },
    "NP-DAT": {"dir": "r", "rules": ["no.*"]},
    "NP-ADDR": {"dir": "r", "rules": [("sérnafn.*|gata.*"), "no.*"]},
    "NP-AGE": {"dir": "r", "rules": ["no.*"]},
    "NP-MEASURE": {
        "dir": "r",
        "rules": [("mælieining.*|töl.*|no.*"), "tala.*", "eo_mst"],
    },
    "NP-COMPANY": {
        "dir": "r",
        "rules": ["fyrirtæki.*", "entity.*", "sérnafn.*", "lo.*"],
    },
    "NP-TITLE": {"dir": "r", "rules": ["no.*", "fn.*"]},
    "ADJP": {"dir": "r", "rules": ["lo.*"]},
    "VP": {"dir": "r", "rules": ["so.*", "VP", "IP-INF"]},
    "VP-AUX": {"dir": "r", "rules": ["so.*"]},
    "PP": {
        "dir": "r",
        "rules": [
            ("no.*|sérnafn.*|person.*|entity.*|fyrirtæki.*|gata.*"),
            "NP",
            "NP-.+",
            "CP-ADV.*",
            "IP",  # TODO: er þetta rétt? IP-SMC upprunalega
            ("PP|ao.*|eo.*|ADVP"),
            ("CP-.*|PP"),
            "IP-INF.*",
            "P",
            "PP",
        ],
    },
    "PP-LOC": {"dir": "r", "rules": ["NP.*", "PP-LOC"]},
    "ADVP": {
        "dir": "r",
        "rules": [
            "no.*",
            ("sérnafn.*|person.*|entity.*|fyrirtæki.*|gata.*"),
            ("ao.*|eo.*"),
        ],
    },
    "ADVP-DATE-ABS": {
        "dir": "r",
        "rules": ["dagsföst", "ártal", "tími", "NP", "ADVP-DATE-ABS"],
    },
    "ADVP-DATE-REL": {
        "dir": "r",
        "rules": ["dagsafs", "no.*", "lo.*", "NP", "ADVP-DATE-REL"],
    },
    "ADVP-DIR": {
        "dir": "r",
        "rules": [
            "no.*",
            ("sérnafn.*|person.*|entity.*|fyrirtæki.*|gata.*"),
            ("ao.*|eo.*"),
        ],
    },
    "ADVP-DUR-ABS": {
        "dir": "r",
        "rules": [
            "ártal",
            "NP",
            "ADVP-DATE-ABS",
        ],
    },
    "ADVP-DUR-REL": {"dir": "r", "rules": ["ártal", "no.*", "NP"]},
    "ADVP-DUR-TIME": {"dir": "r", "rules": ["ártal", "no.*", "NP"]},
    "ADVP-TIMESTAMP-ABS": {"dir": "r", "rules": ["dagsföst"]},
    "ADVP-TIMESTAMP-REL": {
        "dir": "r",
        "rules": ["no.*", "ártal", "tími", "lo.*", "NP", "ao.*"],
    },
    "ADVP-TMP-SET": {"dir": "r", "rules": ["ao.*"]},
    "ADVP-PCL": {"dir": "r", "rules": ["ao.*"]},
}

relation_NP = {
    None: "obl",
    "SUBJ": "nsubj",
    "SOURCE": "nsubj",
    "IOBJ": "iobj",
    "OBJ": "obj",
    "PRD": "xcomp",
    "ADP": "obl",
    "POSS": "nmod:poss",
    "DAT": "obl",
    "ADDR": "VANTAR_LIÐ-obl?",  # TODO
    "AGE": "VANTAR_LIÐ-obl?",  # TODO
    "MEASURE": "obl",
    "COMPANY": "VANTAR_LIÐ-obl?",  # TODO
    "TITLE": "obl",  # TODO: Ætti title að vera merkt öðruvísi?
}

relation_IP = {
    None: "VANTAR_LIÐ_IP_None",  # TODO: dep í IcePaHC
    "INF": "xcomp",
    "INF-OBJ": "xcomp",
    "INF-PRD": "csubj",
}

relation_CP = {
    None: "VANTAR_LIÐ",  # TODO: dep í IcePaHC
    "ADV": "advcl",
    "ADV-ACK": "advcl",
    "ADV-CAUSE": "advcl",
    "ADV-COND": "advcl",
    "ADV-CONS": "advcl",
    "ADV-PURP": "advcl",
    "ADV-TEMP": "advcl",
    "ADV-CMP": "advcl",
    "EXPLAIN": "VANTAR_LIÐ",  # TODO: ccomp/xcomp?
    "QUE": "ccomp/xcomp",
    "REL": "acl:relcl",
    "THT": "ccomp/xcomp",
    "QUOTE": "ccomp/xcomp",  # "VANTAR_LIÐ",  # TODO: Er þetta rétt?
}


abbr_tokens = {
    "o.",
    "s.",
    "frv.",
    "t.",
    "t.",
    "d.",
    "fl.",
    "t.$",
    "$d.",
    "þ.$",
    "$e.",
    "$e.$",
    "$a.$",
    "$s.",
    "a$",
    "$m$",
    "$k",
    "m.$",
    "$a.",
    "m.$",
    "$a.$",
    "$s.",
    "t.$",
    "$d.",
}
abbr_map = {
    # abbr : token, lemma, lemma(true)
    "o.": (r"o\.", "og", "og", "og"),
    "s.": (r"s\.", "svo", "svo", ""),
    "frv.": (r"frv\.", "framvegis", "framvegis", ""),
    "t.": (r"t\.", "til", "til", ""),
    "t.": (r"t\.", "til", "t", ""),
    "d.": (r"d\.", "dæmis", "dæmi", ""),
    "fl.": (r"fl\.", "fleira", "margur", ""),
    "t.$": (r"t\.\$", "til", "t", "til"),
    "$d.": (r"\$d\.", "dæmis", "d", "dæmi"),
    "þ.$": (r"þ\.\$", "það", "þú", "þú"),
    "$e.": (r"\$e\.", "er", "vera", ""),
    "$e.$": (r"\$e\.\$", "er", "vera", ""),
    "$a.$": (r"\$a\.\$", "að", "a\.", "að"),
    "$s.": (r"\$s\.", "segja", "s", "segja"),
    "a$": (r"a$", "að", "að", "að"),
    "$m$": (r"\$m$", "minnsta", "lítill", ""),
    # '$k' : (r'\$k', 'kosti', 'kostur', ''), # NOTE: Not needed!
    "m.$": (r"m\.\$", "meðal", "m", "meðal"),
    "$a.": (r"\$a\.", "annars", "annar", ""),
    "m.$": (r"m\.\$", "meira", "m", "meira"),
    "$a.$": (r"\$a\.\$", "að", "a\.", "að"),
    "$s.": (r"\$s\.", "segja", "s", "segja"),
    "t.$": (r"t\.\$", "til", "til", ""),
    "$d.": (r"\$d\.", "dæmis", "dæmis", ""),
}

mwes = [
    "af því að",
    "á meðan",
    "áður en",
    "eftir að",
    "eins og",
    "enda þótt",
    "frá því að",
    "frá því er",
    "frá því",
    "fyrir því að",
    "fyrr en",
    "heldur en",
    "hvar sem",
    "hvaðan er",
    "hvaðan sem",
    "hvenær sem",
    "hvernig sem",
    "hvert er",
    "hvert sem",
    "í sjálfu sér",
    "jafnskjótt og",
    "jafnskjótt sem",
    "jafnvel þótt",
    "með því að",
    "óðar en",
    "sakir þess að",
    "sökum þess að",
    "strax og",
    "svo að",
    "svo framarlega sem",
    "svo sem",
    "til að",
    "til þess að",
    "til þess er",
    "um leið og",
    "undireins og",
    "úr því að",
    "vegna þess að",
    "vel á minnst",
    "þangað er",
    "þangað sem",
    "þangað til að",
    "þar er",
    "þar eð",
    "þar sem",
    "þar sem",
    "þar til að",
    "þar til er",
    "þaðan er",
    "þaðan sem",
    "þá er",
    "þeim mun",
    "þó að",
    "þrátt fyrir að",
    "þrátt fyrir það að",
    "því að",
]

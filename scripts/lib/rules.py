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
    "so": "VERB",
    "lo": "ADJ",
    "fs": "ADP",
    "nhm": "PART",
    "gr": "DET",
    "uh": "?",
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
    "grm": "PUNCT",
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
    "S0.*": {"dir": "r", "rules": ["S-MAIN"]},
    "S-MAIN": {"dir": "r", "rules": ["IP"]},
    "S-HEADING"
    "S-PREFIX"
    "S-QUE"
    "CP-ADV": {"dir": "r", "rules": ["IP-SUB.*"]},  # TODO: aldrei bara CP-ADV?
    "CP-ADV-ACK": {"dir": "r", "rules": ["IP"]},
    "CP-ADV-CAUSE": {"dir": "r", "rules": ["IP"]},
    "CP-ADV-COND": {"dir": "r", "rules": ["IP"]},
    "CP-ADV-CONS": {"dir": "r", "rules": ["IP"]},
    "CP-ADV-PURP": {"dir": "r", "rules": ["IP"]},
    "CP-ADV-TEMP": {"dir": "r", "rules": ["IP"]},
    "CP-ADV-CMP": {"dir": "r", "rules": ["NP"]},
    "CP-QUE": {"dir": "r", "rules": ["IP", "CP-QUE.*"]},  # question
    "CP-REL": {"dir": "r", "rules": ["IP"]},  # relative
    "CP-THT": {"dir": "r", "rules": ["IP", ".*"]},  # að
    "CP-QUOTE"
    "IP"
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
    "NP": {
        "dir": "r",
        "rules": [
            "CP-FRL",
            (
                "no(_\w\w)?_nf.*|person(_\w\w)?_nf.*|entity(_\w\w)?_nf.*|fyrirtæki(_\w\w)?_nf.*|gata(_\w\w)?_nf.*"
            ),
            ("no.*|sérnafn.*|person.*|entity.*|fyrirtæki.*|gata.*"),
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
                "no(_\w\w)?_nf.*|person(_\w\w)?_nf.*|entity(_\w\w)?_nf.*|fyrirtæki(_\w\w)?_nf.*|gata(_\w\w)?_nf.*"
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
    "NP-ADP"
    "NP-POSS"
    "NP-DAT"
    "NP-ADDR"
    "NP-AGE"
    "NP-MEASURE"
    "NP-COMPANY"
    "NP-TITLE"
    "VP": {"dir": "r", "rules": ["so.*", "VP"]},
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
    ## KOMIN HINGAÐ!!
    "ADJP": {
        "dir": "r",
        "rules": [
            "(VAN|VAG|ADJ-.|ADJR-.|ADJS-.|Q.*|ONE.*)",
            "ADJR-.",
            "ADJS-.",
            "ADVP",
            "ADVR",
            "ONE",
            "ONES",
            "CP-TMP",
            "(N-.+|NS-.+)",
            "NP",
            "(ADJX|ADJP|CONJP)",
            "IP-SUB",
        ],
    },
    "ADJP-SPR": {"dir": "r", "rules": ["ADJ-.", "ADJS-N"]},  # SPR = secondary predicate
    "ADJP-SPR-LFD": {"dir": "r", "rules": ["ADJ-.", "ADJS-N"]},
    "ADJP-DIR": {
        "dir": "r",
        "rules": ["ADJ-.", "ADJR-.", "ADJS-.", "ADVR", "ONE", "ONES", "CP-TMP", "Q.*"],
    },
    "ADJP-LFD": {
        "dir": "r",
        "rules": ["ADJ-.", "ADJR-.", "ADJS-.", "ADVR", "ONE", "ONES", "CP-TMP", "Q.*"],
    },
    "ADJP-LOC": {
        "dir": "r",
        "rules": ["ADJ-.", "ADJR-.", "ADJS-.", "ADVR", "ONE", "ONES", "CP-TMP", "Q.*"],
    },  # one occurrence of ADJP-OC
    "ADJP-PRN": {
        "dir": "r",
        "rules": [
            "ADJ-.",
            "ADJR-.",
            "ADJS-.",
            "ADVR",
            "ADJP",
            "ONE",
            "ONES",
            "CP-TMP",
            "Q.*",
        ],
    },
    "ADJP-PRN-ELAB": {
        "dir": "r",
        "rules": ["ADJ-.", "ADJR-.", "ADJS-.", "ADVR", "ONE", "ONES", "CP-TMP", "Q.*"],
    },
    "ADJP-RSP": {
        "dir": "r",
        "rules": ["ADJ-.", "ADJR-.", "ADJS-.", "ADVR", "ONE", "ONES", "CP-TMP", "Q.*"],
    },
    "ADJP-TMP": {
        "dir": "r",
        "rules": ["ADJ-.", "ADJR-.", "ADJS-.", "ADVR", "ONE", "ONES", "CP-TMP", "Q.*"],
    },
    "ADJX": {"dir": "r", "rules": ["ADJ.*"]},
    "WADJP": {"dir": "r", "rules": ["ADJ.*", "ADV.*"]},
    "WADJX": {"dir": "r", "rules": ["ADJ.*", "ADV.*"]},
    "PX": {
        "dir": "r",
        "rules": [
            "CP-FRL",
            "NP",
            "NP-.+",
            "FS",
            "CP-ADV",
            "IP-SMC",
            "ADVP",
            "ADJP",
            "CP-.*",
            "IP-INF.*",
            "P",
        ],
    },
    "PP-BY": {
        "dir": "r",
        "rules": [
            "NP",
            "NP-.+",
            "CP-ADV",
            "IP-SMC",
            "ADVP",
            "ADJP",
            "CP-.*",
            "IP-INF.*",
            "P",
        ],
    },
    "PP-BY-RSP": {
        "dir": "r",
        "rules": [
            "NP",
            "NP-.+",
            "CP-ADV",
            "IP-SMC",
            "ADVP",
            "ADJP",
            "CP-.*",
            "IP-INF.*",
            "P",
        ],
    },
    "PP-PRN": {"dir": "r", "rules": ["CP-ADV", "NP", "P"]},
    "PP-PRN-ELAB": {"dir": "r", "rules": ["CP-ADV", "NP", "P"]},
    "PP-RSP": {
        "dir": "r",
        "rules": [
            "NP",
            "NP-.+",
            "CP-ADV",
            "IP-SMC",
            "ADVP",
            "ADJP",
            "CP-.*",
            "IP-INF.*",
            "P",
        ],
    },
    "PP-SBJ": {
        "dir": "r",
        "rules": [
            "NP",
            "NP-.+",
            "CP-ADV",
            "IP-SMC",
            "ADVP",
            "ADJP",
            "CP-.*",
            "IP-INF.*",
            "P",
        ],
    },
    "PP-LFD": {
        "dir": "r",
        "rules": ["CP-ADV.*", "CP-THT.*", "NP", "PP"],
    },  # left dislocation
    "P": {"dir": "r", "rules": ["P"]},
    "ADVP": {
        "dir": "r",
        "rules": [
            "N-.",
            "NS-.",
            "NPR-.",
            "NPRS-.",
            "ADV",
            "ADVR",
            "ADVS",
            "WADV",
        ],
    },
    "ADVP-DIR": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-DIR-LFD": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-DIR-RSP": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-LOC": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-LOC-LFD": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-LOC-RSP": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-TMP": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV.*", "WADV"],
    },
    "ADVP-TMP-LFD": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-TMP-PRN": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-TMP-RSP": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-RSP": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-RSP-RSP": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-TMP-RSP": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-ELAB": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-LFD": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-MSR": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-PRN": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-PRN-ELAB": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-PRN-REP": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVP-RMP": {
        "dir": "r",
        "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"],
    },
    "ADVX": {"dir": "r", "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "ADV", "WADV"]},
    "WADVP": {"dir": "r", "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "WADV"]},
    "WADVP-LOC": {"dir": "r", "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "WADV"]},
    "WADVP-NaN": {"dir": "r", "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "WADV"]},
    "CONJP": {
        "dir": "r",
        "rules": [
            "IP-INF-SPE",
            "IP-MAT-SPE",
            "IP-MAT-SPE=1",
            "IP-SUB",
            "IP-SUB=5",
            "IP-SUB=2",
            "N-.",
            "NS-.",
            "NPR-.",
            "NPRS-.",
            "NP.*",
            "NX",
            "NUMP.*",
            "NUM-.",
            "QTP",
            "QP",
            "QX",
            "IP-SUB",
            "IP-MAT.*",
            "IP-INF",
            "IP-INF.*",
            "IP-.+",
            "CP-QUE",
            "ADJP",
            "ADJX",
            "ADJ-.",
            ("ADJS-.|VAN-."),
            "CP-THT",
            "ADVP.*",
            "PP",
            "RRC",
            "Q.*",
            "CONJ",
            "FRAG",
        ],
    },
    "CONJP-PP": {
        "dir": "r",
        "rules": [
            "NP.*",
            "NX",
            "N-.",
            "NS-.",
            "NPR-.",
            "NPRS-.",
            "NUM-.",
            "QP",
            "QX",
            "IP-SUB",
            "IP-MAT",
            "IP-INF",
            "IP-.+",
            "CP-QUE",
            "ADJP",
            "ADJX",
            "PP",
            "RRC",
            "CONJ",
        ],
    },
    "CONJP-PRN": {
        "dir": "r",
        "rules": [
            "NP.*",
            "NX",
            "N-.",
            "NS-.",
            "NPR-.",
            "NPRS-.",
            "NUM-.",
            "QP",
            "QX",
            "IP-SUB",
            "IP-MAT",
            "IP-INF",
            "IP-.+",
            "CP-QUE",
            "ADJP",
            "ADJX",
            "PP",
            "RRC",
            "CONJ",
        ],
    },
    "WNP": {
        "dir": "r",
        "rules": [
            "N-.",
            "NS-.",
            "NPR-.",
            "NPRS-.",
            "Q-.",
            "WQ-.",
            "WPRO-.",
            "PRO-.",
            "WD-.",
            "NP.*",
            "WNP.*",
        ],
    },
    "WNP-COM": {
        "dir": "r",
        "rules": [
            "N-.",
            "NS-.",
            "NPR-.",
            "NPRS-.",
            "Q-.",
            "WQ-.",
            "WPRO-.",
            "PRO-.",
            "WD-.",
            "NP.*",
            "WNP.*",
        ],
    },
    "WNP-MSR": {
        "dir": "r",
        "rules": [
            "N-.",
            "NS-.",
            "NPR-.",
            "NPRS-.",
            "Q-.",
            "WQ-.",
            "WPRO-.",
            "PRO-.",
            "WD-.",
            "NP.*",
            "WNP.*",
        ],
    },
    "WNP-POS": {
        "dir": "r",
        "rules": [
            "N-.",
            "NS-.",
            "NPR-.",
            "NPRS-.",
            "Q-.",
            "WQ-.",
            "WPRO-.",
            "PRO-.",
            "NP.*",
            "WNP.*",
        ],
    },
    "WNP-PRN-ELAB": {
        "dir": "r",
        "rules": [
            "N-.",
            "NS-.",
            "NPR-.",
            "NPRS-.",
            "Q-.",
            "WQ-.",
            "WPRO-.",
            "PRO-.",
            "WD-.",
            "NP.*",
            "WNP.*",
        ],
    },
    "WPP": {"dir": "r", "rules": ["WNP.*", "WADVP.*", "NP.*"]},
    "NX": {"dir": "r", "rules": [("N-.|NS-."), "NPR-.", "NPRS-.", "NP.*"]},
    "WNX": {"dir": "r", "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", "NP.*"]},
    "FRAG-LFD": {"dir": "r", "rules": ["CP.*", "IP.*", "NP.*", "PP"]},
    "FRAG": {
        "dir": "r",
        "rules": [
            "CP.*",
            "IP.*",
            "N-.",
            "NS-.",
            "NPR-.",
            "NPRS-.",
            "NP.*",
            "PP",
            "ADJP",
        ],
    },
    "FRAG-SPE": {
        "dir": "r",
        "rules": [
            "CP.*",
            "IP.*",
            "N-.",
            "NS-.",
            "NPR-.",
            "NPRS-.",
            "NP.*",
            "PP",
            "ADJP",
        ],
    },
    "FRAG-SPE-SBJ": {"dir": "r", "rules": ["CP-THT-SPE"]},
    "QP": {"dir": "r", "rules": ["N-.", "NS-.", "Q-.", "QS-.", "QR-."]},
    "WQP": {"dir": "r", "rules": ["Q-.", "QS-.", "QR-."]},
    "QTP": {
        "dir": "r",
        "rules": [
            ("IP.*|FW"),
            ("NP.*|N-.*|NS-.*"),
            "VAN",
            "ADVP",
            "QTP",
            "INTJP",
            "PP",
            "WNP",
            ".+[^PUNCT]",
        ],
    },  # quote phrase
    "QTP-SBJ": {"dir": "r", "rules": ["IP.*", "NP.*"]},
    "REP": {"dir": "r", "rules": ["NP", "PP", "ADJP", "IP.*", "VB.*"]},  # repetition
    "RRC": {
        "dir": "r",
        "rules": ["V.+", "ADJP", "RRC.*", "PP", ".AG"],
    },  # reduced relative clause
    "RRC-PRN": {"dir": "r", "rules": ["V.+", "ADJP", "RRC.*", "PP", ".AG"]},
    "RRC-SPE": {"dir": "r", "rules": ["V.+", "ADJP", "RRC.*", "PP", ".AG"]},
    "NUMP": {"dir": "r", "rules": ["N-.", "NS-.", "NPR-.", "NPRS-.", ("ONE.*|NUM-.")]},
    "INTJP": {"dir": "r", "rules": ["INTJ", "N-.", "NS-.", "NPR-.", "NPRS-.", "FP"]},
    "XP": {"dir": "r", "rules": ["XXX"]},
    "FS": {"dir": "r", "rules": ["CP-ADV"]},
    "META": {"dir": "r", "rules": [("NP|FW"), "N.*", "LATIN", "CODE"]},
    "CODE": {"dir": "r", "rules": ["NP"]},
    "TRANSLATION": {"dir": "r", "rules": ["NP"]},
    "LATIN": {"dir": "r", "rules": ["FW", "CODE"]},
    "MDPI": {"dir": "r", "rules": ["MDPI"]},
}

relation_NP = {
    None: "obl",
    "LFD": "obl",
    "ADV": "obl",
    "ADV-LFD": "obl",
    "ADV-RSP": "obl",
    "CMP": "obl",
    "PRN": "appos",  # appositive
    "PRNL": "appos",
    "PRN-ELAB": "appos",
    "PRN-REP": "appos",
    "RSP": "obl",
    "SBJ": "nsubj",
    "SBJ-LFD": "nsubj",
    "SBJ-RSP": "nsubj",
    "SMC": "obl",
    "SPE": "nsubj",
    "OB1": "obj",
    "OB1-LFD": "obj",
    "OB1-RSP": "obj",
    "OB2": "iobj",
    "OB2-RSP": "iobj",
    "OB3": "iobj",
    "PRD": "xcomp",  # predicate
    "SPR": "xcomp",
    "POS": "nmod:poss",
    "POS-RSP": "nmod:poss",
    "POS-CPD": "nmod:poss",
    "COM": "nmod:poss",
    "ADT": "obl",
    "TMP": "obl",
    "TMP-LFD": "obl",
    "TMP-RSP": "obl",
    "NUM": "nummod",
    "MSR": "obl",
    "MSR-LFD": "obl",
    "MSR-RSP": "obl",
    "VOC": "vocative",
    "VOC-LFD": "vocative",
    "DIR": "obl",
    "DIR-LFD": "obl",
    "DIR-PRN": "obl",
}

relation_IP = {
    None: "VANTAR_LIÐ",
    "INF": "xcomp",
    "INF-ABS": "xcomp",
    "INF-ABS-PRN": "xcomp",
    "INF-PRP": "advcl",  # purpose
    "INF-PRP-PRN": "advcl",
    "INF-PRP-PRN-SPE": "advcl",
    "INF-PRP-SPE": "advcl",
    "INF-PRP-SPE-PRN": "advcl",
    "INF-SPE": "xcomp",
    "INF-SPE-ADT": "advcl",  # ADT = clause-level dative adjunct
    "INF-SPE-DEG": "xcomp",
    "INF-SPE-LFD": "xcomp",
    "INF-SPE-PRN": "xcomp",
    "INF-SPE-PRN-ELAB": "xcomp",  # same as INF-SPE-PRN
    "INF-SPE-PRP": "advcl",  # purpose
    "INF-SPE-PRP-PRN": "advcl",
    "INF-SPE-SBJ": "xcomp",
    "INF-PRN": "xcomp",
    "INF-PRN-ELAB": "xcomp",
    "INF-PRN-PRP": "advcl",  # pronoun-purpose
    "INF-PRN-SPE": "xcomp",
    "INF-RSP": "xcomp",  # RSP = resumptive
    "INF-SBJ": "xcomp",
    "INF-SBJ-SPE": "xcomp",
    "INF-DEG": "xcomp",
    "INF-DEG-PRN": "xcomp",
    "INF-DEG-SPE": "xcomp",
    "INF-LFD": "xcomp",
    "INF-PRD": "csubj",
    "INF-ADT": "advcl",  # clause-level modifier because clause-level dative adjunct
    "INF-ADT-SPE": "advcl",
    "INF-ADT-SPE-LFD": "advcl",
    "INF-ADT-LFD": "advcl",
    "INF-ADT-PRN": "advcl",
    "MAT": "conj",
    "MAT-DIR": "conj",  # same as MAT
    "MAT-LFD": "conj",  # same as MAT
    "MAT-OB1": "advcl",  # occurs once
    "MAT-PRN": "parataxis",
    "MAT-PRN-ELAB": "parataxis",
    "MAT-PRN-LFD": "parataxis",
    "MAT-PRN-SPE": "parataxis",
    "MAT-SBJ": "conj",
    "MAT-SPE": "ccomp/xcomp",
    "MAT-SPE-PRN": "ccomp/xcomp",
    "MAT-SPE-PRN-ELAB": "ccomp/xcomp",
    "MAT-SPE-PRN-LFD": "ccomp/xcomp",
    "MAT-SPE-SBJ": "ccomp/xcomp",
    "MAT-SUB-SPE": "ccomp/xcomp",
    "MAT-SMC": "conj",  # same as MAT, occurs once
    "SUB": "conj",
    "SUB-INF": "xcomp",
    "SUB-LFD": "conj",
    "SUB-PRN": "conj",
    "SUB-PRN-ELAB": "conj",
    "SUB-REP": "conj",  # REP = repetition
    "SUB-SPE": "conj",
    "SUB-SPE-PRN": "conj",
    "SUB-SPE-PRN-ELAB": "conj",  # ELAB = elaborations
    "IMP": "ccomp",
    "IMP-PRN": "ccomp",
    "IMP-SPE": "ccomp",
    "IMP-SPE-PRN": "ccomp",
    "IMP-SPE-SBJ": "ccomp",
    "SMC": "ccomp/xcomp",
    "SMC-SBJ": "ccomp/xcomp",
    "SMC-SPE": "ccomp/xcomp",
    "PPL": "acl/advcl",
    "PPL-ABS": "acl/advcl",
    "PPL-ABS-SPE": "acl/advcl",
    "PPL-OB1": "acl/advcl",
    "PPL-OB1-SPE": "acl/advcl",
    "PPL-OB2": "acl/advcl",
    "PPL-PRD": "acl/advcl",
    "PPL-PRN": "acl/advcl",
    "PPL-SBJ": "acl/advcl",
    "PPL-SPE": "acl/advcl",
    "PPL-SPE-OB1": "acl/advcl",
    "PPL-SPE-PRD": "acl/advcl",
    "ABS": "acl/advcl",  # absolutus
    "ABS-PRN": "acl/advcl",
    "ABS-SBJ": "acl/advcl",
}

relation_CP = {
    None: "VANTAR_LIÐ",
    "THT": "ccomp/xcomp",
    "THT-SBJ": "ccomp/xcomp",
    "THT-SBJ-SPE": "ccomp/xcomp",
    "THT-SPE": "ccomp/xcomp",
    "THT-SPE-PRN": "ccomp/xcomp",
    "THT-SPE-SBJ": "ccomp/xcomp",
    "THT-PRN": "ccomp/xcomp",
    "THT-PRN-NaN": "ccomp/xcomp",
    "THT-PRN-SPE": "ccomp/xcomp",
    "THT-LFD": "ccomp/xcomp",
    "THT-RSP": "ccomp/xcomp",  # resumptive element
    "CAR": "acl:relcl",
    "CAR-SPE": "acl:relcl",
    "CLF": "acl:relcl",
    "CLF-SPE": "acl:relcl",
    "CMP": "advcl",
    "CMP-LFD": "advcl",
    "CMP-SPE": "advcl",
    "DEG": "advcl",
    "DEG-SPE": "advcl",
    "FRL": "ccomp/xcomp",  # free relative
    "FRL-SPE": "ccomp/xcomp",
    "REL": "acl:relcl",
    "REL-SPE": "acl:relcl",
    "REL-SPE-PRN": "acl:relcl",
    "QUE": "ccomp/xcomp",
    "QUE-SPE": "ccomp/xcomp",
    "QUE-SPE-LFD": "ccomp/xcomp",
    "QUE-SPE-LFD-PRN": "ccomp/xcomp",
    "QUE-SPE-LFD-SBJ": "ccomp/xcomp",
    "QUE-SPE-PRN": "ccomp/xcomp",
    "QUE-SPE-SBJ": "ccomp/xcomp",
    "QUE-ADV": "ccomp/xcomp",
    "QUE-ADV-LFD": "ccomp/xcomp",
    "QUE-ADV-SPE": "ccomp/xcomp",
    "QUE-ADV-SPE-LFD": "ccomp/xcomp",
    "QUE-LFD": "ccomp/xcomp",
    "QUE-PRN": "ccomp/xcomp",
    "QUE-PRN-ELAB": "ccomp/xcomp",
    "QUE-PRN-SPE": "ccomp/xcomp",
    "QUE-SBJ": "ccomp/xcomp",
    "ADV": "advcl",
    "ADV-LFD": "advcl",
    "ADV-LFD-SPE": "advcl",
    "ADV-PRN": "advcl",
    "ADV-RSP": "advcl",
    "ADV-SPE": "advcl",
    "ADV-SPE-LFD": "advcl",
    "ADV-SPE-PRN": "advcl",
    "EOP": "xcomp",  # infinitival verb always follows, no sbj.
    "EOP-SPE": "xcomp",
    "EOP-SPE-PRN": "xcomp",
    "EXL": "ccomp/xcomp",  # exclamative, same parse as QUE
    "EXL-SPE": "ccomp/xcomp",
    "TMC": "xcomp",  # infinitival verb always follows, no sbj.
    "TMC-SPE": "xcomp",
    "TMP": "xcomp",  # infinitival verb always follows, no sbj.
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

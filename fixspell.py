import json
from itertools import product

# TODO allow adding character overrides in a user-defined file

enderBraille = "-RPGT"

LATIN_ALPHABET_DATA = {
    "minStroke": "*",
    "majStroke": "*P",
    "letters": [
        {
            "majuscule": "A",
            "minuscule": "a",
            "strokes": ["A"],
            "link": "https://en.wikipedia.org/wiki/A",
        },
        {
            "majuscule": "B",
            "minuscule": "b",
            "strokes": ["PW"],
            "link": "https://en.wikipedia.org/wiki/B",
        },
        {
            "majuscule": "C",
            "minuscule": "c",
            "strokes": ["KR"],
            "link": "https://en.wikipedia.org/wiki/C",
        },
        {
            "majuscule": "D",
            "minuscule": "d",
            "strokes": ["TK"],
            "link": "https://en.wikipedia.org/wiki/D",
        },
        {
            "majuscule": "E",
            "minuscule": "e",
            "strokes": ["E"],
            "link": "https://en.wikipedia.org/wiki/E",
        },
        {
            "majuscule": "F",
            "minuscule": "f",
            "strokes": ["TP"],
            "link": "https://en.wikipedia.org/wiki/F",
        },
        {
            "majuscule": "G",
            "minuscule": "g",
            "strokes": ["TKPW"],
            "link": "https://en.wikipedia.org/wiki/G",
        },
        {
            "majuscule": "H",
            "minuscule": "h",
            "strokes": ["H"],
            "link": "https://en.wikipedia.org/wiki/H",
        },
        {
            "majuscule": "I",
            "minuscule": "i",
            "strokes": ["EU"],
            "link": "https://en.wikipedia.org/wiki/I",
        },
        {
            "majuscule": "J",
            "minuscule": "j",
            "strokes": ["SKWR"],
            "link": "https://en.wikipedia.org/wiki/J",
        },
        {
            "majuscule": "K",
            "minuscule": "k",
            "strokes": ["K"],
            "link": "https://en.wikipedia.org/wiki/K",
        },
        {
            "majuscule": "L",
            "minuscule": "l",
            "strokes": ["HR"],
            "link": "https://en.wikipedia.org/wiki/L",
        },
        {
            "majuscule": "M",
            "minuscule": "m",
            "strokes": ["PH"],
            "link": "https://en.wikipedia.org/wiki/M",
        },
        {
            "majuscule": "N",
            "minuscule": "n",
            "strokes": ["TPH"],
            "link": "https://en.wikipedia.org/wiki/N",
        },
        {
            "majuscule": "O",
            "minuscule": "o",
            "strokes": ["O"],
            "link": "https://en.wikipedia.org/wiki/O",
        },
        {
            "majuscule": "P",
            "minuscule": "p",
            "strokes": ["P"],
            "link": "https://en.wikipedia.org/wiki/P",
        },
        {
            "majuscule": "Q",
            "minuscule": "q",
            "strokes": ["KW"],
            "link": "https://en.wikipedia.org/wiki/Q",
        },
        {
            "majuscule": "R",
            "minuscule": "r",
            "strokes": ["R"],
            "link": "https://en.wikipedia.org/wiki/R",
        },
        {
            "majuscule": "S",
            "minuscule": "s",
            "strokes": ["S"],
            "link": "https://en.wikipedia.org/wiki/S",
        },
        {
            "majuscule": "T",
            "minuscule": "t",
            "strokes": ["T"],
            "link": "https://en.wikipedia.org/wiki/T",
        },
        {
            "majuscule": "U",
            "minuscule": "u",
            "strokes": ["U"],
            "link": "https://en.wikipedia.org/wiki/U",
        },
        {
            "majuscule": "V",
            "minuscule": "v",
            "strokes": ["SR"],
            "link": "https://en.wikipedia.org/wiki/V",
        },
        {
            "majuscule": "W",
            "minuscule": "w",
            "strokes": ["W"],
            "link": "https://en.wikipedia.org/wiki/W",
        },
        {
            "majuscule": "X",
            "minuscule": "x",
            "strokes": ["KP"],
            "link": "https://en.wikipedia.org/wiki/X",
        },
        {
            "majuscule": "Y",
            "minuscule": "y",
            "strokes": ["KWR"],
            "link": "https://en.wikipedia.org/wiki/Y",
        },
        {
            "majuscule": "Z",
            "minuscule": "z",
            "strokes": ["STKPW", "STK"],
            "link": "https://en.wikipedia.org/wiki/Z",
        },
    ]
}

GREEK_ALPHABET_DATA = {
    "minStroke": "-FLG",
    "majStroke": "*FLG",
    "letters": [
        {
            "name": "alpha",
            "majuscule": "Α",
            "minuscule": "α",
            "strokes": ["A"],
            "link": "https://en.wikipedia.org/wiki/Alpha",
            "docs": "Sounds like A.",
        },
        {
            "name": "beta",
            "majuscule": "Β",
            "minuscule": "β",
            "strokes": ["PW"],
            "link": "https://en.wikipedia.org/wiki/Beta",
            "docs": "Sounds like B.",
        },
        {
            "name": "gamma",
            "majuscule": "Γ",
            "minuscule": "γ",
            "strokes": ["TKPW"],
            "link": "https://en.wikipedia.org/wiki/Gamma",
            "docs": "Sounds like G.",
        },
        {
            "name": "delta",
            "majuscule": "Δ",
            "minuscule": "δ",
            "strokes": ["TK"],
            "link": "https://en.wikipedia.org/wiki/Delta_(letter)",
            "docs": "Sounds like D.",
        },
        {
            "name": "epsilon",
            "majuscule": "Ε",
            "minuscule": "ε",
            "strokes": ["E"],
            "link": "https://en.wikipedia.org/wiki/Epsilon",
            "docs": "Sounds like E",
        },
        {
            "name": "zeta",
            "majuscule": "Ζ",
            "minuscule": "ζ",
            "strokes": ["STKPW"],
            "link": "https://en.wikipedia.org/wiki/Zeta",
            "docs": "Sounds like Z.",
        },
        {
            "name": "eta",
            "majuscule": "Η",
            "minuscule": "η",
            "strokes": ["AEU"],
            "link": "https://en.wikipedia.org/wiki/Eta",
            "docs": "Makes the Ā sound.",
        },
        {
            "name": "theta",
            "majuscule": "Θ",
            "minuscule": "θ",
            "strokes": ["TH"],
            "link": "https://en.wikipedia.org/wiki/Theta",
            "docs": "Makes the TH sound.",
        },
        {
            "name": "iota",
            "majuscule": "Ι",
            "minuscule": "ι",
            "strokes": ["EU"],
            "link": "https://en.wikipedia.org/wiki/Iota",
            "docs": "Sounds like I.",
        },
        {
            "name": "kappa",
            "majuscule": "Κ",
            "minuscule": "κ",
            "strokes": ["K"],
            "link": "https://en.wikipedia.org/wiki/Kappa",
            "docs": "Sounds like K.",
        },
        {
            "name": "lambda",
            "majuscule": "Λ",
            "minuscule": "λ",
            "strokes": ["HR"],
            "link": "https://en.wikipedia.org/wiki/Lambda",
            "docs": "Sounds like L.",
        },
        {
            "name": "mu",
            "majuscule": "Μ",
            "minuscule": "μ",
            "strokes": ["PH"],
            "link": "https://en.wikipedia.org/wiki/Mu_(letter)",
            "docs": "Sounds like M.",
        },
        {
            "name": "nu",
            "majuscule": "Ν",
            "minuscule": "ν",
            "strokes": ["TPH"],
            "link": "https://en.wikipedia.org/wiki/Nu_(letter)",
            "docs": "We use the N chord, for the sound, even though the lowercase looks like a v.",
        },
        {
            "name": "xi",
            "majuscule": "Ξ",
            "minuscule": "ξ",
            "strokes": ["KP"],
            "link": "https://en.wikipedia.org/wiki/Xi_(letter)",
            "docs": "Sounds like X.",
        },
        {
            "name": "omicron",
            "majuscule": "Ο",
            "minuscule": "ο",
            "strokes": ["O"],
            "link": "https://en.wikipedia.org/wiki/Omicron",
            "docs": "Sounds like O.",
        },
        {
            "name": "pi",
            "majuscule": "Π",
            "minuscule": "π",
            "strokes": ["P"],
            "link": "https://en.wikipedia.org/wiki/Pi_(letter)",
            "docs": "Sounds like P.",
        },
        {
            "name": "rho",
            "majuscule": "Ρ",
            "minuscule": "ρ",
            "strokes": ["R"],
            "link": "https://en.wikipedia.org/wiki/Rho",
            "docs": "It looks like a P, but we respect that it sounds like an R.",
        },
        {
            "name": "sigma",
            "majuscule": "Σ",
            "minuscule": "σ",
            "strokes": ["S"],
            "link": "https://en.wikipedia.org/wiki/Sigma",
            "docs": "Sounds like S.",
        },
        {
            "name": "word-final sigma",
            "majuscule": None,
            "minuscule": "ς",
            "strokes": ["SE"],
            "link": "https://en.wikipedia.org/wiki/Sigma",
            "docs": "This system is built around majuscule/minuscule, but then this weirdo second minuscule sigma comes along. The E in the chord is for \"end\" (of word), as it's the word-final variant.",
        },
        {
            "name": "tau",
            "majuscule": "Τ",
            "minuscule": "τ",
            "strokes": ["T"],
            "link": "https://en.wikipedia.org/wiki/Tau",
            "docs": "Sounds like T.",
        },
        {
            "name": "upsilon",
            "majuscule": "Υ",
            "minuscule": "υ",
            "strokes": ["U"],
            "link": "https://en.wikipedia.org/wiki/Upsilon",
            "docs": "The capital looks like a Y, but we respect that it's a U sound.",
        },
        {
            "name": "phi",
            "majuscule": "Φ",
            "minuscule": "φ",
            "strokes": ["TP"],
            "link": "https://en.wikipedia.org/wiki/Phi",
            "docs": "Sounds like F.",
        },
        {
            "name": "chi",
            "majuscule": "Χ",
            "minuscule": "χ",
            "strokes": ["KH"],
            "link": "https://en.wikipedia.org/wiki/Chi_(letter)",
            "docs": "It's actual sound is hard to represent in steno, but CH is a reasonable fit. The Latin English steno X shape is in use by Xi, so we he can't provide it as an orthographic alternate for this one.",
        },
        {
            "name": "psi",
            "majuscule": "Ψ",
            "minuscule": "ψ",
            "strokes": ["SP"],
            "link": "https://en.wikipedia.org/wiki/Psi_(Greek)",
            "docs": "Sounds like PS (as in \"lapse\"), so we used the swapped form, as we don't have a PS sound on the left-hand side, where the consonants live.",
        },
        {
            "name": "omega",
            "majuscule": "Ω",
            "minuscule": "ω",
            "strokes": ["OE"],
            "link": "https://en.wikipedia.org/wiki/Omega",
            "docs": "O is taken by omicron, which people pronounce with an initial long or short O sound, but this one is only ever the long O, so we use OE for this one.",
        },
    ]
}

RUSSIAN_ALPHABET_DATA = {
    "minStroke": "-RPG",
    "majStroke": "*RPG",
    "letters": [
        {
            "name": "А",
            "majuscule": "А",
            "minuscule": "а",
            "strokes": ["A"],
            "link": "https://en.wikipedia.org/wiki/A_(Cyrillic)",
            "docs": "Sounds like A.",
        },
        {
            "name": "Бэ",
            "majuscule": "Б",
            "minuscule": "б",
            "strokes": ["PW"],
            "link": "https://en.wikipedia.org/wiki/Be_(Cyrillic)",
            "docs": "Sounds like B.",
        },
        {
            "name": "Вэ",
            "majuscule": "В",
            "minuscule": "в",
            "strokes": ["SR"],
            "link": "https://en.wikipedia.org/wiki/Ve_(Cyrillic)",
            "docs": "Sounds like V.",
        },
        {
            "name": "Гэ",
            "majuscule": "Г",
            "minuscule": "г",
            "strokes": ["TKPW"],
            "link": "https://en.wikipedia.org/wiki/Ge_(Cyrillic)",
            "docs": "Sounds like G.",
        },
        {
            "name": "Дэ",
            "majuscule": "Д",
            "minuscule": "д",
            "strokes": ["TK"],
            "link": "https://en.wikipedia.org/wiki/De_(Cyrillic)",
            "docs": "Sounds like D.",
        },
        {
            "name": "Е",
            "majuscule": "Е",
            "minuscule": "е",
            "strokes": ["KWRE"],
            "link": "https://en.wikipedia.org/wiki/Ye_(Cyrillic)",
            "docs": "Makes the YE sound, sort of.",
        },
        {
            "name": "Ё",
            "majuscule": "Ё",
            "minuscule": "ё",
            "strokes": ["KWROE", "KWRO"],
            "link": "https://en.wikipedia.org/wiki/%D0%81",
            "docs": "Makes the YŌ sound. Slightly simpler YO alternate provided.",
        },
        {
            "name": "Жэ",
            "majuscule": "Ж",
            "minuscule": "ж",
            "strokes": ["STKPWH", "STKPW", "SKWR"],
            "link": "https://en.wikipedia.org/wiki/Zhe_(Cyrillic)",
            "docs": "A literal steno ZH, as when this symbol is transliterated to English, i.e. in \"Dr. Zhivago.\" Alternate, simpler form of Z provided, and an alternate J sound as well.",
        },
        {
            "name": "Зэ",
            "majuscule": "З",
            "minuscule": "з",
            "strokes": ["STKPW"],
            "link": "https://en.wikipedia.org/wiki/Ze_(Cyrillic)",
            "docs": "Sounds like Z.",
        },
        {
            "name": "И",
            "majuscule": "И",
            "minuscule": "и",
            "strokes": ["AOE", "EU"],
            "link": "https://en.wikipedia.org/wiki/I_(Cyrillic)",
            "docs": "Makes the Ē sound. A simpler I-sound alternate is provided for anyone who can imagine I as a long E sound; in my Spanish dictionary, I just use I (EU) for all letters I, and don't think of it like the English short I when working in that language.",
        },
        {
            "name": "И Краткое",
            "majuscule": "Й",
            "minuscule": "й",
            "strokes": ["KWR"],
            "link": "https://en.wikipedia.org/wiki/Short_I_(Cyrillic)",
            "docs": "Sounds like Y, sort of.",
        },
        {
            "name": "Ка",
            "majuscule": "К",
            "minuscule": "к",
            "strokes": ["K"],
            "link": "https://en.wikipedia.org/wiki/Ka_(Cyrillic)",
            "docs": "Sounds like K.",
        },
        {
            "name": "Эль",
            "majuscule": "Л",
            "minuscule": "л",
            "strokes": ["HR"],
            "link": "https://en.wikipedia.org/wiki/El_(Cyrillic)",
            "docs": "Sounds like L.",
        },
        {
            "name": "Эм",
            "majuscule": "М",
            "minuscule": "м",
            "strokes": ["PH"],
            "link": "https://en.wikipedia.org/wiki/Em_(Cyrillic)",
            "docs": "Sounds like M.",
        },
        {
            "name": "Эн",
            "majuscule": "Н",
            "minuscule": "н",
            "strokes": ["TPH"],
            "link": "https://en.wikipedia.org/wiki/En_(Cyrillic)",
            "docs": "Sounds like N.",
        },
        {
            "name": "О",
            "majuscule": "О",
            "minuscule": "о",
            "strokes": ["O"],
            "link": "https://en.wikipedia.org/wiki/O_(Cyrillic)",
            "docs": "Sounds like O.",
        },
        {
            "name": "Пэ",
            "majuscule": "П",
            "minuscule": "п",
            "strokes": ["P"],
            "link": "https://en.wikipedia.org/wiki/Pe_(Cyrillic)",
            "docs": "Sounds like P.",
        },
        {
            "name": "Эр",
            "majuscule": "Р",
            "minuscule": "р",
            "strokes": ["R"],
            "link": "https://en.wikipedia.org/wiki/Er_(Cyrillic)",
            "docs": "Sounds like R.",
        },
        {
            "name": "Эс",
            "majuscule": "С",
            "minuscule": "с",
            "strokes": ["S"],
            "link": "https://en.wikipedia.org/wiki/Es_(Cyrillic)",
            "docs": "Sounds like S.",
        },
        {
            "name": "Тэ",
            "majuscule": "Т",
            "minuscule": "т",
            "strokes": ["T"],
            "link": "https://en.wikipedia.org/wiki/Te_(Cyrillic)",
            "docs": "Sounds like T.",
        },
        {
            "name": "У",
            "majuscule": "У",
            "minuscule": "у",
            "strokes": ["AOU", "AO"],
            "link": "https://en.wikipedia.org/wiki/U_(Cyrillic)",
            "docs": "Makes the Ū sound, sort of. An alternate form is included, for anyone who wants to think of that sound from the viewpoint of the orthographic AO →\"oo\" spelling trick in Plover theory.",
        },
        {
            "name": "Эф",
            "majuscule": "Ф",
            "minuscule": "ф",
            "strokes": ["TP"],
            "link": "https://en.wikipedia.org/wiki/Ef_(Cyrillic)",
            "docs": "Sounds like F.",
        },
        {
            "name": "Ха",
            "majuscule": "Х",
            "minuscule": "х",
            "strokes": ["KP"],
            "link": "https://en.wikipedia.org/wiki/Kha_(Cyrillic)",
            "docs": "Uses orthography to get around the conflict with Ч/ч, which makes the \"ch\" sound. As this looks exactly like an X, we go with the steno X chord.",
        },
        {
            "name": "Цэ",
            "majuscule": "Ц",
            "minuscule": "ц",
            "strokes": ["ST"],
            "link": "https://en.wikipedia.org/wiki/Tse_(Cyrillic)",
            "docs": "This is supposed to make the TS sound, as in \"cats\", but we don't have that chord on the left-hand side of the board, so we employ the Plover theory trick of allowing one adjacent sound swap.",
        },
        {
            "name": "Че",
            "majuscule": "Ч",
            "minuscule": "ч",
            "strokes": ["KH"],
            "link": "https://en.wikipedia.org/wiki/Che_(Cyrillic)",
            "docs": "Makes the CH sound.",
        },
        {
            "name": "Ша",
            "majuscule": "Ш",
            "minuscule": "ш",
            "strokes": ["SH"],
            "link": "https://en.wikipedia.org/wiki/Sha_(Cyrillic)",
            "docs": "Makes the SH sound.",
        },
        {
            "name": "Ща",
            "majuscule": "Щ",
            "minuscule": "щ",
            "strokes": ["SKH"],
            "link": "https://en.wikipedia.org/wiki/Shcha",
            "docs": "Think of this one as a letter brief. The sound should be SHCH, like the sound between the words in \"fresh cheese,\" but we don't have that in English steno, so we just merge SH and KH (CH).",
        },
        {
            "name": "твёрдый знак",
            "majuscule": "Ъ",
            "minuscule": "ъ",
            "strokes": ["PWH"],
            "link": "https://en.wikipedia.org/wiki/Hard_sign",
            "docs": "This letter looks like the b in the English alphabet. It doesn't have its own sound, so I'm just leaning on what's visually sensible to an English speaker, and adding the H to denote that this is the hard sign (see: мягкий знак (soft sign)).",
        },
        {
            "name": "Ы",
            "majuscule": "Ы",
            "minuscule": "ы",
            "strokes": ["U"],
            "link": "https://en.wikipedia.org/wiki/Yery",
            "docs": "I'm told this letter makes a sound somewhere between the vowels in \"bit\" and \"put\", and my best take on that is the short U sound.",
        },
        {
            "name": "мягкий знак",
            "majuscule": "Ь",
            "minuscule": "ь",
            "strokes": ["PWR"],
            "link": "https://en.wikipedia.org/wiki/Soft_sign",
            "docs": "Like the hard sign, but with the R instead of the H, to denote the soft sound. The choice of R is positional; H is hard, and R is the soft version below it. (see: твёрдый знак (hard sign)).",
        },
        {
            "name": "Э",
            "majuscule": "Э",
            "minuscule": "э",
            "strokes": ["E"],
            "link": "https://en.wikipedia.org/wiki/E_(Cyrillic)",
            "docs": "Sounds like E.",
        },
        {
            "name": "Ю",
            "majuscule": "Ю",
            "minuscule": "ю",
            "strokes": ["KWRAOU"],
            "link": "https://en.wikipedia.org/wiki/Yu_(Cyrillic)",
            "docs": "Makes the YŪ sound.",
        },
        {
            "name": "Я",
            "majuscule": "Я",
            "minuscule": "я",
            "strokes": ["KWRA"],
            "link": "https://en.wikipedia.org/wiki/Ya_(Cyrillic)",
            "docs": "Makes the YA sound.",
        },
    ]
}

cyrillicNonSlavicAlphabet = [
    {
        "name": "Cyrillic A with breve",
        "majuscule": ("A", "Ӑ"),
        "minuscule": ("a", "ӑ"),
        "modifiers": ["breve"],
        "link": "https://en.wikipedia.org/wiki/A_with_breve_(Cyrillic)",
    },
    {
        "name": "",
        "majuscule": ("A", "Ӓ"),
        "minuscule": ("a", "ӓ"),
        "modifiers": ["diaeresis"],
        "link": "https://en.wikipedia.org/wiki/A_with_diaeresis_(Cyrillic)",
    },
    {
        "name": "",
        "majuscule": ("", "Ґ"),
        "minuscule": ("", "ґ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ђ"),
        "minuscule": ("", "ђ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ѓ"),
        "minuscule": ("", "ѓ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Є"),
        "minuscule": ("", "є"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ѕ"),
        "minuscule": ("", "ѕ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ї"),
        "minuscule": ("", "ї"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ꙇ"),
        "minuscule": ("", "ꙇ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ӣ"),
        "minuscule": ("", "ӣ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ӥ"),
        "minuscule": ("", "ӥ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ј"),
        "minuscule": ("", "ј"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Љ"),
        "minuscule": ("", "љ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Њ"),
        "minuscule": ("", "њ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ӧ"),
        "minuscule": ("", "ӧ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ћ"),
        "minuscule": ("", "ћ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ќ"),
        "minuscule": ("", "ќ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ӯ"),
        "minuscule": ("", "ӯ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ў"),
        "minuscule": ("", "ў"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ӱ"),
        "minuscule": ("", "ӱ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Џ"),
        "minuscule": ("", "џ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "Ꙏ"),
        "minuscule": ("", "ꙏ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "ʼ"),
        "minuscule": ("", "ʼ"),
        "modifiers": [],
        "link": "",
    },
    {
        "name": "",
        "majuscule": ("", "ˮ"),
        "minuscule": ("", "ˮ"),
        "modifiers": [],
        "link": "",
    },
]

# The following Slavic letters don't have code points, and are composed with
# diacritical marks. See: https://en.wikipedia.org/wiki/Cyrillic_script
# А̂а̂ А̄а̄ Е̂е̂ Е̄е̄ Є́є́ З́з́ І́і́ И̂и̂ О̂о̂ О̄о̄ С́с́ У̂у̂


# These string pairs are used to wrap output characters to enforce case.
minWraps = ("{>}{&", "}")
majWraps = ("{-|}{&", "}")

# This is all the modifiers, plus info about each one.
# Modifiers include diacritics, ligatures, rotations, and so on.
MODIFIERS = {

    #      _ _                 _ _   _
    #   __| (_) __ _  ___ _ __(_) |_(_) ___ ___
    #  / _` | |/ _` |/ __| '__| | __| |/ __/ __|
    # | (_| | | (_| | (__| |  | | |_| | (__\__ \
    #  \__,_|_|\__,_|\___|_|  |_|\__|_|\___|___/
    "acute": {
        "outline": "-RP",
        "name": "Acute",
        "docs": "Shaped like the [acute accent](https://en.wikipedia.org/wiki/Acute_accent).",
    },
    "acuteDoubled": {
        "outline": "ERP",
        "name": "Double Acute",
        "docs": "The [double acute accent](https://en.wikipedia.org/wiki/Double_acute_accent) uses the acute modifier shape, with the '[extra](#modifier-tweaks)' tweak.",
    },
    "breve": {
        "outline": "-FRBLG",
        "name": "Breve",
        "docs": "Shaped like the [breve](https://en.wikipedia.org/wiki/Breve).",
    },
    "breveBelow": {
        "outline": "UFRBLG",
        "name": "Breve Below",
        "docs": "The [breve below](https://en.wikipedia.org/wiki/Breve#Breve_below) uses the breve modifier shape, with the '[under](#modifier-tweaks)' tweak.",
    },
    "breveInverted": {
        "outline": "-FRPLG",
        "name": "Breve Inverted",
        "docs": "Shaped like the [inverted breve](https://en.wikipedia.org/wiki/Inverted_breve) symbol.",
    },
    "caron": {
        "outline": "-FBL",
        "name": "Caron",
        "docs": "Shaped like the [caron](https://en.wikipedia.org/wiki/Caron).",
    },
    "cedilla": {
        "outline": "EB",
        "name": "Cedilla",
        "docs": "The [cedilla](https://en.wikipedia.org/wiki/Cedilla) is based on the the \"comma below\" modifier stroke, with the '[extra](#modifier-tweaks)' tweak, because it's like a comma, but a little bit more than a comma.",
    },
    "circumflex": {
        "outline": "-RPG",
        "name": "Circumflex",
        "docs": "Shaped like the [circumflex](https://en.wikipedia.org/wiki/Circumflex).",
    },
    "circumflexBelow": {
        "outline": "URPG",
        "name": "Circumflex Below",
        "docs": "The [circumflex below](https://en.wikipedia.org/wiki/Circumflex#Circumflex_below) uses the circumflex modifier shape, with the '[under](#modifier-tweaks)' tweak.",
    },
    "commaBelow": {
        "outline": "-B",
        "name": "Comma Below",
        "docs": "The [comma below](https://en.wikipedia.org/wiki/Comma#Diacritical_usage) mirrors the shape used for the comma in the [Emily's Symbols](https://github.com/EPLHREU/emily-symbols) plugin.",
    },
    "diaeresis": {
        "outline": "-FL",
        "name": "Diaeresis/Umlaut",
        "docs": "Shaped like the [diaeresis/umlaut](https://en.wikipedia.org/wiki/Two_dots_(diacritic)) symbols.<BR><BR>NOTE: [diaeresis](https://en.wikipedia.org/wiki/Diaeresis_(diacritic)) and [umlaut](https://en.wikipedia.org/wiki/Umlaut_(diacritic)) are distinct concepts, with separate uses, but are represented by the same Unicode code points. They are created via the same outline in this spelling system.",
    },
    "diaeresisBelow": {
        "outline": "-RG",
        "name": "Diaeresis Below",
        "docs": "The diaeresis/umlaut shape, but lower.",
    },
    "dotAbove": {
        "outline": "-F",
        "name": "Dot Above",
        "docs": "A single key, up high, like a [dot above](https://en.wikipedia.org/wiki/Dot_(diacritic)). See dot below.",
    },
    "dotBelow": {
        "outline": "-R",
        "name": "Dot Below",
        "docs": "The [dot below](https://en.wikipedia.org/wiki/Dot_(diacritic)) stroke is chosen to mirror the shape used for the period in the [Emily's Symbols](https://github.com/EPLHREU/emily-symbols) plugin. A single key, down low, like a dot below. See dot above.",
    },
    "grave": {
        "outline": "-FB",
        "name": "Grave",
        "docs": "Shaped like the [grave accent](https://en.wikipedia.org/wiki/Grave_accent).",
    },
    "graveDoubled": {
        "outline": "EFB",
        "name": "Double Grave",
        "docs": "The [double grave](https://en.wikipedia.org/wiki/Double_grave_accent) uses the grave modifier shape, with the '[extra](#modifier-tweaks)' tweak.",
    },
    "hookAbove": {
        "outline": "-FPB",
        "name": "Hook Above",
        "docs": "Shaped like the [hook above](https://en.wikipedia.org/wiki/Hook_above) symbol, sticking up, and curling to the left.",
    },
    "hook": {
        "outline": "-FRP",
        "name": "Hook",
        "docs": "Distinct from 'hook above', which is a detached diacritic, the [hook](https://en.wikipedia.org/wiki/Hook_(diacritic)) is for characters with an attached hook. The hook modifier shape was chosen to match most of its examples in this system, which either curl up, then to the right, or to the left, then down, which makes the same curve. Imagine the chord shape attaching to some at the −R, and others at the −P. Ultimately, however, this one, of all the diacritic modifier chords, will just need to be memorized, because it doesn't visually match every example.",
    },
    "horn": {
        "outline": "-BLG",
        "name": "Horn",
        "docs": "Shaped like the [horn](https://en.wikipedia.org/wiki/Horn_(diacritic)), sticking out to the right and curving upward. The shape is also on the right-hand side of the modifier keys cluster, as the horn attaches to the upper right side of its characters.",
    },
    "interpunct": {
        "outline": "-FR",
        "name": "Interpunct",
        "docs": "The [interpunct](https://en.wikipedia.org/wiki/Interpunct) is an odd one, which joins the dot above and dot below characters. Think of it as the midpoint of the above and below dots, made by stroking both together.",
    },
    "lineBelow": {
        "outline": "UFP",
        "name": "Line Below",
        "docs": "When [line below](https://en.wikipedia.org/wiki/Macron_below) is decomposed into base character + diacritic, the combining character for this set of Unicode composed characters is the macron below. Rather than use the the lower version of the chord, on the bottom row, this uses the '[under](#modifier-tweaks)' tweak with the macron shape, to respect this relation.",
    },
    "macron": {
        "outline": "-FP",
        "name": "Macron",
        "docs": "Shaped like the [macron](https://en.wikipedia.org/wiki/Macron_(diacritic)).",
    },
    "ogonek": {
        "outline": "-PBG", # "little tail"
        "name": "Ogonek",
        "docs": "The [ogonek](https://en.wikipedia.org/wiki/Ogonek), meaning 'little tail' in Polish, hangs off the bottom of its character, curling down and to the right.",
    },
    "ringAbove": {
        "outline": "-FRPB",
        "name": "Ring Above",
        "docs": "For the [ring above](https://en.wikipedia.org/wiki/Ring_(diacritic)) think of this square of keys like a little circle, or ring.",
    },
    "ringBelow": {
        "outline": "UFRPB",
        "name": "Ring Below",
        "docs": "The [ring below](https://en.wikipedia.org/wiki/Ring_(diacritic)) uses the ring above modifier shape, with the '[under](#modifier-tweaks)' tweak.",
    },
    "stroke": {
        "outline": "-RB",
        "name": "Stroke",
        "docs": "The [stroke](https://en.wikipedia.org/wiki/Bar_(diacritic)), or bar, modifier is like the macron, but lower, because it cuts through the character, rather than flying above it.",
    },
    "slash": {
        "outline": "-BL",
        "name": "Slash",
        "docs": "The [slash](https://en.wikipedia.org/wiki/Bar_(diacritic)) is really just a version of the bar, or stroke, but, because certain letters exist in both forms, I gave it its own modifier, to help differentiate between horizontal and vertical strokes/bars. The symbol is like the acute, but shifted, to indicate that it's lower, and cuts through the character. A bit of a stretch, as it's shifted to the right, not down, but other options were used up. Maybe think of it like moving to the right while reading this text, which eventually wraps, and takes you down a line.",
    },
    "tilde": {
        "outline": "-FPBG",
        "name": "Tilde",
        "docs": "Shaped like the [tilde](https://en.wikipedia.org/wiki/Tilde).",
    },
    "tildeBelow": {
        "outline": "UFPBG",
        "name": "Tilde Below",
        "docs": "The tilde modifier shape, with the '[under](#modifier-tweaks)' tweak.",
    },

    #                      _ _  __ _           _   _
    #  _ __ ___   ___   __| (_)/ _(_) ___ __ _| |_(_) ___  _ __  ___
    # | '_ ` _ \ / _ \ / _` | | |_| |/ __/ _` | __| |/ _ \| '_ \/ __|
    # | | | | | | (_) | (_| | |  _| | (_| (_| | |_| | (_) | | | \__ \
    # |_| |_| |_|\___/ \__,_|_|_| |_|\___\__,_|\__|_|\___/|_| |_|___/
    "ligature": {
        "outline": "-FRLG",
        "name": "Ligature",
        "docs": "[Ligatures](https://en.wikipedia.org/wiki/Ligature_(writing)) are two or more graphemes joined together, as in Æ. To output an existing ligature, stroke the two letters in left-to-right order, then stroke this modifier to merge them. Think of the two vertical columns as the two graphemes being joined. For characters that modify ligatures, like the AE ligature with circumflex, or the AE ligature turned, create the ligature first, before modifying it further."
    },
    "turned": {
        "outline": "-RL",
        "name": "Turned/Rotated",
        "docs": "This modifier allows access to characters that are turned, or [rotated](https://en.wikipedia.org/wiki/Rotated_letter).",
    },
    "reversed": {
        "outline": "EURL",
        "name": "Reversed",
        "docs": "The turned modifier shape, with the '[inverted](#modifier-tweaks)' tweak.<BR><BR>This allows access to characters that are flipped, inverted, or reversed.",
    },
    "bold": {
        "outline": "-FRPBLG",
        "name": "Bold",
        "docs": "All the keys. So bold.",
    },
    "italic": {
        "outline": "EUFRPBLG",
        "name": "Italic",
        "docs": "The bold modifier shape, with the '[inverted](#modifier-tweaks)' tweak. In this case, the I (EU) of the tweak stands for \"italic\".",
    },
    "script": {
        "outline": "-RPBL",
        "name": "Script",
        "docs": "Shaped like an S",
    },
    "doubleStruck": {
        "outline": "EFRLG",
        "name": "Double Struck",
        "docs": "Two columns, to represent the two strikes, plus the '[extra](#modifier-tweaks)' tweak, to really hammer home the doubleness of it all.",
    },
    "fraktur": {
        "outline": "EFR",
        "name": "Fraktur",
        "docs": "FR, for \"Fraktur\", plus the '[extra](#modifier-tweaks)' tweak, for extra frakting, and because FR alone was already in use.",
    },
    "sansSerif": {
        "outline": "UFPBL",
        "name": "Sans-Serif",
        "docs": "Shaped like a serifed ascender, with the '[under](#modifier-tweaks)' tweak − here, representing \"un–\", because we're *_not_* seriffing. I apologize for verbing \"serif\".",
    },
    "monospace": {
        "outline": "-PBL",
        "name": "Monospace",
        "docs": "Tough one to think of a chord for. This is just the right-hand side's M and N chords, for \"MoNo\", superimposed."
    },
    "currency": {
        "outline": "-PB",
        "name": "Currency with Bar",
        "docs": "A lot of currency signs [use a bar](https://en.wikipedia.org/wiki/Bar_(diacritic)#Currency_signs_with_bar) through a letter. Not all of them use a vertical bar, but we have to pick a stroke, and this also helps to differentiate this bar from the more typically horizontal bar diacritics through many of the same letters. See Currency with Double Bar.",
    },
    "doubleCurrency": {
        "outline": "EPB",
        "name": "Currency with Double Bar",
        "docs": "Like the Currency with Bar characters, but for those with double bars. See Currency with Bar.",
    },
}

tbd = [
    {
        "name": "A with ogonek (Cyrillic)", # TODO
        "majuscule": ("A", "А̨"),
        "minuscule": ("a", "а̨"),
        "modifiers": ["ogonek"],
        "link": "https://en.wikipedia.org/wiki/A_with_ogonek_(Cyrillic)",
    },
    {
        "name": "Ɛ̧", # TODO
        "majuscule": ("E", "Ɛ̧"),
        "minuscule": ("e", "ɛ̧"),
        "modifiers": [], # TODO
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "Reversed E",
        "majuscule": ("E", "Ǝ"),
        "minuscule": ("e", "ǝ"),
        "modifiers": ["reversed"],
        "link": "https://en.wikipedia.org/wiki/%C6%8E",
    },
    {
        "name": "Eth",
        "majuscule": ("D", "Ð"),
        "minuscule": ("d", "ð"),
        "modifiers": ["slash"],
        "link": "https://en.wikipedia.org/wiki/Eth",
    },
    {
        "name": "Voiced glottal fricative",
        "majuscule": ("H", "Ɦ"),
        "minuscule": ("h", "ɦ"),
        "modifiers": [], # TODO
        "link": "https://en.wikipedia.org/wiki/Voiced_glottal_fricative",
    },
    {
        "name": "Ezh with caron",
        "majuscule": ("", "Ǯ"),
        "minuscule": ("", "ǯ"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/%C7%AE",
    },
    {
        "name": "African D",
        "majuscule": ("D", "Ɖ"),
        "minuscule": ("d", "ɖ"),
        "modifiers": [], # TODO
        "link": "https://en.wikipedia.org/wiki/African_D",
    },
    {
        "name": "palatal nasal", # TODO
        "majuscule": ("N", "Ɲ"),
        "minuscule": ("n", "ɲ"),
        "modifiers": [], # TODO
        "link": "https://en.wikipedia.org/wiki/%C6%9D",
    },
]

MODIFIED_LATIN_CHARS = [

    #  _ _             _
    # | (_) __ _  __ _| |_ _   _ _ __ ___  ___
    # | | |/ _` |/ _` | __| | | | '__/ _ \/ __|
    # | | | (_| | (_| | |_| |_| | | |  __/\__ \
    # |_|_|\__, |\__,_|\__|\__,_|_|  \___||___/
    #      |___/
    {
        "name": "AA ligature",
        "majuscule": ("AA", "Ꜳ"),
        "minuscule": ("aa", "ꜳ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "AE ligature",
        "majuscule": ("AE", "Æ"),
        "minuscule": ("ae", "æ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "AO ligature",
        "majuscule": ("AO", "Ꜵ"),
        "minuscule": ("ao", "ꜵ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "AU ligature",
        "majuscule": ("AU", "Ꜷ"),
        "minuscule": ("au", "ꜷ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "AV ligature",
        "majuscule": ("AV", "Ꜹ"),
        "minuscule": ("av", "ꜻ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "AY ligature",
        "majuscule": ("AY", "Ꜽ"),
        "minuscule": ("ay", "ꜽ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "FF ligature",
        "majuscule": None,
        "minuscule": ("ff", "ﬀ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "FFI ligature",
        "majuscule": None,
        "minuscule": ("ffi", "ﬃ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "FFL ligature",
        "majuscule": None,
        "minuscule": ("ffl", "ﬄ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "FI ligature",
        "majuscule": None,
        "minuscule": ("fi", "ﬁ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "FL ligature",
        "majuscule": None,
        "minuscule": ("fl", "ﬂ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "HV ligature",
        "majuscule": ("Hv", "Ƕ"),
        "minuscule": ("hv", "ƕ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "LB ligature",
        "majuscule": None,
        "minuscule": ("lb", "℔"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "IL ligature",
        "majuscule": ("IL", "Ỻ"),
        "minuscule": ("il", "ỻ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "OE ligature",
        "majuscule": ("OE", "Œ"),
        "minuscule": ("oe", "œ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "OO ligature",
        "majuscule": ("OO", "Ꝏ"),
        "minuscule": ("oo", "ꝏ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "ST ligature",
        "majuscule": None,
        "minuscule": ("st", "ﬆ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "TZ ligature",
        "majuscule": ("TZ", "Ꜩ"),
        "minuscule": ("tz", "ꜩ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "UE ligature",
        "majuscule": None,
        "minuscule": ("ue", "ᵫ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "UO ligature",
        "majuscule": None,
        "minuscule": ("uo", "ꭣ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "VV ligature",
        "majuscule": ("VV", "W"), # literally just capital W (U+OO57)
        "minuscule": ("vv", "w"), # literally just lowercase W (U+OO77)
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "VY ligature",
        "majuscule": ("VY", "Ꝡ"),
        "minuscule": ("vy", "ꝡ"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)",
    },
    {
        "name": "Eszett (SZ ligature)",
        "majuscule": ("SZ", "ẞ"),
        "minuscule": ("sz", "ß"),
        "modifiers": ["ligature"],
        "link": "https://en.wikipedia.org/wiki/%C3%9F",
    },

    #  _                        __
    # | |_ _ __ __ _ _ __  ___ / _| ___  _ __ _ __ ___  ___
    # | __| '__/ _` | '_ \/ __| |_ / _ \| '__| '_ ` _ \/ __|
    # | |_| | | (_| | | | \__ \  _| (_) | |  | | | | | \__ \
    #  \__|_|  \__,_|_| |_|___/_|  \___/|_|  |_| |_| |_|___/
    #
    {
        "name": "Schwa",
        "majuscule": ("E", "Ə"),
        "minuscule": ("e", "ə"),
        "modifiers": ["turned"],
        "link": "https://en.wikipedia.org/wiki/Mid_central_vowel",
    },
    {
        "name": "Reversed C",
        "majuscule": ("C", "Ↄ"),
        "minuscule": ("c", "ↄ"),
        "modifiers": ["reversed"],
        "link": "https://en.wikipedia.org/wiki/Claudian_letters", # TODO research these
    },
    {
        "name": "Turned F",
        "majuscule": ("F", "Ⅎ"),
        "minuscule": ("f", "ⅎ"),
        "modifiers": ["turned"],
        "link": "https://en.wikipedia.org/wiki/Claudian_letters", # TODO research these
    },

    #  _ _             _                        _ _                 _ _   _
    # | (_) __ _  __ _| |_ _   _ _ __ ___    __| (_) __ _  ___ _ __(_) |_(_) ___ ___
    # | | |/ _` |/ _` | __| | | | '__/ _ \  / _` | |/ _` |/ __| '__| | __| |/ __/ __|
    # | | | (_| | (_| | |_| |_| | | |  __/ | (_| | | (_| | (__| |  | | |_| | (__\__ \
    # |_|_|\__, |\__,_|\__|\__,_|_|  \___|  \__,_|_|\__,_|\___|_|  |_|\__|_|\___|___/
    #      |___/
    {
        "name": "AE ligature with acute",
        "majuscule": ("AE", "Ǽ"),
        "minuscule": ("ae", "ǽ"),
        "modifiers": ["ligature", "acute"],
        "link": "https://en.wikipedia.org/wiki/%C3%86",
    },
    {
        "name": "AE ligature with macron",
        "majuscule": ("AE", "Ǣ"),
        "minuscule": ("ae", "ǣ"),
        "modifiers": ["ligature", "macron"],
        "link": "https://en.wikipedia.org/wiki/%C3%86",
    },

    #  _                             _   _ _             _
    # | |_ _   _ _ __ _ __   ___  __| | | (_) __ _  __ _| |_ _   _ _ __ ___  ___
    # | __| | | | '__| '_ \ / _ \/ _` | | | |/ _` |/ _` | __| | | | '__/ _ \/ __|
    # | |_| |_| | |  | | | |  __/ (_| | | | | (_| | (_| | |_| |_| | | |  __/\__ \
    #  \__|\__,_|_|  |_| |_|\___|\__,_| |_|_|\__, |\__,_|\__|\__,_|_|  \___||___/
    #                                        |___/
    {
        "name": "AE ligature turned",
        "majuscule": None,
        "minuscule": ("ae", "ᴂ"),
        "modifiers": ["ligature", "turned"],
        "link": "https://en.wiktionary.org/wiki/%E1%B4%82#Translingual",
    },

    #      _ _                 _ _   _
    #   __| (_) __ _  ___ _ __(_) |_(_) ___ ___
    #  / _` | |/ _` |/ __| '__| | __| |/ __/ __|
    # | (_| | | (_| | (__| |  | | |_| | (__\__ \
    #  \__,_|_|\__,_|\___|_|  |_|\__|_|\___|___/
    #
    {
        "name": "A with ogonek",
        "majuscule": ("A", "Ą"),
        "minuscule": ("a", "ą"),
        "modifiers": ["ogonek"], #TODO look more into ogonek
        "link": "https://en.wikipedia.org/wiki/%C4%84",
    },
    {
        "name": "B with hook",
        "majuscule": ("B", "Ɓ"),
        "minuscule": ("b", "ɓ"),
        "modifiers": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%81",
    },
    {
        "name": "C with hook",
        "majuscule": ("C", "Ƈ"),
        "minuscule": ("c", "ƈ"),
        "modifiers": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%87",
    },
    {
        "name": "C with cedilla",
        "majuscule": ("C", "Ç"),
        "minuscule": ("c", "ç"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/%C3%87",
    },
    {
        "name": "D with stroke",
        "majuscule": ("D", "Đ"),
        "minuscule": ("d", "đ"),
        "modifiers": ["stroke"],
        "link": "https://en.wikipedia.org/wiki/D_with_stroke",
    },
    {
        "name": "D with hook",
        "majuscule": ("D", "Ɗ"),
        "minuscule": ("d", "ɗ"),
        "modifiers": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%8A",
    },
    {
        "name": "E with ogonek",
        "majuscule": ("E", "Ę"),
        "minuscule": ("e", "ę"),
        "modifiers": ["ogonek"],
        "link": "https://en.wikipedia.org/wiki/%C4%98",
    },
    {
        "name": "E with cedilla",
        "majuscule": ("E", "Ȩ"),
        "minuscule": ("e", "ȩ"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "F with hook",
        "majuscule": ("F", "Ƒ"),
        "minuscule": ("f", "ƒ"),
        "modifiers": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%91",
    },
    {
        "name": "G with stroke",
        "majuscule": ("G", "Ǥ"),
        "minuscule": ("g", "ǥ"),
        "modifiers": ["stroke"],
        "link": "https://en.wikipedia.org/wiki/G_with_stroke",
    },
    {
        "name": "G with hook",
        "majuscule": ("G", "Ɠ"),
        "minuscule": ("g", "ɠ"),
        "modifiers": ["hook"],
        "link": "https://en.wikipedia.org/wiki/G_with_hook",
    },
    {
        "name": "H with stroke",
        "majuscule": ("H", "Ħ"),
        "minuscule": ("h", "ħ"),
        "modifiers": ["stroke"],
        "link": "https://en.wikipedia.org/wiki/H_with_stroke",
    },
    {
        "name": "I with ogonek",
        "majuscule": ("I", "Į"),
        "minuscule": ("i", "į"),
        "modifiers": ["ogonek"],
        "link": "https://en.wikipedia.org/wiki/%C4%AE",
    },
    {
        "name": "I with bar",
        "majuscule": ("I", "Ɨ"),
        "minuscule": ("i", "ɨ"),
        "modifiers": ["stroke"],
        "link": "https://en.wikipedia.org/wiki/I_with_bar", # TODO look more into bar
    },
    {
        "name": "K with hook",
        "majuscule": ("K", "Ƙ"),
        "minuscule": ("k", "ƙ"),
        "modifiers": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%98",
    },
    {
        "name": "L with stroke",
        "majuscule": ("L", "Ł"),
        "minuscule": ("l", "ł"),
        "modifiers": ["slash"], # TODO look more into stroke
        "link": "https://en.wikipedia.org/wiki/%C5%81",
    },
    {
        "name": "L with bar",
        "majuscule": ("L", "Ƚ"),
        "minuscule": ("l", "ƚ"),
        "modifiers": ["stroke"],
        "link": "https://en.wikipedia.org/wiki/L_with_bar",
    },
    {
        "name": "O with ogonek",
        "majuscule": ("O", "Ǫ"),
        "minuscule": ("o", "ǫ"),
        "modifiers": ["ogonek"],
        "link": "https://en.wikipedia.org/wiki/%C7%AA",
    },
    {
        "name": "O with stroke",
        "majuscule": ("O", "Ø"),
        "minuscule": ("o", "ø"),
        "modifiers": ["slash"],
        "link": "https://en.wikipedia.org/wiki/%C3%98",
    },
    {
        "name": "O with horn",
        "majuscule": ("O", "Ơ"),
        "minuscule": ("o", "ơ"),
        "modifiers": ["horn"],
        "link": "https://en.wikipedia.org/wiki/%C6%A0",
    },
    {
        "name": "P with hook",
        "majuscule": ("P", "Ƥ"),
        "minuscule": ("p", "ƥ"),
        "modifiers": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%A4",
    },
    {
        "name": "R with stroke",
        "majuscule": ("R", "Ɍ"),
        "minuscule": ("r", "ɍ"),
        "modifiers": ["stroke"],
        "link": "https://en.wikipedia.org/wiki/R_with_stroke",
    },
    {
        "name": "S with cedilla",
        "majuscule": ("S", "Ş"),
        "minuscule": ("s", "ş"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/%C5%9E",
    },
    {
        "name": "T with hook",
        "majuscule": ("T", "Ƭ"),
        "minuscule": ("t", "ƭ"),
        "modifiers": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%AC",
    },
    {
        "name": "T with cedilla",
        "majuscule": ("T", "Ţ"),
        "minuscule": ("t", "ţ"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/%C5%A2",
    },
    {
        "name": "T with stroke",
        "majuscule": ("T", "Ŧ"),
        "minuscule": ("t", "ŧ"),
        "modifiers": ["stroke"],
        "link": "https://en.wikipedia.org/wiki/T_with_stroke",
    },
    {
        "name": "U with ogonek",
        "majuscule": ("U", "Ų"),
        "minuscule": ("u", "ų"),
        "modifiers": ["ogonek"],
        "link": "https://en.wikipedia.org/wiki/%C5%B2",
    },
    {
        "name": "U with horn",
        "majuscule": ("U", "Ư"),
        "minuscule": ("u", "ư"),
        "modifiers": ["horn"],
        "link": "https://en.wikipedia.org/wiki/%C6%AF",
    },
    {
        "name": "U with bar",
        "majuscule": ("U", "Ʉ"),
        "minuscule": ("u", "ʉ"),
        "modifiers": ["stroke"],
        "link": "https://en.wikipedia.org/wiki/U_with_bar",
    },
    {
        "name": "Y with hook",
        "majuscule": ("Y", "Ƴ"),
        "minuscule": ("y", "ƴ"),
        "modifiers": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%B3",
    },
    {
        "name": "A with acute",
        "majuscule": ("A", "Á"),
        "minuscule": ("a", "á"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/%C3%81",
    },
    {
        "name": "A with grave",
        "majuscule": ("A", "À"),
        "minuscule": ("a", "à"),
        "modifiers": ["grave"],
        "link": "https://en.wikipedia.org/wiki/%C3%80",
    },
    {
        "name": "A with dot above",
        "majuscule": ("A", "Ȧ"),
        "minuscule": ("a", "ȧ"),
        "modifiers": ["dotAbove"],
        "link": "https://en.wikipedia.org/wiki/%C8%A6",
    },
    {
        "name": "A with circumflex",
        "majuscule": ("A", "Â"),
        "minuscule": ("a", "â"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/%C3%82",
    },
    {
        "name": "A with diaeresis",
        "majuscule": ("A", "Ä"),
        "minuscule": ("a", "ä"),
        "modifiers": ["diaeresis"],
        "link": "https://en.wikipedia.org/wiki/%C3%84",
    },
    {
        "name": "A with diaeresis and macron",
        "majuscule": ("A", "Ǟ"),
        "minuscule": ("a", "ǟ"),
        "modifiers": ["diaeresis", "macron"],
        "link": "https://en.wikipedia.org/wiki/Livonian_language#Alphabet",
    },
    {
        "name": "A with caron",
        "majuscule": ("A", "Ǎ"),
        "minuscule": ("a", "ǎ"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/Caron",
    },
    {
        "name": "A with breve",
        "majuscule": ("A", "Ă"),
        "minuscule": ("a", "ă"),
        "modifiers": ["breve"],
        "link": "https://en.wikipedia.org/wiki/%C4%82",
    },
    {
        "name": "A with macron",
        "majuscule": ("A", "Ā"),
        "minuscule": ("a", "ā"),
        "modifiers": ["macron"],
        "link": "https://en.wikipedia.org/wiki/%C4%80",
    },
    {
        "name": "A with tilde",
        "majuscule": ("A", "Ã"),
        "minuscule": ("a", "ã"),
        "modifiers": ["tilde"],
        "link": "https://en.wikipedia.org/wiki/%C3%83",
    },
    {
        "name": "A with ring above",
        "majuscule": ("A", "Å"),
        "minuscule": ("a", "å"),
        "modifiers": ["ringAbove"],
        "link": "https://en.wikipedia.org/wiki/%C3%85",
    },
    {
        "name": "B with dot below",
        "majuscule": ("B", "Ḅ"),
        "minuscule": ("b", "ḅ"),
        "modifiers": ["dotBelow"],
        "link": "https://en.wikipedia.org/wiki/Dot_(diacritic)",
    },
    {
        "name": "C with acute",
        "majuscule": ("C", "Ć"),
        "minuscule": ("c", "ć"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/%C4%86",
    },
    {
        "name": "C with dot above",
        "majuscule": ("C", "Ċ"),
        "minuscule": ("c", "ċ"),
        "modifiers": ["dotAbove"],
        "link": "https://en.wikipedia.org/wiki/%C4%8A",
    },
    {
        "name": "C with circumflex",
        "majuscule": ("C", "Ĉ"),
        "minuscule": ("c", "ĉ"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/%C4%88",
    },
    {
        "name": "C with caron",
        "majuscule": ("C", "Č"),
        "minuscule": ("c", "č"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/%C4%8C",
    },
    {
        "name": "D with dot below",
        "majuscule": ("D", "Ḍ"),
        "minuscule": ("d", "ḍ"),
        "modifiers": ["dotBelow"],
        "link": "https://en.wikipedia.org/wiki/%E1%B8%8C",
    },
    {
        "name": "D with cedilla",
        "majuscule": ("D", "Ḑ"),
        "minuscule": ("d", "ḑ"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/%E1%B8%90",
    },
    {
        "name": "D with circumflex",
        "majuscule": ("D", "Ḓ"),
        "minuscule": ("d", "ḓ"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/Circumflex",
    },
    {
        "name": "E with acute",
        "majuscule": ("E", "É"),
        "minuscule": ("e", "é"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/%C3%89",
    },
    {
        "name": "E with grave",
        "majuscule": ("E", "È"),
        "minuscule": ("e", "è"),
        "modifiers": ["grave"],
        "link": "https://en.wikipedia.org/wiki/%C3%88",
    },
    {
        "name": "E with dot above",
        "majuscule": ("E", "Ė"),
        "minuscule": ("e", "ė"),
        "modifiers": ["dotAbove"],
        "link": "https://en.wikipedia.org/wiki/%C4%96",
    },
    {
        "name": "E with circumflex",
        "majuscule": ("E", "Ê"),
        "minuscule": ("e", "ê"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/%C3%8A",
    },
    {
        "name": "E with diaeresis",
        "majuscule": ("E", "Ë"),
        "minuscule": ("e", "ë"),
        "modifiers": ["diaeresis"],
        "link": "https://en.wikipedia.org/wiki/%C3%8B",
    },
    {
        "name": "E with caron",
        "majuscule": ("E", "Ě"),
        "minuscule": ("e", "ě"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/%C4%9A",
    },
    {
        "name": "E with breve",
        "majuscule": ("E", "Ĕ"),
        "minuscule": ("e", "ĕ"),
        "modifiers": ["breve"],
        "link": "https://en.wikipedia.org/wiki/Breve#Letters_with_breve",
    },
    {
        "name": "E with macron",
        "majuscule": ("E", "Ē"),
        "minuscule": ("e", "ē"),
        "modifiers": ["macron"],
        "link": "https://en.wikipedia.org/wiki/Macron_(diacritic)",
    },
    {
        "name": "E with tilde",
        "majuscule": ("E", "Ẽ"),
        "minuscule": ("e", "ẽ"),
        "modifiers": ["tilde"],
        "link": "https://en.wikipedia.org/wiki/%E1%BA%BC",
    },
    {
        "name": "E with dot below",
        "majuscule": ("E", "Ẹ"),
        "minuscule": ("e", "ẹ"),
        "modifiers": ["dotBelow"],
        "link": "https://en.wikipedia.org/wiki/Dot_(diacritic)",
    },
    {
        "name": "G with acute",
        "majuscule": ("G", "Ǵ"),
        "minuscule": ("g", "ǵ"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/%C7%B4",
    },
    {
        "name": "G with dot above",
        "majuscule": ("G", "Ġ"),
        "minuscule": ("g", "ġ"),
        "modifiers": ["dotAbove"],
        "link": "https://en.wikipedia.org/wiki/%C4%A0",
    },
    {
        "name": "G with circumflex",
        "majuscule": ("G", "Ĝ"),
        "minuscule": ("g", "ĝ"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/%C4%9C",
    },
    {
        "name": "G with caron",
        "majuscule": ("G", "Ǧ"),
        "minuscule": ("g", "ǧ"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/%C7%A6",
    },
    {
        "name": "G with breve",
        "majuscule": ("G", "Ğ"),
        "minuscule": ("g", "ğ"),
        "modifiers": ["breve"],
        "link": "https://en.wikipedia.org/wiki/%C4%9E",
    },
    {
        "name": "G with cedilla",
        "majuscule": ("G", "Ģ"),
        "minuscule": ("g", "ģ"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/%C4%A2",
    },
    {
        "name": "H with circumflex",
        "majuscule": ("H", "Ĥ"),
        "minuscule": ("h", "ĥ"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/%C4%A4",
    },
    {
        "name": "H with dot below",
        "majuscule": ("H", "Ḥ"),
        "minuscule": ("h", "ḥ"),
        "modifiers": ["dotBelow"],
        "link": "https://en.wikipedia.org/wiki/Dot_(diacritic)",
    },
    {
        "name": "I with acute",
        "majuscule": ("I", "Í"),
        "minuscule": ("i", "í"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/%C3%8D",
    },
    {
        "name": "I with grave",
        "majuscule": ("I", "Ì"),
        "minuscule": ("i", "ì"),
        "modifiers": ["grave"],
        "link": "https://en.wikipedia.org/wiki/%C3%8C",
    },
    {
        "name": "I with dot above",
        "majuscule": ("I", "İ"),
        "minuscule": ("i", "i"), # literally just lowercase i, U+0069
        "modifiers": ["dotAbove"],
        "link": "https://en.wikipedia.org/wiki/%C4%B0",
    },
    {
        "name": "I with circumflex",
        "majuscule": ("I", "Î"),
        "minuscule": ("i", "î"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/%C3%8E",
    },
    {
        "name": "I with diaeresis",
        "majuscule": ("I", "Ï"),
        "minuscule": ("i", "ï"),
        "modifiers": ["diaeresis"],
        "link": "https://en.wikipedia.org/wiki/%C3%8F",
    },
    {
        "name": "I with caron",
        "majuscule": ("I", "Ǐ"),
        "minuscule": ("i", "ǐ"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/Caron",
    },
    {
        "name": "I with breve",
        "majuscule": ("I", "Ĭ"),
        "minuscule": ("i", "ĭ"),
        "modifiers": ["breve"],
        "link": "https://en.wikipedia.org/wiki/Breve",
    },
    {
        "name": "I with macron",
        "majuscule": ("I", "Ī"),
        "minuscule": ("i", "ī"),
        "modifiers": ["macron"],
        "link": "https://en.wikipedia.org/wiki/Macron_(diacritic)",
    },
    {
        "name": "I with tilde",
        "majuscule": ("I", "Ĩ"),
        "minuscule": ("i", "ĩ"),
        "modifiers": ["tilde"],
        "link": "https://en.wikipedia.org/wiki/Tilde",
    },
    {
        "name": "I with dot below",
        "majuscule": ("I", "Ị"),
        "minuscule": ("i", "ị"),
        "modifiers": ["dotBelow"],
        "link": "https://en.wikipedia.org/wiki/Dot_(diacritic)",
    },
    {
        "name": "J with circumflex",
        "majuscule": ("J", "Ĵ"),
        "minuscule": ("j", "ĵ"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/%C4%B4",
    },
    {
        "name": "K with cedilla",
        "majuscule": ("K", "Ķ"),
        "minuscule": ("k", "ķ"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/%C4%B6",
    },
    {
        "name": "K with caron",
        "majuscule": ("K", "Ǩ"),
        "minuscule": ("k", "ǩ"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/%C7%A8",
    },
    {
        "name": "L with acute",
        "majuscule": ("L", "Ĺ"),
        "minuscule": ("l", "ĺ"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/Acute_accent",
    },
    {
        "name": "L with cedilla",
        "majuscule": ("L", "Ļ"),
        "minuscule": ("l", "ļ"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "L with caron",
        "majuscule": ("L", "Ľ"),
        "minuscule": ("l", "ľ"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/%C4%BD",
    },
    {
        "name": "L with interpunct",
        "majuscule": ("L", "Ŀ"),
        "minuscule": ("l", "ŀ"),
        "modifiers": ["interpunct"],
        "link": "https://en.wikipedia.org/wiki/Interpunct#Catalan",
    },
    {
        "name": "L with dot below",
        "majuscule": ("L", "Ḷ"),
        "minuscule": ("l", "ḷ"),
        "modifiers": ["dotBelow"],
        "link": "https://en.wikipedia.org/wiki/%E1%B8%B6",
    },
    {
        "name": "L with circumflex",
        "majuscule": ("L", "Ḽ"),
        "minuscule": ("l", "ḽ"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/Circumflex",
    },
    {
        "name": "N with acute",
        "majuscule": ("N", "Ń"),
        "minuscule": ("n", "ń"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/%C5%83",
    },
    {
        "name": "N with dot above",
        "majuscule": ("N", "Ṅ"),
        "minuscule": ("n", "ṅ"),
        "modifiers": ["dotAbove"],
        "link": "https://en.wikipedia.org/wiki/%E1%B9%84",
    },
    {
        "name": "N with caron",
        "majuscule": ("N", "Ň"),
        "minuscule": ("n", "ň"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/%C5%87",
    },
    {
        "name": "N with tilde",
        "majuscule": ("N", "Ñ"),
        "minuscule": ("n", "ñ"),
        "modifiers": ["tilde"],
        "link": "https://en.wikipedia.org/wiki/%C3%91",
    },
    {
        "name": "N with cedilla",
        "majuscule": ("N", "Ņ"),
        "minuscule": ("n", "ņ"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "N with circumflex",
        "majuscule": ("N", "Ṋ"),
        "minuscule": ("n", "ṋ"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/Circumflex",
    },
    {
        "name": "O with acute",
        "majuscule": ("O", "Ó"),
        "minuscule": ("o", "ó"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/%C3%93",
    },
    {
        "name": "O with grave",
        "majuscule": ("O", "Ò"),
        "minuscule": ("o", "ò"),
        "modifiers": ["grave"],
        "link": "https://en.wikipedia.org/wiki/%C3%92",
    },
    {
        "name": "O with dot above",
        "majuscule": ("O", "Ȯ"),
        "minuscule": ("o", "ȯ"),
        "modifiers": ["dotAbove"],
        "link": "https://en.wikipedia.org/wiki/Dot_(diacritic)",
    },
    {
        "name": "O with dot above and macron",
        "majuscule": ("O", "Ȱ"),
        "minuscule": ("o", "ȱ"),
        "modifiers": ["dotAbove", "macron"],
        "link": "https://en.wikipedia.org/wiki/Dot_(diacritic)",
    },
    {
        "name": "O with circumflex",
        "majuscule": ("O", "Ô"),
        "minuscule": ("o", "ô"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/Circumflex",
    },
    {
        "name": "O with diaeresis",
        "majuscule": ("O", "Ö"),
        "minuscule": ("o", "ö"),
        "modifiers": ["diaeresis"],
        "link": "https://en.wikipedia.org/wiki/%C3%96",
    },
    {
        "name": "O with diaeresis and macron",
        "majuscule": ("O", "Ȫ"),
        "minuscule": ("o", "ȫ"),
        "modifiers": ["diaeresis", "macron"],
        "link": "https://en.wikipedia.org/wiki/%C3%96",
    },
    {
        "name": "O with caron",
        "majuscule": ("O", "Ǒ"),
        "minuscule": ("o", "ǒ"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/Caron",
    },
    {
        "name": "O with breve",
        "majuscule": ("O", "Ŏ"),
        "minuscule": ("o", "ŏ"),
        "modifiers": ["breve"],
        "link": "https://en.wikipedia.org/wiki/Breve",
    },
    {
        "name": "O with macron",
        "majuscule": ("O", "Ō"),
        "minuscule": ("o", "ō"),
        "modifiers": ["macron"],
        "link": "https://en.wikipedia.org/wiki/Macron_(diacritic)",
    },
    {
        "name": "O with tilde",
        "majuscule": ("O", "Õ"),
        "minuscule": ("o", "õ"),
        "modifiers": ["tilde"],
        "link": "https://en.wikipedia.org/wiki/%C3%95"
    },
    {
        "name": "O with tilde and macron",
        "majuscule": ("O", "Ȭ"),
        "minuscule": ("o", "ȭ"),
        "modifiers": ["tilde", "macron"],
        "link": "https://en.wikipedia.org/wiki/Livonian_language#Alphabet",
    },
    {
        "name": "O with double acute",
        "majuscule": ("O", "Ő"),
        "minuscule": ("o", "ő"),
        "modifiers": ["acuteDoubled"],
        "link": "https://en.wikipedia.org/wiki/%C5%90",
    },
    {
        "name": "O with dot below",
        "majuscule": ("O", "Ọ"),
        "minuscule": ("o", "ọ"),
        "modifiers": ["dotBelow"],
        "link": "https://en.wikipedia.org/wiki/Dot_(diacritic)",
    },
    {
        "name": "O with slash and acute",
        "majuscule": ("O", "Ǿ"),
        "minuscule": ("o", "ǿ"),
        "modifiers": ["slash", "acute"],
        "link": "https://en.wikipedia.org/wiki/%C3%98#%C7%BE",
    },
    {
        "name": "O with horn",
        "majuscule": ("O", "Ơ"),
        "minuscule": ("o", "ơ"),
        "modifiers": ["horn"],
        "link": "https://en.wikipedia.org/wiki/%C6%A0",
    },
    {
        "name": "R with acute",
        "majuscule": ("R", "Ŕ"),
        "minuscule": ("r", "ŕ"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/%C5%94",
    },
    {
        "name": "R with caron",
        "majuscule": ("R", "Ř"),
        "minuscule": ("r", "ř"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/%C5%98",
    },
    {
        "name": "R with cedilla",
        "majuscule": ("R", "Ŗ"),
        "minuscule": ("r", "ŗ"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "R with dot below",
        "majuscule": ("R", "Ṛ"),
        "minuscule": ("r", "ṛ"),
        "modifiers": ["dotBelow"],
        "link": "https://en.wikipedia.org/wiki/%E1%B9%9A",
    },
    {
        "name": "S with acute",
        "majuscule": ("S", "Ś"),
        "minuscule": ("s", "ś"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/%C5%9A",
    },
    {
        "name": "S with caron",
        "majuscule": ("S", "Ŝ"),
        "minuscule": ("s", "ŝ"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/%C5%9C",
    },
    {
        "name": "S with dot above",
        "majuscule": ("S", "Ṡ"),
        "minuscule": ("s", "ṡ"), # TODO add "ẛ"
        "modifiers": ["dotAbove"],
        "link": "https://en.wikipedia.org/wiki/%E1%B9%A0",
    },
    {
        "name": "S with caron",
        "majuscule": ("S", "Š"),
        "minuscule": ("s", "š"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/%C5%A0",
    },
    {
        "name": "S with comma below",
        "majuscule": ("S", "Ș"),
        "minuscule": ("s", "ș"),
        "modifiers": ["commaBelow"],
        "link": "https://en.wikipedia.org/wiki/%C8%98",
    },
    {
        "name": "S with dot below",
        "majuscule": ("S", "Ș"),
        "minuscule": ("s", "ș"),
        "modifiers": ["dotBelow"],
        "link": "https://en.wikipedia.org/wiki/%E1%B9%A2",
    },
    {
        "name": "T with caron",
        "majuscule": ("T", "Ť"),
        "minuscule": ("t", "ť"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/%C5%A4",
    },
    {
        "name": "T with comma",
        "majuscule": ("T", "Ț"),
        "minuscule": ("t", "ț"),
        "modifiers": ["commaBelow"],
        "link": "https://en.wikipedia.org/wiki/%C8%9A",
    },
    {
        "name": "T with dot below",
        "majuscule": ("T", "Ṭ"),
        "minuscule": ("t", "ṭ"),
        "modifiers": ["dotBelow"],
        "link": "https://en.wikipedia.org/wiki/%E1%B9%AC",
    },
    {
        "name": "T with circumflex",
        "majuscule": ("T", "Ṱ"),
        "minuscule": ("t", "ṱ"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/Circumflex",
    },
    {
        "name": "U with acute",
        "majuscule": ("U", "Ú"),
        "minuscule": ("u", "ú"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/%C3%9A",
    },
    {
        "name": "U with grave",
        "majuscule": ("U", "Ù"),
        "minuscule": ("u", "ù"),
        "modifiers": ["grave"],
        "link": "https://en.wikipedia.org/wiki/Grave_accent",
    },
    {
        "name": "U with circumflex",
        "majuscule": ("U", "Û"),
        "minuscule": ("u", "û"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/%C3%9B",
    },
    {
        "name": "U with diaeresis",
        "majuscule": ("U", "Ü"),
        "minuscule": ("u", "ü"),
        "modifiers": ["diaeresis"],
        "link": "https://en.wikipedia.org/wiki/%C3%9C",
    },
    {
        "name": "U with caron",
        "majuscule": ("U", "Ǔ"),
        "minuscule": ("u", "ǔ"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/Caron",
    },
    {
        "name": "U with breve",
        "majuscule": ("U", "Ŭ"),
        "minuscule": ("u", "ŭ"),
        "modifiers": ["breve"],
        "link": "https://en.wikipedia.org/wiki/%C5%AC",
    },
    {
        "name": "U with macron",
        "majuscule": ("U", "Ū"),
        "minuscule": ("u", "ū"),
        "modifiers": ["macron"],
        "link": "https://en.wikipedia.org/wiki/Macron_(diacritic)",
    },
    {
        "name": "U with tilde",
        "majuscule": ("U", "Ũ"),
        "minuscule": ("u", "ũ"),
        "modifiers": ["tilde"],
        "link": "https://en.wikipedia.org/wiki/Tilde",
    },
    {
        "name": "U with double acute",
        "majuscule": ("U", "Ű"),
        "minuscule": ("u", "ű"),
        "modifiers": ["acuteDoubled"],
        "link": "https://en.wikipedia.org/wiki/Double_acute_accent#Letters_with_double_acute",
    },
    {
        "name": "U with ring above",
        "majuscule": ("U", "Ů"),
        "minuscule": ("u", "ů"),
        "modifiers": ["ringAbove"],
        "link": "https://en.wikipedia.org/wiki/Ring_(diacritic)",
    },
    {
        "name": "U with dot below",
        "majuscule": ("U", "Ụ"),
        "minuscule": ("u", "ụ"),
        "modifiers": ["dotBelow"],
        "link": "https://en.wikipedia.org/wiki/Dot_(diacritic)",
    },
    {
        "name": "W with acute",
        "majuscule": ("W", "Ẃ"),
        "minuscule": ("w", "ẃ"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/%E1%BA%82",
    },
    {
        "name": "W with grave",
        "majuscule": ("W", "Ẁ"),
        "minuscule": ("w", "ẁ"),
        "modifiers": ["grave"],
        "link": "https://en.wikipedia.org/wiki/Grave_accent",
    },
    {
        "name": "W with circumflex",
        "majuscule": ("W", "Ŵ"),
        "minuscule": ("w", "ŵ"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/Circumflex",
    },
    {
        "name": "W with diaeresis",
        "majuscule": ("W", "Ẅ"),
        "minuscule": ("w", "ẅ"),
        "modifiers": ["diaeresis"],
        "link": "https://en.wikipedia.org/wiki/Two_dots_(diacritic)",
    },
    {
        "name": "X with dot above",
        "majuscule": ("X", "Ẋ"),
        "minuscule": ("x", "ẋ"),
        "modifiers": ["dotAbove"],
        "link": "https://en.wikipedia.org/wiki/%E1%BA%8A",
    },
    {
        "name": "Y with acute",
        "majuscule": ("Y", "Ý"),
        "minuscule": ("y", "ý"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/%C3%9D",
    },
    {
        "name": "Y with grave",
        "majuscule": ("Y", "Ỳ"),
        "minuscule": ("y", "ỳ"),
        "modifiers": ["grave"],
        "link": "https://en.wikipedia.org/wiki/Grave_accent",
    },
    {
        "name": "Y with circumflex",
        "majuscule": ("Y", "Ŷ"),
        "minuscule": ("y", "ŷ"),
        "modifiers": ["circumflex"],
        "link": "https://en.wikipedia.org/wiki/Circumflex",
    },
    {
        "name": "Y with diaeresis",
        "majuscule": ("Y", "Ÿ"),
        "minuscule": ("y", "ÿ"),
        "modifiers": ["diaeresis"],
        "link": "https://en.wikipedia.org/wiki/%C5%B8",
    },
    {
        "name": "Y with macron",
        "majuscule": ("Y", "Ȳ"),
        "minuscule": ("y", "ȳ"),
        "modifiers": ["macron"],
        "link": "https://en.wikipedia.org/wiki/%C8%B2",
    },
    {
        "name": "Y with tilde",
        "majuscule": ("Y", "Ỹ"),
        "minuscule": ("y", "ỹ"),
        "modifiers": ["tilde"],
        "link": "https://en.wikipedia.org/wiki/Tilde",
    },
    {
        "name": "Y with double acute",
        "majuscule": ("Y", "Ӳ"),
        "minuscule": ("y", "ӳ"),
        "modifiers": ["acuteDoubled"],
        "link": "https://en.wikipedia.org/wiki/Double_acute_accent#Letters_with_double_acute",
    },
    {
        "name": "Z with acute",
        "majuscule": ("Z", "Ź"),
        "minuscule": ("z", "ź"),
        "modifiers": ["acute"],
        "link": "https://en.wikipedia.org/wiki/%C5%B9",
    },
    {
        "name": "Z with dot above",
        "majuscule": ("Z", "Ż"),
        "minuscule": ("z", "ż"),
        "modifiers": ["dotAbove"],
        "link": "https://en.wikipedia.org/wiki/%C5%BB",
    },
    {
        "name": "Z with caron",
        "majuscule": ("Z", "Ž"),
        "minuscule": ("z", "ž"),
        "modifiers": ["caron"],
        "link": "https://en.wikipedia.org/wiki/%C5%BD",
    },
    {
        "name": "Z with dot below",
        "majuscule": ("Z", "Ẓ"),
        "minuscule": ("z", "ẓ"),
        "modifiers": ["dotBelow"],
        "link": "https://en.wikipedia.org/wiki/%E1%BA%92",
    },
    {
        "name": "Y with hook above",
        "majuscule": ("Y", "Ỷ"),
        "minuscule": ("y", "ỷ"),
        "modifiers": ["hookAbove"],
        "link": "",
    },
    {
        "name": "Y with dot below",
        "majuscule": ("Y", "Ỵ"),
        "minuscule": ("y", "ỵ"),
        "modifiers": ["dotBelow"],
        "link": "",
    },
    {
        "name": "A with breve and hook above",
        "majuscule": ("A", "Ẳ"),
        "minuscule": ("a", "ẳ"),
        "modifiers": ["breve", "hookAbove"],
        "link": "",
    },
    {
        "name": "A with breve and tilde",
        "majuscule": ("A", "Ẵ"),
        "minuscule": ("a", "ẵ"),
        "modifiers": ["breve", "tilde"],
        "link": "",
    },
    {
        "name": "A with breve and grave",
        "majuscule": ("A", "Ằ"),
        "minuscule": ("a", "ằ"),
        "modifiers": ["breve", "grave"],
        "link": "",
    },
    {
        "name": "A with breve and acute",
        "majuscule": ("A", "Ắ"),
        "minuscule": ("A", "ắ"),
        "modifiers": ["breve", "acute"],
        "link": "",
    },
    {
        "name": "A with hook above",
        "majuscule": ("A", "Ả"),
        "minuscule": ("a", "ả"),
        "modifiers": ["hookAbove"],
        "link": "",
    },
    {
        "name": "A with dot below",
        "majuscule": ("A", "Ạ"),
        "minuscule": ("a", "ạ"),
        "modifiers": ["dotBelow"],
        "link": "",
    },
    {
        "name": "A with breve and dot below",
        "majuscule": ("A", "Ặ"),
        "minuscule": ("a", "ặ"),
        "modifiers": ["breve", "dotBelow"],
        "link": "",
    },
    {
        "name": "A with circumflex and dot below",
        "majuscule": ("A", "Ậ"),
        "minuscule": ("a", "ậ"),
        "modifiers": ["circumflex", "dotBelow"],
        "link": "",
    },
    {
        "name": "A with circumflex and hook above",
        "majuscule": ("A", "Ẩ"),
        "minuscule": ("a", "ẩ"),
        "modifiers": ["circumflex", "hookAbove"],
        "link": "",
    },
    {
        "name": "A with circumflex and tilde",
        "majuscule": ("A", "Ẫ"),
        "minuscule": ("a", "ẫ"),
        "modifiers": ["circumflex", "tilde"],
        "link": "",
    },
    {
        "name": "A with circumflex and grave",
        "majuscule": ("A", "Ầ"),
        "minuscule": ("a", "ầ"),
        "modifiers": ["circumflex", "grave"],
        "link": "",
    },
    {
        "name": "A with circumflex and acute",
        "majuscule": ("A", "Ấ"),
        "minuscule": ("a", "ấ"),
        "modifiers": ["circumflex", "acute"],
        "link": "",
    },
    {
        "name": "O with hook above",
        "majuscule": ("O", "Ỏ"),
        "minuscule": ("o", "ỏ"),
        "modifiers": ["hookAbove"],
        "link": "",
    },
    {
        "name": "O with horn and dot below",
        "majuscule": ("O", "Ợ"),
        "minuscule": ("o", "ợ"),
        "modifiers": ["horn", "dotBelow"],
        "link": "",
    },
    {
        "name": "O with circumflex and dot below",
        "majuscule": ("O", "Ộ"),
        "minuscule": ("o", "ộ"),
        "modifiers": ["circumflex", "dotBelow"],
        "link": "",
    },
    {
        "name": "O with horn and hook above",
        "majuscule": ("O", "Ở"),
        "minuscule": ("o", "ở"),
        "modifiers": ["horn", "hookAbove"],
        "link": "",
    },
    {
        "name": "O with horn and tilde",
        "majuscule": ("O", "Ỡ"),
        "minuscule": ("o", "ỡ"),
        "modifiers": ["horn", "tilde"],
        "link": "",
    },
    {
        "name": "O with horn and grave",
        "majuscule": ("O", "Ờ"),
        "minuscule": ("o", "ờ"),
        "modifiers": ["horn", "grave"],
        "link": "",
    },
    {
        "name": "O with horn and acute",
        "majuscule": ("O", "Ớ"),
        "minuscule": ("o", "ớ"),
        "modifiers": ["horn", "acute"],
        "link": "",
    },
    {
        "name": "O with circumflex and hook above",
        "majuscule": ("O", "Ổ"),
        "minuscule": ("o", "ổ"),
        "modifiers": ["circumflex", "hookAbove"],
        "link": "",
    },
    {
        "name": "O with circumflex and tilde",
        "majuscule": ("O", "Ỗ"),
        "minuscule": ("o", "ỗ"),
        "modifiers": ["circumflex", "tilde"],
        "link": "",
    },
    {
        "name": "O with circumflex and grave",
        "majuscule": ("O", "Ồ"),
        "minuscule": ("o", "ồ"),
        "modifiers": ["circumflex", "grave"],
        "link": "",
    },
    {
        "name": "O with circumflex and acute",
        "majuscule": ("O", "Ố"),
        "minuscule": ("o", "ố"),
        "modifiers": ["circumflex", "acute"],
        "link": "",
    },
    {
        "name": "E with hook above",
        "majuscule": ("E", "Ẻ"),
        "minuscule": ("e", "ẻ"),
        "modifiers": ["hookAbove"],
        "link": "",
    },
    {
        "name": "E with circumflex and dot below",
        "majuscule": ("E", "Ệ"),
        "minuscule": ("e", "ệ"),
        "modifiers": ["circumflex", "dotBelow"],
        "link": "",
    },
    {
        "name": "E with circumflex and hook above",
        "majuscule": ("E", "Ể"),
        "minuscule": ("e", "ể"),
        "modifiers": ["circumflex", "hookAbove"],
        "link": "",
    },
    {
        "name": "E with circumflex and tilde",
        "majuscule": ("E", "Ễ"),
        "minuscule": ("e", "ễ"),
        "modifiers": ["circumflex", "tilde"],
        "link": "",
    },
    {
        "name": "E with circumflex and grave",
        "majuscule": ("E", "Ề"),
        "minuscule": ("e", "ề"),
        "modifiers": ["circumflex", "grave"],
        "link": "",
    },
    {
        "name": "E with circumflex and acute",
        "majuscule": ("E", "Ế"),
        "minuscule": ("e", "ế"),
        "modifiers": ["circumflex", "acute"],
        "link": "",
    },
    {
        "name": "I with hook above",
        "majuscule": ("I", "Ỉ"),
        "minuscule": ("i", "ỉ"),
        "modifiers": ["hookAbove"],
        "link": "",
    },
    {
        "name": "U with hook above",
        "majuscule": ("U", "Ủ"),
        "minuscule": ("u", "ủ"),
        "modifiers": ["hookAbove"],
        "link": "",
    },
    {
        "name": "U with horn and dot below",
        "majuscule": ("U", "Ự"),
        "minuscule": ("u", "ự"),
        "modifiers": ["horn", "dotBelow"],
        "link": "",
    },
    {
        "name": "U with horn and hook above",
        "majuscule": ("U", "Ử"),
        "minuscule": ("u", "ử"),
        "modifiers": ["horn", "hookAbove"],
        "link": "",
    },
    {
        "name": "U with horn and tilde",
        "majuscule": ("U", "Ữ"),
        "minuscule": ("u", "ữ"),
        "modifiers": ["horn", "tilde"],
        "link": "",
    },
    {
        "name": "U with horn and grave",
        "majuscule": ("U", "Ừ"),
        "minuscule": ("u", "ừ"),
        "modifiers": ["horn", "grave"],
        "link": "",
    },
    {
        "name": "U with horn and acute",
        "majuscule": ("U", "Ứ"),
        "minuscule": ("u", "ứ"),
        "modifiers": ["horn", "acute"],
        "link": "",
    },
    {
        "name": "D with caron",
        "majuscule": ("D", "Ď"),
        "minuscule": ("d", "ď"),
        "modifiers": ["caron"],
        "link": "",
    },
    {
        "name": "U with diaeresis and acute",
        "majuscule": ("U", "Ǘ"),
        "minuscule": ("u", "ǘ"),
        "modifiers": ["diaeresis", "acute"],
        "link": "",
    },
    {
        "name": "U with diaeresis and macron",
        "majuscule": ("U", "Ǖ"),
        "minuscule": ("u", "ǖ"),
        "modifiers": ["diaeresis", "macron"],
        "link": "",
    },
    {
        "name": "U with diaeresis and caron",
        "majuscule": ("U", "Ǚ"),
        "minuscule": ("u", "ǚ"),
        "modifiers": ["diaeresis", "macron"],
        "link": "",
    },
    {
        "name": "U with diaeresis and grave",
        "majuscule": ("U", "Ǜ"),
        "minuscule": ("u", "ǜ"),
        "modifiers": ["diaeresis", "grave"],
        "link": "",
    },
    {
        "name": "A with dot above and macron",
        "majuscule": ("A", "Ǡ"),
        "minuscule": ("a", "ǡ"),
        "modifiers": ["dotAbove", "macron"],
        "link": "",
    },
    {
        "name": "O with ogonek and macron",
        "majuscule": ("O", "Ǭ"),
        "minuscule": ("o", "ǭ"),
        "modifiers": ["ogonek", "macron"],
        "link": "",
    },
    {
        "name": "N with grave",
        "majuscule": ("N", "Ǹ"),
        "minuscule": ("n", "ǹ"),
        "modifiers": ["grave"],
        "link": "",
    },
    {
        "name": "A with double grave",
        "majuscule": ("A", "Ȁ"),
        "minuscule": ("a", "ȁ"),
        "modifiers": ["graveDoubled"],
        "link": "",
    },
    {
        "name": "A with inverted breve",
        "majuscule": ("A", "Ȃ"),
        "minuscule": ("a", "ȃ"),
        "modifiers": ["breveInverted"],
        "link": "",
    },
    {
        "name": "E with double grave",
        "majuscule": ("E", "Ȅ"),
        "minuscule": ("e", "ȅ"),
        "modifiers": ["graveDoubled"],
        "link": "",
    },
    {
        "name": "E with inverted breve",
        "majuscule": ("E", "Ȇ"),
        "minuscule": ("e", "ȇ"),
        "modifiers": ["breveInverted"],
        "link": "",
    },
    {
        "name": "I with double grave",
        "majuscule": ("I", "Ȉ"),
        "minuscule": ("i", "ȉ"),
        "modifiers": ["graveDoubled"],
        "link": "",
    },
    {
        "name": "I with inverted breve",
        "majuscule": ("I", "Ȋ"),
        "minuscule": ("i", "ȋ"),
        "modifiers": ["breveInverted"],
        "link": "",
    },
    {
        "name": "O with double grave",
        "majuscule": ("O", "Ȍ"),
        "minuscule": ("o", "ȍ"),
        "modifiers": ["graveDoubled"],
        "link": "",
    },
    {
        "name": "O with inverted breve",
        "majuscule": ("O", "Ȏ"),
        "minuscule": ("o", "ȏ"),
        "modifiers": ["breveInverted"],
        "link": "",
    },
    {
        "name": "R with double grave",
        "majuscule": ("R", "Ȑ"),
        "minuscule": ("r", "ȑ"),
        "modifiers": ["graveDoubled"],
        "link": "",
    },
    {
        "name": "R with inverted breve",
        "majuscule": ("R", "Ȓ"),
        "minuscule": ("r", "ȓ"),
        "modifiers": ["breveInverted"],
        "link": "",
    },
    {
        "name": "U with double grave",
        "majuscule": ("U", "Ȕ"),
        "minuscule": ("u", "ȕ"),
        "modifiers": ["graveDoubled"],
        "link": "",
    },
    {
        "name": "U with inverted breve",
        "majuscule": ("U", "Ȗ"),
        "minuscule": ("u", "ȗ"),
        "modifiers": ["breveInverted"],
        "link": "",
    },
    {
        "name": "H with caron",
        "majuscule": ("H", "Ȟ"),
        "minuscule": ("h", "ȟ"),
        "modifiers": ["caron"],
        "link": "",
    },
    {
        "name": "A with ring below",
        "majuscule": ("A", "Ḁ"),
        "minuscule": ("a", "ḁ"),
        "modifiers": ["ringBelow"],
        "link": "",
    },
    {
        "name": "B with dot above",
        "majuscule": ("B", "Ḃ"),
        "minuscule": ("b", "ḃ"),
        "modifiers": ["dotAbove"],
        "link": "",
    },
    {
        "name": "B with line below",
        "majuscule": ("B", "Ḇ"),
        "minuscule": ("b", "ḇ"),
        "modifiers": ["lineBelow"],
        "link": "",
    },
    {
        "name": "C with cedilla and acute",
        "majuscule": ("C", "Ḉ"),
        "minuscule": ("c", "ḉ"),
        "modifiers": ["cedilla","acute"],
        "link": "",
    },
    {
        "name": "D with dot above",
        "majuscule": ("D", "Ḋ"),
        "minuscule": ("d", "ḋ"),
        "modifiers": ["dotAbove"],
        "link": "",
    },
    {
        "name": "D with line below",
        "majuscule": ("D", "Ḏ"),
        "minuscule": ("d", "ḏ"),
        "modifiers": ["lineBelow"],
        "link": "",
    },
    {
        "name": "E with macron and grave accent",
        "majuscule": ("E", "Ḕ"),
        "minuscule": ("e", "ḕ"),
        "modifiers": ["macron", "grave"],
        "link": "",
    },
    {
        "name": "E with macron and acute",
        "majuscule": ("E", "Ḗ"),
        "minuscule": ("e", "ḗ"),
        "modifiers": ["macron", "acute"],
        "link": "",
    },
    {
        "name": "E with circumflex below",
        "majuscule": ("E", "Ḙ"),
        "minuscule": ("e", "ḙ"),
        "modifiers": ["circumflexBelow"],
        "link": "",
    },
    {
        "name": "E with tilde below",
        "majuscule": ("E", "Ḛ"),
        "minuscule": ("e", "ḛ"),
        "modifiers": ["tildeBelow"],
        "link": "",
    },
    {
        "name": "E with cedilla and breve",
        "majuscule": ("E", "Ḝ"),
        "minuscule": ("e", "ḝ"),
        "modifiers": ["cedilla", "breve"],
        "link": "",
    },
    {
        "name": "F with dot to above",
        "majuscule": ("F", "Ḟ"),
        "minuscule": ("f", "ḟ"),
        "modifiers": ["dotAbove"],
        "link": "",
    },
    {
        "name": "G with macron",
        "majuscule": ("G", "Ḡ"),
        "minuscule": ("g", "ḡ"),
        "modifiers": ["macron"],
        "link": "",
    },
    {
        "name": "H with dot above",
        "majuscule": ("H", "Ḣ"),
        "minuscule": ("h", "ḣ"),
        "modifiers": ["dotAbove"],
        "link": "",
    },
    {
        "name": "H with diaeresis",
        "majuscule": ("H", "Ḧ"),
        "minuscule": ("h", "ḧ"),
        "modifiers": ["diaeresis"],
        "link": "",
    },
    {
        "name": "H with cedilla",
        "majuscule": ("H", "Ḩ"),
        "minuscule": ("h", "ḩ"),
        "modifiers": ["cedilla"],
        "link": "",
    },
    {
        "name": "H with breve below",
        "majuscule": ("H", "Ḫ"),
        "minuscule": ("h", "ḫ"),
        "modifiers": ["breveBelow"],
        "link": "",
    },
    {
        "name": "I with tilde below",
        "majuscule": ("I", "Ḭ"),
        "minuscule": ("I", "ḭ"),
        "modifiers": ["tildeBelow"],
        "link": "",
    },
    {
        "name": "I with diaeresis and acute",
        "majuscule": ("I", "Ḯ"),
        "minuscule": ("i", "ḯ"),
        "modifiers": ["diaeresis", "acute"],
        "link": "",
    },
    {
        "name": "K with acute",
        "majuscule": ("K", "Ḱ"),
        "minuscule": ("k", "ḱ"),
        "modifiers": ["acute"],
        "link": "",
    },
    {
        "name": "K with dot below",
        "majuscule": ("K", "Ḳ"),
        "minuscule": ("k", "ḳ"),
        "modifiers": ["dotBelow"],
        "link": "",
    },
    {
        "name": "K with line below",
        "majuscule": ("K", "Ḵ"),
        "minuscule": ("k", "ḵ"),
        "modifiers": ["lineBelow"],
        "link": "",
    },
    {
        "name": "L with dot below and macron",
        "majuscule": ("L", "Ḹ"),
        "minuscule": ("l", "ḹ"),
        "modifiers": ["dotBelow", "macron"],
        "link": "",
    },
    {
        "name": "L with line below",
        "majuscule": ("L", "Ḻ"),
        "minuscule": ("l", "ḻ"),
        "modifiers": ["lineBelow"],
        "link": "",
    },
    {
        "name": "M with acute",
        "majuscule": ("M", "Ḿ"),
        "minuscule": ("m", "ḿ"),
        "modifiers": ["acute"],
        "link": "",
    },
    {
        "name": "M with dot above",
        "majuscule": ("M", "Ṁ"),
        "minuscule": ("m", "ṁ"),
        "modifiers": ["dotAbove"],
        "link": "",
    },
    {
        "name": "M with dot below",
        "majuscule": ("M", "Ṃ"),
        "minuscule": ("m", "ṃ"),
        "modifiers": ["dotBelow"],
        "link": "",
    },
    {
        "name": "N with dot below",
        "majuscule": ("N", "Ṇ"),
        "minuscule": ("n", "ṇ"),
        "modifiers": ["dotBelow"],
        "link": "",
    },
    {
        "name": "N with line below",
        "majuscule": ("N", "Ṉ"),
        "minuscule": ("n", "ṉ"),
        "modifiers": ["lineBelow"],
        "link": "",
    },
    {
        "name": "O with tilde and acute",
        "majuscule": ("O", "Ṍ"),
        "minuscule": ("o", "ṍ"),
        "modifiers": ["tilde", "acute"],
        "link": "",
    },
    {
        "name": "O with tilde and diaeresis",
        "majuscule": ("O", "Ṏ"),
        "minuscule": ("o", "ṏ"),
        "modifiers": ["tilde", "diaeresis"],
        "link": "",
    },
    {
        "name": "O with macron and grave",
        "majuscule": ("O", "Ṑ"),
        "minuscule": ("o", "ṑ"),
        "modifiers": ["macron", "grave"],
        "link": "",
    },
    {
        "name": "O with macron and acute",
        "majuscule": ("O", "Ṓ"),
        "minuscule": ("o", "ṓ"),
        "modifiers": ["macron", "acute"],
        "link": "",
    },
    {
        "name": "P with acute",
        "majuscule": ("P", "Ṕ"),
        "minuscule": ("p", "ṕ"),
        "modifiers": ["acute"],
        "link": "",
    },
    {
        "name": "P with dot above",
        "majuscule": ("P", "Ṗ"),
        "minuscule": ("p", "ṗ"),
        "modifiers": ["dotAbove"],
        "link": "",
    },
    {
        "name": "R with dot above",
        "majuscule": ("R", "Ṙ"),
        "minuscule": ("r", "ṙ"),
        "modifiers": ["dotAbove"],
        "link": "",
    },
    {
        "name": "R with dot below and macron",
        "majuscule": ("R", "Ṝ"),
        "minuscule": ("r", "ṝ"),
        "modifiers": ["dotBelow", "macron"],
        "link": "",
    },
    {
        "name": "R with line below",
        "majuscule": ("R", "Ṟ"),
        "minuscule": ("r", "ṟ"),
        "modifiers": ["lineBelow"],
        "link": "",
    },
    {
        "name": "S with dot below",
        "majuscule": ("S", "Ṣ"),
        "minuscule": ("s", "ṣ"),
        "modifiers": ["dotBelow"],
        "link": "",
    },
    {
        "name": "S with acute and dot above",
        "majuscule": ("S", "Ṥ"),
        "minuscule": ("s", "ṥ"),
        "modifiers": ["acute", "dotAbove"],
        "link": "",
    },
    {
        "name": "S with caron and dot above",
        "majuscule": ("S", "Ṧ"),
        "minuscule": ("s", "ṧ"),
        "modifiers": ["caron", "dotAbove"],
        "link": "",
    },
    {
        "name": "S with dot below and dot above",
        "majuscule": ("S", "Ṩ"),
        "minuscule": ("s", "ṩ"),
        "modifiers": ["dotBelow", "dotAbove"],
        "link": "",
    },
    {
        "name": "T with dot above",
        "majuscule": ("T", "Ṫ"),
        "minuscule": ("t", "ṫ"),
        "modifiers": ["dotAbove"],
        "link": "",
    },
    {
        "name": "T with line below",
        "majuscule": ("T", "Ṯ"),
        "minuscule": ("t", "ṯ"),
        "modifiers": ["lineBelow"],
        "link": "",
    },
    {
        "name": "U with diaeresis below",
        "majuscule": ("U", "Ṳ"),
        "minuscule": ("u", "ṳ"),
        "modifiers": ["diaeresisBelow"],
        "link": "",
    },
    {
        "name": "U with tilde below",
        "majuscule": ("U", "Ṵ"),
        "minuscule": ("u", "ṵ"),
        "modifiers": ["tildeBelow"],
        "link": "",
    },
    {
        "name": "U with circumflex below",
        "majuscule": ("U", "Ṷ"),
        "minuscule": ("u", "ṷ"),
        "modifiers": ["circumflexBelow"],
        "link": "",
    },
    {
        "name": "U with tilde and acute",
        "majuscule": ("U", "Ṹ"),
        "minuscule": ("u", "ṹ"),
        "modifiers": ["tilde", "acute"],
        "link": "",
    },
    {
        "name": "U with macron and diaeresis",
        "majuscule": ("U", "Ṻ"),
        "minuscule": ("u", "ṻ"),
        "modifiers": ["macron", "diaeresis"],
        "link": "",
    },
    {
        "name": "V with tilde",
        "majuscule": ("V", "Ṽ"),
        "minuscule": ("v", "ṽ"),
        "modifiers": ["tilde"],
        "link": "",
    },
    {
        "name": "V with dot below",
        "majuscule": ("V", "Ṿ"),
        "minuscule": ("v", "ṿ"),
        "modifiers": ["dotBelow"],
        "link": "",
    },
    {
        "name": "W with dot above",
        "majuscule": ("W", "Ẇ"),
        "minuscule": ("w", "ẇ"),
        "modifiers": ["dotAbove"],
        "link": "",
    },
    {
        "name": "W with dot below",
        "majuscule": ("W", "Ẉ"),
        "minuscule": ("w", "ẉ"),
        "modifiers": ["dotBelow"],
        "link": "",
    },
    {
        "name": "X with diaeresis",
        "majuscule": ("X", "Ẍ"),
        "minuscule": ("x", "ẍ"),
        "modifiers": ["diaeresis"],
        "link": "",
    },
    {
        "name": "Y with dot above",
        "majuscule": ("Y", "Ẏ"),
        "minuscule": ("y", "ẏ"),
        "modifiers": ["dotAbove"],
        "link": "",
    },
    {
        "name": "Z with circumflex",
        "majuscule": ("Z", "Ẑ"),
        "minuscule": ("z", "ẑ"),
        "modifiers": ["circumflex"],
        "link": "",
    },
    {
        "name": "Z with line below",
        "majuscule": ("Z", "Ẕ"),
        "minuscule": ("z", "ẕ"),
        "modifiers": ["lineBelow"],
        "link": "",
    },
    {
        "name": "H with line below",
        "majuscule": None,
        "minuscule": ("h", "ẖ"),
        "modifiers": ["lineBelow"],
        "link": "",
    },
    {
        "name": "T with diaeresis",
        "majuscule": None,
        "minuscule": ("t", "ẗ"),
        "modifiers": ["diaeresis"],
        "link": "",
    },
    {
        "name": "W with ring above",
        "majuscule": None,
        "minuscule": ("w", "ẘ"),
        "modifiers": ["ringAbove"],
        "link": "",
    },
    {
        "name": "Y with ring above",
        "majuscule": None,
        "minuscule": ("y", "ẙ"),
        "modifiers": ["ringAbove"],
        "link": "",
    },
    {
        "name": "J with caron",
        "majuscule": None,
        "minuscule": ("j", "ǰ"),
        "modifiers": ["caron"],
        "link": "",
    },

    #  _        _  _____ ___ _   _   __  __    _  _____ _   _
    # | |      / \|_   _|_ _| \ | | |  \/  |  / \|_   _| | | |
    # | |     / _ \ | |  | ||  \| | | |\/| | / _ \ | | | |_| |
    # | |___ / ___ \| |  | || |\  | | |  | |/ ___ \| | |  _  |
    # |_____/_/   \_\_| |___|_| \_| |_|  |_/_/   \_\_| |_| |_|

    #  _           _     _
    # | |__   ___ | | __| |
    # | '_ \ / _ \| |/ _` |
    # | |_) | (_) | | (_| |
    # |_.__/ \___/|_|\__,_|
    {
        "name": "Mathematical Bold A",
        "majuscule": ("A", "𝐀"),
        "minuscule": ("a", "𝐚"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold B",
        "majuscule": ("B", "𝐁"),
        "minuscule": ("b", "𝐛"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold C",
        "majuscule": ("C", "𝐂"),
        "minuscule": ("c", "𝐜"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold D",
        "majuscule": ("D", "𝐃"),
        "minuscule": ("d", "𝐝"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold E",
        "majuscule": ("E", "𝐄"),
        "minuscule": ("e", "𝐞"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold F",
        "majuscule": ("F", "𝐅"),
        "minuscule": ("f", "𝐟"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold G",
        "majuscule": ("G", "𝐆"),
        "minuscule": ("g", "𝐠"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold H",
        "majuscule": ("H", "𝐇"),
        "minuscule": ("h", "𝐡"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold I",
        "majuscule": ("I", "𝐈"),
        "minuscule": ("i", "𝐢"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold J",
        "majuscule": ("J", "𝐉"),
        "minuscule": ("j", "𝐣"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold K",
        "majuscule": ("K", "𝐊"),
        "minuscule": ("k", "𝐤"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold L",
        "majuscule": ("L", "𝐋"),
        "minuscule": ("l", "𝐥"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold M",
        "majuscule": ("M", "𝐌"),
        "minuscule": ("m", "𝐦"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold N",
        "majuscule": ("N", "𝐍"),
        "minuscule": ("n", "𝐧"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold O",
        "majuscule": ("O", "𝐎"),
        "minuscule": ("o", "𝐨"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold P",
        "majuscule": ("P", "𝐏"),
        "minuscule": ("p", "𝐩"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Q",
        "majuscule": ("Q", "𝐐"),
        "minuscule": ("q", "𝐪"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold R",
        "majuscule": ("R", "𝐑"),
        "minuscule": ("r", "𝐫"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold S",
        "majuscule": ("S", "𝐒"),
        "minuscule": ("s", "𝐬"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold T",
        "majuscule": ("T", "𝐓"),
        "minuscule": ("t", "𝐭"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold U",
        "majuscule": ("U", "𝐔"),
        "minuscule": ("u", "𝐮"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold V",
        "majuscule": ("V", "𝐕"),
        "minuscule": ("v", "𝐯"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold W",
        "majuscule": ("W", "𝐖"),
        "minuscule": ("w", "𝐰"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold X",
        "majuscule": ("X", "𝐗"),
        "minuscule": ("x", "𝐱"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Y",
        "majuscule": ("Y", "𝐘"),
        "minuscule": ("y", "𝐲"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Z",
        "majuscule": ("Z", "𝐙"),
        "minuscule": ("z", "𝐳"),
        "modifiers": ["bold"],
    },

    #  _ _        _ _
    # (_) |_ __ _| (_) ___
    # | | __/ _` | | |/ __|
    # | | || (_| | | | (__
    # |_|\__\__,_|_|_|\___|
    {
        "name": "Mathematical Italic A",
        "majuscule": ("A", "𝐴"),
        "minuscule": ("a", "𝑎"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic B",
        "majuscule": ("B", "𝐵"),
        "minuscule": ("b", "𝑏"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic C",
        "majuscule": ("C", "𝐶"),
        "minuscule": ("c", "𝑐"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic D",
        "majuscule": ("D", "𝐷"),
        "minuscule": ("d", "𝑑"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic E",
        "majuscule": ("E", "𝐸"),
        "minuscule": ("e", "𝑒"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic F",
        "majuscule": ("F", "𝐹"),
        "minuscule": ("f", "𝑓"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic G",
        "majuscule": ("G", "𝐺"),
        "minuscule": ("g", "𝑔"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic H",
        "majuscule": ("H", "𝐻"),
        "minuscule": ("h", "𝑯"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic I",
        "majuscule": ("I", "𝐼"),
        "minuscule": ("i", "𝑖"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic J",
        "majuscule": ("J", "𝐽"),
        "minuscule": ("j", "𝑗"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic K",
        "majuscule": ("K", "𝐾"),
        "minuscule": ("k", "𝑘"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic L",
        "majuscule": ("L", "𝐿"),
        "minuscule": ("l", "𝑙"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic M",
        "majuscule": ("M", "𝑀"),
        "minuscule": ("m", "𝑚"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic N",
        "majuscule": ("N", "𝑁"),
        "minuscule": ("n", "𝑛"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic O",
        "majuscule": ("O", "𝑂"),
        "minuscule": ("o", "𝑜"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic P",
        "majuscule": ("P", "𝑃"),
        "minuscule": ("p", "𝑝"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Q",
        "majuscule": ("Q", "𝑄"),
        "minuscule": ("q", "𝑞"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic R",
        "majuscule": ("R", "𝑅"),
        "minuscule": ("r", "𝑟"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic S",
        "majuscule": ("S", "𝑆"),
        "minuscule": ("s", "𝑠"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic T",
        "majuscule": ("T", "𝑇"),
        "minuscule": ("t", "𝑡"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic U",
        "majuscule": ("U", "𝑈"),
        "minuscule": ("u", "𝑢"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic V",
        "majuscule": ("V", "𝑉"),
        "minuscule": ("v", "𝑣"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic W",
        "majuscule": ("W", "𝑊"),
        "minuscule": ("w", "𝑤"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic X",
        "majuscule": ("X", "𝑋"),
        "minuscule": ("x", "𝑥"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Y",
        "majuscule": ("Y", "𝑌"),
        "minuscule": ("y", "𝑦"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Z",
        "majuscule": ("Z", "𝑍"),
        "minuscule": ("z", "𝑧"),
        "modifiers": ["italic"],
    },

    #  _           _     _   _ _        _ _
    # | |__   ___ | | __| | (_) |_ __ _| (_) ___
    # | '_ \ / _ \| |/ _` | | | __/ _` | | |/ __|
    # | |_) | (_) | | (_| | | | || (_| | | | (__
    # |_.__/ \___/|_|\__,_| |_|\__\__,_|_|_|\___|
    {
        "name": "Mathematical Bold Italic A",
        "majuscule": ("A", "𝑨"),
        "minuscule": ("a", "𝒂"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic B",
        "majuscule": ("B", "𝑩"),
        "minuscule": ("b", "𝒃"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic C",
        "majuscule": ("C", "𝑪"),
        "minuscule": ("c", "𝒄"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic D",
        "majuscule": ("D", "𝑫"),
        "minuscule": ("d", "𝒅"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic E",
        "majuscule": ("E", "𝑬"),
        "minuscule": ("e", "𝒆"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic F",
        "majuscule": ("F", "𝑭"),
        "minuscule": ("f", "𝒇"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic G",
        "majuscule": ("G", "𝑮"),
        "minuscule": ("g", "𝒈"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic H",
        "majuscule": ("H", "𝑯"),
        "minuscule": ("h", "𝒉"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic I",
        "majuscule": ("I", "𝑰"),
        "minuscule": ("i", "𝒊"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic J",
        "majuscule": ("J", "𝑱"),
        "minuscule": ("j", "𝒋"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic K",
        "majuscule": ("K", "𝑲"),
        "minuscule": ("k", "𝒌"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic L",
        "majuscule": ("L", "𝑳"),
        "minuscule": ("l", "𝒍"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic M",
        "majuscule": ("M", "𝑴"),
        "minuscule": ("m", "𝒎"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic N",
        "majuscule": ("N", "𝑵"),
        "minuscule": ("n", "𝒏"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic O",
        "majuscule": ("O", "𝑶"),
        "minuscule": ("o", "𝒐"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic P",
        "majuscule": ("P", "𝑷"),
        "minuscule": ("p", "𝒑"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Q",
        "majuscule": ("Q", "𝑸"),
        "minuscule": ("q", "𝒒"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic R",
        "majuscule": ("R", "𝑹"),
        "minuscule": ("r", "𝒓"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic S",
        "majuscule": ("S", "𝑺"),
        "minuscule": ("s", "𝒔"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic T",
        "majuscule": ("T", "𝑻"),
        "minuscule": ("t", "𝒕"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic U",
        "majuscule": ("U", "𝑼"),
        "minuscule": ("u", "𝒖"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic V",
        "majuscule": ("V", "𝑽"),
        "minuscule": ("v", "𝒗"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic W",
        "majuscule": ("W", "𝑾"),
        "minuscule": ("w", "𝒘"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic X",
        "majuscule": ("X", "𝑿"),
        "minuscule": ("x", "𝒙"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Y",
        "majuscule": ("Y", "𝒀"),
        "minuscule": ("y", "𝒚"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Z",
        "majuscule": ("Z", "𝒁"),
        "minuscule": ("z", "𝒛"),
        "modifiers": ["bold", "italic"],
    },

    #                _       _
    #  ___  ___ _ __(_)_ __ | |_
    # / __|/ __| '__| | '_ \| __|
    # \__ \ (__| |  | | |_) | |_
    # |___/\___|_|  |_| .__/ \__|
    #                 |_|
    {
        "name": "Mathematical Script A",
        "majuscule": ("A", "𝒜"),
        "minuscule": ("a", "𝒶"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script B",
        "majuscule": ("B", "𝓑"),
        "minuscule": ("b", "𝒷"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script C",
        "majuscule": ("C", "𝒞"),
        "minuscule": ("c", "𝒸"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script D",
        "majuscule": ("D", "𝒟"),
        "minuscule": ("d", "𝒹"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script E",
        "majuscule": ("E", "𝓔"),
        "minuscule": ("e", "𝓔"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script F",
        "majuscule": ("F", "𝓕"),
        "minuscule": ("f", "𝒻"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script G",
        "majuscule": ("G", "𝒢"),
        "minuscule": ("g", "𝓖"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script H",
        "majuscule": ("H", "𝓗"),
        "minuscule": ("h", "𝒽"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script I",
        "majuscule": ("I", "𝓘"),
        "minuscule": ("i", "𝒾"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script J",
        "majuscule": ("J", "𝒥"),
        "minuscule": ("j", "𝒿"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script K",
        "majuscule": ("K", "𝒦"),
        "minuscule": ("k", "𝓀"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script L",
        "majuscule": ("L", "𝓛"),
        "minuscule": ("l", "𝓁"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script M",
        "majuscule": ("M", "𝓜"),
        "minuscule": ("m", "𝓂"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script N",
        "majuscule": ("N", "𝒩"),
        "minuscule": ("n", "𝓃"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script O",
        "majuscule": ("O", "𝒪"),
        "minuscule": ("o", "𝓞"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script P",
        "majuscule": ("P", "𝒫"),
        "minuscule": ("p", "𝓅"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script Q",
        "majuscule": ("Q", "𝒬"),
        "minuscule": ("q", "𝓆"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script R",
        "majuscule": ("R", "𝓡"),
        "minuscule": ("r", "𝓇"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script S",
        "majuscule": ("S", "𝒮"),
        "minuscule": ("s", "𝓈"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script T",
        "majuscule": ("T", "𝒯"),
        "minuscule": ("t", "𝓉"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script U",
        "majuscule": ("U", "𝒰"),
        "minuscule": ("u", "𝓊"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script V",
        "majuscule": ("V", "𝒱"),
        "minuscule": ("v", "𝓋"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script W",
        "majuscule": ("W", "𝒲"),
        "minuscule": ("w", "𝓌"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script X",
        "majuscule": ("X", "𝒳"),
        "minuscule": ("x", "𝓍"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script Y",
        "majuscule": ("Y", "𝒴"),
        "minuscule": ("y", "𝓎"),
        "modifiers": ["script"],
    },
    {
        "name": "Mathematical Script Z",
        "majuscule": ("Z", "𝒵"),
        "minuscule": ("z", "𝓏"),
        "modifiers": ["script"],
    },

    #  _           _     _                 _       _
    # | |__   ___ | | __| |  ___  ___ _ __(_)_ __ | |_
    # | '_ \ / _ \| |/ _` | / __|/ __| '__| | '_ \| __|
    # | |_) | (_) | | (_| | \__ \ (__| |  | | |_) | |_
    # |_.__/ \___/|_|\__,_| |___/\___|_|  |_| .__/ \__|
    #                                       |_|
    {
        "name": "Mathematical Bold Script A",
        "majuscule": ("A", "𝓐"),
        "minuscule": ("a", "𝓪"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script B",
        "majuscule": ("B", "𝓑"),
        "minuscule": ("b", "𝓫"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script C",
        "majuscule": ("C", "𝓒"),
        "minuscule": ("c", "𝓬"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script D",
        "majuscule": ("D", "𝓓"),
        "minuscule": ("d", "𝓭"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script E",
        "majuscule": ("E", "𝓔"),
        "minuscule": ("e", "𝓮"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script F",
        "majuscule": ("F", "𝓕"),
        "minuscule": ("f", "𝓯"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script G",
        "majuscule": ("G", "𝓖"),
        "minuscule": ("g", "𝓰"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script H",
        "majuscule": ("H", "𝓗"),
        "minuscule": ("h", "𝓱"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script I",
        "majuscule": ("I", "𝓘"),
        "minuscule": ("i", "𝓲"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script J",
        "majuscule": ("J", "𝓙"),
        "minuscule": ("j", "𝓳"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script K",
        "majuscule": ("K", "𝓚"),
        "minuscule": ("k", "𝓴"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script L",
        "majuscule": ("L", "𝓛"),
        "minuscule": ("l", "𝓵"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script M",
        "majuscule": ("M", "𝓜"),
        "minuscule": ("m", "𝓶"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script N",
        "majuscule": ("N", "𝓝"),
        "minuscule": ("n", "𝓷"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script O",
        "majuscule": ("O", "𝓞"),
        "minuscule": ("o", "𝓸"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script P",
        "majuscule": ("P", "𝓟"),
        "minuscule": ("p", "𝓹"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script Q",
        "majuscule": ("Q", "𝓠"),
        "minuscule": ("q", "𝓺"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script R",
        "majuscule": ("R", "𝓡"),
        "minuscule": ("r", "𝓻"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script S",
        "majuscule": ("S", "𝓢"),
        "minuscule": ("s", "𝓼"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script T",
        "majuscule": ("T", "𝓣"),
        "minuscule": ("t", "𝓽"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script U",
        "majuscule": ("U", "𝓤"),
        "minuscule": ("u", "𝓾"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script V",
        "majuscule": ("V", "𝓥"),
        "minuscule": ("v", "𝓿"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script W",
        "majuscule": ("W", "𝓦"),
        "minuscule": ("w", "𝔀"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script X",
        "majuscule": ("X", "𝓧"),
        "minuscule": ("x", "𝔁"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script Y",
        "majuscule": ("Y", "𝓨"),
        "minuscule": ("y", "𝔂"),
        "modifiers": ["bold", "script"],
    },
    {
        "name": "Mathematical Bold Script Z",
        "majuscule": ("Z", "𝓩"),
        "minuscule": ("z", "𝔃"),
        "modifiers": ["bold", "script"],
    },

    #  _____               _    _
    # |  ___| __ __ _  ___| | _| |_ _   _ _ __
    # | |_ | '__/ _` |/ __| |/ / __| | | | '__|
    # |  _|| | | (_| | (__|   <| |_| |_| | |
    # |_|  |_|  \__,_|\___|_|\_\\__|\__,_|_|
    {
        "name": "Mathematical Fraktur A",
        "majuscule": ("A", "𝔄"),
        "minuscule": ("a", "𝔞"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur B",
        "majuscule": ("B", "𝔅"),
        "minuscule": ("b", "𝔟"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur C",
        "majuscule": None,
        "minuscule": ("c", "𝔠"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur D",
        "majuscule": ("D", "𝔇"),
        "minuscule": ("d", "𝔡"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur E",
        "majuscule": ("E", "𝔈"),
        "minuscule": ("e", "𝔢"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur F",
        "majuscule": ("F", "𝔉"),
        "minuscule": ("f", "𝔣"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur G",
        "majuscule": ("G", "𝔊"),
        "minuscule": ("g", "𝔤"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur H",
        "majuscule": None,
        "minuscule": ("h", "𝔥"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur I",
        "majuscule": None,
        "minuscule": ("i", "𝔦"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur J",
        "majuscule": ("J", "𝔍"),
        "minuscule": ("j", "𝔧"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur K",
        "majuscule": ("K", "𝔎"),
        "minuscule": ("k", "𝔨"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur L",
        "majuscule": ("L", "𝔏"),
        "minuscule": ("l", "𝔩"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur M",
        "majuscule": ("M", "𝔐"),
        "minuscule": ("m", "𝔪"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur N",
        "majuscule": ("N", "𝔑"),
        "minuscule": ("n", "𝔫"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur O",
        "majuscule": ("O", "𝔒"),
        "minuscule": ("o", "𝔬"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur P",
        "majuscule": ("P", "𝔓"),
        "minuscule": ("p", "𝔭"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur Q",
        "majuscule": ("Q", "𝔔"),
        "minuscule": ("q", "𝔮"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur R",
        "majuscule": None,
        "minuscule": ("r", "𝔯"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur S",
        "majuscule": ("S", "𝔖"),
        "minuscule": ("s", "𝔰"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur T",
        "majuscule": ("T", "𝔗"),
        "minuscule": ("t", "𝔱"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur U",
        "majuscule": ("U", "𝔘"),
        "minuscule": ("u", "𝔲"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur V",
        "majuscule": ("V", "𝔙"),
        "minuscule": ("v", "𝔳"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur W",
        "majuscule": ("W", "𝔚"),
        "minuscule": ("w", "𝔴"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur X",
        "majuscule": ("X", "𝔛"),
        "minuscule": ("x", "𝔵"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur Y",
        "majuscule": ("Y", "𝔜"),
        "minuscule": ("y", "𝔶"),
        "modifiers": ["fraktur"],
    },
    {
        "name": "Mathematical Fraktur Z",
        "majuscule": None,
        "minuscule": ("z", "𝔷"),
        "modifiers": ["fraktur"],
    },

    #      _             _     _                _                   _
    #   __| | ___  _   _| |__ | | ___       ___| |_ _ __ _   _  ___| | __
    #  / _` |/ _ \| | | | '_ \| |/ _ \_____/ __| __| '__| | | |/ __| |/ /
    # | (_| | (_) | |_| | |_) | |  __/_____\__ \ |_| |  | |_| | (__|   <
    #  \__,_|\___/ \__,_|_.__/|_|\___|     |___/\__|_|   \__,_|\___|_|\_\
    {
        "name": "Mathematical Double-Struck A",
        "majuscule": ("A", "𝔸"),
        "minuscule": ("a", "𝕒"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck B",
        "majuscule": ("B", "𝔹"),
        "minuscule": ("b", "𝕓"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck C",
        "majuscule": None,
        "minuscule": ("c", "𝕔"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck D",
        "majuscule": ("D", "𝔻"),
        "minuscule": ("d", "𝕕"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck E",
        "majuscule": ("E", "𝔼"),
        "minuscule": ("e", "𝕖"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck F",
        "majuscule": ("F", "𝔽"),
        "minuscule": ("f", "𝕗"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck G",
        "majuscule": ("G", "𝔾"),
        "minuscule": ("g", "𝕘"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck H",
        "majuscule": None,
        "minuscule": ("h", "𝕙"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck I",
        "majuscule": ("I", "𝕀"),
        "minuscule": ("i", "𝕚"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck J",
        "majuscule": ("J", "𝕁"),
        "minuscule": ("j", "𝕛"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck K",
        "majuscule": ("K", "𝕂"),
        "minuscule": ("k", "𝕜"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck L",
        "majuscule": ("L", "𝕃"),
        "minuscule": ("l", "𝕝"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck M",
        "majuscule": ("M", "𝕄"),
        "minuscule": ("m", "𝕞"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck N",
        "majuscule": None,
        "minuscule": ("n", "𝕟"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck O",
        "majuscule": ("O", "𝕆"),
        "minuscule": ("o", "𝕠"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck P",
        "majuscule": None,
        "minuscule": ("p", "𝕡"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck Q",
        "majuscule": None,
        "minuscule": ("q", "𝕢"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck R",
        "majuscule": None,
        "minuscule": ("r", "𝕣"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck S",
        "majuscule": ("S", "𝕊"),
        "minuscule": ("s", "𝕤"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck T",
        "majuscule": ("T", "𝕋"),
        "minuscule": ("t", "𝕥"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck U",
        "majuscule": ("U", "𝕌"),
        "minuscule": ("u", "𝕦"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck V",
        "majuscule": ("V", "𝕍"),
        "minuscule": ("v", "𝕧"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck W",
        "majuscule": ("W", "𝕎"),
        "minuscule": ("w", "𝕨"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck X",
        "majuscule": ("X", "𝕏"),
        "minuscule": ("x", "𝕩"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck Y",
        "majuscule": ("Y", "𝕐"),
        "minuscule": ("y", "𝕪"),
        "modifiers": ["doubleStruck"],
    },
    {
        "name": "Mathematical Double-Struck Z",
        "majuscule": None,
        "minuscule": ("z", "𝕫"),
        "modifiers": ["doubleStruck"],
    },

    #  _           _     _   _____          _    _
    # | |__   ___ | | __| | |  ___| __ __ _| | _| |_ _   _ _ __
    # | '_ \ / _ \| |/ _` | | |_ | '__/ _` | |/ / __| | | | '__|
    # | |_) | (_) | | (_| | |  _|| | | (_| |   <| |_| |_| | |
    # |_.__/ \___/|_|\__,_| |_|  |_|  \__,_|_|\_\\__|\__,_|_|
    {
        "name": "Mathematical Bold Fraktur A",
        "majuscule": ("A", "𝕬"),
        "minuscule": ("a", "𝖆"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur B",
        "majuscule": ("B", "𝕭"),
        "minuscule": ("b", "𝖇"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur C",
        "majuscule": ("C", "𝕮"),
        "minuscule": ("c", "𝖈"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur D",
        "majuscule": ("D", "𝕯"),
        "minuscule": ("d", "𝖉"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur E",
        "majuscule": ("E", "𝕰"),
        "minuscule": ("e", "𝖊"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur F",
        "majuscule": ("F", "𝕱"),
        "minuscule": ("f", "𝖋"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur G",
        "majuscule": ("G", "𝕲"),
        "minuscule": ("g", "𝖌"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur H",
        "majuscule": ("H", "𝕳"),
        "minuscule": ("h", "𝖍"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur I",
        "majuscule": ("I", "𝕴"),
        "minuscule": ("i", "𝖎"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur J",
        "majuscule": ("J", "𝕵"),
        "minuscule": ("j", "𝖏"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur K",
        "majuscule": ("K", "𝕶"),
        "minuscule": ("k", "𝖐"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur L",
        "majuscule": ("L", "𝕷"),
        "minuscule": ("l", "𝖑"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur M",
        "majuscule": ("M", "𝕸"),
        "minuscule": ("m", "𝖒"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur N",
        "majuscule": ("N", "𝕹"),
        "minuscule": ("n", "𝖓"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur O",
        "majuscule": ("O", "𝕺"),
        "minuscule": ("o", "𝖔"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur P",
        "majuscule": ("P", "𝕻"),
        "minuscule": ("p", "𝖕"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur Q",
        "majuscule": ("Q", "𝕼"),
        "minuscule": ("q", "𝖖"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur R",
        "majuscule": ("R", "𝕽"),
        "minuscule": ("r", "𝖗"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur S",
        "majuscule": ("S", "𝕾"),
        "minuscule": ("s", "𝖘"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur T",
        "majuscule": ("T", "𝕿"),
        "minuscule": ("t", "𝖙"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur U",
        "majuscule": ("U", "𝖀"),
        "minuscule": ("u", "𝖚"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur V",
        "majuscule": ("V", "𝖁"),
        "minuscule": ("v", "𝖛"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur W",
        "majuscule": ("W", "𝖂"),
        "minuscule": ("w", "𝖜"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur X",
        "majuscule": ("X", "𝖃"),
        "minuscule": ("x", "𝖝"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur Y",
        "majuscule": ("Y", "𝖄"),
        "minuscule": ("y", "𝖞"),
        "modifiers": ["bold", "fraktur"],
    },
    {
        "name": "Mathematical Bold Fraktur Z",
        "majuscule": ("Z", "𝖅"),
        "minuscule": ("z", "𝖟"),
        "modifiers": ["bold", "fraktur"],
    },

    #                                          _  __
    #  ___  __ _ _ __  ___       ___  ___ _ __(_)/ _|
    # / __|/ _` | '_ \/ __|_____/ __|/ _ \ '__| | |_
    # \__ \ (_| | | | \__ \_____\__ \  __/ |  | |  _|
    # |___/\__,_|_| |_|___/     |___/\___|_|  |_|_|
    {
        "name": "Mathematical Sans-Serif A",
        "majuscule": ("A", "𝖠"),
        "minuscule": ("a", "𝖺"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif B",
        "majuscule": ("B", "𝖡"),
        "minuscule": ("b", "𝖻"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif C",
        "majuscule": ("C", "𝖢"),
        "minuscule": ("c", "𝖼"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif D",
        "majuscule": ("D", "𝖣"),
        "minuscule": ("d", "𝖽"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif E",
        "majuscule": ("E", "𝖤"),
        "minuscule": ("e", "𝖾"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif F",
        "majuscule": ("F", "𝖥"),
        "minuscule": ("f", "𝖿"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif G",
        "majuscule": ("G", "𝖦"),
        "minuscule": ("g", "𝗀"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif H",
        "majuscule": ("H", "𝖧"),
        "minuscule": ("h", "𝗁"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif I",
        "majuscule": ("I", "𝖨"),
        "minuscule": ("i", "𝗂"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif J",
        "majuscule": ("J", "𝖩"),
        "minuscule": ("j", "𝗃"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif K",
        "majuscule": ("K", "𝖪"),
        "minuscule": ("k", "𝗄"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif L",
        "majuscule": ("L", "𝖫"),
        "minuscule": ("l", "𝗅"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif M",
        "majuscule": ("M", "𝖬"),
        "minuscule": ("m", "𝗆"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif N",
        "majuscule": ("N", "𝖭"),
        "minuscule": ("n", "𝗇"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif O",
        "majuscule": ("O", "𝖮"),
        "minuscule": ("o", "𝗈"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif P",
        "majuscule": ("P", "𝖯"),
        "minuscule": ("p", "𝗉"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif Q",
        "majuscule": ("Q", "𝖰"),
        "minuscule": ("q", "𝗊"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif R",
        "majuscule": ("R", "𝖱"),
        "minuscule": ("r", "𝗋"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif S",
        "majuscule": ("S", "𝖲"),
        "minuscule": ("s", "𝗌"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif T",
        "majuscule": ("T", "𝖳"),
        "minuscule": ("t", "𝗍"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif U",
        "majuscule": ("U", "𝖴"),
        "minuscule": ("u", "𝗎"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif V",
        "majuscule": ("V", "𝖵"),
        "minuscule": ("v", "𝗏"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif W",
        "majuscule": ("W", "𝖶"),
        "minuscule": ("w", "𝗐"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif X",
        "majuscule": ("X", "𝖷"),
        "minuscule": ("x", "𝗑"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif Y",
        "majuscule": ("Y", "𝖸"),
        "minuscule": ("y", "𝗒"),
        "modifiers": ["sansSerif"],
    },
    {
        "name": "Mathematical Sans-Serif Z",
        "majuscule": ("Z", "𝖹"),
        "minuscule": ("z", "𝗓"),
        "modifiers": ["sansSerif"],
    },

    #                                          _  __   _           _     _
    #  ___  __ _ _ __  ___       ___  ___ _ __(_)/ _| | |__   ___ | | __| |
    # / __|/ _` | '_ \/ __|_____/ __|/ _ \ '__| | |_  | '_ \ / _ \| |/ _` |
    # \__ \ (_| | | | \__ \_____\__ \  __/ |  | |  _| | |_) | (_) | | (_| |
    # |___/\__,_|_| |_|___/     |___/\___|_|  |_|_|   |_.__/ \___/|_|\__,_|
    {
        "name": "Mathematical Sans-Serif Bold A",
        "majuscule": ("A", "𝗔"),
        "minuscule": ("a", "𝗮"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold B",
        "majuscule": ("B", "𝗕"),
        "minuscule": ("b", "𝗯"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold C",
        "majuscule": ("C", "𝗖"),
        "minuscule": ("c", "𝗰"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold D",
        "majuscule": ("D", "𝗗"),
        "minuscule": ("d", "𝗱"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold E",
        "majuscule": ("E", "𝗘"),
        "minuscule": ("e", "𝗲"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold F",
        "majuscule": ("F", "𝗙"),
        "minuscule": ("f", "𝗳"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold G",
        "majuscule": ("G", "𝗚"),
        "minuscule": ("g", "𝗴"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold H",
        "majuscule": ("H", "𝗛"),
        "minuscule": ("h", "𝗵"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold I",
        "majuscule": ("I", "𝗜"),
        "minuscule": ("i", "𝗶"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold J",
        "majuscule": ("J", "𝗝"),
        "minuscule": ("j", "𝗷"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold K",
        "majuscule": ("K", "𝗞"),
        "minuscule": ("k", "𝗸"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold L",
        "majuscule": ("L", "𝗟"),
        "minuscule": ("l", "𝗹"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold M",
        "majuscule": ("M", "𝗠"),
        "minuscule": ("m", "𝗺"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold N",
        "majuscule": ("N", "𝗡"),
        "minuscule": ("n", "𝗻"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold O",
        "majuscule": ("O", "𝗢"),
        "minuscule": ("o", "𝗼"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold P",
        "majuscule": ("P", "𝗣"),
        "minuscule": ("p", "𝗽"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Q",
        "majuscule": ("Q", "𝗤"),
        "minuscule": ("q", "𝗾"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold R",
        "majuscule": ("R", "𝗥"),
        "minuscule": ("r", "𝗿"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold S",
        "majuscule": ("S", "𝗦"),
        "minuscule": ("s", "𝘀"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold T",
        "majuscule": ("T", "𝗧"),
        "minuscule": ("t", "𝘁"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold U",
        "majuscule": ("U", "𝗨"),
        "minuscule": ("u", "𝘂"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold V",
        "majuscule": ("V", "𝗩"),
        "minuscule": ("v", "𝘃"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold W",
        "majuscule": ("W", "𝗪"),
        "minuscule": ("w", "𝘄"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold X",
        "majuscule": ("X", "𝗫"),
        "minuscule": ("x", "𝘅"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Y",
        "majuscule": ("Y", "𝗬"),
        "minuscule": ("y", "𝘆"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Z",
        "majuscule": ("Z", "𝗭"),
        "minuscule": ("z", "𝘇"),
        "modifiers": ["sansSerif", "bold"],
    },

    #                                          _  __   _ _        _ _
    #  ___  __ _ _ __  ___       ___  ___ _ __(_)/ _| (_) |_ __ _| (_) ___
    # / __|/ _` | '_ \/ __|_____/ __|/ _ \ '__| | |_  | | __/ _` | | |/ __|
    # \__ \ (_| | | | \__ \_____\__ \  __/ |  | |  _| | | || (_| | | | (__
    # |___/\__,_|_| |_|___/     |___/\___|_|  |_|_|   |_|\__\__,_|_|_|\___|
    {
        "name": "Mathematical Sans-Serif Italic A",
        "majuscule": ("A", "𝘈"),
        "minuscule": ("a", "𝘢"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic B",
        "majuscule": ("B", "𝘉"),
        "minuscule": ("b", "𝘣"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic C",
        "majuscule": ("C", "𝘊"),
        "minuscule": ("c", "𝘤"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic D",
        "majuscule": ("D", "𝘋"),
        "minuscule": ("d", "𝘥"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic E",
        "majuscule": ("E", "𝘌"),
        "minuscule": ("e", "𝘦"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic F",
        "majuscule": ("F", "𝘍"),
        "minuscule": ("f", "𝘧"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic G",
        "majuscule": ("G", "𝘎"),
        "minuscule": ("g", "𝘨"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic H",
        "majuscule": ("H", "𝘏"),
        "minuscule": ("h", "𝘩"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic I",
        "majuscule": ("I", "𝘐"),
        "minuscule": ("i", "𝘪"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic J",
        "majuscule": ("J", "𝘑"),
        "minuscule": ("j", "𝘫"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic K",
        "majuscule": ("K", "𝘒"),
        "minuscule": ("k", "𝘬"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic L",
        "majuscule": ("L", "𝘓"),
        "minuscule": ("l", "𝘭"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic M",
        "majuscule": ("M", "𝘔"),
        "minuscule": ("m", "𝘮"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic N",
        "majuscule": ("N", "𝘕"),
        "minuscule": ("n", "𝘯"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic O",
        "majuscule": ("O", "𝘖"),
        "minuscule": ("o", "𝘰"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic P",
        "majuscule": ("P", "𝘗"),
        "minuscule": ("p", "𝘱"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic Q",
        "majuscule": ("Q", "𝘘"),
        "minuscule": ("q", "𝘲"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic R",
        "majuscule": ("R", "𝘙"),
        "minuscule": ("r", "𝘳"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic S",
        "majuscule": ("S", "𝘚"),
        "minuscule": ("s", "𝘴"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic T",
        "majuscule": ("T", "𝘛"),
        "minuscule": ("t", "𝘵"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic U",
        "majuscule": ("U", "𝘜"),
        "minuscule": ("u", "𝘶"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic V",
        "majuscule": ("V", "𝘝"),
        "minuscule": ("v", "𝘷"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic W",
        "majuscule": ("W", "𝘞"),
        "minuscule": ("w", "𝘸"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic X",
        "majuscule": ("X", "𝘟"),
        "minuscule": ("x", "𝘹"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic Y",
        "majuscule": ("Y", "𝘠"),
        "minuscule": ("y", "𝘺"),
        "modifiers": ["sansSerif", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Italic Z",
        "majuscule": ("Z", "𝘡"),
        "minuscule": ("z", "𝘻"),
        "modifiers": ["sansSerif", "italic"],
    },

    #                                          _  __   _           _     _
    #  ___  __ _ _ __  ___       ___  ___ _ __(_)/ _| | |__   ___ | | __| |
    # / __|/ _` | '_ \/ __|_____/ __|/ _ \ '__| | |_  | '_ \ / _ \| |/ _` |
    # \__ \ (_| | | | \__ \_____\__ \  __/ |  | |  _| | |_) | (_) | | (_| |
    # |___/\__,_|_| |_|___/     |___/\___|_|  |_|_|   |_.__/ \___/|_|\__,_|
    #
    #  _ _        _ _
    # (_) |_ __ _| (_) ___
    # | | __/ _` | | |/ __|
    # | | || (_| | | | (__
    # |_|\__\__,_|_|_|\___|
    {
        "name": "Mathematical Sans-Serif Bold Italic A",
        "majuscule": ("A", "𝘼"),
        "minuscule": ("a", "𝙖"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic B",
        "majuscule": ("B", "𝘽"),
        "minuscule": ("b", "𝙗"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic C",
        "majuscule": ("C", "𝘾"),
        "minuscule": ("c", "𝙘"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic D",
        "majuscule": ("D", "𝘿"),
        "minuscule": ("d", "𝙙"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic E",
        "majuscule": ("E", "𝙀"),
        "minuscule": ("e", "𝙚"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic F",
        "majuscule": ("F", "𝙁"),
        "minuscule": ("f", "𝙛"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic G",
        "majuscule": ("G", "𝙂"),
        "minuscule": ("g", "𝙜"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic H",
        "majuscule": ("H", "𝙃"),
        "minuscule": ("h", "𝙝"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic I",
        "majuscule": ("I", "𝙄"),
        "minuscule": ("i", "𝙞"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic J",
        "majuscule": ("J", "𝙅"),
        "minuscule": ("j", "𝙟"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic K",
        "majuscule": ("K", "𝙆"),
        "minuscule": ("k", "𝙠"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic L",
        "majuscule": ("L", "𝙇"),
        "minuscule": ("l", "𝙡"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic M",
        "majuscule": ("M", "𝙈"),
        "minuscule": ("m", "𝙢"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic N",
        "majuscule": ("N", "𝙉"),
        "minuscule": ("n", "𝙣"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic O",
        "majuscule": ("O", "𝙊"),
        "minuscule": ("o", "𝙤"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic P",
        "majuscule": ("P", "𝙋"),
        "minuscule": ("p", "𝙥"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Q",
        "majuscule": ("Q", "𝙌"),
        "minuscule": ("q", "𝙦"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic R",
        "majuscule": ("R", "𝙍"),
        "minuscule": ("r", "𝙧"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic S",
        "majuscule": ("S", "𝙎"),
        "minuscule": ("s", "𝙨"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic T",
        "majuscule": ("T", "𝙏"),
        "minuscule": ("t", "𝙩"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic U",
        "majuscule": ("U", "𝙐"),
        "minuscule": ("u", "𝙪"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic V",
        "majuscule": ("V", "𝙑"),
        "minuscule": ("v", "𝙫"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic W",
        "majuscule": ("W", "𝙒"),
        "minuscule": ("w", "𝙬"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic X",
        "majuscule": ("X", "𝙓"),
        "minuscule": ("x", "𝙭"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Y",
        "majuscule": ("Y", "𝙔"),
        "minuscule": ("y", "𝙮"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Z",
        "majuscule": ("Z", "𝙕"),
        "minuscule": ("z", "𝙯"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },

    #  _ __ ___   ___  _ __   ___  ___ _ __   __ _  ___ ___
    # | '_ ` _ \ / _ \| '_ \ / _ \/ __| '_ \ / _` |/ __/ _ \
    # | | | | | | (_) | | | | (_) \__ \ |_) | (_| | (_|  __/
    # |_| |_| |_|\___/|_| |_|\___/|___/ .__/ \__,_|\___\___|
    #                                 |_|
    {
        "name": "Mathematical Monospace A",
        "majuscule": ("A", "𝙰"),
        "minuscule": ("a", "𝚊"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace B",
        "majuscule": ("B", "𝙱"),
        "minuscule": ("b", "𝚋"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace C",
        "majuscule": ("C", "𝙲"),
        "minuscule": ("c", "𝚌"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace D",
        "majuscule": ("D", "𝙳"),
        "minuscule": ("d", "𝚍"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace E",
        "majuscule": ("E", "𝙴"),
        "minuscule": ("e", "𝚎"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace F",
        "majuscule": ("F", "𝙵"),
        "minuscule": ("f", "𝚏"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace G",
        "majuscule": ("G", "𝙶"),
        "minuscule": ("g", "𝚐"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace H",
        "majuscule": ("H", "𝙷"),
        "minuscule": ("h", "𝚑"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace I",
        "majuscule": ("I", "𝙸"),
        "minuscule": ("i", "𝚒"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace J",
        "majuscule": ("J", "𝙹"),
        "minuscule": ("j", "𝚓"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace K",
        "majuscule": ("K", "𝙺"),
        "minuscule": ("k", "𝚔"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace L",
        "majuscule": ("L", "𝙻"),
        "minuscule": ("l", "𝚕"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace M",
        "majuscule": ("M", "𝙼"),
        "minuscule": ("m", "𝚖"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace N",
        "majuscule": ("N", "𝙽"),
        "minuscule": ("n", "𝚗"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace O",
        "majuscule": ("O", "𝙾"),
        "minuscule": ("o", "𝚘"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace P",
        "majuscule": ("P", "𝙿"),
        "minuscule": ("p", "𝚙"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace Q",
        "majuscule": ("Q", "𝚀"),
        "minuscule": ("q", "𝚚"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace R",
        "majuscule": ("R", "𝚁"),
        "minuscule": ("r", "𝚛"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace S",
        "majuscule": ("S", "𝚂"),
        "minuscule": ("s", "𝚜"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace T",
        "majuscule": ("T", "𝚃"),
        "minuscule": ("t", "𝚝"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace U",
        "majuscule": ("U", "𝚄"),
        "minuscule": ("u", "𝚞"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace V",
        "majuscule": ("V", "𝚅"),
        "minuscule": ("v", "𝚟"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace W",
        "majuscule": ("W", "𝚆"),
        "minuscule": ("w", "𝚠"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace X",
        "majuscule": ("X", "𝚇"),
        "minuscule": ("x", "𝚡"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace Y",
        "majuscule": ("Y", "𝚈"),
        "minuscule": ("y", "𝚢"),
        "modifiers": ["monospace"],
    },
    {
        "name": "Mathematical Monospace Z",
        "majuscule": ("Z", "𝚉"),
        "minuscule": ("z", "𝚣"),
        "modifiers": ["monospace"],
    },

    #   ___ _   _ _ __ _ __ ___ _ __   ___ _   _
    #  / __| | | | '__| '__/ _ \ '_ \ / __| | | |
    # | (__| |_| | |  | | |  __/ | | | (__| |_| |
    #  \___|\__,_|_|  |_|  \___|_| |_|\___|\__, |
    #  A bit of a hack with Latin letters  |___/
    {
        "name": "Thai Baht",
        "majuscule": ("B", "฿"),
        "minuscule": None,
        "modifiers": ["currency"],
        "link": "https://en.wikipedia.org/wiki/Thai_baht",
    },
    {
        "name": "Ghanaian Cedi",
        "majuscule": ("C", "₵"),
        "minuscule": None,
        "modifiers": ["currency"],
        "link": "https://en.wikipedia.org/wiki/Ghanaian_cedi",
    },
    {
        "name": "United States Cent",
        "majuscule": ("c", "¢"),
        "minuscule": None,
        "modifiers": ["currency"],
        "link": "https://en.wikipedia.org/wiki/Cent_(currency)",
    },
    {
        "name": "Vietnamese Đồng",
        "majuscule": None,
        "minuscule": ("d", "₫"),
        "modifiers": ["currency"],
        "link": "https://en.wikipedia.org/wiki/Vietnamese_%C4%91%E1%BB%93ng",
    },
    {
        "name": "French Franc",
        "majuscule": ("F", "₣"),
        "minuscule": None,
        "modifiers": ["currency"],
        "link": "https://en.wikipedia.org/wiki/French_franc",
    },
    {
        "name": "Paraguayan Guaraní",
        "majuscule": ("G", "₲"),
        "minuscule": None,
        "modifiers": ["currency"],
        "link": "https://en.wikipedia.org/wiki/Paraguayan_guaran%C3%AD",
    },
    {
        "name": "Laotian Kip",
        "majuscule": ("K", "₭"),
        "minuscule": None,
        "modifiers": ["currency"],
        "link": "https://en.wikipedia.org/wiki/Lao_kip",
    },
    {
        "name": "British Pound",
        "majuscule": ("L", "£"),
        "minuscule": None,
        "modifiers": ["currency"],
        "link": "https://en.wikipedia.org/wiki/Pound_sign",
    },
    {
        "name": "Mill (currency)",
        "majuscule": None,
        "minuscule": ("m", "₥"),
        "modifiers": ["currency"],
        "link": "https://en.wikipedia.org/wiki/Mill_(currency)",
    },
    {
        "name": "United States Dollar",
        "majuscule": ("S", "$"),
        "minuscule": None,
        "modifiers": ["currency"],
        "link": "https://en.wikipedia.org/wiki/Dollar_sign",
    },
    {
        "name": "Bangladeshi Taka",
        "majuscule": None,
        "minuscule": ("t", "৳"),
        "modifiers": ["currency"],
        "link": "https://en.wikipedia.org/wiki/Bangladeshi_taka",
    },
    {
        "name": "Cambodian Riel",
        "majuscule": None,
        "minuscule": ("r", "៛"),
        "modifiers": ["currency"],
        "link": "https://en.wikipedia.org/wiki/Cambodian_riel",
    },
    {
        "name": "Argentine Austral",
        "majuscule": ("A", "₳"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Argentine_austral",
    },
    {
        "name": "Bitcoin",
        "majuscule": ("B", "₿"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Bitcoin",
    },
    {
        "name": "Costa Rican Colón",
        "majuscule": ("C", "₡"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Costa_Rican_col%C3%B3n",
    },
    {
        "name": "Euro",
        "majuscule": ("E", "€"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Euro_sign",
    },
    {
        "name": "Georgian Lari",
        "majuscule": ("C", "₾"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Georgian_lari",
    },
    {
        "name": "Ukrainian Hryvnia",
        "majuscule": ("S", "₴"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Hryvnia_sign",
    },
    {
        "name": "Italian Lira",
        "majuscule": ("L", "₤"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Lira",
    },
    {
        "name": "Turkish Lira",
        "majuscule": None,
        "minuscule": ("l", "₺"),
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Lira",
        "docs": "Had to go with the lowercase L, because the Italian lira took the capital.",
    },
    {
        "name": "Nigerian Naira",
        "majuscule": ("N", "₦"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Nigerian_naira",
    },
    {
        "name": "Philippine Peso",
        "majuscule": ("P", "₱"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Philippine_peso_sign",
    },
    {
        "name": "Armenian Dram",
        "majuscule": ("D", "֏"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Armenian_dram_sign",
        "docs": "We don't [yet?] have the Armenian alphabet, so this uses the English D.",
    },
    {
        "name": "Mongolian tögrög",
        "majuscule": ("T", "₮"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Mongolian_t%C3%B6gr%C3%B6g",
    },
    {
        "name": "Korean Won",
        "majuscule": ("W", "₩"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Won_sign",
    },
    {
        "name": "Japanese Yen",
        "majuscule": ("Y", "¥"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Japanese_yen",
    },
    {
        "name": "Indian Rupee",
        "majuscule": ("R", "₹"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Indian_rupee_sign",
    },
]

MODIFIED_GREEK_CHARS = [

    #   ____ ____  _____ _____ _  __  __  __    _  _____ _   _
    #  / ___|  _ \| ____| ____| |/ / |  \/  |  / \|_   _| | | |
    # | |  _| |_) |  _| |  _| | ' /  | |\/| | / _ \ | | | |_| |
    # | |_| |  _ <| |___| |___| . \  | |  | |/ ___ \| | |  _  |
    #  \____|_| \_\_____|_____|_|\_\ |_|  |_/_/   \_\_| |_| |_|

    #  _           _     _
    # | |__   ___ | | __| |
    # | '_ \ / _ \| |/ _` |
    # | |_) | (_) | | (_| |
    # |_.__/ \___/|_|\__,_|
    {
        "name": "Mathematical Bold Alpha",
        "majuscule": ("Α", "𝚨"),
        "minuscule": ("α", "𝛂"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Beta",
        "majuscule": ("Β", "𝚩"),
        "minuscule": ("β", "𝛃"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Gamma",
        "majuscule": ("Γ", "𝚪"),
        "minuscule": ("γ", "𝛄"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Delta",
        "majuscule": ("Δ", "𝚫"),
        "minuscule": ("δ", "𝛅"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Epsilon",
        "majuscule": ("Ε", "𝚬"),
        "minuscule": ("ε", "𝛆"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Zeta",
        "majuscule": ("Ζ", "𝚭"),
        "minuscule": ("ζ", "𝛇"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Eta",
        "majuscule": ("Η", "𝚮"),
        "minuscule": ("η", "𝛈"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Theta",
        "majuscule": ("Θ", "𝚯"),
        "minuscule": ("θ", "𝛉"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Iota",
        "majuscule": ("Ι", "𝚰"),
        "minuscule": ("ι", "𝛊"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Kappa",
        "majuscule": ("Κ", "𝚱"),
        "minuscule": ("κ", "𝛋"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Lamda",
        "majuscule": ("Λ", "𝚲"),
        "minuscule": ("λ", "𝛌"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Mu",
        "majuscule": ("Μ", "𝚳"),
        "minuscule": ("μ", "𝛍"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Nu",
        "majuscule": ("Ν", "𝚴"),
        "minuscule": ("ν", "𝛎"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Xi",
        "majuscule": ("Ξ", "𝚵"),
        "minuscule": ("ξ", "𝛏"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Omicron",
        "majuscule": ("Ο", "𝚶"),
        "minuscule": ("ο", "𝛐"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Pi",
        "majuscule": ("Π", "𝚷"),
        "minuscule": ("π", "𝛑"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Rho",
        "majuscule": ("Ρ", "𝚸"),
        "minuscule": ("ρ", "𝛒"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Sigma",
        "majuscule": ("Σ", "𝚺"),
        "minuscule": ("σ", "𝛔"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Final Sigma",
        "majuscule": None,
        "minuscule": ("ς", "𝛓"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Tau",
        "majuscule": ("Τ", "𝚻"),
        "minuscule": ("τ", "𝛕"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Upsilon",
        "majuscule": ("Υ", "𝚼"),
        "minuscule": ("υ", "𝛖"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Phi",
        "majuscule": ("Φ", "𝚽"),
        "minuscule": ("φ", "𝛗"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Chi",
        "majuscule": ("Χ", "𝚾"),
        "minuscule": ("χ", "𝛘"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Psi",
        "majuscule": ("Ψ", "𝚿"),
        "minuscule": ("ψ", "𝛙"),
        "modifiers": ["bold"],
    },
    {
        "name": "Mathematical Bold Omega",
        "majuscule": ("Ω", "𝛀"),
        "minuscule": ("ω", "𝛚"),
        "modifiers": ["bold"],
    },

    #  _ _        _ _
    # (_) |_ __ _| (_) ___
    # | | __/ _` | | |/ __|
    # | | || (_| | | | (__
    # |_|\__\__,_|_|_|\___|
    {
        "name": "Mathematical Italic Alpha",
        "majuscule": ("Α", "𝛢"),
        "minuscule": ("α", "𝛼"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Beta",
        "majuscule": ("Β", "𝛣"),
        "minuscule": ("β", "𝛽"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Gamma",
        "majuscule": ("Γ", "𝛤"),
        "minuscule": ("γ", "𝛾"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Delta",
        "majuscule": ("Δ", "𝛥"),
        "minuscule": ("δ", "𝛿"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Epsilon",
        "majuscule": ("Ε", "𝛦"),
        "minuscule": ("ε", "𝜀"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Zeta",
        "majuscule": ("Ζ", "𝛧"),
        "minuscule": ("ζ", "𝜁"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Eta",
        "majuscule": ("Η", "𝛨"),
        "minuscule": ("η", "𝜂"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Theta",
        "majuscule": ("Θ", "𝛩"),
        "minuscule": ("θ", "𝜃"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Iota",
        "majuscule": ("Ι", "𝛪"),
        "minuscule": ("ι", "𝜄"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Kappa",
        "majuscule": ("Κ", "𝛫"),
        "minuscule": ("κ", "𝜅"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Lamda",
        "majuscule": ("Λ", "𝛬"),
        "minuscule": ("λ", "𝜆"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Mu",
        "majuscule": ("Μ", "𝛭"),
        "minuscule": ("μ", "𝜇"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Nu",
        "majuscule": ("Ν", "𝛮"),
        "minuscule": ("ν", "𝜈"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Xi",
        "majuscule": ("Ξ", "𝛯"),
        "minuscule": ("ξ", "𝜉"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Omicron",
        "majuscule": ("Ο", "𝛰"),
        "minuscule": ("ο", "𝜊"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Pi",
        "majuscule": ("Π", "𝛱"),
        "minuscule": ("π", "𝜋"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Rho",
        "majuscule": ("Ρ", "𝛲"),
        "minuscule": ("ρ", "𝜌"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Sigma",
        "majuscule": ("Σ", "𝛴"),
        "minuscule": ("σ", "𝜎"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Final Sigma",
        "majuscule": None,
        "minuscule": ("ς", "𝜍"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Tau",
        "majuscule": ("Τ", "𝛵"),
        "minuscule": ("τ", "𝜏"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Upsilon",
        "majuscule": ("Υ", "𝛶"),
        "minuscule": ("υ", "𝜐"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Phi",
        "majuscule": ("Φ", "𝛷"),
        "minuscule": ("φ", "𝜑"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Chi",
        "majuscule": ("Χ", "𝛸"),
        "minuscule": ("χ", "𝜒"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Psi",
        "majuscule": ("Ψ", "𝛹"),
        "minuscule": ("ψ", "𝜓"),
        "modifiers": ["italic"],
    },
    {
        "name": "Mathematical Italic Omega",
        "majuscule": ("Ω", "𝛺"),
        "minuscule": ("ω", "𝜔"),
        "modifiers": ["italic"],
    },

    #  _           _     _   _ _        _ _
    # | |__   ___ | | __| | (_) |_ __ _| (_) ___
    # | '_ \ / _ \| |/ _` | | | __/ _` | | |/ __|
    # | |_) | (_) | | (_| | | | || (_| | | | (__
    # |_.__/ \___/|_|\__,_| |_|\__\__,_|_|_|\___|
    {
        "name": "Mathematical Bold Italic Alpha",
        "majuscule": ("Α", "𝜜"),
        "minuscule": ("α", "𝜶"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Beta",
        "majuscule": ("Β", "𝜝"),
        "minuscule": ("β", "𝜷"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Gamma",
        "majuscule": ("Γ", "𝜞"),
        "minuscule": ("γ", "𝜸"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Delta",
        "majuscule": ("Δ", "𝜟"),
        "minuscule": ("δ", "𝜹"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Epsilon",
        "majuscule": ("Ε", "𝜠"),
        "minuscule": ("ε", "𝜺"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Zeta",
        "majuscule": ("Ζ", "𝜡"),
        "minuscule": ("ζ", "𝜻"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Eta",
        "majuscule": ("Η", "𝜢"),
        "minuscule": ("η", "𝜼"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Theta",
        "majuscule": ("Θ", "𝜣"),
        "minuscule": ("θ", "𝜽"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Iota",
        "majuscule": ("Ι", "𝜤"),
        "minuscule": ("ι", "𝜾"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Kappa",
        "majuscule": ("Κ", "𝜥"),
        "minuscule": ("κ", "𝜿"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Lamda",
        "majuscule": ("Λ", "𝜦"),
        "minuscule": ("λ", "𝝀"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Mu",
        "majuscule": ("Μ", "𝜧"),
        "minuscule": ("μ", "𝝁"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Nu",
        "majuscule": ("Ν", "𝜨"),
        "minuscule": ("ν", "𝝂"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Xi",
        "majuscule": ("Ξ", "𝜩"),
        "minuscule": ("ξ", "𝝃"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Omicron",
        "majuscule": ("Ο", "𝜪"),
        "minuscule": ("ο", "𝝄"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Pi",
        "majuscule": ("Π", "𝜫"),
        "minuscule": ("π", "𝝅"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Rho",
        "majuscule": ("Ρ", "𝜬"),
        "minuscule": ("ρ", "𝝆"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Theta Symbol",
        "majuscule": ("Θ", "𝜭"),
        "minuscule": ("θ", "𝝇"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Sigma",
        "majuscule": ("Σ", "𝜮"),
        "minuscule": ("σ", "𝝈"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Final Sigma",
        "majuscule": None,
        "minuscule": ("ς", "𝝇"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Tau",
        "majuscule": ("Τ", "𝜯"),
        "minuscule": ("τ", "𝝉"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Upsilon",
        "majuscule": ("Υ", "𝜰"),
        "minuscule": ("υ", "𝝊"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Phi",
        "majuscule": ("Φ", "𝜱"),
        "minuscule": ("φ", "𝝋"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Chi",
        "majuscule": ("Χ", "𝜲"),
        "minuscule": ("χ", "𝝌"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Psi",
        "majuscule": ("Ψ", "𝜳"),
        "minuscule": ("ψ", "𝝍"),
        "modifiers": ["bold", "italic"],
    },
    {
        "name": "Mathematical Bold Italic Omega",
        "majuscule": ("Ω", "𝜴"),
        "minuscule": ("ω", "𝝎"),
        "modifiers": ["bold", "italic"],
    },

    #                          _  __   _           _     _
    #  ___       ___  ___ _ __(_)/ _| | |__   ___ | | __| |
    # / __|_____/ __|/ _ \ '__| | |_  | '_ \ / _ \| |/ _` |
    # \__ \_____\__ \  __/ |  | |  _| | |_) | (_) | | (_| |
    # |___/     |___/\___|_|  |_|_|   |_.__/ \___/|_|\__,_|
    {
        "name": "Mathematical Sans-Serif Bold Alpha",
        "majuscule": ("Α", "𝝖"),
        "minuscule": ("α", "𝝰"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Beta",
        "majuscule": ("Β", "𝝗"),
        "minuscule": ("β", "𝝱"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Gamma",
        "majuscule": ("Γ", "𝝘"),
        "minuscule": ("γ", "𝝲"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Delta",
        "majuscule": ("Δ", "𝝙"),
        "minuscule": ("δ", "𝝳"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Epsilon",
        "majuscule": ("Ε", "𝝚"),
        "minuscule": ("ε", "𝝴"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Zeta",
        "majuscule": ("Ζ", "𝝛"),
        "minuscule": ("ζ", "𝝵"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Eta",
        "majuscule": ("Η", "𝝜"),
        "minuscule": ("η", "𝝶"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Theta",
        "majuscule": ("Θ", "𝝝"),
        "minuscule": ("θ", "𝝷"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Iota",
        "majuscule": ("Ι", "𝝞"),
        "minuscule": ("ι", "𝝸"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Kappa",
        "majuscule": ("Κ", "𝝟"),
        "minuscule": ("κ", "𝝹"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Lamda",
        "majuscule": ("Λ", "𝝠"),
        "minuscule": ("λ", "𝝺"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Mu",
        "majuscule": ("Μ", "𝝡"),
        "minuscule": ("μ", "𝝻"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Nu",
        "majuscule": ("Ν", "𝝢"),
        "minuscule": ("ν", "𝝼"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Xi",
        "majuscule": ("Ξ", "𝝣"),
        "minuscule": ("ξ", "𝝽"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Omicron",
        "majuscule": ("Ο", "𝝤"),
        "minuscule": ("ο", "𝝾"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Pi",
        "majuscule": ("Π", "𝝥"),
        "minuscule": ("π", "𝝿"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Rho",
        "majuscule": ("Ρ", "𝝦"),
        "minuscule": ("ρ", "𝞀"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Sigma",
        "majuscule": ("Σ", "𝝨"),
        "minuscule": ("σ", "𝞂"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Sigma",
        "majuscule": None,
        "minuscule": ("ς", "𝞁"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Tau",
        "majuscule": ("Τ", "𝝩"),
        "minuscule": ("τ", "𝞃"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Upsilon",
        "majuscule": ("Υ", "𝝪"),
        "minuscule": ("υ", "𝞄"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Phi",
        "majuscule": ("Φ", "𝝫"),
        "minuscule": ("φ", "𝞅"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Chi",
        "majuscule": ("Χ", "𝝬"),
        "minuscule": ("χ", "𝞆"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Psi",
        "majuscule": ("Ψ", "𝝭"),
        "minuscule": ("ψ", "𝞇"),
        "modifiers": ["sansSerif", "bold"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Omega",
        "majuscule": ("Ω", "𝝮"),
        "minuscule": ("ω", "𝞈"),
        "modifiers": ["sansSerif", "bold"],
    },

    #                          _  __   _           _     _   _ _        _ _
    #  ___       ___  ___ _ __(_)/ _| | |__   ___ | | __| | (_) |_ __ _| (_) ___
    # / __|_____/ __|/ _ \ '__| | |_  | '_ \ / _ \| |/ _` | | | __/ _` | | |/ __|
    # \__ \_____\__ \  __/ |  | |  _| | |_) | (_) | | (_| | | | || (_| | | | (__
    # |___/     |___/\___|_|  |_|_|   |_.__/ \___/|_|\__,_| |_|\__\__,_|_|_|\___|
    {
        "name": "Mathematical Sans-Serif Bold Italic Alpha",
        "majuscule": ("Α", "𝞐"),
        "minuscule": ("α", "𝞪"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Beta",
        "majuscule": ("Β", "𝞑"),
        "minuscule": ("β", "𝞫"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Gamma",
        "majuscule": ("Γ", "𝞒"),
        "minuscule": ("γ", "𝞬"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Delta",
        "majuscule": ("Δ", "𝞓"),
        "minuscule": ("δ", "𝞭"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Epsilon",
        "majuscule": ("Ε", "𝞔"),
        "minuscule": ("ε", "𝞮"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Zeta",
        "majuscule": ("Ζ", "𝞕"),
        "minuscule": ("ζ", "𝞯"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Eta",
        "majuscule": ("Η", "𝞖"),
        "minuscule": ("η", "𝞰"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Theta",
        "majuscule": ("Θ", "𝞗"),
        "minuscule": ("θ", "𝞱"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Iota",
        "majuscule": ("Ι", "𝞘"),
        "minuscule": ("ι", "𝞲"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Kappa",
        "majuscule": ("Κ", "𝞙"),
        "minuscule": ("κ", "𝞳"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Lamda",
        "majuscule": ("Λ", "𝞚"),
        "minuscule": ("λ", "𝞴"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Mu",
        "majuscule": ("Μ", "𝞛"),
        "minuscule": ("μ", "𝞵"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Nu",
        "majuscule": ("Ν", "𝞜"),
        "minuscule": ("ν", "𝞶"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Xi",
        "majuscule": ("Ξ", "𝞝"),
        "minuscule": ("ξ", "𝞷"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Omicron",
        "majuscule": ("Ο", "𝞞"),
        "minuscule": ("ο", "𝞸"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Pi",
        "majuscule": ("Π", "𝞟"),
        "minuscule": ("π", "𝞹"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Rho",
        "majuscule": ("Ρ", "𝞠"),
        "minuscule": ("ρ", "𝞺"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Theta Symbol",
        "majuscule": ("Θ", "𝞡"),
        "minuscule": ("θ", "𝞻"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Sigma",
        "majuscule": ("Σ", "𝞢"),
        "minuscule": ("σ", "𝞼"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Final Sigma",
        "majuscule": None,
        "minuscule": ("ς", "𝞻"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Tau",
        "majuscule": ("Τ", "𝞣"),
        "minuscule": ("τ", "𝞽"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Upsilon",
        "majuscule": ("Υ", "𝞤"),
        "minuscule": ("υ", "𝞾"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Phi",
        "majuscule": ("Φ", "𝞥"),
        "minuscule": ("φ", "𝞿"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Chi",
        "majuscule": ("Χ", "𝞦"),
        "minuscule": ("χ", "𝟀"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Psi",
        "majuscule": ("Ψ", "𝞧"),
        "minuscule": ("ψ", "𝟁"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
    {
        "name": "Mathematical Sans-Serif Bold Italic Omega",
        "majuscule": ("Ω", "𝞨"),
        "minuscule": ("ω", "𝟂"),
        "modifiers": ["sansSerif", "bold", "italic"],
    },
]

# #   ____               _                _
# #  / ___|_ __ ___  ___| | __  _ __ ___ (_)___  ___
# # | |  _| '__/ _ \/ _ \ |/ / | '_ ` _ \| / __|/ __|
# # | |_| | | |  __/  __/   <  | | | | | | \__ \ (__ _
# #  \____|_|  \___|\___|_|\_\ |_| |_| |_|_|___/\___(_)
# {
#     "name": "Mathematical Italic Small Dotless I",
#     "majuscule": ("I", "𝚤"),
# },
# {
#     "name": "Mathematical Italic Small Dotless J",
#     "majuscule": ("J", "𝚥"),
# },
# {
#     "name": "Mathematical Bold Capital Theta Symbol",
#     "majuscule": ("Θ", "𝚹"),
#     "modifiers": ["bold"],
# },
# {
#     "name": "Mathematical Bold Nabla",
#     "majuscule": ("", "𝛁"),
#     "modifiers": ["bold"],
# },
# {
#     "name": "Mathematical Bold Partial Differential",
#     "majuscule": ("", "𝛛"),
# },
# {
#     "name": "Mathematical Bold Epsilon Symbol",
#     "majuscule": ("", "𝛜"),
# },
# {
#     "name": "Mathematical Bold Theta Symbol",
#     "majuscule": ("", "𝛝"),
# },
# {
#     "name": "Mathematical Bold Kappa Symbol",
#     "majuscule": ("", "𝛞"),
# },
# {
#     "name": "Mathematical Bold Phi Symbol",
#     "majuscule": ("", "𝛟"),
# },
# {
#     "name": "Mathematical Bold Rho Symbol",
#     "majuscule": ("", "𝛠"),
# },
# {
#     "name": "Mathematical Bold Pi Symbol",
#     "majuscule": ("", "𝛡"),
# },
# {
#     "name": "Mathematical Italic Capital Theta Symbol",
#     "majuscule": ("", "𝛳"),
# },
# {
#     "name": "Mathematical Italic Nabla",
#     "majuscule": ("", "𝛻"),
# },
# {
#     "name": "Mathematical Italic Partial Differential",
#     "majuscule": ("l", "𝜕"),
# },
# {
#     "name": "Mathematical Italic Epsilon Symbol",
#     "majuscule": ("l", "𝜖"),
# },
# {
#     "name": "Mathematical Italic Theta Symbol",
#     "majuscule": ("l", "𝜗"),
# },
# {
#     "name": "Mathematical Italic Kappa Symbol",
#     "majuscule": ("l", "𝜘"),
# },
# {
#     "name": "Mathematical Italic Phi Symbol",
#     "majuscule": ("l", "𝜙"),
# },
# {
#     "name": "Mathematical Italic Rho Symbol",
#     "majuscule": ("l", "𝜚"),
# },
# {
#     "name": "Mathematical Italic Pi Symbol",
#     "majuscule": ("l", "𝜛"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Capital Theta Symbol",
#     "majuscule": ("l", "𝝧"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Italic Nabla",
#     "majuscule": ("a", "𝞩"),
# },
# {
#     "name": "Mathematical Bold Italic Nabla",
#     "majuscule": ("a", "𝜵"),
# },
# {
#     "name": "Mathematical Bold Italic Partial Differential",
#     "majuscule": ("l", "𝝏"),
# },
# {
#     "name": "Mathematical Bold Italic Epsilon Symbol",
#     "majuscule": ("l", "𝝐"),
# },
# {
#     "name": "Mathematical Bold Italic Theta Symbol",
#     "majuscule": ("l", "𝝑"),
# },
# {
#     "name": "Mathematical Bold Italic Kappa Symbol",
#     "majuscule": ("l", "𝝒"),
# },
# {
#     "name": "Mathematical Bold Italic Phi Symbol",
#     "majuscule": ("l", "𝝓"),
# },
# {
#     "name": "Mathematical Bold Italic Rho Symbol",
#     "majuscule": ("l", "𝝔"),
# },
# {
#     "name": "Mathematical Bold Italic Pi Symbol",
#     "majuscule": ("l", "𝝕"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Nabla",
#     "majuscule": ("a", "𝝯"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Partial Differential",
#     "majuscule": ("l", "𝞉"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Epsilon Symbol",
#     "majuscule": ("l", "𝞊"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Theta Symbol",
#     "majuscule": ("l", "𝞋"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Kappa Symbol",
#     "majuscule": ("l", "𝞌"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Phi Symbol",
#     "majuscule": ("l", "𝞍"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Rho Symbol",
#     "majuscule": ("l", "𝞎"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Pi Symbol",
#     "majuscule": ("l", "𝞏"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Italic Partial Differential",
#     "majuscule": ("l", "𝟃"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Italic Epsilon Symbol",
#     "majuscule": ("l", "𝟄"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Italic Theta Symbol",
#     "majuscule": ("l", "𝟅"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Italic Kappa Symbol",
#     "majuscule": ("l", "𝟆"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Italic Phi Symbol",
#     "majuscule": ("l", "𝟇"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Italic Rho Symbol",
#     "majuscule": ("l", "𝟈"),
# },
# {
#     "name": "Mathematical Sans-Serif Bold Italic Pi Symbol",
#     "majuscule": ("l", "𝟉"),
# },
# {
#     "name": "Mathematical Bold Capital Digamma",
#     "majuscule": ("a", "𝟊"),
# },
# {
#     "name": "Mathematical Bold Small Digamma",
#     "majuscule": ("a", "𝟋"),
# },


#                        _
#  _ __  _   _ _ __ ___ | |__   ___ _ __ ___
# | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__/ __|
# | | | | |_| | | | | | | |_) |  __/ |  \__ \
# |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  |___/

##  _           _     _     _  _
## | |__   ___ | | __| |  _| || |_
## | '_ \ / _ \| |/ _` | |_  ..  _|
## | |_) | (_) | | (_| | |_      _|
## |_.__/ \___/|_|\__,_|   |_||_|
#{
#    "name": "Mathematical Bold Digit Zero",
#    "majuscule": None,
#    "minuscule": ("0", "𝟎"),
#    "modifiers": ["bold"],
#},
#{
#    "name": "Mathematical Bold Digit One",
#    "majuscule": None,
#    "minuscule": ("1", "𝟏"),
#    "modifiers": ["bold"],
#},
#{
#    "name": "Mathematical Bold Digit Two",
#    "majuscule": None,
#    "minuscule": ("2", "𝟐"),
#    "modifiers": ["bold"],
#},
#{
#    "name": "Mathematical Bold Digit Three",
#    "majuscule": None,
#    "minuscule": ("3", "𝟑"),
#    "modifiers": ["bold"],
#},
#{
#    "name": "Mathematical Bold Digit Four",
#    "majuscule": None,
#    "minuscule": ("4", "𝟒"),
#    "modifiers": ["bold"],
#},
#{
#    "name": "Mathematical Bold Digit Five",
#    "majuscule": None,
#    "minuscule": ("5", "𝟓"),
#    "modifiers": ["bold"],
#},
#{
#    "name": "Mathematical Bold Digit Six",
#    "majuscule": None,
#    "minuscule": ("6", "𝟔"),
#    "modifiers": ["bold"],
#},
#{
#    "name": "Mathematical Bold Digit Seven",
#    "majuscule": None,
#    "minuscule": ("7", "𝟕"),
#    "modifiers": ["bold"],
#},
#{
#    "name": "Mathematical Bold Digit Eight",
#    "majuscule": None,
#    "minuscule": ("8", "𝟖"),
#    "modifiers": ["bold"],
#},
#{
#    "name": "Mathematical Bold Digit Nine",
#    "majuscule": None,
#    "minuscule": ("9", "𝟗"),
#    "modifiers": ["bold"],
#},

##      _             _     _                _                   _        _  _
##   __| | ___  _   _| |__ | | ___       ___| |_ _ __ _   _  ___| | __  _| || |_
##  / _` |/ _ \| | | | '_ \| |/ _ \_____/ __| __| '__| | | |/ __| |/ / |_  ..  _|
## | (_| | (_) | |_| | |_) | |  __/_____\__ \ |_| |  | |_| | (__|   <  |_      _|
##  \__,_|\___/ \__,_|_.__/|_|\___|     |___/\__|_|   \__,_|\___|_|\_\   |_||_|
#{
#    "name": "Mathematical Double-Struck Digit Zero",
#    "majuscule": None,
#    "minuscule": ("0", "𝟘"),
#    "modifiers": ["doubleStruck"],
#},
#{
#    "name": "Mathematical Double-Struck Digit One",
#    "majuscule": None,
#    "minuscule": ("1", "𝟙"),
#    "modifiers": ["doubleStruck"],
#},
#{
#    "name": "Mathematical Double-Struck Digit Two",
#    "majuscule": None,
#    "minuscule": ("2", "𝟚"),
#    "modifiers": ["doubleStruck"],
#},
#{
#    "name": "Mathematical Double-Struck Digit Three",
#    "majuscule": None,
#    "minuscule": ("3", "𝟛"),
#    "modifiers": ["doubleStruck"],
#},
#{
#    "name": "Mathematical Double-Struck Digit Four",
#    "majuscule": None,
#    "minuscule": ("4", "𝟜"),
#    "modifiers": ["doubleStruck"],
#},
#{
#    "name": "Mathematical Double-Struck Digit Five",
#    "majuscule": None,
#    "minuscule": ("5", "𝟝"),
#    "modifiers": ["doubleStruck"],
#},
#{
#    "name": "Mathematical Double-Struck Digit Six",
#    "majuscule": None,
#    "minuscule": ("6", "𝟞"),
#    "modifiers": ["doubleStruck"],
#},
#{
#    "name": "Mathematical Double-Struck Digit Seven",
#    "majuscule": None,
#    "minuscule": ("7", "𝟟"),
#    "modifiers": ["doubleStruck"],
#},
#{
#    "name": "Mathematical Double-Struck Digit Eight",
#    "majuscule": None,
#    "minuscule": ("8", "𝟠"),
#    "modifiers": ["doubleStruck"],
#},
#{
#    "name": "Mathematical Double-Struck Digit Nine",
#    "majuscule": None,
#    "minuscule": ("9", "𝟡"),
#    "modifiers": ["doubleStruck"],
#},

##                                          _  __     _  _
##  ___  __ _ _ __  ___       ___  ___ _ __(_)/ _|  _| || |_
## / __|/ _` | '_ \/ __|_____/ __|/ _ \ '__| | |_  |_  ..  _|
## \__ \ (_| | | | \__ \_____\__ \  __/ |  | |  _| |_      _|
## |___/\__,_|_| |_|___/     |___/\___|_|  |_|_|     |_||_|
#{
#    "name": "Mathematical Sans-Serif Digit Zero",
#    "majuscule": None,
#    "minuscule": ("0", "𝟢"),
#    "modifiers": ["sansSerif"],
#},
#{
#    "name": "Mathematical Sans-Serif Digit One",
#    "majuscule": None,
#    "minuscule": ("1", "𝟣"),
#    "modifiers": ["sansSerif"],
#},
#{
#    "name": "Mathematical Sans-Serif Digit Two",
#    "majuscule": None,
#    "minuscule": ("2", "𝟤"),
#    "modifiers": ["sansSerif"],
#},
#{
#    "name": "Mathematical Sans-Serif Digit Three",
#    "majuscule": None,
#    "minuscule": ("3", "𝟥"),
#    "modifiers": ["sansSerif"],
#},
#{
#    "name": "Mathematical Sans-Serif Digit Four",
#    "majuscule": None,
#    "minuscule": ("4", "𝟦"),
#    "modifiers": ["sansSerif"],
#},
#{
#    "name": "Mathematical Sans-Serif Digit Five",
#    "majuscule": None,
#    "minuscule": ("5", "𝟧"),
#    "modifiers": ["sansSerif"],
#},
#{
#    "name": "Mathematical Sans-Serif Digit Six",
#    "majuscule": None,
#    "minuscule": ("6", "𝟨"),
#    "modifiers": ["sansSerif"],
#},
#{
#    "name": "Mathematical Sans-Serif Digit Seven",
#    "majuscule": None,
#    "minuscule": ("7", "𝟩"),
#    "modifiers": ["sansSerif"],
#},
#{
#    "name": "Mathematical Sans-Serif Digit Eight",
#    "majuscule": None,
#    "minuscule": ("8", "𝟪"),
#    "modifiers": ["sansSerif"],
#},
#{
#    "name": "Mathematical Sans-Serif Digit Nine",
#    "majuscule": None,
#    "minuscule": ("9", "𝟫"),
#    "modifiers": ["sansSerif"],
#},

##                                          _  __   _           _     _
##  ___  __ _ _ __  ___       ___  ___ _ __(_)/ _| | |__   ___ | | __| |
## / __|/ _` | '_ \/ __|_____/ __|/ _ \ '__| | |_  | '_ \ / _ \| |/ _` |
## \__ \ (_| | | | \__ \_____\__ \  __/ |  | |  _| | |_) | (_) | | (_| |
## |___/\__,_|_| |_|___/     |___/\___|_|  |_|_|   |_.__/ \___/|_|\__,_|
##
##    _  _
##  _| || |_
## |_  ..  _|
## |_      _|
##   |_||_|
#{
#    "name": "Mathematical Sans-Serif Bold Digit Zero",
#    "majuscule": None,
#    "minuscule": ("0", "𝟬"),
#    "modifiers": ["sansSerif", "bold"],
#},
#{
#    "name": "Mathematical Sans-Serif Bold Digit One",
#    "majuscule": None,
#    "minuscule": ("1", "𝟭"),
#    "modifiers": ["sansSerif", "bold"],
#},
#{
#    "name": "Mathematical Sans-Serif Bold Digit Two",
#    "majuscule": None,
#    "minuscule": ("2", "𝟮"),
#    "modifiers": ["sansSerif", "bold"],
#},
#{
#    "name": "Mathematical Sans-Serif Bold Digit Three",
#    "majuscule": None,
#    "minuscule": ("3", "𝟯"),
#    "modifiers": ["sansSerif", "bold"],
#},
#{
#    "name": "Mathematical Sans-Serif Bold Digit Four",
#    "majuscule": None,
#    "minuscule": ("4", "𝟰"),
#    "modifiers": ["sansSerif", "bold"],
#},
#{
#    "name": "Mathematical Sans-Serif Bold Digit Five",
#    "majuscule": None,
#    "minuscule": ("5", "𝟱"),
#    "modifiers": ["sansSerif", "bold"],
#},
#{
#    "name": "Mathematical Sans-Serif Bold Digit Six",
#    "majuscule": None,
#    "minuscule": ("6", "𝟲"),
#    "modifiers": ["sansSerif", "bold"],
#},
#{
#    "name": "Mathematical Sans-Serif Bold Digit Seven",
#    "majuscule": None,
#    "minuscule": ("7", "𝟳"),
#    "modifiers": ["sansSerif", "bold"],
#},
#{
#    "name": "Mathematical Sans-Serif Bold Digit Eight",
#    "majuscule": None,
#    "minuscule": ("8", "𝟴"),
#    "modifiers": ["sansSerif", "bold"],
#},
#{
#    "name": "Mathematical Sans-Serif Bold Digit Nine",
#    "majuscule": None,
#    "minuscule": ("9", "𝟵"),
#    "modifiers": ["sansSerif", "bold"],
#},

##                                                           _  _
##  _ __ ___   ___  _ __   ___  ___ _ __   __ _  ___ ___   _| || |_
## | '_ ` _ \ / _ \| '_ \ / _ \/ __| '_ \ / _` |/ __/ _ \ |_  ..  _|
## | | | | | | (_) | | | | (_) \__ \ |_) | (_| | (_|  __/ |_      _|
## |_| |_| |_|\___/|_| |_|\___/|___/ .__/ \__,_|\___\___|   |_||_|
##                                 |_|
#{
#    "name": "Mathematical Monospace Digit Zero",
#    "majuscule": None,
#    "minuscule": ("0", "𝟶"),
#    "modifiers": ["monoSpace"],
#},
#{
#    "name": "Mathematical Monospace Digit One",
#    "majuscule": None,
#    "minuscule": ("1", "𝟷"),
#    "modifiers": ["monoSpace"],
#},
#{
#    "name": "Mathematical Monospace Digit Two",
#    "majuscule": None,
#    "minuscule": ("2", "𝟸"),
#    "modifiers": ["monoSpace"],
#},
#{
#    "name": "Mathematical Monospace Digit Three",
#    "majuscule": None,
#    "minuscule": ("3", "𝟹"),
#    "modifiers": ["monoSpace"],
#},
#{
#    "name": "Mathematical Monospace Digit Four",
#    "majuscule": None,
#    "minuscule": ("4", "𝟺"),
#    "modifiers": ["monoSpace"],
#},
#{
#    "name": "Mathematical Monospace Digit Five",
#    "majuscule": None,
#    "minuscule": ("5", "𝟻"),
#    "modifiers": ["monoSpace"],
#},
#{
#    "name": "Mathematical Monospace Digit Six",
#    "majuscule": None,
#    "minuscule": ("6", "𝟼"),
#    "modifiers": ["monoSpace"],
#},
#{
#    "name": "Mathematical Monospace Digit Seven",
#    "majuscule": None,
#    "minuscule": ("7", "𝟽"),
#    "modifiers": ["monoSpace"],
#},
#{
#    "name": "Mathematical Monospace Digit Eight",
#    "majuscule": None,
#    "minuscule": ("8", "𝟾"),
#    "modifiers": ["monoSpace"],
#},
#{
#    "name": "Mathematical Monospace Digit Nine",
#    "majuscule": None,
#    "minuscule": ("9", "𝟿"),
#    "modifiers": ["monoSpace"],
#},

MODIFIED_RUSSIAN_CHARS = [

    #   ___ _   _ _ __ _ __ ___ _ __   ___ _   _
    #  / __| | | | '__| '__/ _ \ '_ \ / __| | | |
    # | (__| |_| | |  | | |  __/ | | | (__| |_| |
    #  \___|\__,_|_|  |_|  \___|_| |_|\___|\__, |
    #  A bit of a hack with Russian letters|___/
    {
        "name": "Russian Ruble",
        "majuscule": ("Р", "₽"),
        "minuscule": None,
        "modifiers": ["doubleCurrency"],
        "link": "https://en.wikipedia.org/wiki/Ruble_sign",
        "docs": "This uses the Russian эр (rolled R, which looks like P/p in English).",
    },
]


# This string is used by the stroke parsing/merging/rendering functions.
# Note the dash before the star, explained further in the functions below.
strokeKeys = "STKPWHRAO-*EUFRPBLGTSDZ"

def parseStroke (stroke):
    """
    Turns a Plover-style stroke string into a list of bools, representing the
    pressed state of every key, in steno order, with the addition of a dash
    between the O and star keys, to represent strokes with no vowels, nor star
    key. Star and dash are never in the same stroke, but in this intermediary
    format, they are allowed to live side-by-side.

    Note: Parsing does not currently support the steno number key.
    """
    pressed = []
    for key in strokeKeys:
        if stroke.startswith(key):
            pressed.append(True)
            stroke = stroke[1:]
        else:
            pressed.append(False)
    return pressed

def mergeStrokes (a, b):
    """
    Merging is nothing more than ORing together all the bools in two strokes.
    This results in a stroke with all True keys from both strokes set to True.
    Note: star and dash can both end up set, which is handled at render time.
    """
    parseA = parseStroke(a)
    parseB = parseStroke(b)
    merge = [x | y for x, y in zip(parseA, parseB)]
    return merge

def renderStroke (stroke):
    """
    Rendering a stroke walks through all the bools in the list, turning all
    Trues into their associated key letters. If any vowels, or the star are
    set to True, the dash, outputs as the empty string.
    """
    vowels = [stroke[7], stroke[8], stroke[11], stroke[12]] # AOEU
    if stroke[10] or any(vowels): # if star or any vowels set...
        stroke[9] = "" # ... don't include dash in the render
    text = [key for key, state in zip(strokeKeys, stroke) if state]
    return "".join(text)


def buildAlphabet (alphabetData):
    # pull out the scule strokes (e.g. "*" for min, "*P" for maj)
    minStroke = alphabetData["minStroke"]
    majStroke = alphabetData["majStroke"]
    # we'll build a dictionary, mapping a letter to list of outlines
    alphabet = {}
    # walk the alphabet data's list of letter data dictionaries
    for letterData in alphabetData["letters"]:
        # scule just stands for minuscule or majuscule
        for scule, sculeStroke in [("min", minStroke), ("maj", majStroke)]:
            # get the current letter, capital or lowercase
            letter = letterData.get(scule + "uscule")
            # not all characters have both majuscule and minuscule
            if letter is not None:
                # begin a list for all outlines we'll build for this letter
                alphabet[letter] = []
                # for each base letter outline (e.g. "SKWR" for J/j)...
                for charStroke in letterData["strokes"]:
                    # merge the character and scule strokes into one
                    # NOTE: the merged stroke will be a list of bools
                    strokeParts = mergeStrokes(charStroke, sculeStroke)
                    # render the stroke parts to a stroke string
                    stroke = renderStroke(strokeParts)
                    # append letter/stroke pair to alphabet dictionary
                    alphabet[letter].append(stroke)
    return alphabet

# Build alphabets
LATIN_ALPHABET = buildAlphabet(LATIN_ALPHABET_DATA)
RUSSIAN_ALPHABET = buildAlphabet(RUSSIAN_ALPHABET_DATA)
GREEK_ALPHABET = buildAlphabet(GREEK_ALPHABET_DATA)

# dicts mapping alphabet characters to their outlines
ALPHABETS = [
    LATIN_ALPHABET,
    GREEK_ALPHABET,
    RUSSIAN_ALPHABET,
]

# lists for building modified characters for each alphabet
CHAR_MOD_LISTS = [
    MODIFIED_LATIN_CHARS,
    MODIFIED_GREEK_CHARS,
]

# modified character defs paired with their required alphabets
CHAR_MOD_LISTS_WITH_ALPHABETS = [
    (MODIFIED_LATIN_CHARS, LATIN_ALPHABET),
    (MODIFIED_GREEK_CHARS, GREEK_ALPHABET),
]


def buildModCharOutlines (alphabet, srcDestChars, modStrokes):
    """
    Takes an alphabet data dictionary to look up base char strokes, a tuple of
    (src, dest) chars, and a list of modifier strokes.

    Returns a pair of the destination character, with its list of outlines,

    alphabet: a dictionary mapping chars to strokes
        e.g. {"a": ["A"], ..., "Z": ["STKPW", "STK"]}

    srcDestChars: a pair of source/destination characters
        e.g. ("a", "á"), ("AE", "Æ"), or ("ae", "ǽ")

    modStrokes: modifier stroke(s) used to get from source to dest
        e.g. ["-FRLG", "-RP"], for ligature followed by macron

    examples:
        >>> buildModCharOutlines(LATIN_ALPHABET, ("ae", "ǣ"), ["-FRLG", "-FP"])
        (ǣ, ["A*/*E/-FRLG/-FP"])

        >>> buildModCharOutlines(LATIN_ALPHABET, ("Z", "Ẑ"), ["-RPG"])
        (Ẑ, ["STKPW*P/-RPG", "STK*P/-RPG"]) # note two forms of base Z outline
    """
    if srcDestChars is None:
        return None

    # pull out src and dest chars for this char mod, e.g. "AE", "Æ"
    srcChars, destChar = srcDestChars

    # pull out all alphabetic outlines for every character in src chars
    # e.g. "ze" → [["STKPW", "STK"], ["E"]] # imaginary ze ligature
    srcCharOutlines = map(lambda c: alphabet[c], srcChars)

    # get the product of all strokes with each character, in order
    # e.g. [["STKPW", "E"], ["STK", "E"]] for earlier "ze" example
    srcCharsProduct = list(map(list, product(*srcCharOutlines)))

    outlines = [srcCharsStrokes + modStrokes for srcCharsStrokes in srcCharsProduct]
    return outlines

def createOutlines (alphabet, entry):
    """
    This creates all outlines for a modified character. It takes an alphabet
    that maps letters to lists of stroke options for said letters, and a
    modified letter entry, which is a dictionary of at least the keys shown in
    this example (where the first parts of the tuples are letters in the
    passed-in alphabet, i.e. source letters), and the second parts are the
    target letters they map to:

        {
            "minuscule": ("a", "á"),
            "majuscule": ("A", "Á"),
            "modifiers": ["acute"],
        }

    It returns a pair of lists of all outlines:

        (minOutlines, majOutlines)
    """
    modStrokes = list(map(lambda x: MODIFIERS[x]["outline"], entry["modifiers"]))
    minuscule = buildModCharOutlines(alphabet, entry["minuscule"], modStrokes)
    majuscule = buildModCharOutlines(alphabet, entry["majuscule"], modStrokes)
    return (minuscule, majuscule)

def buildFingerspellingDict ():
    """
    This is the main function for assembling all the various parts of the
    system into a single, Plover-ready dictionary, and returning it.
    """
    # this dict will collect all definitions for export
    spellingDict = {}

    # strings to force upper/lowercase through Plover
    majL, majR = majWraps
    minL, minR = minWraps

    # add all the letters from every alphabet
    for alphabet in ALPHABETS:
        for character, outlines in alphabet.items():
            for outline in outlines:
                # wrap translation in Plover directives to enforce case
                if character.isupper():
                    translation = majL + character + minR
                elif character.islower():
                    translation = minL + character + minR
                else:
                    translation = character
                # add entire definition to the final spelling dict
                spellingDict[outline] = translation

    # create definitions for all character modifications
    for charMods, alphabet in CHAR_MOD_LISTS_WITH_ALPHABETS:
        for entry in charMods:
            minuscule, majuscule = createOutlines(alphabet, entry)
            for scule, wrapL, wrapR, outlines in [
                    ("min", minL, minR, minuscule),
                    ("maj", majL, majR, majuscule)
                ]:
                # None means character + case isn't defined in Unicode
                if outlines != None:
                    _, translation = entry[scule + "uscule"]
                    for outline in outlines:
                        outlineStr = "/".join(outline)
                        # add entire definition to the final spelling dict
                        spellingDict[outlineStr] = wrapL + translation + wrapR

    # return the complete fingerspelling dictionary
    return spellingDict


if __name__ == "__main__":
    # assemble the entire fingerspelling dictionary
    fixSpell = buildFingerspellingDict()

    # dump the dictionary out over stdout
    # NOTE: ensure_ascii=False to stop "á" converting to "\\u00e1", e.g.
    print(json.dumps(fixSpell, ensure_ascii=False, indent=0))


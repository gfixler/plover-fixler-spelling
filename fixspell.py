import json

# TODO allow adding character overrides in a user-defined file

enderBraille = "-RPGT"

latinAlphabetData = {
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

greekAlphabetData = {
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
            "strokes": ["KH", "KP"],
            "link": "https://en.wikipedia.org/wiki/Chi_(letter)",
            "docs": "It's actual sound is hard to represent in steno, but CH is a reasonable fit. An alternate, orthographic KP is provided, if you just want to write it as X, which matches an alternate in the Russian alphabet for the letter (Хх) that also looks like an X.",
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

russianAlphabetData = {
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
            "docs": "Uses orthography to get around the conflict with Ч/ч, which makes the \"ch\" sound. As this looks exactly like an X, we go with the steno X chord. This also matches an alternate provided in the Greek alphabet for the letter, Chi (Χχ), which also looks like an X.",
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
modifiers = {
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
        "docs": "The [cedilla](https://en.wikipedia.org/wiki/Cedilla) is based on the the comma modifier stroke, with the '[extra](#modifier-tweaks)' tweak, because it's like a comma, but a little bit more than a comma.",
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

entries = [
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

def buildAlphabet (alphabetData, majOutline, minOutline):
    """
    Takes a list of dictionaries, one per letter, with at least these fields:

        {
            "minuscule": "j",
            "majuscule": "J",
            "outline": "SKWR", # only the character part of the stroke
        }

    If either form is missing, set it to None, e.g. "majuscule": None.

    Also takes outlines for minuscule and majuscule for the given alphabet, to
    be merged with the letter outline. For example, for the standard steno
    alphabet for the English letters, minuscule would be "*", and majuscule
    would be "*P". These would be merged with the above examples to yield the
    stroke "SKWR*" for minuscule, and "SKWR*P" for majuscule. These are called
    "outlines", instead of "enders", or "uniqueEnders", to leave room for an
    alphabet to use a unique starter, and right-hand side letter chords, e.g.

    Returns a dictionary mapping both minuscule and majuscule forms to their
    composed outlines.
    """
    alphabet = {}
    minMajParts = [
        ("maj", majOutline, majWraps),
        ("min", minOutline, minWraps)
    ]
    for entry in alphabetData:
        for scule, sculeOutline, (wrapL, wrapR) in minMajParts:
            character = entry.get(scule + "uscule")
            if character is not None:
                entryOutline = entry["outline"]
                stroke = mergeStrokes(entryOutline, sculeOutline)
                alphabet[character] = renderStroke(stroke)
    return alphabet

# Build alphabets
latinAlphabetLUT = buildAlphabet(latinAlphabet, latinMajEnder, latinMinEnder)
russianAlphabetLUT = buildAlphabet(russianAlphabet, russianMajEnder, russianMinEnder)
greekAlphabetLUT = buildAlphabet(greekAlphabet, greekMajEnder, greekMinEnder)

def buildModdedChar (srcDestChars, modStrokes, wraps):
    """
    Takes info surrounding character modification.
    Returns pair of outline and wrapped, modified char.

    srcDestChars: a pair of source/destination characters, like ("a", "á")
    modStrokes: modifier stroke(s) used to get from source to dest
    wraps: lowercase or upper case wrapper pair, like ("{>}{&", "}")

    example:
        >>> buildModdedChar(("a", "á"), "-RP", minWraps)
        ("A*/-RP", "{^}{&á}")
    """
    if srcDestChars is None:
        return None
    srcChars, destChar = srcDestChars
    wrapL, wrapR = wraps
    strokes = [latinAlphabetLUT[c] for c in srcChars] + list(modStrokes)
    return ("/".join(strokes), wrapL + destChar + wrapR, destChar)

def createOutlines (entry):
    """
    This just simplifies creating the minuscule and majuscule entries for all
    character modifications. It takes a single entry dictionary, and returns
    two 3-tuples, with outline, translation (wrapped with Plover case stuff),
    and translation character by itself.
    """
    modStrokes = list(map(lambda x: modifiers[x]["outline"], entry["modifiers"]))
    minuscule = buildModdedChar(entry["minuscule"], modStrokes, minWraps)
    majuscule = buildModdedChar(entry["majuscule"], modStrokes, majWraps)
    return (minuscule, majuscule)

def buildFingerspellingDict ():
    """
    This is the main function for assembling all the various parts of the
    system into a single, Plover-ready dictionary, and returning it.
    """
    spellingDict = {}

    # add all the letters from every alphabet
    alphabets = [
        latinAlphabetLUT,
        greekAlphabetLUT,
        russianAlphabetLUT,
    ]
    for alphabet in alphabets:
        for character, outline in alphabet.items():
            if character.isupper():
                wrapL, wrapR = majWraps
                translation = wrapL + character + wrapR
            elif character.islower():
                wrapL, wrapR = minWraps
                translation = wrapL + character + wrapR
            else:
                translation = character
            spellingDict[outline] = translation

    # create definitions for all character modifications
    for entry in entries:
        minuscule, majuscule = createOutlines(entry)
        for scule in [minuscule, majuscule]:
            if scule != None:
                # None means character + case isn't defined in Unicode
                (outline, translation, character) = scule
                spellingDict[outline] = translation

    return spellingDict

if __name__ == "__main__":
    fixSpell = buildFingerspellingDict()

    # dump the dictionary out over stdout
    # NOTE: ensure_ascii=False to stop "á" converting to "\\u00e1", e.g.
    print(json.dumps(fixSpell, ensure_ascii=False, indent=0))


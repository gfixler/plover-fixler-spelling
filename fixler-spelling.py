diacritics = {
    "cedilla": "-RPB",
    "hook": "-FRP",
    "ogonek": "-PBG", # "little tail"
    "ring": "-FRPB",
    "stroke": "-RB",
}

connected = [
    {
        "name": "Latin A with ogonek",
        "majuscule": ("A", "Ą"),
        "minuscule": ("a", "ą"),
        "diacritics": ["ogonek"], #TODO 
        "link": "https://en.wikipedia.org/wiki/%C4%84",
    },
    {
        "name": "Cyrillic A with ogonek"
        "majuscule": ("A", "А̨"),
        "minuscule": ("a", "а̨"),
        "diacritics": ["ogonek"],
        "link": "https://en.wikipedia.org/wiki/A_with_ogonek_(Cyrillic)",
    },
    {
        "name": "A with cedilla",
        "majuscule": ("A", "Ą"),
        "minuscule": ("a", "Ą"),
        "diacritics": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "B with a hook",
        "majuscule": ("B", "Ɓ"),
        "minuscule": ("b", "ɓ"),
        "diacritics": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%81",
    },
    {
        "name": "C with hook",
        "majuscule": ("C", "Ƈ"),
        "minuscule": ("c", "ƈ"),
        "diacritics": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%87",
    },
    {
        "name": "C with cedilla",
        "majuscule": ("C", "Ç"),
        "minuscule": ("c", "ç"),
        "diacritics": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/%C3%87",
    },
    {
        "name": "D with stroke",
        "majuscule": ("D", "Đ"),
        "minuscule": ("d", "đ"),
        "diacritics": ["stroke"],
        "link": "https://en.wikipedia.org/wiki/D_with_stroke",
    },
    {
        "name": "D with hook",
        "majuscule": ("D", "Ɗ"),
        "minuscule": ("d", "ɗ"),
        "diacritics": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%8A",
    },
    {
        "name": "African D",
        "majuscule": ("D", "Ɖ"),
        "minuscule": ("d", "ɖ"),
        "diacritics": [], # TODO
        "link": "https://en.wikipedia.org/wiki/African_D",
    },
}


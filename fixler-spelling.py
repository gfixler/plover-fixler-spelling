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
}


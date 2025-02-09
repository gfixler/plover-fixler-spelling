diacritics = {
    "cedilla": "-RPB",
    "hook": "-FRP",
    "ogonek": "-PBG", # "little tail"
    "ring": "-FRPB",
    "stroke": "-RB",
    "slash": "-BL",
}

connected = [
    {
        "name": "A with ogonek",
        "majuscule": ("A", "Ą"),
        "minuscule": ("a", "ą"),
        "diacritics": ["ogonek"], #TODO 
        "link": "https://en.wikipedia.org/wiki/%C4%84",
    },
    {
        "name": "A with ogonek (Cyrillic)",
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
    {
        "name": "E with ogonek",
        "majuscule": ("E", "Ę"),
        "minuscule": ("e", "ę"),
        "diacritics": ["ogonek"],
        "link": "https://en.wikipedia.org/wiki/%C4%98",
    },
    {
        "name": "E with cedilla",
        "majuscule": ("E", "Ȩ"),
        "minuscule": ("e", "ȩ"),
        "diacritics": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "Schwa with cedilla",
        "majuscule": ("E", "Ə̧"),
        "minuscule": ("e", "ə̧"),
        "diacritics": [], # TODO
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "Ɛ̧", # TODO
        "majuscule": ("E", "Ɛ̧"),
        "minuscule": ("e", "ɛ̧"),
        "diacritics": [], # TODO
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "F with hook",
        "majuscule": ("F", "Ƒ"),
        "minuscule": ("f", "ƒ"),
        "diacritics": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%91",
    },
    {
        "name": "G with stroke",
        "majuscule": ("G", "Ǥ"),
        "minuscule": ("g", "ǥ"),
        "diacritics": ["stroke"],
        "link": "https://en.wikipedia.org/wiki/G_with_stroke",
    },
    {
        "name": "G with hook",
        "majuscule": ("G", "Ɠ"),
        "minuscule": ("g", "ɠ"),
        "diacritics": ["hook"],
        "link": "https://en.wikipedia.org/wiki/G_with_hook",
    },
    {
        "name": "H with stroke",
        "majuscule": ("H", "Ħ"),
        "minuscule": ("h", "ħ"),
        "diacritics": ["stroke"],
        "link": "https://en.wikipedia.org/wiki/H_with_stroke",
    },
    {
        "name": "Voiced glottal fricative",
        "majuscule": ("H", "Ɦ"),
        "minuscule": ("h", "ɦ"),
        "diacritics": [], # TODO
        "link": "https://en.wikipedia.org/wiki/Voiced_glottal_fricative",
    },
    {
        "name": "I with ogonek",
        "majuscule": ("I", "Į"),
        "minuscule": ("i", "į"),
        "diacritics": ["ogonek"],
        "link": "https://en.wikipedia.org/wiki/%C4%AE",
    },
    {
        "name": "I with cedilla",
        "majuscule": ("I", "I̧"),
        "minuscule": ("i", "į"),
        "diacritics": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "I with bar",
        "majuscule": ("I", "Ɨ"),
        "minuscule": ("i", "ɨ"),
        "diacritics": ["stroke"],
        "link": "https://en.wikipedia.org/wiki/I_with_bar", # TODO
    {
        "name": "Barred I with cedilla",
        "majuscule": ("I", "Ɨ̧"),
        "minuscule": ("i", "ɨ"),
        "diacritics": ["stroke", "cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "K with hook",
        "majuscule": ("K", "Ƙ"),
        "minuscule": ("k", "ƙ"),
        "diacritics": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%98",
    },
    {
        "name": "L with stroke",
        "majuscule": ("L", "Ł"),
        "minuscule": ("l", "ł"),
        "diacritics": ["slash"], # TODO
        "link": "https://en.wikipedia.org/wiki/%C5%81",
    },
    {
        "name": "L with bar",
        "majuscule": ("L", "Ƚ"),
        "minuscule": ("l", "ƚ"),
        "diacritics": ["stroke"], # TODO
        "link": "https://en.wikipedia.org/wiki/L_with_bar",
    },
    {
        "name": "M with cedilla",
        "majuscule": ("M", "M̧"),
        "minuscule": ("m", "m̧"),
        "diacritics": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "palatal nasal", # TODO
        "majuscule": ("N", "Ɲ"),
        "minuscule": ("n", "ɲ"),
        "diacritics": [], # TODO
        "link": "https://en.wikipedia.org/wiki/%C6%9D",
    },
    {
        "name": "O with ogonek",
        "majuscule": ("Q", "Ǫ"),
        "minuscule": ("q", "ǫ"),
        "diacritics": ["ogonek"],
        "link": "https://en.wikipedia.org/wiki/%C7%AA",
    },
    {
        "name": "O with cedilla",
        "majuscule": ("O", "O̧"),
        "minuscule": ("o", "o̧"),
        "diacritics": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "O with stroke",
        "majuscule": ("O", "Ø"),
        "minuscule": ("o", "ø"),
        "diacritics": ["slash"],
        "link": "https://en.wikipedia.org/wiki/%C3%98",
    },
}


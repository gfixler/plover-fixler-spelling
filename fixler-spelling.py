modifiers = {
    "cedilla": "-RPB",
    "comma": "-B",
    "hook": "-FRP",
    "horn": "-BLG",
    "ogonek": "-PBG", # "little tail"
    "ring": "-FRPB",
    "stroke": "-RB",
    "slash": "-BL",
    "turned": "-FG",
    "inverted": "-RBG",
    "reversed": "-LG",
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
        "name": "Schwa with cedilla",
        "majuscule": ("E", "Ə̧"),
        "minuscule": ("e", "ə̧"),
        "modifiers": ["inverted", "cedilla"], # TODO
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "Ɛ̧", # TODO
        "majuscule": ("E", "Ɛ̧"),
        "minuscule": ("e", "ɛ̧"),
        "modifiers": [], # TODO
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "Voiced glottal fricative",
        "majuscule": ("H", "Ɦ"),
        "minuscule": ("h", "ɦ"),
        "modifiers": [], # TODO
        "link": "https://en.wikipedia.org/wiki/Voiced_glottal_fricative",
    },
    {
        "name": "Reversed C", # TODO
        "majuscule": ("C", "Ↄ"),
        "minuscule": ("c", "ↄ"),
        "modifiers": ["reversed"],
        "link": "https://en.wikipedia.org/wiki/Claudian_letters", # TODO
    },
    {
        "name": "Reversed C with cedilla",
        "majuscule": ("C", "Ɔ̧"),
        "minuscule": ("c", "ɔ̧"),
        "modifiers": ["reversed", "cedilla"],
        "link": "https://en.wikipedia.org/wiki/%C6%86%CC%A7",
    {
        "name": "Turned F",
        "majuscule": ("F", "Ⅎ"),
        "minuscule": ("f"_ "ⅎ"),
        "modifiers": ["turned"],
        "link": "https://en.wikipedia.org/wiki/Claudian_letters", # TODO
    },
]

connectedDiacritics = [
    {
        "name": "A with ogonek",
        "majuscule": ("A", "Ą"),
        "minuscule": ("a", "ą"),
        "modifiers": ["ogonek"], #TODO
        "link": "https://en.wikipedia.org/wiki/%C4%84",
    },
    {
        "name": "A with cedilla",
        "majuscule": ("A", "Ą"),
        "minuscule": ("a", "Ą"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "B with a hook",
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
        "name": "African D",
        "majuscule": ("D", "Ɖ"),
        "minuscule": ("d", "ɖ"),
        "modifiers": [], # TODO
        "link": "https://en.wikipedia.org/wiki/African_D",
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
        "name": "I with cedilla",
        "majuscule": ("I", "I̧"),
        "minuscule": ("i", "į"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "I with bar",
        "majuscule": ("I", "Ɨ"),
        "minuscule": ("i", "ɨ"),
        "modifiers": ["stroke"],
        "link": "https://en.wikipedia.org/wiki/I_with_bar", # TODO
    {
        "name": "Barred I with cedilla",
        "majuscule": ("I", "Ɨ̧"),
        "minuscule": ("i", "ɨ"),
        "modifiers": ["stroke", "cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
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
        "modifiers": ["slash"], # TODO
        "link": "https://en.wikipedia.org/wiki/%C5%81",
    },
    {
        "name": "L with bar",
        "majuscule": ("L", "Ƚ"),
        "minuscule": ("l", "ƚ"),
        "modifiers": ["stroke"], # TODO
        "link": "https://en.wikipedia.org/wiki/L_with_bar",
    },
    {
        "name": "M with cedilla",
        "majuscule": ("M", "M̧"),
        "minuscule": ("m", "m̧"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
    },
    {
        "name": "palatal nasal", # TODO
        "majuscule": ("N", "Ɲ"),
        "minuscule": ("n", "ɲ"),
        "modifiers": [], # TODO
        "link": "https://en.wikipedia.org/wiki/%C6%9D",
    },
    {
        "name": "O with ogonek",
        "majuscule": ("Q", "Ǫ"),
        "minuscule": ("q", "ǫ"),
        "modifiers": ["ogonek"],
        "link": "https://en.wikipedia.org/wiki/%C7%AA",
    },
    {
        "name": "O with cedilla",
        "majuscule": ("O", "O̧"),
        "minuscule": ("o", "o̧"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
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
        "name": "U with cedilla",
        "majuscule": ("U", "U̧"),
        "minuscule": ("u", "u̧"),
        "modifiers": ["cedilla"],
        "link": "https://en.wikipedia.org/wiki/Cedilla",
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
        "name": "Y with ogonek",
        "majuscule": ("Y", "Y̨"),
        "minuscule": ("y", "y̨"),
        "modifiers": ["ogonek"],
        "link": "https://en.wikipedia.org/wiki/Ogonek",
    },
    {
        "name": "Y with hook",
        "majuscule": ("Y", "Ƴ"),
        "minuscule": ("y", "ƴ"),
        "modifiers": ["hook"],
        "link": "https://en.wikipedia.org/wiki/%C6%B3",
    },
}


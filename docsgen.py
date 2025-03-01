from fixspell import entries, modifiers


readmeTitle = """
# Fixler Spelling for Plover
A fingerspelling system for the [Plover](https://www.openstenoproject.org/plover/) steno software.
"""

readmeGoals = """
## Design Goals
* provide upper and lowercase letters, with some extras, like Æ/æ, and Ə/ə
* systematize writing most precomposed Latin letters with diacritics
* extend system to allow composing in combining characters
* add in other symbols, ligatures, etc., on a case-by-case basis
* include some similar alphabets (NATO, Braille, Morse, Greek, etc.)
"""

readmeSections = """
## Diacritic Keys
The following 6 keys are used to add diacritics.
```
🅂🅃🄿🄷 🄾 🅵🅿🅻🅃🄳
🅂🄺🅆🅁 🄾 🆁🅱🅶🅂🅉
　　　🄰🄾 🄴🅄
```
"""

readmeAddingModifiers = """
## Adding Diacritics/Modifiers
Modify base letters by stroking a diacritic or modifier outline immediately after a base letter.

For example, to get á, stroke A* for "a", then the acute modifier outline to convert it.

NOTE: Modifiers are currently precomposed with their letters. The system doesn't look back at previous output, meaning you must stroke the letter as defined, followed by any modifiers. This in turn means you must use this system's strokes for each letter, e.g. STKPW for "z", and not STK. Currently, the only way to fix this is to modify the python file, and regenerate the dictionary.
""" # TODO allow adding character overrides in a user-defined file

readmeTweaks = """
## Modifier Tweaks
Tweaks are added to a modifier stroke using the E and U keys:

    🅂🅃🄿🄷 🄾 🄵🄿🄻🅃🄳
    🅂🄺🅆🅁 🄾 🅁🄱🄶🅂🅉
    　　　🄰🄾 🅴🆄

|Tweak|Description|
|-|-|
|<a name="e-tweak"></a>![E](image/E_tweak.png)|Think of E as meaning "extra". This is added to acute and grave strokes to double them.|
|<a name="u-tweak"></a>![U](image/U_tweak.png)|Think of U as meaning "under". This is added to various diacritic strokes to turn them into their "below" versions: breve below, circumflex below, line below, ring below, and tilde below.|
|<a name="eu-tweak"></a>![EU](image/EU_tweak.png)|Think of EU (the "i" chord in steno) as meaning "invert".
"""

readmeAvailableDiacritics = """
## Available Diacritics/Modifiers
In general, the diacritic chords are meant to visually resemble their symbols, to ease remembering them all.

For other modifiers, like rotation or inversion, an attempt was made to be memorable. See notes with each modifier.
"""

def getEntriesWithModifier (modifier):
    search = lambda x: modifier in x["modifiers"]
    return filter(search, entries)

unicodeCodePtURL = "https://www.compart.com/en/unicode/"

def generateDiacriticsSection ():
    print("|Pattern|Notes|")
    print("|-|-|")
    for name, data in modifiers.items():
        prettyName = data["name"]
        info = data["docs"]
        print("|" + prettyName + "| |")
        chars = []
        for e in getEntriesWithModifier(name):
            for scule in ["min", "maj"]:
                if e[scule + "uscule"]:
                    l = ""
                    r = ""
                    if (scule + "CodePt") in e:
                        l = "["
                        r = "](" + unicodeCodePtURL + e[scule + "CodePt"] + ")"
                    elif e["link"]:
                        l = "["
                        r = "](" + e["link"] + ")"
                    chars.append(l + e[scule + "uscule"][1] + r)
        charsStr = " ".join(chars)
        img = "![" + name + "](images/" + name + ".png)"
        print("|" + img + "|" + info + "<BR><BR>Used in: " + charsStr + "|")

def generateReadme ():
    print(readmeTitle)
    charCount = 0
    for entry in entries:
        if "minuscule" in entry:
            if entry["minuscule"]:
                charCount += 1
        if "majuscule" in entry:
            if entry["majuscule"]:
                charCount += 1
    print("This library currently provides quick access to " + str(charCount) + " characters.")
    print(readmeGoals)
    print(readmeSections)
    print(readmeAddingModifiers)
    print(readmeTweaks)
    print(readmeAvailableDiacritics)
    generateDiacriticsSection()

if __name__ == "__main__":
    generateReadme()


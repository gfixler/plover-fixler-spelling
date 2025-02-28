from fixspell import entries, modifiers


readmeTitle = """
# Fixler Spelling for Plover
A fingerspelling system for the [Plover](https://www.openstenoproject.org/plover/) steno software.
"""

readmeGoals = """
## Design Goals
* allow writing all Latin alphabet letters, upper and lowercase
* provide system for most precomposed Latin letters with diacritics
* provide system for many common combining characters
* allow other symbols, ligatures, etc., on a case-by-case basis
* absorb some other alphabets (Greek, NATO, Braille, Morse, etc.)
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

For example, to get á, stroke A* for "a", then the acute modifier outline to  convert it.

NOTE: The outlines are [currently] pre-built, and don't take into account character output. This means you must use the chord specified for each letter in this system, before following up with a diacritic stroke. Currently, if you want to use a different stroke for a letter (like STK instead of STKPW for z), you must change it in the python file.
"""

readmeAvailableDiacritics = """
## Available Diacritics
The chords are meant to resemble their diacritics, generally speaking.

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
    print(readmeAvailableDiacritics)
    generateDiacriticsSection()

if __name__ == "__main__":
    generateReadme()


from fixspell import entries, modifiers


readmeTop = """
# Fixler Spelling for Plover
A fingerspelling system for the Plover steno software

## Design Goals
* allow writing all Latin alphabet letters, upper and lowercase
* provide system for most precomposed Latin letters with diacritics
* provide system for many common combining characters
* allow other symbols, ligatures, etc., on a case-by-case basis
* absorb some other alphabets (Greek, NATO, Braille, Morse, etc.)

## Diacritic Keys
The following 6 keys are used to add diacritics.

```
🅂🅃🄿🄷 🄾 🅵🅿🅻🅃🄳
🅂🄺🅆🅁 🄾 🆁🅱🅶🅂🅉
　　　🄰🄾 🄴🅄
```

## Adding Diacritics
Add diacritics to letters by stroking a chord from the diacritic keys after stroking a letter chord.

In general, the chord used is meant to visually resemble, the diacritic being added.

NOTE: The chords are pre-built, and don't work with Plover's stroke history. This means you must use the chord specified for each letter in this system, before following up with a diacritic stroke. Currently, if you want to use a different stroke for a letter (e.g. STK instead of STKPW for z), you must change it in the python file. This limitation may be addressed at some point.

## Available Diacritics
"""

def getEntriesWithModifier (modifier):
    search = lambda x: modifier in x["modifiers"]
    return filter(search, entries)

def generateDiacriticsSection ():
    print("|Pattern|Notes|")
    print("|-|-|")
    for modifierName in modifiers:
        print("|" + modifierName.capitalize() + "| |")
        chars = []
        for e in getEntriesWithModifier(modifierName):
            maju = e["majuscule"][1] if e["majuscule"] else ""
            minu = e["minuscule"][1] if e["minuscule"] else ""
            chars += maju + minu
        charsStr = " ".join(chars)
        img = "![" + modifierName + "](images/" + modifierName + ".png)"
        print("|" + img + "|Used in: " + charsStr + "|")

def generateReadme ():
    print(readmeTop)
    generateDiacriticsSection()


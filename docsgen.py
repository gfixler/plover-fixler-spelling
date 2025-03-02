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

readmeNotesOnDesign = """
## Notes on Design
The core of this system is about spelling, and revolves around the Latin letters with diacritics, and alphabets that map well to and from Latin letters. That said, this library is not above including other, fun things that don't exactly fit, but also don't feel terribly out of place here.

Modifiers do not currently look at stroke history. The modifier system simply creates multi-stroke outlines that pair a base letter with one or more modifiers, e.g., "á" ("a with acute") is simply defined as the two-stroke outline, A*/-RP. You can't stroke KAT to write "cat", then stroke a modifier to add a diacritic to the "t" on the end of the word.

Because letters are "baked in" to the outlines with their modifiers, it means you must use the letter chords as defined in this library. This limitation should be removed in the future. This means if you use STK for "z", for example, and this system uses STKPW, you must use this system's version to write, e.g., the ẓ character.

All characters in the core system, seen in the "Used by" lists following each modifier in the [Available Diacritics/Modifiers](#available-diacriticsmodifiers) section below are "precomposed" characters in Unicode, meaning they have a single code point in The Unicode Standard. Many characters not in these lists, encountered in the wild, are actually composed of a base letter, and one or more [combining characters](https://en.wikipedia.org/wiki/Combining_character). For example, z with acute exists in Unicode, but currently, z with grave does not, so it's not in the core system here. If you see a z with grave, it's composed of small letter z (U+007A) and the combining grave diacritic (U+0323). Even characters that do have a precomposed (single code point) version often show up as [composed versions](https://en.wikipedia.org/wiki/Unicode_equivalence) of themselves.

Characters with more than one modifier, like "ẫ" ("a with circumflex and tilde"), are made by stroking the letter chord, followed by each modifier chord in sequence. The order of these is based primarily on the Unicode name, where "ẫ" (Unicode code point U+1EAB) is called "LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE", and means you stroke the circumflex modifier before the tilde modifier.
"""
# TODO allow adding character overrides in a user-defined file

readmeSections = """
## Diacritic Keys
The following 6 keys are used to add diacritics.
```
🅂🅃🄿🄷 🄾 🅵🅿🅻🅃🄳
🅂🄺🅆🅁 🄾 🆁🅱🅶🅂🅉
　　　🄰🄾 🄴🅄
```
"""

readmeUsingModifiers = """
## UsingDiacritics/Modifiers
Modify base letters by stroking a diacritic or modifier outline immediately after a base letter.

For example, to get á, stroke A* for "a", then the acute modifier outline to convert it.
"""

readmeTweaks = """
## Modifier Tweaks
Tweaks are added to a modifier stroke using the E and U keys.

|Tweak|Description|
|-|-|
|![EU Up](images/EU_up.png)|Neither E nor U pressed means no tweak to the modifier stroke.|
|![E Down](images/E_down.png)|Think of E as meaning "extra". This is added to acute and grave strokes to double them.|
|![U Down](images/U_down.png)|Think of U as meaning "under". This is added to various diacritic strokes to turn them into their "below" versions: breve below, circumflex below, line below, ring below, and tilde below.|
|![EU Down](images/EU_down.png)|Think of EU (the "i" chord in steno) as meaning "invert".
"""

readmeAvailableDiacritics = """
## Available Diacritics/Modifiers
In general, the diacritic chords are meant to visually resemble their symbols, to ease remembering them all.

For other modifiers, like rotation or inversion, an attempt was made to be memorable. See notes with each modifier.

NOTE: Modifier and Tweak are part of the same stroke.
"""

def getEntriesWithModifier (modifier):
    search = lambda x: modifier in x["modifiers"]
    return filter(search, entries)

unicodeCodePtURL = "https://www.compart.com/en/unicode/"

def generateDiacriticsSection ():
    print("|Modifier|Tweak|Notes|")
    print("|-|-|-|")
    for name, data in modifiers.items():
        prettyName = data["name"]
        info = data["docs"]
        stroke = data["outline"]
        tweak = "EU_up"
        if "E" in stroke and "U" in stroke:
            tweak = "EU_down"
        elif "E" in stroke:
            tweak = "E_down"
        elif "U" in stroke:
            tweak = "U_down"
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
        print("|" + img + "|![tweak](images/" + tweak + ".png)|" + info + "<BR><BR>Used in: " + charsStr + "|")

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
    print(readmeNotesOnDesign)
    print(readmeSections)
    print(readmeUsingModifiers)
    print(readmeTweaks)
    print(readmeAvailableDiacritics)
    generateDiacriticsSection()

if __name__ == "__main__":
    generateReadme()


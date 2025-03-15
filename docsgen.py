import unicodedata


from fixspell import \
    entries, \
    modifiers, \
    latinAlphabetLUT, \
    greekAlphabetLUT, \
    russianAlphabetLUT, \
    buildFingerspellingDict


# build entire fingerspelling dictionary
allCharacters = buildFingerspellingDict()

# get count of all characters for use in docs
charCount = len(allCharacters)


readmeTitle = """
# Fixler Spelling for Plover
A fingerspelling system for the [Plover](https://www.openstenoproject.org/plover/) steno software.
"""

readmeGoals = """
## Design Goals
* provide upper and lowercase English alphabet
* systematize writing many Latin letters with diacritics
* allow use of many diacritics as combining diacritical marks
* systematize writing many ligatures, rotations, inversions, etc.
* include some other alphabets where possible (Greek, NATO, Morse...)
"""

readmeNotesOnDesign = """
## Notes on Design
### The Core
The core of this system is spelling, and revolves around the Latin letters with diacritics, and alphabets that map well to and from Latin letters. That said, this library is not above including other, fun things that don't exactly fit, but also don't feel terribly out of place here.

### It's Just Outlines
Modifiers are not currently programmatic, and do not look at stroke history. This is not a Plover Python dictionary. The modifier system simply exports a JSON file filled with multi-stroke outlines that pair a base letter with one or more modifiers. This means "á" ("a with acute") is simply defined as the two-stroke outline, A*/-RP. You can't stroke KAT to write "cat", then stroke a modifier to add a diacritic to the "t" at the end of the word.

### System Letters
Because letter chords are part of the outlines with their modifiers, you must use the letter chords as defined in this library. This means if you use STK for "z", for example, and this system uses STKPW, you must use this system's version to write, e.g., the ẓ character. Currently, the way around this is to modify the Python file, and reexport the dictionary.

### Precomposed Characters
All characters defined in this system—as seen in the "Used by" lists following each modifier in the [Available Diacritics and Other Modifiers](#available-diacritics-and-other-modifiers) section below—are "precomposed" characters in Unicode, meaning they have a single code point in The Unicode Standard. Many characters not in these lists, encountered in the wild, are actually composed of a base letter, with one or more [combining characters](https://en.wikipedia.org/wiki/Combining_character) following them. For example, z with acute exists in Unicode, but currently (Unicode v16.0), z with grave does not, so it's not defined in the core system here. If you see a z with grave, it's composed of small letter z (U+007A) and the combining grave diacritic (U+0323). Even characters that do have a precomposed (single code point) version often show up in the wild as [composed versions](https://en.wikipedia.org/wiki/Unicode_equivalence) of themselves. (See: [When an é is not an é](https://nation.marketo.com/t5/product-blogs/when-an-e%CC%81-is-not-an-%C3%A9-about-unicode-precomposed-vs-decomposed/ba-p/339051)).

### Stacking Modifiers
Characters with more than one modifier, like "ẫ" ("a with circumflex and tilde"), are made by stroking the letter chord, followed by each modifier chord in sequence. The order of these is based on the Unicode name, where "ẫ" (Unicode code point U+1EAB) is called "LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE", and means you stroke the circumflex modifier before the tilde modifier.<BR><BR>Unicode actually has a collation order for diacritics, based on things like closeness to the base character, and position around the character, but it's [a bit involved](https://www.unicode.org/reports/tr10/). Ultimately, Unicode doesn't care in what order diacritics are combined, and will normalize multiple diacritics back to a canonical ordering. The way around this is to use the [combining grapheme joiner](https://en.wikipedia.org/wiki/Combining_grapheme_joiner), but that's currently outside the scope of this system.

### Playing Nice
When coming up with alphabet enders, and the starter for combining diacritics, I tried hard not to stomp on some really great systems in the Plover world, including [Emily's Symbols](https://github.com/EPLHREU/emily-symbols), [Emily's Modifiers](https://github.com/EPLHREU/emily-modifiers), and [Jeff's phrasing system](https://github.com/jthlim/jeff-phrasing). That said, I did not scan several other things, like [Lapwing theory](https://lapwing.aerick.ca/), and [Cocoa theory](https://github.com/Kaoffie/cocoa-specs).
"""

readmeSections = """
## Modifier Keys
The following 6 keys are used to add diacritics and other modifiers.

See the following section, [Using Modifiers](#using-modifiers), for usage instructions.
```
🅂🅃🄿🄷 🄾 🅵🅿🅻🅃🄳
🅂🄺🅆🅁 🄾 🆁🅱🅶🅂🅉
　　　🄰🄾 🄴🅄
```
"""

readmeUsingModifiers = """
## Using Modifiers
Modify base letters by stroking a diacritic or modifier outline immediately after a base letter.

For example, to get á, stroke A* for "a", then the acute modifier outline to convert it.
"""

readmeTweaks = """
## Modifier Tweaks
Tweaks are added to a modifier stroke using the E and U keys.

|Tweak|Description|
|-|-|
|![EU Up](images/EU_up.png)|Neither E nor U pressed means no tweak to the modifier stroke.|
|![E Down](images/E_down.png)|Think of E as meaning "extra". This is added to acute and grave strokes to double them, but also serves as a kind of wildcard when something "extra" is needed from a modifier, whatever that may be.|
|![U Down](images/U_down.png)|Think of U as meaning "under". This is added to various diacritic strokes to turn them into their "below" versions: breve below, circumflex below, line below, ring below, and tilde below.|
|![EU Down](images/EU_down.png)|Think of EU (the "i" chord in steno) as meaning "invert".
"""

readmeAvailableDiacritics = """
## Available Diacritics and Other Modifiers
In general, the diacritic chords are meant to visually resemble their symbols, to ease remembering them all.

For other modifiers, like rotation or inversion, which appear after the diacritics in the below list, an attempt was made to be memorable. See notes with each modifier.

NOTE: Modifier and Tweak are part of the same stroke.
"""

unicodeCodePtURL = "https://www.compart.com/en/unicode/"
toCodePt = lambda char: "U+" + ("0000" + hex(ord(char))[2:])[-4:].upper()
toURL = lambda char: unicodeCodePtURL + toCodePt(char)

def ccc_sort_key (c):
    normalized = unicodedata.normalize("NFD", c)
    base_letter = normalized[0]
    return (base_letter.lower(), normalized[1:], base_letter.islower())

def getEntriesWithModifier (modifier):
    search = lambda x: modifier in x["modifiers"]
    return filter(search, entries)

def getAnchorTextForChar (c):
     return "-".join(unicodedata.name(c).lower().split())

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
        for entry in getEntriesWithModifier(name):
            for scule in ["min", "maj"]:
                sculeData = entry[scule + "uscule"]
                if sculeData != None:
                    character = sculeData[1]
                    anchor = getAnchorTextForChar(character)
                    chars.append("[" + character + "](#char-" + anchor + ")")
        charsStr = " ".join(sorted(chars, key=ccc_sort_key))
        img = "![" + name + "](images/" + name + ".png)"
        print("|" + img + "|![tweak](images/" + tweak + ".png)|" + info + "<BR><BR>Used in: " + charsStr + "|")

readmeAllCharacters = """
## All Characters List
Here are [currently] all """ + str(charCount) + """ characters this library exports.

Code points currently link to their associated page on [Compart](https://www.compart.com/en/about-compart)'s site. No affiliation; it just showed up in character searches, seems to have all pages, and it's easy to turn Unicode code points into its various URLs.

There are many ways to sort such a list. I opted not to go with Unicode code point, because it ends up somewhat nonsensical. Instead, I wrote a custom sort based on a 3-tuple of:

    1. lowercase base letter (e.g. "a" for "Â")
    2. decomposed, Unicode-ordered diacritics list
    3. True if base letter is lower, otherwise False

This creates a list that feels at least a bit alphabetical in nature, and positions upper and lowercase letters with the same diacritics together.

|Char|Code Pt|Name|
|-|-|-|"""

readmeKnownIssues = """
## Known Issues
* We'll probably never get all combining diacritics. There are hundreds, including things like [Znamenny Combining Mark Gorazdo Nizko S Kryzhem On Right](https://codepoints.net/znamenny_musical_notation).
* We're also never getting anywhere near all of Unicode, even just the "spelling" bits, as Unicode v16 now has more than 65,000 code points.
* The characters native to this system are all precomposed, i.e. they have a single Unicode code point. As you add diacritics, you're always replacing one single code point character with another. If you try to add a diacritic to a character that doesn't exist as a single code point in Unicode, you'll just get an untrans. All of this goes for non-diacritic modifiers as well. This isn't so much an issue, as a design decision, something for the user to be aware of. The system could try to solve for this and compose a character out of combining diacritics, when a single code point version doesn't exist, but that would be messy, and lead to confusion, especially given the next issue...
* When you press star to undo the addition of a diacritic or modification, Plover will simply re-replace the character with the previous one it came from. This works for all the single-code-point characters native to the system. However, if you use the combining diacritics feature, this doesn't work; star will delete the entire character you composed, even if you combined in 5 diacritics. This matches how backspace works for me for combined characters in every program I've tried, so it's not super out of the ordinary, but it can be a bit jarring to write a character, combine in two diacritics, star back to remove the last one, and have the entire character vanish. If anyone has a fix for this, let me know.
"""

def generateReadme ():
    print(readmeTitle)
    print("This library currently provides quick access to " + str(charCount) + " characters.")
    print(readmeGoals)
    print(readmeNotesOnDesign)
    print(readmeSections)
    print(readmeUsingModifiers)
    print(readmeTweaks)
    print(readmeAvailableDiacritics)
    generateDiacriticsSection()
    print(readmeAllCharacters)
    chars = []
    for entry in entries:
        if entry["minuscule"] != None:
            chars.append(entry["minuscule"][1])
        if entry["majuscule"] != None:
            chars.append(entry["majuscule"][1])
    chars += (latinAlphabetLUT)
    chars += (greekAlphabetLUT)
    chars += (russianAlphabetLUT)
    cccs = sorted(chars, key=ccc_sort_key)
    for ccc in cccs:
        anchor = "<a name=\"char-" + getAnchorTextForChar(ccc) + "\"></a>"
        print("|" + anchor + ccc + "|[" + toCodePt(ccc) + "](" + toURL(ccc) + ")|" + unicodedata.name(ccc) + "|")
    print(readmeKnownIssues)


if __name__ == "__main__":
    generateReadme()


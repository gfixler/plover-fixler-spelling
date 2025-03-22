import unicodedata


from fixspell import \
    MODIFIERS, \
    ALPHABETS, \
    CHAR_MOD_LISTS, \
    buildFingerspellingDict


# build entire fingerspelling dictionary
fullSpellingDict = buildFingerspellingDict()

# get count of all characters for use in docs
charCount = len(fullSpellingDict)

superAlphabet = dict([kv for d in ALPHABETS for kv in d.items()])


readmeTitle = """
# Fixler Spelling for Plover
A fingerspelling system for the [Plover](https://www.openstenoproject.org/plover/) steno software.
"""

readmeTOC = """
## Table of Contents
This is a long readme. GitHub provides a table of contents under the hamburger menu, at the top right of this readme.

The burger menu looks like this:
![burger menu](images/hamburgerMenu.png)
"""

readmeGoals = """
## Design Goals
* provide upper and lowercase English alphabet
* systematize writing many Latin letters with diacritics
* allow use of many diacritics as combining diacritical marks
* systematize writing many ligatures, rotations, inversions, etc.
* include some other alphabets where possible (Greek, Russian, NATO...)
"""

readmeNotesOnDesign = """
## Notes on Design
### The Core
The core of this system is fingerspelling, and revolves around the Latin letters with diacritics, and alphabets that map well to and from Latin letters. That said, this library is not above including other, fun things that don't exactly fit, but also don't feel terribly out of place here.

### It's Just Outlines
Modifiers are not currently programmatic, and do not look at stroke history. This is not a Plover Python dictionary. The modifier system simply exports a JSON file mapping letters to outlines.

### System Letters
Because letter chords are part of the outlines with their modifiers, you must use the letter chords as defined in this library. This means if you use STK for "z", for example, and this system only exports STKPW, you must use this system's version when composition, e.g., the ẓ ("Z with dot below") character. Currently, the way around this is to modify the Python file, and reexport the dictionary.

### Precomposed Characters
All characters defined in this system, as seen in the "Used by" lists following each modifier in the [Available Diacritics and Other Modifiers](#available-diacritics-and-other-modifiers) section, and in the [All Characters List](#all-characters-list), are "precomposed" characters in Unicode, meaning they have a single code point in The Unicode Standard. Many characters encountered in the wild, are actually composed of a base letter, with one or more [combining characters](https://en.wikipedia.org/wiki/Combining_character) following them, and your font rendering system does the work of displaying them in composed form, although they can look different, and may fail to render well, or not at all.

For example, "Z with acute" exists in Unicode (Ź: U+0179, ź: U+017A), but currently (Unicode v16.0), "Z with grave" does not, so it's **not** defined in the core system here. If you see a z with grave, it's composed of small letter z (U+007A) followed by the combining grave diacritic (U+0323). Even characters that do have a precomposed (single code point) version often show up in the wild as [composed versions](https://en.wikipedia.org/wiki/Unicode_equivalence) of themselves. (See: [When an é is not an é](https://nation.marketo.com/t5/product-blogs/when-an-e%CC%81-is-not-an-%C3%A9-about-unicode-precomposed-vs-decomposed/ba-p/339051)).

### Stacking Modifiers
Characters with more than one modifier, like "ẫ" ("A with circumflex and tilde"), are made by stroking the letter chord, followed by each modifier chord in sequence. The order of these is based on the Unicode name, where "ẫ" (Unicode code point U+1EAB) is called "LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE", and means you stroke the circumflex modifier before the tilde modifier.<BR><BR>Unicode has a collation order for diacritics, based on things like "closeness" to, and position around, the base character, but it's [a bit involved](https://www.unicode.org/reports/tr10/). Ultimately, Unicode doesn't care in what order diacritics are combined, and will normalize multiple diacritics back to a canonical ordering. Side note: The way around this is to use the [combining grapheme joiner](https://en.wikipedia.org/wiki/Combining_grapheme_joiner), but that's currently outside the scope of this system.

### Playing Nice
When coming up with alphabet enders, and the starter for combining diacritics, I tried hard not to stomp on some really great systems in the Plover world, including [Emily's Symbols](https://github.com/EPLHREU/emily-symbols), [Emily's Modifiers](https://github.com/EPLHREU/emily-modifiers), and [Jeff's phrasing system](https://github.com/jthlim/jeff-phrasing).<BR><BR>I also wrote some code to scour Plover's main.json, to find unique enders that don't conflict, when combined with the standard steno alphabet. For example,  I wouldn't use -FR as an ender, because AFR is the after– prefix, and EFR is "every". Tons of chords are open on the right-hand side, but are very uncomfortable to stroke. I tried to find things with some mnemonic aspect, that still felt ergonomic. That said, I did not scan everything out there for conflicts, like [Lapwing theory](https://lapwing.aerick.ca/), and [Cocoa theory](https://github.com/Kaoffie/cocoa-specs).
"""

# TODO allow stroking diacritics and modifiers in any order
# TODO allow customizing starters, enders, letters, etc.

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
# TODO replace graphic above with rendered image version

readmeUsingModifiers = """
## Using Modifiers
Modify base letters by stroking a diacritic or modifier outline, or sequences thereof, immediately after a base letter. See [Available Diacritics and Other Modifiers](#available-diacritics-and-other-modifiers) section.

#### Examples
á (A with acute): Stroke letter a, then the acute diacritic
AE (AE ligature): Stroke a, then e, then the ligature modifier
ẫ (A with circumflex and tilde) Stroke a, then each diacritic
ǽ (AE ligature with acute) Stroke a, e, ligature, then acute
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
In general, the diacritic chords are meant to visually resemble their symbols, to ease recall.

For other modifiers—like rotation or inversion, which appear after the diacritics in the list below—an attempt was made to be memorable. See notes with each modifier.

NOTE: Modifier and Tweak are part of the same stroke.
"""

unicodeCodePtURL = "https://www.compart.com/en/unicode/"
toCodePt = lambda char: "U+" + ("0000" + hex(ord(char))[2:])[-4:].upper()
toURL = lambda char: unicodeCodePtURL + toCodePt(char)

def ccc_sort_key (c):
    normalized = unicodedata.normalize("NFD", c)
    base_letter = normalized[0]
    return (base_letter.lower(), normalized[1:], base_letter.islower())

def getEntriesWithModifiers (charModLists, usedMods):
    search = lambda x: usedMods in x["modifiers"]
    return filter(search, charModLists)

def getAnchorTextForChar (c):
     return "-".join(unicodedata.name(c).lower().split())

def generateModifiersSection ():
    print("|Modifier|Tweak|Notes|")
    print("|-|-|-|")
    for name, data in MODIFIERS.items():
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
        print("|" + prettyName + "| | |")
        chars = []
        for charModList in CHAR_MOD_LISTS:
            for entry in getEntriesWithModifiers(charModList, name):
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

Code points currently link to their associated page on [Compart](https://www.compart.com/en/about-compart)'s site. No affiliation; it just showed up in character searches, seems to have all pages, and it's easy to turn Unicode code points into its URLs.

There are many ways to sort such a list. I opted not to go with Unicode code point, because it ends up somewhat nonsensical. Instead, this uses a custom sort based on a 3-tuple of:

    1. lowercase base letter (e.g. "a" for "Â")
    2. decomposed, Unicode-ordered, diacritics list
    3. True, if base letter is lower, otherwise False

This creates a list that feels at least a bit alphabetical in nature, and positions upper and lowercase letters with the same diacritics together.

|Char|Code Pt|Name|
|-|-|-|"""

readmeKnownIssues = """
## Known Issues
* Despite careful efforts, some conflicts are bound to arise. I've run into a few, like "ABCs of"—fingerspelling the first bit—became "ABCṡ", where the -F for "of" turned the "s" into "s with dot above". The solution was to add a space (S-P for me) before the -F. As we tend not to spell often in steno, and this system is really just to give access to a much broader range of characters for the occasional need, I think this is, and should remain, a small issue.
* We'll probably never get all combining diacritics. There are hundreds, including things like [Znamenny Combining Mark Gorazdo Nizko S Kryzhem On Right](https://codepoints.net/znamenny_musical_notation).
* We're also never getting anywhere near all of Unicode, even just the "spelling" bits, as Unicode v16 now has more than 65,000 code points.
* The characters native to this system are all precomposed, i.e. they have a single Unicode code point. As you add diacritics, you're always replacing one single code point character with another. If you try to add a diacritic to a character that doesn't exist as a single code point in Unicode, you'll just get an untrans. All of this goes for non-diacritic modifiers as well. This isn't so much an issue, as a design decision, something for the user to be aware of. The system could try to solve for this and compose a character out of combining diacritics, when a single code point version doesn't exist, but that would be messy, and lead to confusion, especially given the next issue...
* When you press star to undo the addition of a diacritic or modification, Plover will simply re-replace the character with the previous one it came from. This works for all the single-code-point characters native to the system. However, if you use the combining diacritics feature, this doesn't work; star will delete the entire character you composed, even if you combined in 5 diacritics. This matches how backspace works for me for combined characters in every program I've tried, so it's not super out of the ordinary, but it can be a bit jarring to write a character, combine in two diacritics, star back to remove the last one, and have the entire character vanish.
"""

def generateReadme ():
    print(readmeTitle)
    print("This library currently provides quick access to " + str(charCount) + " characters.")
    print(readmeTOC)
    print(readmeGoals)
    print(readmeNotesOnDesign)
    print(readmeSections)
    print(readmeUsingModifiers)
    print(readmeTweaks)
    print(readmeAvailableDiacritics)
    generateModifiersSection()
    print(readmeAllCharacters)
    chars = []
    for charModList in CHAR_MOD_LISTS:
        for entry in charModList:
            if entry["minuscule"] != None:
                chars.append(entry["minuscule"][1])
            if entry["majuscule"] != None:
                chars.append(entry["majuscule"][1])
    for alphabet in ALPHABETS:
        chars += alphabet.keys()
    cccs = sorted(chars, key=ccc_sort_key)
    for ccc in cccs:
        anchor = "<a name=\"char-" + getAnchorTextForChar(ccc) + "\"></a>"
        print("|" + anchor + ccc + "|[" + toCodePt(ccc) + "](" + toURL(ccc) + ")|" + unicodedata.name(ccc) + "|")
    print(readmeKnownIssues)


if __name__ == "__main__":
    generateReadme()


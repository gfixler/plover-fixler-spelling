import unicodedata


from fixspell import \
    DIACRITICS, \
    MODIFIERS, \
    ALPHABET_DATA, \
    ALPHABETS, \
    CHAR_MOD_LISTS, \
    mergeStrokes, \
    renderStroke, \
    buildFingerspellingDict


# build entire fingerspelling dictionary
fullSpellingDict = buildFingerspellingDict()

# get count of all characters for use in docs
charCount = len(fullSpellingDict)

superAlphabet = dict([kv for d in ALPHABETS for kv in d.items()])


readmeTitle = """
# Fixler Spelling for Plover
A fingerspelling system for the [Plover](https://www.openstenoproject.org/plover/) steno software.

This library currently provides quick access to """ + str(charCount) + """ characters.
"""

readmeGoals = """
## Design Goals
* provide upper and lowercase English alphabet
* systematize writing many Latin letters with diacritics
* allow use of many diacritics as combining diacritical marks
* systematize writing many ligatures, rotations, inversions, etc.
* include some other alphabets where possible (Greek, Russian, NATO...)
"""

readmeTOC = """
## Table of Contents
This is a long readme. GitHub provides a table of contents under the hamburger menu, at the top right of this readme.

The hamburger menu looks like this:

![burger menu](images/hamburgerMenu.png)
"""

readmeInstallation = """
## Installation

Just save the `fixler-spelling.json` file somewhere locally, probably in your Plover config directory (`File → Open config folder` in Plover). Then add it to your dictionaries in Plover, wherever makes sense to you, or at the top, if you're not sure.

Note: This is not a Python dictionary.
"""

readmeNotesOnDesign = """
## Notes on Design
### The Core
The core of this system is fingerspelling, and revolves around the Latin letters with diacritics, and alphabets that map well to and from Latin letters. That said, this library is not above including other, fun things that don't exactly fit, but also don't feel terribly out of place here.

### It's Just Outlines
Modifiers are not currently programmatic, and do not look at stroke history. This is not a Plover Python dictionary. The modifier system simply exports a JSON file mapping letters to outlines.

### System Letters
Because letter chords are part of the outlines with their modifiers, you must use the letter chords as defined in this library. This means if you use STK for "z", for example, and this system only exports STKPW, you must use this system's version when composing, e.g., the ẓ ("Z with dot below") character. Currently, the way around this is to modify the Python file, and reexport the dictionary. Note: This system does export both of those chords for Z/z, and their compositions..

### Precomposed Characters
All characters defined in this system, as seen in the "Used by" lists following each modifier in the [Available Diacritics and Other Modifiers](#available-diacritics-and-other-modifiers) section, and in the [All Characters List](#all-characters-list), are "precomposed" characters in Unicode, meaning they have a single code point in The Unicode Standard. Many letters with diacritics, encountered in the wild, are really composed of a base letter, with one or more [combining characters](https://en.wikipedia.org/wiki/Combining_character) following them, and your font rendering system does the work of displaying them in composed form, although they can look different, and may fail to render well, or not at all.

For example, "Z with acute" exists in Unicode (Ź: U+0179, ź: U+017A), and is thus defined in this system, but currently (Unicode v16.0), "Z with grave" does not, so it's **not** defined here. If you see a z with grave, somewhere, it's composed of small letter z (U+007A) followed by the combining grave diacritic (U+0323). Even characters that do have a precomposed (single code point) version often show up in the wild as [composed versions](https://en.wikipedia.org/wiki/Unicode_equivalence) of themselves. (See: [When an é is not an é](https://nation.marketo.com/t5/product-blogs/when-an-e%CC%81-is-not-an-%C3%A9-about-unicode-precomposed-vs-decomposed/ba-p/339051)).

### Stacking Modifiers
Characters with more than one modifier, like "ẫ" ("A with circumflex and tilde"), are made by stroking the letter chord, followed by each modifier chord in sequence. The order of these is based on the Unicode name, where "ẫ" (Unicode code point U+1EAB) is called "LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE", and means you stroke the circumflex modifier before the tilde modifier.<BR><BR>Unicode has a collation order for diacritics, based on things like "closeness" to, and position around, the base character, but it's [a bit involved](https://www.unicode.org/reports/tr10/). Ultimately, Unicode doesn't care in what order diacritics are combined, and will normalize multiple diacritics back to a canonical ordering. Side note: The way around this is to use the [combining grapheme joiner](https://en.wikipedia.org/wiki/Combining_grapheme_joiner), but that's currently outside the scope of this system.

### Playing Nice
When coming up with alphabet enders, and the starter for combining diacritics, I tried hard not to stomp on some really great systems in the Plover world, including [Emily's Symbols](https://github.com/EPLHREU/emily-symbols), [Emily's Modifiers](https://github.com/EPLHREU/emily-modifiers), and [Jeff's phrasing system](https://github.com/jthlim/jeff-phrasing).<BR><BR>I also wrote some code to scour Plover's main.json, to find unique enders that don't conflict, when combined with the standard steno alphabet chords. For example,  I wouldn't use -FR as an ender, because AFR is the after– prefix, and EFR is "every". Tons of chords are open on the right-hand side, but are very uncomfortable to stroke. I tried to find things with some mnemonic aspect, that still felt ergonomic. That said, I did not scan everything out there for conflicts, like [Lapwing theory](https://lapwing.aerick.ca/), and [Cocoa theory](https://github.com/Kaoffie/cocoa-specs).
"""

# TODO allow stroking diacritics and modifiers in any order
# TODO allow customizing starters, enders, letters, etc.

readmeKeyboardSections = """
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
Modify base letters by stroking a diacritic or modifier outline, or sequences thereof, immediately after a base letter. See the [Available Diacritics and Other Modifiers](#available-diacritics-and-other-modifiers) section.

#### Examples
* á (A with acute): Stroke letter a, then the acute diacritic
* AE (AE ligature): Stroke a, then e, then the ligature modifier
* ẫ (A with circumflex and tilde) Stroke a, then each diacritic
* ǽ (AE ligature with acute) Stroke a, e, ligature, then acute
"""

readmeTweaks = """
## Modifier Tweaks
Tweaks are added to a modifier stroke using the E and U keys.

The descriptions explain the general idea of each, but liberties are taken here and there by some modifiers, to eke more abilities from each, like, in one example, using the I (EU) tweak to mean "italic". See notes with each modifier in the [Available Diacritics and Other Modifiers](#available-diacritics-and-other-modifiers) section.

|Tweak|Description|
|-|-|
|![EU Up](images/EU_up.png)|Neither E nor U pressed means no tweak to the modifier stroke.|
|![E Down](images/E_down.png)|Think of E as meaning "extra". This is added to acute and grave strokes to double them, but also serves as a kind of wildcard when something "extra" is needed from a modifier, whatever that may be.|
|![U Down](images/U_down.png)|Think of U as meaning "under". This is added to various diacritic strokes to turn them into their "below" versions: breve below, circumflex below, line below, ring below, and tilde below.|
|![EU Down](images/EU_down.png)|Think of EU (the "i" chord in steno) as meaning "invert".
"""

readmeAvailableDiacritics = """
## Available Diacritics and Other Modifiers
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
    for modDict in [DIACRITICS, MODIFIERS]:
        print("## " + modDict["name"] + "<BR>")
        print(modDict["docs"])
        print("|Chord|Tweak|Notes|")
        print("|-|-|-|")
        for name, data in modDict["modifiers"].items():
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

def generateAllCharactersSection ():
    print("""## All Characters List
Here are [currently] all """ + str(charCount) + """ characters this library exports, base alphabets first, followed by all composed characters built from them.

Code points currently link to their associated page on [Compart](https://www.compart.com/en/about-compart)'s site. No affiliation; it just showed up in character searches, seems to have all pages, and it's easy to turn Unicode code points into its URLs.
""")
    # first, the alphabets
    for alphabet in ALPHABET_DATA:
        name = alphabet["name"]
        docs = alphabet["docs"]
        letters = alphabet["letters"]
        majStroke = alphabet["majStroke"]
        minStroke = alphabet["minStroke"]
        print("### " + name)
        print(alphabet["enderThoughts"] + "<BR>")
        print("**Majuscule Ender:** `" + majStroke + "`<BR>")
        print("**Minuscule Ender:** `" + minStroke + "`<BR>")
        print("<BR>")
        print(docs + "<BR>")
        print("|Letter|Code Pt|Name|Stroke(s)|Notes|")
        print("|-|-|-|-|-|")
        for letter in letters:
            for scule, sculeStroke in [("maj", majStroke), ("min", minStroke)]:
                char = letter[scule + "uscule"]
                if char is not None:
                    docs = letter["docs"] if "docs" in letter else ""
                    strokes = ["`" + renderStroke(mergeStrokes(sculeStroke, stroke)) + "`" for stroke in letter["strokes"]]
                    strokesStr = "<BR>".join(strokes)
                    print("|" + char + "|[" + toCodePt(char) + "](" + toURL(char) + ")|" + unicodedata.name(char) + "|" + strokesStr + "|" + docs + "|")

    print("""### All Composed Characters

There are many ways to sort such a list. I opted not to go with Unicode code point, because it ends up somewhat nonsensical. Instead, this uses a custom sort based on a 3-tuple of:

1. lowercase base letter (e.g. "a" for "Â")
2. decomposed, Unicode-ordered, diacritics list
3. True, if base letter is lower, otherwise False

This creates a list that feels at least a bit alphabetical in nature, and positions upper and lowercase letters with the same diacritics together.
""")
    chars = [] # for collecting every exported character on its own
    modHowTos = {} # reverse lookup of mod strokes per character
    print("|Char|Code Pt|Name + How To Stroke|\n|-|-|-|")
    # go through all modified character data lists
    for charModList in CHAR_MOD_LISTS:
        for entry in charModList:
            for scule in ["min", "maj"]:
                # not every character has both minuscule and majuscule
                if entry[scule + "uscule"] != None:
                    src, dest = entry[scule + "uscule"]
                    # remember how to build the character
                    # e.g. "ẫ": ["a", "circumflex", "tilde"]
                    modHowTos[dest] = [src] + entry["modifiers"]
                    # record this character in the list of exported
                    chars.append(dest)
    # sort all characters into a decent sorting for output
    cccs = sorted(chars, key=ccc_sort_key)
    for ccc in cccs:
        # create anchor, so other parts of readme can link to each character
        anchor = "<a name=\"char-" + getAnchorTextForChar(ccc) + "\"></a>"
        # assemble parts of character to show how to build it in strokes
        howTo = " + ".join(modHowTos[ccc]) if ccc in modHowTos else ""
        print("|" + anchor + ccc + "|[" + toCodePt(ccc) + "](" + toURL(ccc) + ")|" + unicodedata.name(ccc) + "<BR>" + howTo + "|")


readmeKnownIssues = """
## Known Issues
* Despite careful efforts, some conflicts are bound to arise. I've run into a few, like "ABCs of"—fingerspelling the first bit—became "ABCṡ", where the -F for "of" turned the "s" into "s with dot above". The solution was to add a space (S-P for me) before the -F. As we tend not to spell often in steno, and this system is really just to give access to a much broader range of characters for the occasional need, I think this is, and should remain, a small issue.
* We'll probably never get all combining diacritics. There are hundreds, including things like [Znamenny Combining Mark Gorazdo Nizko S Kryzhem On Right](https://codepoints.net/znamenny_musical_notation).
* We're also never getting anywhere near all of Unicode, even just the "spelling" bits, as Unicode v16 is a mere two code points shy of 155,000 entries.
* The characters native to this system are all precomposed, i.e. they have a single Unicode code point. As you add diacritics, you're always replacing one single code point character with another. If you try to add a diacritic to a character that doesn't exist as a single code point in Unicode, you'll just get an untrans. All of this goes for non-diacritic modifiers as well. This isn't so much an issue, as a design decision, something for the user to be aware of. The system could try to solve for this and compose a character out of combining diacritics, when a single code point version doesn't exist, but that would be messy, and lead to confusion, especially given the next issue...
* When you press star to undo the addition of a diacritic or modification, Plover will simply re-replace the character with the previous one it came from. This works for all the single-code-point characters native to the system. However, if you use the combining diacritics feature, this doesn't work; star will delete the entire character you composed, even if you combined in 5 diacritics. This matches how backspace works for me for combined characters in every program I've tried, so it's not super out of the ordinary, but it can be a bit jarring to write a character, combine in two diacritics, star back to remove the last one, and have the entire character vanish.
"""

def generateReadme ():
    print(readmeTitle)
    print(readmeGoals)
    print(readmeTOC)
    print(readmeInstallation)
    print(readmeNotesOnDesign)
    print(readmeKeyboardSections)
    print(readmeUsingModifiers)
    print(readmeTweaks)
    print(readmeAvailableDiacritics)
    generateModifiersSection()
    generateAllCharactersSection()
    print(readmeKnownIssues)


if __name__ == "__main__":
    generateReadme()


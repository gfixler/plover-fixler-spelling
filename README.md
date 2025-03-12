
# Fixler Spelling for Plover
A fingerspelling system for the [Plover](https://www.openstenoproject.org/plover/) steno software.

This library currently provides quick access to 583 characters.

## Design Goals
* provide upper and lowercase English alphabet
* systematize writing many Latin letters with diacritics
* allow use of many diacritics as combining diacritical marks
* systematize writing many ligatures, rotations, inversions, etc.
* include some other alphabets where possible (Greek, NATO, Morse...)


## Notes on Design
### The Core
The core of this system is about spelling, and revolves around the Latin letters with diacritics, and alphabets that map well to and from Latin letters. That said, this library is not above including other, fun things that don't exactly fit, but also don't feel terribly out of place here.

### It's Just Outlines
Modifiers are not currently programmatic, and do not look at stroke history. This is not a Plover Python dictionary. The modifier system simply exports a JSON file filled with multi-stroke outlines that pair a base letter with one or more modifiers. This means "á" ("a with acute") is simply defined as the two-stroke outline, A*/-RP. You can't stroke KAT to write "cat", then stroke a modifier to add a diacritic to the "t" at the end of the word.

### System Letters
Because letter chords are part of the outlines with their modifiers, you must use the letter chords as defined in this library. This means if you use STK for "z", for example, and this system uses STKPW, you must use this system's version to write, e.g., the ẓ character. Currently, the way around this is to modify the Python file, and reexport the dictionary.

### Precomposed Characters
All characters defined in this system—as seen in the "Used by" lists following each modifier in the [Available Diacritics and Other Modifiers](#available-diacritics-and-other-modifiers) section below—are "precomposed" characters in Unicode, meaning they have a single code point in The Unicode Standard. Many characters not in these lists, encountered in the wild, are actually composed of a base letter, with one or more [combining characters](https://en.wikipedia.org/wiki/Combining_character) following them. For example, z with acute exists in Unicode, but currently (Unicode v16.0), z with grave does not, so it's not defined in the core system here. If you see a z with grave, it's composed of small letter z (U+007A) and the combining grave diacritic (U+0323). Even characters that do have a precomposed (single code point) version often show up in the wild as [composed versions](https://en.wikipedia.org/wiki/Unicode_equivalence) of themselves. (See: [When an é is not an é](https://nation.marketo.com/t5/product-blogs/when-an-e%CC%81-is-not-an-%C3%A9-about-unicode-precomposed-vs-decomposed/ba-p/339051)).

### Stacking Modifiers
Characters with more than one modifier, like "ẫ" ("a with circumflex and tilde"), are made by stroking the letter chord, followed by each modifier chord in sequence. The order of these is based on the Unicode name, where "ẫ" (Unicode code point U+1EAB) is called "LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE", and means you stroke the circumflex modifier before the tilde modifier.<BR><BR>Unicode actually has a collation order for diacritics, based on things like closeness to the base character, and position around the character, but it's [a bit involved](https://www.unicode.org/reports/tr10/). Ultimately, Unicode doesn't care in what order diacritics are combined, and will normalize multiple diacritics back to a canonical ordering. The way around this is to use the [combining grapheme joiner](https://en.wikipedia.org/wiki/Combining_grapheme_joiner), but that's currently outside the scope of this system.


## Modifier Keys
The following 6 keys are used to add diacritics and other modifiers.

See the following section, [Using Modifiers](#using-modifiers), for usage instructions.
```
🅂🅃🄿🄷 🄾 🅵🅿🅻🅃🄳
🅂🄺🅆🅁 🄾 🆁🅱🅶🅂🅉
　　　🄰🄾 🄴🅄
```


## Using Modifiers
Modify base letters by stroking a diacritic or modifier outline immediately after a base letter.

For example, to get á, stroke A* for "a", then the acute modifier outline to convert it.


## Modifier Tweaks
Tweaks are added to a modifier stroke using the E and U keys.

|Tweak|Description|
|-|-|
|![EU Up](images/EU_up.png)|Neither E nor U pressed means no tweak to the modifier stroke.|
|![E Down](images/E_down.png)|Think of E as meaning "extra". This is added to acute and grave strokes to double them.|
|![U Down](images/U_down.png)|Think of U as meaning "under". This is added to various diacritic strokes to turn them into their "below" versions: breve below, circumflex below, line below, ring below, and tilde below.|
|![EU Down](images/EU_down.png)|Think of EU (the "i" chord in steno) as meaning "invert".


## Available Diacritics and Other Modifiers
In general, the diacritic chords are meant to visually resemble their symbols, to ease remembering them all.

For other modifiers, like rotation or inversion, an attempt was made to be memorable. See notes with each modifier.

NOTE: Modifier and Tweak are part of the same stroke.

|Modifier|Tweak|Notes|
|-|-|-|
|Acute| |
|![acute](images/acute.png)|![tweak](images/EU_up.png)|Shaped like the acute symbol.<BR><BR>Used in: [Á](#char-latin-capital-letter-a-with-acute) [Ấ](#char-latin-capital-letter-a-with-circumflex-and-acute) [Ắ](#char-latin-capital-letter-a-with-breve-and-acute) [Ć](#char-latin-capital-letter-c-with-acute) [Ḉ](#char-latin-capital-letter-c-with-cedilla-and-acute) [É](#char-latin-capital-letter-e-with-acute) [Ế](#char-latin-capital-letter-e-with-circumflex-and-acute) [Ḗ](#char-latin-capital-letter-e-with-macron-and-acute) [Ǵ](#char-latin-capital-letter-g-with-acute) [Í](#char-latin-capital-letter-i-with-acute) [Ḯ](#char-latin-capital-letter-i-with-diaeresis-and-acute) [Ḱ](#char-latin-capital-letter-k-with-acute) [Ĺ](#char-latin-capital-letter-l-with-acute) [Ḿ](#char-latin-capital-letter-m-with-acute) [Ń](#char-latin-capital-letter-n-with-acute) [Ó](#char-latin-capital-letter-o-with-acute) [Ố](#char-latin-capital-letter-o-with-circumflex-and-acute) [Ṍ](#char-latin-capital-letter-o-with-tilde-and-acute) [Ṓ](#char-latin-capital-letter-o-with-macron-and-acute) [Ớ](#char-latin-capital-letter-o-with-horn-and-acute) [Ṕ](#char-latin-capital-letter-p-with-acute) [Ŕ](#char-latin-capital-letter-r-with-acute) [Ś](#char-latin-capital-letter-s-with-acute) [Ṥ](#char-latin-capital-letter-s-with-acute-and-dot-above) [Ú](#char-latin-capital-letter-u-with-acute) [Ṹ](#char-latin-capital-letter-u-with-tilde-and-acute) [Ǘ](#char-latin-capital-letter-u-with-diaeresis-and-acute) [Ứ](#char-latin-capital-letter-u-with-horn-and-acute) [Ẃ](#char-latin-capital-letter-w-with-acute) [Ý](#char-latin-capital-letter-y-with-acute) [Ź](#char-latin-capital-letter-z-with-acute) [á](#char-latin-small-letter-a-with-acute) [ấ](#char-latin-small-letter-a-with-circumflex-and-acute) [ắ](#char-latin-small-letter-a-with-breve-and-acute) [ć](#char-latin-small-letter-c-with-acute) [ḉ](#char-latin-small-letter-c-with-cedilla-and-acute) [é](#char-latin-small-letter-e-with-acute) [ế](#char-latin-small-letter-e-with-circumflex-and-acute) [ḗ](#char-latin-small-letter-e-with-macron-and-acute) [ǵ](#char-latin-small-letter-g-with-acute) [í](#char-latin-small-letter-i-with-acute) [ḯ](#char-latin-small-letter-i-with-diaeresis-and-acute) [ḱ](#char-latin-small-letter-k-with-acute) [ĺ](#char-latin-small-letter-l-with-acute) [ḿ](#char-latin-small-letter-m-with-acute) [ń](#char-latin-small-letter-n-with-acute) [ó](#char-latin-small-letter-o-with-acute) [ố](#char-latin-small-letter-o-with-circumflex-and-acute) [ṍ](#char-latin-small-letter-o-with-tilde-and-acute) [ṓ](#char-latin-small-letter-o-with-macron-and-acute) [ớ](#char-latin-small-letter-o-with-horn-and-acute) [ṕ](#char-latin-small-letter-p-with-acute) [ŕ](#char-latin-small-letter-r-with-acute) [ś](#char-latin-small-letter-s-with-acute) [ṥ](#char-latin-small-letter-s-with-acute-and-dot-above) [ú](#char-latin-small-letter-u-with-acute) [ṹ](#char-latin-small-letter-u-with-tilde-and-acute) [ǘ](#char-latin-small-letter-u-with-diaeresis-and-acute) [ứ](#char-latin-small-letter-u-with-horn-and-acute) [ẃ](#char-latin-small-letter-w-with-acute) [ý](#char-latin-small-letter-y-with-acute) [ź](#char-latin-small-letter-z-with-acute) [Ǽ](#char-latin-capital-letter-ae-with-acute) [Ǿ](#char-latin-capital-letter-o-with-stroke-and-acute) [ǽ](#char-latin-small-letter-ae-with-acute) [ǿ](#char-latin-small-letter-o-with-stroke-and-acute)|
|Double Acute| |
|![acuteDoubled](images/acuteDoubled.png)|![tweak](images/E_down.png)|The acute modifier shape, with the '[extra](#modifier-tweaks)' tweak.<BR><BR>Used in: [Ő](#char-latin-capital-letter-o-with-double-acute) [Ű](#char-latin-capital-letter-u-with-double-acute) [ő](#char-latin-small-letter-o-with-double-acute) [ű](#char-latin-small-letter-u-with-double-acute) [Ӳ](#char-cyrillic-capital-letter-u-with-double-acute) [ӳ](#char-cyrillic-small-letter-u-with-double-acute)|
|Breve| |
|![breve](images/breve.png)|![tweak](images/EU_up.png)|Shaped like the breve symbol.<BR><BR>Used in: [Ă](#char-latin-capital-letter-a-with-breve) [Ằ](#char-latin-capital-letter-a-with-breve-and-grave) [Ắ](#char-latin-capital-letter-a-with-breve-and-acute) [Ẵ](#char-latin-capital-letter-a-with-breve-and-tilde) [Ẳ](#char-latin-capital-letter-a-with-breve-and-hook-above) [Ặ](#char-latin-capital-letter-a-with-breve-and-dot-below) [Ĕ](#char-latin-capital-letter-e-with-breve) [Ḝ](#char-latin-capital-letter-e-with-cedilla-and-breve) [Ğ](#char-latin-capital-letter-g-with-breve) [Ĭ](#char-latin-capital-letter-i-with-breve) [Ŏ](#char-latin-capital-letter-o-with-breve) [Ŭ](#char-latin-capital-letter-u-with-breve) [ă](#char-latin-small-letter-a-with-breve) [ằ](#char-latin-small-letter-a-with-breve-and-grave) [ắ](#char-latin-small-letter-a-with-breve-and-acute) [ẵ](#char-latin-small-letter-a-with-breve-and-tilde) [ẳ](#char-latin-small-letter-a-with-breve-and-hook-above) [ặ](#char-latin-small-letter-a-with-breve-and-dot-below) [ĕ](#char-latin-small-letter-e-with-breve) [ḝ](#char-latin-small-letter-e-with-cedilla-and-breve) [ğ](#char-latin-small-letter-g-with-breve) [ĭ](#char-latin-small-letter-i-with-breve) [ŏ](#char-latin-small-letter-o-with-breve) [ŭ](#char-latin-small-letter-u-with-breve)|
|Breve Below| |
|![breveBelow](images/breveBelow.png)|![tweak](images/U_down.png)|The breve modifier shape, with the '[under](#modifier-tweaks)' tweak.<BR><BR>Used in: [Ḫ](#char-latin-capital-letter-h-with-breve-below) [ḫ](#char-latin-small-letter-h-with-breve-below)|
|Breve Inverted| |
|![breveInverted](images/breveInverted.png)|![tweak](images/EU_up.png)|Shaped like the inverted breve symbol.<BR><BR>Used in: [Ȃ](#char-latin-capital-letter-a-with-inverted-breve) [Ȇ](#char-latin-capital-letter-e-with-inverted-breve) [Ȋ](#char-latin-capital-letter-i-with-inverted-breve) [Ȏ](#char-latin-capital-letter-o-with-inverted-breve) [Ȓ](#char-latin-capital-letter-r-with-inverted-breve) [Ȗ](#char-latin-capital-letter-u-with-inverted-breve) [ȃ](#char-latin-small-letter-a-with-inverted-breve) [ȇ](#char-latin-small-letter-e-with-inverted-breve) [ȋ](#char-latin-small-letter-i-with-inverted-breve) [ȏ](#char-latin-small-letter-o-with-inverted-breve) [ȓ](#char-latin-small-letter-r-with-inverted-breve) [ȗ](#char-latin-small-letter-u-with-inverted-breve)|
|Caron| |
|![caron](images/caron.png)|![tweak](images/EU_up.png)|Shaped like the caron symbol.<BR><BR>Used in: [Ǎ](#char-latin-capital-letter-a-with-caron) [Č](#char-latin-capital-letter-c-with-caron) [Ď](#char-latin-capital-letter-d-with-caron) [Ě](#char-latin-capital-letter-e-with-caron) [Ǧ](#char-latin-capital-letter-g-with-caron) [Ȟ](#char-latin-capital-letter-h-with-caron) [Ǐ](#char-latin-capital-letter-i-with-caron) [Ǩ](#char-latin-capital-letter-k-with-caron) [Ľ](#char-latin-capital-letter-l-with-caron) [Ň](#char-latin-capital-letter-n-with-caron) [Ǒ](#char-latin-capital-letter-o-with-caron) [Ř](#char-latin-capital-letter-r-with-caron) [Ŝ](#char-latin-capital-letter-s-with-circumflex) [Š](#char-latin-capital-letter-s-with-caron) [Ṧ](#char-latin-capital-letter-s-with-caron-and-dot-above) [Ť](#char-latin-capital-letter-t-with-caron) [Ǔ](#char-latin-capital-letter-u-with-caron) [Ž](#char-latin-capital-letter-z-with-caron) [ǎ](#char-latin-small-letter-a-with-caron) [č](#char-latin-small-letter-c-with-caron) [ď](#char-latin-small-letter-d-with-caron) [ě](#char-latin-small-letter-e-with-caron) [ǧ](#char-latin-small-letter-g-with-caron) [ȟ](#char-latin-small-letter-h-with-caron) [ǐ](#char-latin-small-letter-i-with-caron) [ǰ](#char-latin-small-letter-j-with-caron) [ǩ](#char-latin-small-letter-k-with-caron) [ľ](#char-latin-small-letter-l-with-caron) [ň](#char-latin-small-letter-n-with-caron) [ǒ](#char-latin-small-letter-o-with-caron) [ř](#char-latin-small-letter-r-with-caron) [ŝ](#char-latin-small-letter-s-with-circumflex) [š](#char-latin-small-letter-s-with-caron) [ṧ](#char-latin-small-letter-s-with-caron-and-dot-above) [ť](#char-latin-small-letter-t-with-caron) [ǔ](#char-latin-small-letter-u-with-caron) [ž](#char-latin-small-letter-z-with-caron)|
|Cedilla| |
|![cedilla](images/cedilla.png)|![tweak](images/EU_up.png)|Shaped like the cedilla, which hangs below the character, and curves to the left.<BR><BR>Used in: [Ç](#char-latin-capital-letter-c-with-cedilla) [Ḉ](#char-latin-capital-letter-c-with-cedilla-and-acute) [Ḑ](#char-latin-capital-letter-d-with-cedilla) [Ȩ](#char-latin-capital-letter-e-with-cedilla) [Ḝ](#char-latin-capital-letter-e-with-cedilla-and-breve) [Ģ](#char-latin-capital-letter-g-with-cedilla) [Ḩ](#char-latin-capital-letter-h-with-cedilla) [Ķ](#char-latin-capital-letter-k-with-cedilla) [Ļ](#char-latin-capital-letter-l-with-cedilla) [Ņ](#char-latin-capital-letter-n-with-cedilla) [Ŗ](#char-latin-capital-letter-r-with-cedilla) [Ş](#char-latin-capital-letter-s-with-cedilla) [Ţ](#char-latin-capital-letter-t-with-cedilla) [ç](#char-latin-small-letter-c-with-cedilla) [ḉ](#char-latin-small-letter-c-with-cedilla-and-acute) [ḑ](#char-latin-small-letter-d-with-cedilla) [ȩ](#char-latin-small-letter-e-with-cedilla) [ḝ](#char-latin-small-letter-e-with-cedilla-and-breve) [ģ](#char-latin-small-letter-g-with-cedilla) [ḩ](#char-latin-small-letter-h-with-cedilla) [ķ](#char-latin-small-letter-k-with-cedilla) [ļ](#char-latin-small-letter-l-with-cedilla) [ņ](#char-latin-small-letter-n-with-cedilla) [ŗ](#char-latin-small-letter-r-with-cedilla) [ş](#char-latin-small-letter-s-with-cedilla) [ţ](#char-latin-small-letter-t-with-cedilla)|
|Circumflex| |
|![circumflex](images/circumflex.png)|![tweak](images/EU_up.png)|Shaped like the circumflex symbol.<BR><BR>Used in: [Â](#char-latin-capital-letter-a-with-circumflex) [Ầ](#char-latin-capital-letter-a-with-circumflex-and-grave) [Ấ](#char-latin-capital-letter-a-with-circumflex-and-acute) [Ẫ](#char-latin-capital-letter-a-with-circumflex-and-tilde) [Ẩ](#char-latin-capital-letter-a-with-circumflex-and-hook-above) [Ậ](#char-latin-capital-letter-a-with-circumflex-and-dot-below) [Ĉ](#char-latin-capital-letter-c-with-circumflex) [Ḓ](#char-latin-capital-letter-d-with-circumflex-below) [Ê](#char-latin-capital-letter-e-with-circumflex) [Ề](#char-latin-capital-letter-e-with-circumflex-and-grave) [Ế](#char-latin-capital-letter-e-with-circumflex-and-acute) [Ễ](#char-latin-capital-letter-e-with-circumflex-and-tilde) [Ể](#char-latin-capital-letter-e-with-circumflex-and-hook-above) [Ệ](#char-latin-capital-letter-e-with-circumflex-and-dot-below) [Ĝ](#char-latin-capital-letter-g-with-circumflex) [Ĥ](#char-latin-capital-letter-h-with-circumflex) [Î](#char-latin-capital-letter-i-with-circumflex) [Ĵ](#char-latin-capital-letter-j-with-circumflex) [Ḽ](#char-latin-capital-letter-l-with-circumflex-below) [Ṋ](#char-latin-capital-letter-n-with-circumflex-below) [Ô](#char-latin-capital-letter-o-with-circumflex) [Ồ](#char-latin-capital-letter-o-with-circumflex-and-grave) [Ố](#char-latin-capital-letter-o-with-circumflex-and-acute) [Ỗ](#char-latin-capital-letter-o-with-circumflex-and-tilde) [Ổ](#char-latin-capital-letter-o-with-circumflex-and-hook-above) [Ộ](#char-latin-capital-letter-o-with-circumflex-and-dot-below) [Ṱ](#char-latin-capital-letter-t-with-circumflex-below) [Û](#char-latin-capital-letter-u-with-circumflex) [Ŵ](#char-latin-capital-letter-w-with-circumflex) [Ŷ](#char-latin-capital-letter-y-with-circumflex) [Ẑ](#char-latin-capital-letter-z-with-circumflex) [â](#char-latin-small-letter-a-with-circumflex) [ầ](#char-latin-small-letter-a-with-circumflex-and-grave) [ấ](#char-latin-small-letter-a-with-circumflex-and-acute) [ẫ](#char-latin-small-letter-a-with-circumflex-and-tilde) [ẩ](#char-latin-small-letter-a-with-circumflex-and-hook-above) [ậ](#char-latin-small-letter-a-with-circumflex-and-dot-below) [ĉ](#char-latin-small-letter-c-with-circumflex) [ḓ](#char-latin-small-letter-d-with-circumflex-below) [ê](#char-latin-small-letter-e-with-circumflex) [ề](#char-latin-small-letter-e-with-circumflex-and-grave) [ế](#char-latin-small-letter-e-with-circumflex-and-acute) [ễ](#char-latin-small-letter-e-with-circumflex-and-tilde) [ể](#char-latin-small-letter-e-with-circumflex-and-hook-above) [ệ](#char-latin-small-letter-e-with-circumflex-and-dot-below) [ĝ](#char-latin-small-letter-g-with-circumflex) [ĥ](#char-latin-small-letter-h-with-circumflex) [î](#char-latin-small-letter-i-with-circumflex) [ĵ](#char-latin-small-letter-j-with-circumflex) [ḽ](#char-latin-small-letter-l-with-circumflex-below) [ṋ](#char-latin-small-letter-n-with-circumflex-below) [ô](#char-latin-small-letter-o-with-circumflex) [ồ](#char-latin-small-letter-o-with-circumflex-and-grave) [ố](#char-latin-small-letter-o-with-circumflex-and-acute) [ỗ](#char-latin-small-letter-o-with-circumflex-and-tilde) [ổ](#char-latin-small-letter-o-with-circumflex-and-hook-above) [ộ](#char-latin-small-letter-o-with-circumflex-and-dot-below) [ṱ](#char-latin-small-letter-t-with-circumflex-below) [û](#char-latin-small-letter-u-with-circumflex) [ŵ](#char-latin-small-letter-w-with-circumflex) [ŷ](#char-latin-small-letter-y-with-circumflex) [ẑ](#char-latin-small-letter-z-with-circumflex)|
|Circumflex Below| |
|![circumflexBelow](images/circumflexBelow.png)|![tweak](images/U_down.png)|The circumflex modifier shape, with the '[under](#modifier-tweaks)' tweak.<BR><BR>Used in: [Ḙ](#char-latin-capital-letter-e-with-circumflex-below) [Ṷ](#char-latin-capital-letter-u-with-circumflex-below) [ḙ](#char-latin-small-letter-e-with-circumflex-below) [ṷ](#char-latin-small-letter-u-with-circumflex-below)|
|Comma Below| |
|![commaBelow](images/commaBelow.png)|![tweak](images/EU_up.png)|Chosen to mirror the shape used for the comma in the [Emily's Symbols](https://github.com/EPLHREU/emily-symbols) plugin.<BR><BR>Used in: [Ș](#char-latin-capital-letter-s-with-comma-below) [Ț](#char-latin-capital-letter-t-with-comma-below) [ș](#char-latin-small-letter-s-with-comma-below) [ț](#char-latin-small-letter-t-with-comma-below)|
|Diaeresis/Umlaut| |
|![diaeresis](images/diaeresis.png)|![tweak](images/EU_up.png)|Shaped like the diaeresis/umlaut symbols.<BR><BR>NOTE: [diaeresis](https://en.wikipedia.org/wiki/Diaeresis_(diacritic)) and [umlaut](https://en.wikipedia.org/wiki/Umlaut_(diacritic)) are distinct concepts, with separate uses, but are represented by the same Unicode code points. They are created via the same outline in this spelling system.<BR><BR>Used in: [Ä](#char-latin-capital-letter-a-with-diaeresis) [Ǟ](#char-latin-capital-letter-a-with-diaeresis-and-macron) [Ë](#char-latin-capital-letter-e-with-diaeresis) [Ḧ](#char-latin-capital-letter-h-with-diaeresis) [Ï](#char-latin-capital-letter-i-with-diaeresis) [Ḯ](#char-latin-capital-letter-i-with-diaeresis-and-acute) [Ṏ](#char-latin-capital-letter-o-with-tilde-and-diaeresis) [Ö](#char-latin-capital-letter-o-with-diaeresis) [Ȫ](#char-latin-capital-letter-o-with-diaeresis-and-macron) [Ṻ](#char-latin-capital-letter-u-with-macron-and-diaeresis) [Ü](#char-latin-capital-letter-u-with-diaeresis) [Ǜ](#char-latin-capital-letter-u-with-diaeresis-and-grave) [Ǘ](#char-latin-capital-letter-u-with-diaeresis-and-acute) [Ǖ](#char-latin-capital-letter-u-with-diaeresis-and-macron) [Ǚ](#char-latin-capital-letter-u-with-diaeresis-and-caron) [Ẅ](#char-latin-capital-letter-w-with-diaeresis) [Ẍ](#char-latin-capital-letter-x-with-diaeresis) [Ÿ](#char-latin-capital-letter-y-with-diaeresis) [ä](#char-latin-small-letter-a-with-diaeresis) [ǟ](#char-latin-small-letter-a-with-diaeresis-and-macron) [ë](#char-latin-small-letter-e-with-diaeresis) [ḧ](#char-latin-small-letter-h-with-diaeresis) [ï](#char-latin-small-letter-i-with-diaeresis) [ḯ](#char-latin-small-letter-i-with-diaeresis-and-acute) [ṏ](#char-latin-small-letter-o-with-tilde-and-diaeresis) [ö](#char-latin-small-letter-o-with-diaeresis) [ȫ](#char-latin-small-letter-o-with-diaeresis-and-macron) [ẗ](#char-latin-small-letter-t-with-diaeresis) [ṻ](#char-latin-small-letter-u-with-macron-and-diaeresis) [ü](#char-latin-small-letter-u-with-diaeresis) [ǜ](#char-latin-small-letter-u-with-diaeresis-and-grave) [ǘ](#char-latin-small-letter-u-with-diaeresis-and-acute) [ǖ](#char-latin-small-letter-u-with-diaeresis-and-macron) [ǚ](#char-latin-small-letter-u-with-diaeresis-and-caron) [ẅ](#char-latin-small-letter-w-with-diaeresis) [ẍ](#char-latin-small-letter-x-with-diaeresis) [ÿ](#char-latin-small-letter-y-with-diaeresis)|
|Diaeresis Below| |
|![diaeresisBelow](images/diaeresisBelow.png)|![tweak](images/EU_up.png)|The diaeresis/umlaut shape, but lower.<BR><BR>Used in: [Ṳ](#char-latin-capital-letter-u-with-diaeresis-below) [ṳ](#char-latin-small-letter-u-with-diaeresis-below)|
|Dot Above| |
|![dotAbove](images/dotAbove.png)|![tweak](images/EU_up.png)|A single key, up high, like a dot above. See dot below.<BR><BR>Used in: [Ȧ](#char-latin-capital-letter-a-with-dot-above) [Ǡ](#char-latin-capital-letter-a-with-dot-above-and-macron) [Ḃ](#char-latin-capital-letter-b-with-dot-above) [Ċ](#char-latin-capital-letter-c-with-dot-above) [Ḋ](#char-latin-capital-letter-d-with-dot-above) [Ė](#char-latin-capital-letter-e-with-dot-above) [Ḟ](#char-latin-capital-letter-f-with-dot-above) [Ġ](#char-latin-capital-letter-g-with-dot-above) [Ḣ](#char-latin-capital-letter-h-with-dot-above) [İ](#char-latin-capital-letter-i-with-dot-above) [Ṁ](#char-latin-capital-letter-m-with-dot-above) [Ṅ](#char-latin-capital-letter-n-with-dot-above) [Ȯ](#char-latin-capital-letter-o-with-dot-above) [Ȱ](#char-latin-capital-letter-o-with-dot-above-and-macron) [Ṗ](#char-latin-capital-letter-p-with-dot-above) [Ṙ](#char-latin-capital-letter-r-with-dot-above) [Ṥ](#char-latin-capital-letter-s-with-acute-and-dot-above) [Ṡ](#char-latin-capital-letter-s-with-dot-above) [Ṧ](#char-latin-capital-letter-s-with-caron-and-dot-above) [Ṩ](#char-latin-capital-letter-s-with-dot-below-and-dot-above) [Ṫ](#char-latin-capital-letter-t-with-dot-above) [Ẇ](#char-latin-capital-letter-w-with-dot-above) [Ẋ](#char-latin-capital-letter-x-with-dot-above) [Ẏ](#char-latin-capital-letter-y-with-dot-above) [Ż](#char-latin-capital-letter-z-with-dot-above) [ȧ](#char-latin-small-letter-a-with-dot-above) [ǡ](#char-latin-small-letter-a-with-dot-above-and-macron) [ḃ](#char-latin-small-letter-b-with-dot-above) [ċ](#char-latin-small-letter-c-with-dot-above) [ḋ](#char-latin-small-letter-d-with-dot-above) [ė](#char-latin-small-letter-e-with-dot-above) [ḟ](#char-latin-small-letter-f-with-dot-above) [ġ](#char-latin-small-letter-g-with-dot-above) [ḣ](#char-latin-small-letter-h-with-dot-above) [i](#char-latin-small-letter-i) [ṁ](#char-latin-small-letter-m-with-dot-above) [ṅ](#char-latin-small-letter-n-with-dot-above) [ȯ](#char-latin-small-letter-o-with-dot-above) [ȱ](#char-latin-small-letter-o-with-dot-above-and-macron) [ṗ](#char-latin-small-letter-p-with-dot-above) [ṙ](#char-latin-small-letter-r-with-dot-above) [ṥ](#char-latin-small-letter-s-with-acute-and-dot-above) [ṡ](#char-latin-small-letter-s-with-dot-above) [ṧ](#char-latin-small-letter-s-with-caron-and-dot-above) [ṩ](#char-latin-small-letter-s-with-dot-below-and-dot-above) [ṫ](#char-latin-small-letter-t-with-dot-above) [ẇ](#char-latin-small-letter-w-with-dot-above) [ẋ](#char-latin-small-letter-x-with-dot-above) [ẏ](#char-latin-small-letter-y-with-dot-above) [ż](#char-latin-small-letter-z-with-dot-above)|
|Dot Below| |
|![dotBelow](images/dotBelow.png)|![tweak](images/EU_up.png)|Chosen to mirror the shape used for the period in the [Emily's Symbols](https://github.com/EPLHREU/emily-symbols) plugin. A single key, down low, like a dot below. See dot above.<BR><BR>Used in: [Ạ](#char-latin-capital-letter-a-with-dot-below) [Ậ](#char-latin-capital-letter-a-with-circumflex-and-dot-below) [Ặ](#char-latin-capital-letter-a-with-breve-and-dot-below) [Ḅ](#char-latin-capital-letter-b-with-dot-below) [Ḍ](#char-latin-capital-letter-d-with-dot-below) [Ẹ](#char-latin-capital-letter-e-with-dot-below) [Ệ](#char-latin-capital-letter-e-with-circumflex-and-dot-below) [Ḥ](#char-latin-capital-letter-h-with-dot-below) [Ị](#char-latin-capital-letter-i-with-dot-below) [Ḳ](#char-latin-capital-letter-k-with-dot-below) [Ḷ](#char-latin-capital-letter-l-with-dot-below) [Ḹ](#char-latin-capital-letter-l-with-dot-below-and-macron) [Ṃ](#char-latin-capital-letter-m-with-dot-below) [Ṇ](#char-latin-capital-letter-n-with-dot-below) [Ợ](#char-latin-capital-letter-o-with-horn-and-dot-below) [Ọ](#char-latin-capital-letter-o-with-dot-below) [Ộ](#char-latin-capital-letter-o-with-circumflex-and-dot-below) [Ṛ](#char-latin-capital-letter-r-with-dot-below) [Ṝ](#char-latin-capital-letter-r-with-dot-below-and-macron) [Ṣ](#char-latin-capital-letter-s-with-dot-below) [Ṩ](#char-latin-capital-letter-s-with-dot-below-and-dot-above) [Ș](#char-latin-capital-letter-s-with-comma-below) [Ṭ](#char-latin-capital-letter-t-with-dot-below) [Ự](#char-latin-capital-letter-u-with-horn-and-dot-below) [Ụ](#char-latin-capital-letter-u-with-dot-below) [Ṿ](#char-latin-capital-letter-v-with-dot-below) [Ẉ](#char-latin-capital-letter-w-with-dot-below) [Ỵ](#char-latin-capital-letter-y-with-dot-below) [Ẓ](#char-latin-capital-letter-z-with-dot-below) [ạ](#char-latin-small-letter-a-with-dot-below) [ậ](#char-latin-small-letter-a-with-circumflex-and-dot-below) [ặ](#char-latin-small-letter-a-with-breve-and-dot-below) [ḅ](#char-latin-small-letter-b-with-dot-below) [ḍ](#char-latin-small-letter-d-with-dot-below) [ẹ](#char-latin-small-letter-e-with-dot-below) [ệ](#char-latin-small-letter-e-with-circumflex-and-dot-below) [ḥ](#char-latin-small-letter-h-with-dot-below) [ị](#char-latin-small-letter-i-with-dot-below) [ḳ](#char-latin-small-letter-k-with-dot-below) [ḷ](#char-latin-small-letter-l-with-dot-below) [ḹ](#char-latin-small-letter-l-with-dot-below-and-macron) [ṃ](#char-latin-small-letter-m-with-dot-below) [ṇ](#char-latin-small-letter-n-with-dot-below) [ợ](#char-latin-small-letter-o-with-horn-and-dot-below) [ọ](#char-latin-small-letter-o-with-dot-below) [ộ](#char-latin-small-letter-o-with-circumflex-and-dot-below) [ṛ](#char-latin-small-letter-r-with-dot-below) [ṝ](#char-latin-small-letter-r-with-dot-below-and-macron) [ṣ](#char-latin-small-letter-s-with-dot-below) [ṩ](#char-latin-small-letter-s-with-dot-below-and-dot-above) [ș](#char-latin-small-letter-s-with-comma-below) [ṭ](#char-latin-small-letter-t-with-dot-below) [ự](#char-latin-small-letter-u-with-horn-and-dot-below) [ụ](#char-latin-small-letter-u-with-dot-below) [ṿ](#char-latin-small-letter-v-with-dot-below) [ẉ](#char-latin-small-letter-w-with-dot-below) [ỵ](#char-latin-small-letter-y-with-dot-below) [ẓ](#char-latin-small-letter-z-with-dot-below)|
|Grave| |
|![grave](images/grave.png)|![tweak](images/EU_up.png)|Shaped like the grave symbol.<BR><BR>Used in: [À](#char-latin-capital-letter-a-with-grave) [Ầ](#char-latin-capital-letter-a-with-circumflex-and-grave) [Ằ](#char-latin-capital-letter-a-with-breve-and-grave) [È](#char-latin-capital-letter-e-with-grave) [Ề](#char-latin-capital-letter-e-with-circumflex-and-grave) [Ḕ](#char-latin-capital-letter-e-with-macron-and-grave) [Ì](#char-latin-capital-letter-i-with-grave) [Ǹ](#char-latin-capital-letter-n-with-grave) [Ò](#char-latin-capital-letter-o-with-grave) [Ồ](#char-latin-capital-letter-o-with-circumflex-and-grave) [Ṑ](#char-latin-capital-letter-o-with-macron-and-grave) [Ờ](#char-latin-capital-letter-o-with-horn-and-grave) [Ù](#char-latin-capital-letter-u-with-grave) [Ǜ](#char-latin-capital-letter-u-with-diaeresis-and-grave) [Ừ](#char-latin-capital-letter-u-with-horn-and-grave) [Ẁ](#char-latin-capital-letter-w-with-grave) [Ỳ](#char-latin-capital-letter-y-with-grave) [à](#char-latin-small-letter-a-with-grave) [ầ](#char-latin-small-letter-a-with-circumflex-and-grave) [ằ](#char-latin-small-letter-a-with-breve-and-grave) [è](#char-latin-small-letter-e-with-grave) [ề](#char-latin-small-letter-e-with-circumflex-and-grave) [ḕ](#char-latin-small-letter-e-with-macron-and-grave) [ì](#char-latin-small-letter-i-with-grave) [ǹ](#char-latin-small-letter-n-with-grave) [ò](#char-latin-small-letter-o-with-grave) [ồ](#char-latin-small-letter-o-with-circumflex-and-grave) [ṑ](#char-latin-small-letter-o-with-macron-and-grave) [ờ](#char-latin-small-letter-o-with-horn-and-grave) [ù](#char-latin-small-letter-u-with-grave) [ǜ](#char-latin-small-letter-u-with-diaeresis-and-grave) [ừ](#char-latin-small-letter-u-with-horn-and-grave) [ẁ](#char-latin-small-letter-w-with-grave) [ỳ](#char-latin-small-letter-y-with-grave)|
|Double Grave| |
|![graveDoubled](images/graveDoubled.png)|![tweak](images/E_down.png)|The grave modifier shape, with the '[extra](#modifier-tweaks)' tweak.<BR><BR>Used in: [Ȁ](#char-latin-capital-letter-a-with-double-grave) [Ȅ](#char-latin-capital-letter-e-with-double-grave) [Ȉ](#char-latin-capital-letter-i-with-double-grave) [Ȍ](#char-latin-capital-letter-o-with-double-grave) [Ȑ](#char-latin-capital-letter-r-with-double-grave) [Ȕ](#char-latin-capital-letter-u-with-double-grave) [ȁ](#char-latin-small-letter-a-with-double-grave) [ȅ](#char-latin-small-letter-e-with-double-grave) [ȉ](#char-latin-small-letter-i-with-double-grave) [ȍ](#char-latin-small-letter-o-with-double-grave) [ȑ](#char-latin-small-letter-r-with-double-grave) [ȕ](#char-latin-small-letter-u-with-double-grave)|
|Hook Above| |
|![hookAbove](images/hookAbove.png)|![tweak](images/EU_up.png)|Shaped like the hook above symbol, sticking up, and curling to the left.<BR><BR>Used in: [Ẩ](#char-latin-capital-letter-a-with-circumflex-and-hook-above) [Ẳ](#char-latin-capital-letter-a-with-breve-and-hook-above) [Ả](#char-latin-capital-letter-a-with-hook-above) [Ể](#char-latin-capital-letter-e-with-circumflex-and-hook-above) [Ẻ](#char-latin-capital-letter-e-with-hook-above) [Ỉ](#char-latin-capital-letter-i-with-hook-above) [Ổ](#char-latin-capital-letter-o-with-circumflex-and-hook-above) [Ỏ](#char-latin-capital-letter-o-with-hook-above) [Ở](#char-latin-capital-letter-o-with-horn-and-hook-above) [Ủ](#char-latin-capital-letter-u-with-hook-above) [Ử](#char-latin-capital-letter-u-with-horn-and-hook-above) [Ỷ](#char-latin-capital-letter-y-with-hook-above) [ẩ](#char-latin-small-letter-a-with-circumflex-and-hook-above) [ẳ](#char-latin-small-letter-a-with-breve-and-hook-above) [ả](#char-latin-small-letter-a-with-hook-above) [ể](#char-latin-small-letter-e-with-circumflex-and-hook-above) [ẻ](#char-latin-small-letter-e-with-hook-above) [ỉ](#char-latin-small-letter-i-with-hook-above) [ổ](#char-latin-small-letter-o-with-circumflex-and-hook-above) [ỏ](#char-latin-small-letter-o-with-hook-above) [ở](#char-latin-small-letter-o-with-horn-and-hook-above) [ủ](#char-latin-small-letter-u-with-hook-above) [ử](#char-latin-small-letter-u-with-horn-and-hook-above) [ỷ](#char-latin-small-letter-y-with-hook-above)|
|Hook| |
|![hook](images/hook.png)|![tweak](images/EU_up.png)|Distinct from 'hook above', which is a detached diacritic, this is for characters with an attached hook. The hook shape was chosen to match most of these characters, which either curl up, then to the right, or to the left, then down, which makes the same curve. Imagine the chord shape attaching to some at the −R, and others at the −P. Some of the visual nature of this is down to fonts and rendering, of course, and a few letters don't match up well to this chord shape, and will just have to be memorized as exceptions for now.<BR><BR>Used in: [Ɓ](#char-latin-capital-letter-b-with-hook) [Ƈ](#char-latin-capital-letter-c-with-hook) [ƈ](#char-latin-small-letter-c-with-hook) [Ɗ](#char-latin-capital-letter-d-with-hook) [Ƒ](#char-latin-capital-letter-f-with-hook) [ƒ](#char-latin-small-letter-f-with-hook) [Ɠ](#char-latin-capital-letter-g-with-hook) [Ƙ](#char-latin-capital-letter-k-with-hook) [ƙ](#char-latin-small-letter-k-with-hook) [Ƥ](#char-latin-capital-letter-p-with-hook) [ƥ](#char-latin-small-letter-p-with-hook) [Ƭ](#char-latin-capital-letter-t-with-hook) [ƭ](#char-latin-small-letter-t-with-hook) [Ƴ](#char-latin-capital-letter-y-with-hook) [ƴ](#char-latin-small-letter-y-with-hook) [ɓ](#char-latin-small-letter-b-with-hook) [ɗ](#char-latin-small-letter-d-with-hook) [ɠ](#char-latin-small-letter-g-with-hook)|
|Horn| |
|![horn](images/horn.png)|![tweak](images/EU_up.png)|Shaped like the horn symbol, sticking out to the right and curving upward. The shape is also on the right-hand side of the modifier keys cluster, as the horn sticks out the right side of its characters.<BR><BR>Used in: [Ơ](#char-latin-capital-letter-o-with-horn) [Ơ](#char-latin-capital-letter-o-with-horn) [Ờ](#char-latin-capital-letter-o-with-horn-and-grave) [Ớ](#char-latin-capital-letter-o-with-horn-and-acute) [Ỡ](#char-latin-capital-letter-o-with-horn-and-tilde) [Ở](#char-latin-capital-letter-o-with-horn-and-hook-above) [Ợ](#char-latin-capital-letter-o-with-horn-and-dot-below) [Ư](#char-latin-capital-letter-u-with-horn) [Ừ](#char-latin-capital-letter-u-with-horn-and-grave) [Ứ](#char-latin-capital-letter-u-with-horn-and-acute) [Ữ](#char-latin-capital-letter-u-with-horn-and-tilde) [Ử](#char-latin-capital-letter-u-with-horn-and-hook-above) [Ự](#char-latin-capital-letter-u-with-horn-and-dot-below) [ơ](#char-latin-small-letter-o-with-horn) [ơ](#char-latin-small-letter-o-with-horn) [ờ](#char-latin-small-letter-o-with-horn-and-grave) [ớ](#char-latin-small-letter-o-with-horn-and-acute) [ỡ](#char-latin-small-letter-o-with-horn-and-tilde) [ở](#char-latin-small-letter-o-with-horn-and-hook-above) [ợ](#char-latin-small-letter-o-with-horn-and-dot-below) [ư](#char-latin-small-letter-u-with-horn) [ừ](#char-latin-small-letter-u-with-horn-and-grave) [ứ](#char-latin-small-letter-u-with-horn-and-acute) [ữ](#char-latin-small-letter-u-with-horn-and-tilde) [ử](#char-latin-small-letter-u-with-horn-and-hook-above) [ự](#char-latin-small-letter-u-with-horn-and-dot-below)|
|Interpunct| |
|![interpunct](images/interpunct.png)|![tweak](images/EU_up.png)|An odd one, which joins the dot above and dot below characters. Think of it as the midpoint of the above and below dots, made by stroking both together.<BR><BR>Used in: [Ŀ](#char-latin-capital-letter-l-with-middle-dot) [ŀ](#char-latin-small-letter-l-with-middle-dot)|
|Line Below| |
|![lineBelow](images/lineBelow.png)|![tweak](images/U_down.png)|When decomposed into base character + diacritic, the combining character for this set of Unicode composed characters is the macron below. Rather than use the the lower version of the chord, on the bottom row, this uses the '[under](#modifier-tweaks)' tweak with the macron shape, to respect this relation.<BR><BR>Used in: [Ḇ](#char-latin-capital-letter-b-with-line-below) [Ḏ](#char-latin-capital-letter-d-with-line-below) [Ḵ](#char-latin-capital-letter-k-with-line-below) [Ḻ](#char-latin-capital-letter-l-with-line-below) [Ṉ](#char-latin-capital-letter-n-with-line-below) [Ṟ](#char-latin-capital-letter-r-with-line-below) [Ṯ](#char-latin-capital-letter-t-with-line-below) [Ẕ](#char-latin-capital-letter-z-with-line-below) [ḇ](#char-latin-small-letter-b-with-line-below) [ḏ](#char-latin-small-letter-d-with-line-below) [ẖ](#char-latin-small-letter-h-with-line-below) [ḵ](#char-latin-small-letter-k-with-line-below) [ḻ](#char-latin-small-letter-l-with-line-below) [ṉ](#char-latin-small-letter-n-with-line-below) [ṟ](#char-latin-small-letter-r-with-line-below) [ṯ](#char-latin-small-letter-t-with-line-below) [ẕ](#char-latin-small-letter-z-with-line-below)|
|Macron| |
|![macron](images/macron.png)|![tweak](images/EU_up.png)|Shaped like the macron symbol.<BR><BR>Used in: [Ā](#char-latin-capital-letter-a-with-macron) [Ǡ](#char-latin-capital-letter-a-with-dot-above-and-macron) [Ǟ](#char-latin-capital-letter-a-with-diaeresis-and-macron) [Ē](#char-latin-capital-letter-e-with-macron) [Ḕ](#char-latin-capital-letter-e-with-macron-and-grave) [Ḗ](#char-latin-capital-letter-e-with-macron-and-acute) [Ḡ](#char-latin-capital-letter-g-with-macron) [Ī](#char-latin-capital-letter-i-with-macron) [Ḹ](#char-latin-capital-letter-l-with-dot-below-and-macron) [Ȭ](#char-latin-capital-letter-o-with-tilde-and-macron) [Ō](#char-latin-capital-letter-o-with-macron) [Ṑ](#char-latin-capital-letter-o-with-macron-and-grave) [Ṓ](#char-latin-capital-letter-o-with-macron-and-acute) [Ȱ](#char-latin-capital-letter-o-with-dot-above-and-macron) [Ȫ](#char-latin-capital-letter-o-with-diaeresis-and-macron) [Ǭ](#char-latin-capital-letter-o-with-ogonek-and-macron) [Ṝ](#char-latin-capital-letter-r-with-dot-below-and-macron) [Ū](#char-latin-capital-letter-u-with-macron) [Ṻ](#char-latin-capital-letter-u-with-macron-and-diaeresis) [Ǖ](#char-latin-capital-letter-u-with-diaeresis-and-macron) [Ǚ](#char-latin-capital-letter-u-with-diaeresis-and-caron) [Ȳ](#char-latin-capital-letter-y-with-macron) [ā](#char-latin-small-letter-a-with-macron) [ǡ](#char-latin-small-letter-a-with-dot-above-and-macron) [ǟ](#char-latin-small-letter-a-with-diaeresis-and-macron) [ē](#char-latin-small-letter-e-with-macron) [ḕ](#char-latin-small-letter-e-with-macron-and-grave) [ḗ](#char-latin-small-letter-e-with-macron-and-acute) [ḡ](#char-latin-small-letter-g-with-macron) [ī](#char-latin-small-letter-i-with-macron) [ḹ](#char-latin-small-letter-l-with-dot-below-and-macron) [ȭ](#char-latin-small-letter-o-with-tilde-and-macron) [ō](#char-latin-small-letter-o-with-macron) [ṑ](#char-latin-small-letter-o-with-macron-and-grave) [ṓ](#char-latin-small-letter-o-with-macron-and-acute) [ȱ](#char-latin-small-letter-o-with-dot-above-and-macron) [ȫ](#char-latin-small-letter-o-with-diaeresis-and-macron) [ǭ](#char-latin-small-letter-o-with-ogonek-and-macron) [ṝ](#char-latin-small-letter-r-with-dot-below-and-macron) [ū](#char-latin-small-letter-u-with-macron) [ṻ](#char-latin-small-letter-u-with-macron-and-diaeresis) [ǖ](#char-latin-small-letter-u-with-diaeresis-and-macron) [ǚ](#char-latin-small-letter-u-with-diaeresis-and-caron) [ȳ](#char-latin-small-letter-y-with-macron) [Ǣ](#char-latin-capital-letter-ae-with-macron) [ǣ](#char-latin-small-letter-ae-with-macron)|
|Ogonek| |
|![ogonek](images/ogonek.png)|![tweak](images/EU_up.png)|The ogonek, meaning 'little tail' in Polish, hangs off the bottom of its character, curling down and to the right.<BR><BR>Used in: [Ą](#char-latin-capital-letter-a-with-ogonek) [Ę](#char-latin-capital-letter-e-with-ogonek) [Į](#char-latin-capital-letter-i-with-ogonek) [Ǫ](#char-latin-capital-letter-o-with-ogonek) [Ǭ](#char-latin-capital-letter-o-with-ogonek-and-macron) [Ų](#char-latin-capital-letter-u-with-ogonek) [ą](#char-latin-small-letter-a-with-ogonek) [ę](#char-latin-small-letter-e-with-ogonek) [į](#char-latin-small-letter-i-with-ogonek) [ǫ](#char-latin-small-letter-o-with-ogonek) [ǭ](#char-latin-small-letter-o-with-ogonek-and-macron) [ų](#char-latin-small-letter-u-with-ogonek)|
|Ring Above| |
|![ringAbove](images/ringAbove.png)|![tweak](images/EU_up.png)|Think of this square of keys like a little circle, or ring.<BR><BR>Used in: [Å](#char-latin-capital-letter-a-with-ring-above) [Ů](#char-latin-capital-letter-u-with-ring-above) [å](#char-latin-small-letter-a-with-ring-above) [ů](#char-latin-small-letter-u-with-ring-above) [ẘ](#char-latin-small-letter-w-with-ring-above) [ẙ](#char-latin-small-letter-y-with-ring-above)|
|Ring Below| |
|![ringBelow](images/ringBelow.png)|![tweak](images/U_down.png)|The ring above modifier shape, with the '[under](#modifier-tweaks)' tweak.<BR><BR>Used in: [Ḁ](#char-latin-capital-letter-a-with-ring-below) [ḁ](#char-latin-small-letter-a-with-ring-below)|
|Stroke| |
|![stroke](images/stroke.png)|![tweak](images/EU_up.png)|Like the macron, but lower, because it cuts through the character, rather than flying above it.<BR><BR>Used in: [Đ](#char-latin-capital-letter-d-with-stroke) [đ](#char-latin-small-letter-d-with-stroke) [Ħ](#char-latin-capital-letter-h-with-stroke) [ħ](#char-latin-small-letter-h-with-stroke) [Ŧ](#char-latin-capital-letter-t-with-stroke) [ŧ](#char-latin-small-letter-t-with-stroke) [Ɨ](#char-latin-capital-letter-i-with-stroke) [ƚ](#char-latin-small-letter-l-with-bar) [Ǥ](#char-latin-capital-letter-g-with-stroke) [ǥ](#char-latin-small-letter-g-with-stroke) [Ƚ](#char-latin-capital-letter-l-with-bar) [Ʉ](#char-latin-capital-letter-u-bar) [Ɍ](#char-latin-capital-letter-r-with-stroke) [ɍ](#char-latin-small-letter-r-with-stroke) [ɨ](#char-latin-small-letter-i-with-stroke) [ʉ](#char-latin-small-letter-u-bar)|
|Slash| |
|![slash](images/slash.png)|![tweak](images/EU_up.png)|Like the acute, but shifted, to indicate that it's lower, and cuts through the character. A bit of a stretch, as it's shifted to the right, not down, but other options were used up. Maybe think of it like moving to the right while reading this text, which eventually wraps, and takes you down a line.<BR><BR>Used in: [Ø](#char-latin-capital-letter-o-with-stroke) [Ǿ](#char-latin-capital-letter-o-with-stroke-and-acute) [ø](#char-latin-small-letter-o-with-stroke) [ǿ](#char-latin-small-letter-o-with-stroke-and-acute) [Ł](#char-latin-capital-letter-l-with-stroke) [ł](#char-latin-small-letter-l-with-stroke)|
|Tilde| |
|![tilde](images/tilde.png)|![tweak](images/EU_up.png)|Shaped like the tilde symbol.<BR><BR>Used in: [Ẫ](#char-latin-capital-letter-a-with-circumflex-and-tilde) [Ã](#char-latin-capital-letter-a-with-tilde) [Ẵ](#char-latin-capital-letter-a-with-breve-and-tilde) [Ễ](#char-latin-capital-letter-e-with-circumflex-and-tilde) [Ẽ](#char-latin-capital-letter-e-with-tilde) [Ĩ](#char-latin-capital-letter-i-with-tilde) [Ñ](#char-latin-capital-letter-n-with-tilde) [Ỗ](#char-latin-capital-letter-o-with-circumflex-and-tilde) [Õ](#char-latin-capital-letter-o-with-tilde) [Ṍ](#char-latin-capital-letter-o-with-tilde-and-acute) [Ȭ](#char-latin-capital-letter-o-with-tilde-and-macron) [Ṏ](#char-latin-capital-letter-o-with-tilde-and-diaeresis) [Ỡ](#char-latin-capital-letter-o-with-horn-and-tilde) [Ũ](#char-latin-capital-letter-u-with-tilde) [Ṹ](#char-latin-capital-letter-u-with-tilde-and-acute) [Ữ](#char-latin-capital-letter-u-with-horn-and-tilde) [Ṽ](#char-latin-capital-letter-v-with-tilde) [Ỹ](#char-latin-capital-letter-y-with-tilde) [ẫ](#char-latin-small-letter-a-with-circumflex-and-tilde) [ã](#char-latin-small-letter-a-with-tilde) [ẵ](#char-latin-small-letter-a-with-breve-and-tilde) [ễ](#char-latin-small-letter-e-with-circumflex-and-tilde) [ẽ](#char-latin-small-letter-e-with-tilde) [ĩ](#char-latin-small-letter-i-with-tilde) [ñ](#char-latin-small-letter-n-with-tilde) [ỗ](#char-latin-small-letter-o-with-circumflex-and-tilde) [õ](#char-latin-small-letter-o-with-tilde) [ṍ](#char-latin-small-letter-o-with-tilde-and-acute) [ȭ](#char-latin-small-letter-o-with-tilde-and-macron) [ṏ](#char-latin-small-letter-o-with-tilde-and-diaeresis) [ỡ](#char-latin-small-letter-o-with-horn-and-tilde) [ũ](#char-latin-small-letter-u-with-tilde) [ṹ](#char-latin-small-letter-u-with-tilde-and-acute) [ữ](#char-latin-small-letter-u-with-horn-and-tilde) [ṽ](#char-latin-small-letter-v-with-tilde) [ỹ](#char-latin-small-letter-y-with-tilde)|
|Tilde Below| |
|![tildeBelow](images/tildeBelow.png)|![tweak](images/U_down.png)|The tilde modifier shape, with the '[under](#modifier-tweaks)' tweak.<BR><BR>Used in: [Ḛ](#char-latin-capital-letter-e-with-tilde-below) [Ḭ](#char-latin-capital-letter-i-with-tilde-below) [Ṵ](#char-latin-capital-letter-u-with-tilde-below) [ḛ](#char-latin-small-letter-e-with-tilde-below) [ḭ](#char-latin-small-letter-i-with-tilde-below) [ṵ](#char-latin-small-letter-u-with-tilde-below)|
|Ligature| |
|![ligature](images/ligature.png)|![tweak](images/EU_up.png)|[Ligatures](https://en.wikipedia.org/wiki/Ligature_(writing)) are two or more graphemes joined together, as in Æ. To output an existing ligature, stroke the two letters in left-to-right order, then stroke this modifier to merge them. Think of the two vertical columns as the two graphemes being joined. For characters that modify ligatures, like the AE ligature with circumflex, or the AE ligature turned, create the ligature first, before modifying it further.<BR><BR>Used in: [W](#char-latin-capital-letter-w) [w](#char-latin-small-letter-w) [Æ](#char-latin-capital-letter-ae) [Ǽ](#char-latin-capital-letter-ae-with-acute) [Ǣ](#char-latin-capital-letter-ae-with-macron) [ß](#char-latin-small-letter-sharp-s) [æ](#char-latin-small-letter-ae) [ǽ](#char-latin-small-letter-ae-with-acute) [ǣ](#char-latin-small-letter-ae-with-macron) [Œ](#char-latin-capital-ligature-oe) [œ](#char-latin-small-ligature-oe) [ƕ](#char-latin-small-letter-hv) [Ƕ](#char-latin-capital-letter-hwair) [ᴂ](#char-latin-small-letter-turned-ae) [ᵫ](#char-latin-small-letter-ue) [ẞ](#char-latin-capital-letter-sharp-s) [Ỻ](#char-latin-capital-letter-middle-welsh-ll) [ỻ](#char-latin-small-letter-middle-welsh-ll) [℔](#char-l-b-bar-symbol) [Ꜩ](#char-latin-capital-letter-tz) [ꜩ](#char-latin-small-letter-tz) [Ꜳ](#char-latin-capital-letter-aa) [ꜳ](#char-latin-small-letter-aa) [Ꜵ](#char-latin-capital-letter-ao) [ꜵ](#char-latin-small-letter-ao) [Ꜷ](#char-latin-capital-letter-au) [ꜷ](#char-latin-small-letter-au) [Ꜹ](#char-latin-capital-letter-av) [ꜻ](#char-latin-small-letter-av-with-horizontal-bar) [Ꜽ](#char-latin-capital-letter-ay) [ꜽ](#char-latin-small-letter-ay) [Ꝏ](#char-latin-capital-letter-oo) [ꝏ](#char-latin-small-letter-oo) [Ꝡ](#char-latin-capital-letter-vy) [ꝡ](#char-latin-small-letter-vy) [ꭣ](#char-latin-small-letter-uo) [ﬀ](#char-latin-small-ligature-ff) [ﬁ](#char-latin-small-ligature-fi) [ﬂ](#char-latin-small-ligature-fl) [ﬃ](#char-latin-small-ligature-ffi) [ﬄ](#char-latin-small-ligature-ffl) [ﬆ](#char-latin-small-ligature-st)|
|Turned/Rotated| |
|![turned](images/turned.png)|![tweak](images/EU_up.png)|This modifier allows access to characters that are turned, or rotated.<BR><BR>Used in: [Ə](#char-latin-capital-letter-schwa) [ə](#char-latin-small-letter-schwa) [ᴂ](#char-latin-small-letter-turned-ae) [Ⅎ](#char-turned-capital-f) [ⅎ](#char-turned-small-f)|
|Reversed| |
|![reversed](images/reversed.png)|![tweak](images/EU_down.png)|The turned modifier shape, with the '[inverted](#modifier-tweaks)' tweak.<BR><BR>This allows access to characters that are flipped, inverted, or reversed.<BR><BR>Used in: [Ↄ](#char-roman-numeral-reversed-one-hundred) [ↄ](#char-latin-small-letter-reversed-c)|

## Character List
Here are all the characters this library exports.

Code points currently link to their associated page on [Compart](https://www.compart.com/en/about-compart)'s site. No affiliation; it just showed up in character searches, seems to have all pages, and it's easy to turn Unicode code points into its various URLs.
|Char|Code Pt|Name|
|-|-|-|
|<a name="char-latin-capital-letter-a-with-grave"></a>À|[U+00C0](https://www.compart.com/en/unicode/U+00C0)|LATIN CAPITAL LETTER A WITH GRAVE|
|<a name="char-latin-small-letter-a-with-grave"></a>à|[U+00E0](https://www.compart.com/en/unicode/U+00E0)|LATIN SMALL LETTER A WITH GRAVE|
|<a name="char-latin-capital-letter-a-with-acute"></a>Á|[U+00C1](https://www.compart.com/en/unicode/U+00C1)|LATIN CAPITAL LETTER A WITH ACUTE|
|<a name="char-latin-small-letter-a-with-acute"></a>á|[U+00E1](https://www.compart.com/en/unicode/U+00E1)|LATIN SMALL LETTER A WITH ACUTE|
|<a name="char-latin-capital-letter-a-with-circumflex"></a>Â|[U+00C2](https://www.compart.com/en/unicode/U+00C2)|LATIN CAPITAL LETTER A WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-a-with-circumflex"></a>â|[U+00E2](https://www.compart.com/en/unicode/U+00E2)|LATIN SMALL LETTER A WITH CIRCUMFLEX|
|<a name="char-latin-capital-letter-a-with-circumflex-and-grave"></a>Ầ|[U+1EA6](https://www.compart.com/en/unicode/U+1EA6)|LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND GRAVE|
|<a name="char-latin-small-letter-a-with-circumflex-and-grave"></a>ầ|[U+1EA7](https://www.compart.com/en/unicode/U+1EA7)|LATIN SMALL LETTER A WITH CIRCUMFLEX AND GRAVE|
|<a name="char-latin-capital-letter-a-with-circumflex-and-acute"></a>Ấ|[U+1EA4](https://www.compart.com/en/unicode/U+1EA4)|LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND ACUTE|
|<a name="char-latin-small-letter-a-with-circumflex-and-acute"></a>ấ|[U+1EA5](https://www.compart.com/en/unicode/U+1EA5)|LATIN SMALL LETTER A WITH CIRCUMFLEX AND ACUTE|
|<a name="char-latin-capital-letter-a-with-circumflex-and-tilde"></a>Ẫ|[U+1EAA](https://www.compart.com/en/unicode/U+1EAA)|LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND TILDE|
|<a name="char-latin-small-letter-a-with-circumflex-and-tilde"></a>ẫ|[U+1EAB](https://www.compart.com/en/unicode/U+1EAB)|LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE|
|<a name="char-latin-capital-letter-a-with-circumflex-and-hook-above"></a>Ẩ|[U+1EA8](https://www.compart.com/en/unicode/U+1EA8)|LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND HOOK ABOVE|
|<a name="char-latin-small-letter-a-with-circumflex-and-hook-above"></a>ẩ|[U+1EA9](https://www.compart.com/en/unicode/U+1EA9)|LATIN SMALL LETTER A WITH CIRCUMFLEX AND HOOK ABOVE|
|<a name="char-latin-capital-letter-a-with-tilde"></a>Ã|[U+00C3](https://www.compart.com/en/unicode/U+00C3)|LATIN CAPITAL LETTER A WITH TILDE|
|<a name="char-latin-small-letter-a-with-tilde"></a>ã|[U+00E3](https://www.compart.com/en/unicode/U+00E3)|LATIN SMALL LETTER A WITH TILDE|
|<a name="char-latin-capital-letter-a-with-macron"></a>Ā|[U+0100](https://www.compart.com/en/unicode/U+0100)|LATIN CAPITAL LETTER A WITH MACRON|
|<a name="char-latin-small-letter-a-with-macron"></a>ā|[U+0101](https://www.compart.com/en/unicode/U+0101)|LATIN SMALL LETTER A WITH MACRON|
|<a name="char-latin-capital-letter-a-with-breve"></a>Ă|[U+0102](https://www.compart.com/en/unicode/U+0102)|LATIN CAPITAL LETTER A WITH BREVE|
|<a name="char-latin-small-letter-a-with-breve"></a>ă|[U+0103](https://www.compart.com/en/unicode/U+0103)|LATIN SMALL LETTER A WITH BREVE|
|<a name="char-latin-capital-letter-a-with-breve-and-grave"></a>Ằ|[U+1EB0](https://www.compart.com/en/unicode/U+1EB0)|LATIN CAPITAL LETTER A WITH BREVE AND GRAVE|
|<a name="char-latin-small-letter-a-with-breve-and-grave"></a>ằ|[U+1EB1](https://www.compart.com/en/unicode/U+1EB1)|LATIN SMALL LETTER A WITH BREVE AND GRAVE|
|<a name="char-latin-capital-letter-a-with-breve-and-acute"></a>Ắ|[U+1EAE](https://www.compart.com/en/unicode/U+1EAE)|LATIN CAPITAL LETTER A WITH BREVE AND ACUTE|
|<a name="char-latin-small-letter-a-with-breve-and-acute"></a>ắ|[U+1EAF](https://www.compart.com/en/unicode/U+1EAF)|LATIN SMALL LETTER A WITH BREVE AND ACUTE|
|<a name="char-latin-capital-letter-a-with-breve-and-tilde"></a>Ẵ|[U+1EB4](https://www.compart.com/en/unicode/U+1EB4)|LATIN CAPITAL LETTER A WITH BREVE AND TILDE|
|<a name="char-latin-small-letter-a-with-breve-and-tilde"></a>ẵ|[U+1EB5](https://www.compart.com/en/unicode/U+1EB5)|LATIN SMALL LETTER A WITH BREVE AND TILDE|
|<a name="char-latin-capital-letter-a-with-breve-and-hook-above"></a>Ẳ|[U+1EB2](https://www.compart.com/en/unicode/U+1EB2)|LATIN CAPITAL LETTER A WITH BREVE AND HOOK ABOVE|
|<a name="char-latin-small-letter-a-with-breve-and-hook-above"></a>ẳ|[U+1EB3](https://www.compart.com/en/unicode/U+1EB3)|LATIN SMALL LETTER A WITH BREVE AND HOOK ABOVE|
|<a name="char-latin-capital-letter-a-with-dot-above"></a>Ȧ|[U+0226](https://www.compart.com/en/unicode/U+0226)|LATIN CAPITAL LETTER A WITH DOT ABOVE|
|<a name="char-latin-small-letter-a-with-dot-above"></a>ȧ|[U+0227](https://www.compart.com/en/unicode/U+0227)|LATIN SMALL LETTER A WITH DOT ABOVE|
|<a name="char-latin-capital-letter-a-with-dot-above-and-macron"></a>Ǡ|[U+01E0](https://www.compart.com/en/unicode/U+01E0)|LATIN CAPITAL LETTER A WITH DOT ABOVE AND MACRON|
|<a name="char-latin-small-letter-a-with-dot-above-and-macron"></a>ǡ|[U+01E1](https://www.compart.com/en/unicode/U+01E1)|LATIN SMALL LETTER A WITH DOT ABOVE AND MACRON|
|<a name="char-latin-capital-letter-a-with-diaeresis"></a>Ä|[U+00C4](https://www.compart.com/en/unicode/U+00C4)|LATIN CAPITAL LETTER A WITH DIAERESIS|
|<a name="char-latin-small-letter-a-with-diaeresis"></a>ä|[U+00E4](https://www.compart.com/en/unicode/U+00E4)|LATIN SMALL LETTER A WITH DIAERESIS|
|<a name="char-latin-capital-letter-a-with-diaeresis-and-macron"></a>Ǟ|[U+01DE](https://www.compart.com/en/unicode/U+01DE)|LATIN CAPITAL LETTER A WITH DIAERESIS AND MACRON|
|<a name="char-latin-small-letter-a-with-diaeresis-and-macron"></a>ǟ|[U+01DF](https://www.compart.com/en/unicode/U+01DF)|LATIN SMALL LETTER A WITH DIAERESIS AND MACRON|
|<a name="char-latin-capital-letter-a-with-hook-above"></a>Ả|[U+1EA2](https://www.compart.com/en/unicode/U+1EA2)|LATIN CAPITAL LETTER A WITH HOOK ABOVE|
|<a name="char-latin-small-letter-a-with-hook-above"></a>ả|[U+1EA3](https://www.compart.com/en/unicode/U+1EA3)|LATIN SMALL LETTER A WITH HOOK ABOVE|
|<a name="char-latin-capital-letter-a-with-ring-above"></a>Å|[U+00C5](https://www.compart.com/en/unicode/U+00C5)|LATIN CAPITAL LETTER A WITH RING ABOVE|
|<a name="char-latin-small-letter-a-with-ring-above"></a>å|[U+00E5](https://www.compart.com/en/unicode/U+00E5)|LATIN SMALL LETTER A WITH RING ABOVE|
|<a name="char-latin-capital-letter-a-with-caron"></a>Ǎ|[U+01CD](https://www.compart.com/en/unicode/U+01CD)|LATIN CAPITAL LETTER A WITH CARON|
|<a name="char-latin-small-letter-a-with-caron"></a>ǎ|[U+01CE](https://www.compart.com/en/unicode/U+01CE)|LATIN SMALL LETTER A WITH CARON|
|<a name="char-latin-capital-letter-a-with-double-grave"></a>Ȁ|[U+0200](https://www.compart.com/en/unicode/U+0200)|LATIN CAPITAL LETTER A WITH DOUBLE GRAVE|
|<a name="char-latin-small-letter-a-with-double-grave"></a>ȁ|[U+0201](https://www.compart.com/en/unicode/U+0201)|LATIN SMALL LETTER A WITH DOUBLE GRAVE|
|<a name="char-latin-capital-letter-a-with-inverted-breve"></a>Ȃ|[U+0202](https://www.compart.com/en/unicode/U+0202)|LATIN CAPITAL LETTER A WITH INVERTED BREVE|
|<a name="char-latin-small-letter-a-with-inverted-breve"></a>ȃ|[U+0203](https://www.compart.com/en/unicode/U+0203)|LATIN SMALL LETTER A WITH INVERTED BREVE|
|<a name="char-latin-capital-letter-a-with-dot-below"></a>Ạ|[U+1EA0](https://www.compart.com/en/unicode/U+1EA0)|LATIN CAPITAL LETTER A WITH DOT BELOW|
|<a name="char-latin-small-letter-a-with-dot-below"></a>ạ|[U+1EA1](https://www.compart.com/en/unicode/U+1EA1)|LATIN SMALL LETTER A WITH DOT BELOW|
|<a name="char-latin-capital-letter-a-with-circumflex-and-dot-below"></a>Ậ|[U+1EAC](https://www.compart.com/en/unicode/U+1EAC)|LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND DOT BELOW|
|<a name="char-latin-small-letter-a-with-circumflex-and-dot-below"></a>ậ|[U+1EAD](https://www.compart.com/en/unicode/U+1EAD)|LATIN SMALL LETTER A WITH CIRCUMFLEX AND DOT BELOW|
|<a name="char-latin-capital-letter-a-with-breve-and-dot-below"></a>Ặ|[U+1EB6](https://www.compart.com/en/unicode/U+1EB6)|LATIN CAPITAL LETTER A WITH BREVE AND DOT BELOW|
|<a name="char-latin-small-letter-a-with-breve-and-dot-below"></a>ặ|[U+1EB7](https://www.compart.com/en/unicode/U+1EB7)|LATIN SMALL LETTER A WITH BREVE AND DOT BELOW|
|<a name="char-latin-capital-letter-a-with-ring-below"></a>Ḁ|[U+1E00](https://www.compart.com/en/unicode/U+1E00)|LATIN CAPITAL LETTER A WITH RING BELOW|
|<a name="char-latin-small-letter-a-with-ring-below"></a>ḁ|[U+1E01](https://www.compart.com/en/unicode/U+1E01)|LATIN SMALL LETTER A WITH RING BELOW|
|<a name="char-latin-capital-letter-a-with-ogonek"></a>Ą|[U+0104](https://www.compart.com/en/unicode/U+0104)|LATIN CAPITAL LETTER A WITH OGONEK|
|<a name="char-latin-small-letter-a-with-ogonek"></a>ą|[U+0105](https://www.compart.com/en/unicode/U+0105)|LATIN SMALL LETTER A WITH OGONEK|
|<a name="char-latin-capital-letter-b-with-dot-above"></a>Ḃ|[U+1E02](https://www.compart.com/en/unicode/U+1E02)|LATIN CAPITAL LETTER B WITH DOT ABOVE|
|<a name="char-latin-small-letter-b-with-dot-above"></a>ḃ|[U+1E03](https://www.compart.com/en/unicode/U+1E03)|LATIN SMALL LETTER B WITH DOT ABOVE|
|<a name="char-latin-capital-letter-b-with-dot-below"></a>Ḅ|[U+1E04](https://www.compart.com/en/unicode/U+1E04)|LATIN CAPITAL LETTER B WITH DOT BELOW|
|<a name="char-latin-small-letter-b-with-dot-below"></a>ḅ|[U+1E05](https://www.compart.com/en/unicode/U+1E05)|LATIN SMALL LETTER B WITH DOT BELOW|
|<a name="char-latin-capital-letter-b-with-line-below"></a>Ḇ|[U+1E06](https://www.compart.com/en/unicode/U+1E06)|LATIN CAPITAL LETTER B WITH LINE BELOW|
|<a name="char-latin-small-letter-b-with-line-below"></a>ḇ|[U+1E07](https://www.compart.com/en/unicode/U+1E07)|LATIN SMALL LETTER B WITH LINE BELOW|
|<a name="char-latin-capital-letter-c-with-acute"></a>Ć|[U+0106](https://www.compart.com/en/unicode/U+0106)|LATIN CAPITAL LETTER C WITH ACUTE|
|<a name="char-latin-small-letter-c-with-acute"></a>ć|[U+0107](https://www.compart.com/en/unicode/U+0107)|LATIN SMALL LETTER C WITH ACUTE|
|<a name="char-latin-capital-letter-c-with-circumflex"></a>Ĉ|[U+0108](https://www.compart.com/en/unicode/U+0108)|LATIN CAPITAL LETTER C WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-c-with-circumflex"></a>ĉ|[U+0109](https://www.compart.com/en/unicode/U+0109)|LATIN SMALL LETTER C WITH CIRCUMFLEX|
|<a name="char-latin-capital-letter-c-with-dot-above"></a>Ċ|[U+010A](https://www.compart.com/en/unicode/U+010A)|LATIN CAPITAL LETTER C WITH DOT ABOVE|
|<a name="char-latin-small-letter-c-with-dot-above"></a>ċ|[U+010B](https://www.compart.com/en/unicode/U+010B)|LATIN SMALL LETTER C WITH DOT ABOVE|
|<a name="char-latin-capital-letter-c-with-caron"></a>Č|[U+010C](https://www.compart.com/en/unicode/U+010C)|LATIN CAPITAL LETTER C WITH CARON|
|<a name="char-latin-small-letter-c-with-caron"></a>č|[U+010D](https://www.compart.com/en/unicode/U+010D)|LATIN SMALL LETTER C WITH CARON|
|<a name="char-latin-capital-letter-c-with-cedilla"></a>Ç|[U+00C7](https://www.compart.com/en/unicode/U+00C7)|LATIN CAPITAL LETTER C WITH CEDILLA|
|<a name="char-latin-small-letter-c-with-cedilla"></a>ç|[U+00E7](https://www.compart.com/en/unicode/U+00E7)|LATIN SMALL LETTER C WITH CEDILLA|
|<a name="char-latin-capital-letter-c-with-cedilla-and-acute"></a>Ḉ|[U+1E08](https://www.compart.com/en/unicode/U+1E08)|LATIN CAPITAL LETTER C WITH CEDILLA AND ACUTE|
|<a name="char-latin-small-letter-c-with-cedilla-and-acute"></a>ḉ|[U+1E09](https://www.compart.com/en/unicode/U+1E09)|LATIN SMALL LETTER C WITH CEDILLA AND ACUTE|
|<a name="char-latin-capital-letter-d-with-dot-above"></a>Ḋ|[U+1E0A](https://www.compart.com/en/unicode/U+1E0A)|LATIN CAPITAL LETTER D WITH DOT ABOVE|
|<a name="char-latin-small-letter-d-with-dot-above"></a>ḋ|[U+1E0B](https://www.compart.com/en/unicode/U+1E0B)|LATIN SMALL LETTER D WITH DOT ABOVE|
|<a name="char-latin-capital-letter-d-with-caron"></a>Ď|[U+010E](https://www.compart.com/en/unicode/U+010E)|LATIN CAPITAL LETTER D WITH CARON|
|<a name="char-latin-small-letter-d-with-caron"></a>ď|[U+010F](https://www.compart.com/en/unicode/U+010F)|LATIN SMALL LETTER D WITH CARON|
|<a name="char-latin-capital-letter-d-with-dot-below"></a>Ḍ|[U+1E0C](https://www.compart.com/en/unicode/U+1E0C)|LATIN CAPITAL LETTER D WITH DOT BELOW|
|<a name="char-latin-small-letter-d-with-dot-below"></a>ḍ|[U+1E0D](https://www.compart.com/en/unicode/U+1E0D)|LATIN SMALL LETTER D WITH DOT BELOW|
|<a name="char-latin-capital-letter-d-with-cedilla"></a>Ḑ|[U+1E10](https://www.compart.com/en/unicode/U+1E10)|LATIN CAPITAL LETTER D WITH CEDILLA|
|<a name="char-latin-small-letter-d-with-cedilla"></a>ḑ|[U+1E11](https://www.compart.com/en/unicode/U+1E11)|LATIN SMALL LETTER D WITH CEDILLA|
|<a name="char-latin-capital-letter-d-with-circumflex-below"></a>Ḓ|[U+1E12](https://www.compart.com/en/unicode/U+1E12)|LATIN CAPITAL LETTER D WITH CIRCUMFLEX BELOW|
|<a name="char-latin-small-letter-d-with-circumflex-below"></a>ḓ|[U+1E13](https://www.compart.com/en/unicode/U+1E13)|LATIN SMALL LETTER D WITH CIRCUMFLEX BELOW|
|<a name="char-latin-capital-letter-d-with-line-below"></a>Ḏ|[U+1E0E](https://www.compart.com/en/unicode/U+1E0E)|LATIN CAPITAL LETTER D WITH LINE BELOW|
|<a name="char-latin-small-letter-d-with-line-below"></a>ḏ|[U+1E0F](https://www.compart.com/en/unicode/U+1E0F)|LATIN SMALL LETTER D WITH LINE BELOW|
|<a name="char-latin-capital-letter-e-with-grave"></a>È|[U+00C8](https://www.compart.com/en/unicode/U+00C8)|LATIN CAPITAL LETTER E WITH GRAVE|
|<a name="char-latin-small-letter-e-with-grave"></a>è|[U+00E8](https://www.compart.com/en/unicode/U+00E8)|LATIN SMALL LETTER E WITH GRAVE|
|<a name="char-latin-capital-letter-e-with-acute"></a>É|[U+00C9](https://www.compart.com/en/unicode/U+00C9)|LATIN CAPITAL LETTER E WITH ACUTE|
|<a name="char-latin-small-letter-e-with-acute"></a>é|[U+00E9](https://www.compart.com/en/unicode/U+00E9)|LATIN SMALL LETTER E WITH ACUTE|
|<a name="char-latin-capital-letter-e-with-circumflex"></a>Ê|[U+00CA](https://www.compart.com/en/unicode/U+00CA)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-e-with-circumflex"></a>ê|[U+00EA](https://www.compart.com/en/unicode/U+00EA)|LATIN SMALL LETTER E WITH CIRCUMFLEX|
|<a name="char-latin-capital-letter-e-with-circumflex-and-grave"></a>Ề|[U+1EC0](https://www.compart.com/en/unicode/U+1EC0)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND GRAVE|
|<a name="char-latin-small-letter-e-with-circumflex-and-grave"></a>ề|[U+1EC1](https://www.compart.com/en/unicode/U+1EC1)|LATIN SMALL LETTER E WITH CIRCUMFLEX AND GRAVE|
|<a name="char-latin-capital-letter-e-with-circumflex-and-acute"></a>Ế|[U+1EBE](https://www.compart.com/en/unicode/U+1EBE)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND ACUTE|
|<a name="char-latin-small-letter-e-with-circumflex-and-acute"></a>ế|[U+1EBF](https://www.compart.com/en/unicode/U+1EBF)|LATIN SMALL LETTER E WITH CIRCUMFLEX AND ACUTE|
|<a name="char-latin-capital-letter-e-with-circumflex-and-tilde"></a>Ễ|[U+1EC4](https://www.compart.com/en/unicode/U+1EC4)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND TILDE|
|<a name="char-latin-small-letter-e-with-circumflex-and-tilde"></a>ễ|[U+1EC5](https://www.compart.com/en/unicode/U+1EC5)|LATIN SMALL LETTER E WITH CIRCUMFLEX AND TILDE|
|<a name="char-latin-capital-letter-e-with-circumflex-and-hook-above"></a>Ể|[U+1EC2](https://www.compart.com/en/unicode/U+1EC2)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE|
|<a name="char-latin-small-letter-e-with-circumflex-and-hook-above"></a>ể|[U+1EC3](https://www.compart.com/en/unicode/U+1EC3)|LATIN SMALL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE|
|<a name="char-latin-capital-letter-e-with-tilde"></a>Ẽ|[U+1EBC](https://www.compart.com/en/unicode/U+1EBC)|LATIN CAPITAL LETTER E WITH TILDE|
|<a name="char-latin-small-letter-e-with-tilde"></a>ẽ|[U+1EBD](https://www.compart.com/en/unicode/U+1EBD)|LATIN SMALL LETTER E WITH TILDE|
|<a name="char-latin-capital-letter-e-with-macron"></a>Ē|[U+0112](https://www.compart.com/en/unicode/U+0112)|LATIN CAPITAL LETTER E WITH MACRON|
|<a name="char-latin-small-letter-e-with-macron"></a>ē|[U+0113](https://www.compart.com/en/unicode/U+0113)|LATIN SMALL LETTER E WITH MACRON|
|<a name="char-latin-capital-letter-e-with-macron-and-grave"></a>Ḕ|[U+1E14](https://www.compart.com/en/unicode/U+1E14)|LATIN CAPITAL LETTER E WITH MACRON AND GRAVE|
|<a name="char-latin-small-letter-e-with-macron-and-grave"></a>ḕ|[U+1E15](https://www.compart.com/en/unicode/U+1E15)|LATIN SMALL LETTER E WITH MACRON AND GRAVE|
|<a name="char-latin-capital-letter-e-with-macron-and-acute"></a>Ḗ|[U+1E16](https://www.compart.com/en/unicode/U+1E16)|LATIN CAPITAL LETTER E WITH MACRON AND ACUTE|
|<a name="char-latin-small-letter-e-with-macron-and-acute"></a>ḗ|[U+1E17](https://www.compart.com/en/unicode/U+1E17)|LATIN SMALL LETTER E WITH MACRON AND ACUTE|
|<a name="char-latin-capital-letter-e-with-breve"></a>Ĕ|[U+0114](https://www.compart.com/en/unicode/U+0114)|LATIN CAPITAL LETTER E WITH BREVE|
|<a name="char-latin-small-letter-e-with-breve"></a>ĕ|[U+0115](https://www.compart.com/en/unicode/U+0115)|LATIN SMALL LETTER E WITH BREVE|
|<a name="char-latin-capital-letter-e-with-dot-above"></a>Ė|[U+0116](https://www.compart.com/en/unicode/U+0116)|LATIN CAPITAL LETTER E WITH DOT ABOVE|
|<a name="char-latin-small-letter-e-with-dot-above"></a>ė|[U+0117](https://www.compart.com/en/unicode/U+0117)|LATIN SMALL LETTER E WITH DOT ABOVE|
|<a name="char-latin-capital-letter-e-with-diaeresis"></a>Ë|[U+00CB](https://www.compart.com/en/unicode/U+00CB)|LATIN CAPITAL LETTER E WITH DIAERESIS|
|<a name="char-latin-small-letter-e-with-diaeresis"></a>ë|[U+00EB](https://www.compart.com/en/unicode/U+00EB)|LATIN SMALL LETTER E WITH DIAERESIS|
|<a name="char-latin-capital-letter-e-with-hook-above"></a>Ẻ|[U+1EBA](https://www.compart.com/en/unicode/U+1EBA)|LATIN CAPITAL LETTER E WITH HOOK ABOVE|
|<a name="char-latin-small-letter-e-with-hook-above"></a>ẻ|[U+1EBB](https://www.compart.com/en/unicode/U+1EBB)|LATIN SMALL LETTER E WITH HOOK ABOVE|
|<a name="char-latin-capital-letter-e-with-caron"></a>Ě|[U+011A](https://www.compart.com/en/unicode/U+011A)|LATIN CAPITAL LETTER E WITH CARON|
|<a name="char-latin-small-letter-e-with-caron"></a>ě|[U+011B](https://www.compart.com/en/unicode/U+011B)|LATIN SMALL LETTER E WITH CARON|
|<a name="char-latin-capital-letter-e-with-double-grave"></a>Ȅ|[U+0204](https://www.compart.com/en/unicode/U+0204)|LATIN CAPITAL LETTER E WITH DOUBLE GRAVE|
|<a name="char-latin-small-letter-e-with-double-grave"></a>ȅ|[U+0205](https://www.compart.com/en/unicode/U+0205)|LATIN SMALL LETTER E WITH DOUBLE GRAVE|
|<a name="char-latin-capital-letter-e-with-inverted-breve"></a>Ȇ|[U+0206](https://www.compart.com/en/unicode/U+0206)|LATIN CAPITAL LETTER E WITH INVERTED BREVE|
|<a name="char-latin-small-letter-e-with-inverted-breve"></a>ȇ|[U+0207](https://www.compart.com/en/unicode/U+0207)|LATIN SMALL LETTER E WITH INVERTED BREVE|
|<a name="char-latin-capital-letter-e-with-dot-below"></a>Ẹ|[U+1EB8](https://www.compart.com/en/unicode/U+1EB8)|LATIN CAPITAL LETTER E WITH DOT BELOW|
|<a name="char-latin-small-letter-e-with-dot-below"></a>ẹ|[U+1EB9](https://www.compart.com/en/unicode/U+1EB9)|LATIN SMALL LETTER E WITH DOT BELOW|
|<a name="char-latin-capital-letter-e-with-circumflex-and-dot-below"></a>Ệ|[U+1EC6](https://www.compart.com/en/unicode/U+1EC6)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND DOT BELOW|
|<a name="char-latin-small-letter-e-with-circumflex-and-dot-below"></a>ệ|[U+1EC7](https://www.compart.com/en/unicode/U+1EC7)|LATIN SMALL LETTER E WITH CIRCUMFLEX AND DOT BELOW|
|<a name="char-latin-capital-letter-e-with-cedilla"></a>Ȩ|[U+0228](https://www.compart.com/en/unicode/U+0228)|LATIN CAPITAL LETTER E WITH CEDILLA|
|<a name="char-latin-small-letter-e-with-cedilla"></a>ȩ|[U+0229](https://www.compart.com/en/unicode/U+0229)|LATIN SMALL LETTER E WITH CEDILLA|
|<a name="char-latin-capital-letter-e-with-cedilla-and-breve"></a>Ḝ|[U+1E1C](https://www.compart.com/en/unicode/U+1E1C)|LATIN CAPITAL LETTER E WITH CEDILLA AND BREVE|
|<a name="char-latin-small-letter-e-with-cedilla-and-breve"></a>ḝ|[U+1E1D](https://www.compart.com/en/unicode/U+1E1D)|LATIN SMALL LETTER E WITH CEDILLA AND BREVE|
|<a name="char-latin-capital-letter-e-with-ogonek"></a>Ę|[U+0118](https://www.compart.com/en/unicode/U+0118)|LATIN CAPITAL LETTER E WITH OGONEK|
|<a name="char-latin-small-letter-e-with-ogonek"></a>ę|[U+0119](https://www.compart.com/en/unicode/U+0119)|LATIN SMALL LETTER E WITH OGONEK|
|<a name="char-latin-capital-letter-e-with-circumflex-below"></a>Ḙ|[U+1E18](https://www.compart.com/en/unicode/U+1E18)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX BELOW|
|<a name="char-latin-small-letter-e-with-circumflex-below"></a>ḙ|[U+1E19](https://www.compart.com/en/unicode/U+1E19)|LATIN SMALL LETTER E WITH CIRCUMFLEX BELOW|
|<a name="char-latin-capital-letter-e-with-tilde-below"></a>Ḛ|[U+1E1A](https://www.compart.com/en/unicode/U+1E1A)|LATIN CAPITAL LETTER E WITH TILDE BELOW|
|<a name="char-latin-small-letter-e-with-tilde-below"></a>ḛ|[U+1E1B](https://www.compart.com/en/unicode/U+1E1B)|LATIN SMALL LETTER E WITH TILDE BELOW|
|<a name="char-latin-capital-letter-f-with-dot-above"></a>Ḟ|[U+1E1E](https://www.compart.com/en/unicode/U+1E1E)|LATIN CAPITAL LETTER F WITH DOT ABOVE|
|<a name="char-latin-small-letter-f-with-dot-above"></a>ḟ|[U+1E1F](https://www.compart.com/en/unicode/U+1E1F)|LATIN SMALL LETTER F WITH DOT ABOVE|
|<a name="char-latin-capital-letter-g-with-acute"></a>Ǵ|[U+01F4](https://www.compart.com/en/unicode/U+01F4)|LATIN CAPITAL LETTER G WITH ACUTE|
|<a name="char-latin-small-letter-g-with-acute"></a>ǵ|[U+01F5](https://www.compart.com/en/unicode/U+01F5)|LATIN SMALL LETTER G WITH ACUTE|
|<a name="char-latin-capital-letter-g-with-circumflex"></a>Ĝ|[U+011C](https://www.compart.com/en/unicode/U+011C)|LATIN CAPITAL LETTER G WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-g-with-circumflex"></a>ĝ|[U+011D](https://www.compart.com/en/unicode/U+011D)|LATIN SMALL LETTER G WITH CIRCUMFLEX|
|<a name="char-latin-capital-letter-g-with-macron"></a>Ḡ|[U+1E20](https://www.compart.com/en/unicode/U+1E20)|LATIN CAPITAL LETTER G WITH MACRON|
|<a name="char-latin-small-letter-g-with-macron"></a>ḡ|[U+1E21](https://www.compart.com/en/unicode/U+1E21)|LATIN SMALL LETTER G WITH MACRON|
|<a name="char-latin-capital-letter-g-with-breve"></a>Ğ|[U+011E](https://www.compart.com/en/unicode/U+011E)|LATIN CAPITAL LETTER G WITH BREVE|
|<a name="char-latin-small-letter-g-with-breve"></a>ğ|[U+011F](https://www.compart.com/en/unicode/U+011F)|LATIN SMALL LETTER G WITH BREVE|
|<a name="char-latin-capital-letter-g-with-dot-above"></a>Ġ|[U+0120](https://www.compart.com/en/unicode/U+0120)|LATIN CAPITAL LETTER G WITH DOT ABOVE|
|<a name="char-latin-small-letter-g-with-dot-above"></a>ġ|[U+0121](https://www.compart.com/en/unicode/U+0121)|LATIN SMALL LETTER G WITH DOT ABOVE|
|<a name="char-latin-capital-letter-g-with-caron"></a>Ǧ|[U+01E6](https://www.compart.com/en/unicode/U+01E6)|LATIN CAPITAL LETTER G WITH CARON|
|<a name="char-latin-small-letter-g-with-caron"></a>ǧ|[U+01E7](https://www.compart.com/en/unicode/U+01E7)|LATIN SMALL LETTER G WITH CARON|
|<a name="char-latin-capital-letter-g-with-cedilla"></a>Ģ|[U+0122](https://www.compart.com/en/unicode/U+0122)|LATIN CAPITAL LETTER G WITH CEDILLA|
|<a name="char-latin-small-letter-g-with-cedilla"></a>ģ|[U+0123](https://www.compart.com/en/unicode/U+0123)|LATIN SMALL LETTER G WITH CEDILLA|
|<a name="char-latin-capital-letter-h-with-circumflex"></a>Ĥ|[U+0124](https://www.compart.com/en/unicode/U+0124)|LATIN CAPITAL LETTER H WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-h-with-circumflex"></a>ĥ|[U+0125](https://www.compart.com/en/unicode/U+0125)|LATIN SMALL LETTER H WITH CIRCUMFLEX|
|<a name="char-latin-capital-letter-h-with-dot-above"></a>Ḣ|[U+1E22](https://www.compart.com/en/unicode/U+1E22)|LATIN CAPITAL LETTER H WITH DOT ABOVE|
|<a name="char-latin-small-letter-h-with-dot-above"></a>ḣ|[U+1E23](https://www.compart.com/en/unicode/U+1E23)|LATIN SMALL LETTER H WITH DOT ABOVE|
|<a name="char-latin-capital-letter-h-with-diaeresis"></a>Ḧ|[U+1E26](https://www.compart.com/en/unicode/U+1E26)|LATIN CAPITAL LETTER H WITH DIAERESIS|
|<a name="char-latin-small-letter-h-with-diaeresis"></a>ḧ|[U+1E27](https://www.compart.com/en/unicode/U+1E27)|LATIN SMALL LETTER H WITH DIAERESIS|
|<a name="char-latin-capital-letter-h-with-caron"></a>Ȟ|[U+021E](https://www.compart.com/en/unicode/U+021E)|LATIN CAPITAL LETTER H WITH CARON|
|<a name="char-latin-small-letter-h-with-caron"></a>ȟ|[U+021F](https://www.compart.com/en/unicode/U+021F)|LATIN SMALL LETTER H WITH CARON|
|<a name="char-latin-capital-letter-h-with-dot-below"></a>Ḥ|[U+1E24](https://www.compart.com/en/unicode/U+1E24)|LATIN CAPITAL LETTER H WITH DOT BELOW|
|<a name="char-latin-small-letter-h-with-dot-below"></a>ḥ|[U+1E25](https://www.compart.com/en/unicode/U+1E25)|LATIN SMALL LETTER H WITH DOT BELOW|
|<a name="char-latin-capital-letter-h-with-cedilla"></a>Ḩ|[U+1E28](https://www.compart.com/en/unicode/U+1E28)|LATIN CAPITAL LETTER H WITH CEDILLA|
|<a name="char-latin-small-letter-h-with-cedilla"></a>ḩ|[U+1E29](https://www.compart.com/en/unicode/U+1E29)|LATIN SMALL LETTER H WITH CEDILLA|
|<a name="char-latin-capital-letter-h-with-breve-below"></a>Ḫ|[U+1E2A](https://www.compart.com/en/unicode/U+1E2A)|LATIN CAPITAL LETTER H WITH BREVE BELOW|
|<a name="char-latin-small-letter-h-with-breve-below"></a>ḫ|[U+1E2B](https://www.compart.com/en/unicode/U+1E2B)|LATIN SMALL LETTER H WITH BREVE BELOW|
|<a name="char-latin-small-letter-h-with-line-below"></a>ẖ|[U+1E96](https://www.compart.com/en/unicode/U+1E96)|LATIN SMALL LETTER H WITH LINE BELOW|
|<a name="char-latin-small-letter-i"></a>i|[U+0069](https://www.compart.com/en/unicode/U+0069)|LATIN SMALL LETTER I|
|<a name="char-latin-capital-letter-i-with-grave"></a>Ì|[U+00CC](https://www.compart.com/en/unicode/U+00CC)|LATIN CAPITAL LETTER I WITH GRAVE|
|<a name="char-latin-small-letter-i-with-grave"></a>ì|[U+00EC](https://www.compart.com/en/unicode/U+00EC)|LATIN SMALL LETTER I WITH GRAVE|
|<a name="char-latin-capital-letter-i-with-acute"></a>Í|[U+00CD](https://www.compart.com/en/unicode/U+00CD)|LATIN CAPITAL LETTER I WITH ACUTE|
|<a name="char-latin-small-letter-i-with-acute"></a>í|[U+00ED](https://www.compart.com/en/unicode/U+00ED)|LATIN SMALL LETTER I WITH ACUTE|
|<a name="char-latin-capital-letter-i-with-circumflex"></a>Î|[U+00CE](https://www.compart.com/en/unicode/U+00CE)|LATIN CAPITAL LETTER I WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-i-with-circumflex"></a>î|[U+00EE](https://www.compart.com/en/unicode/U+00EE)|LATIN SMALL LETTER I WITH CIRCUMFLEX|
|<a name="char-latin-capital-letter-i-with-tilde"></a>Ĩ|[U+0128](https://www.compart.com/en/unicode/U+0128)|LATIN CAPITAL LETTER I WITH TILDE|
|<a name="char-latin-small-letter-i-with-tilde"></a>ĩ|[U+0129](https://www.compart.com/en/unicode/U+0129)|LATIN SMALL LETTER I WITH TILDE|
|<a name="char-latin-capital-letter-i-with-macron"></a>Ī|[U+012A](https://www.compart.com/en/unicode/U+012A)|LATIN CAPITAL LETTER I WITH MACRON|
|<a name="char-latin-small-letter-i-with-macron"></a>ī|[U+012B](https://www.compart.com/en/unicode/U+012B)|LATIN SMALL LETTER I WITH MACRON|
|<a name="char-latin-capital-letter-i-with-breve"></a>Ĭ|[U+012C](https://www.compart.com/en/unicode/U+012C)|LATIN CAPITAL LETTER I WITH BREVE|
|<a name="char-latin-small-letter-i-with-breve"></a>ĭ|[U+012D](https://www.compart.com/en/unicode/U+012D)|LATIN SMALL LETTER I WITH BREVE|
|<a name="char-latin-capital-letter-i-with-dot-above"></a>İ|[U+0130](https://www.compart.com/en/unicode/U+0130)|LATIN CAPITAL LETTER I WITH DOT ABOVE|
|<a name="char-latin-capital-letter-i-with-diaeresis"></a>Ï|[U+00CF](https://www.compart.com/en/unicode/U+00CF)|LATIN CAPITAL LETTER I WITH DIAERESIS|
|<a name="char-latin-small-letter-i-with-diaeresis"></a>ï|[U+00EF](https://www.compart.com/en/unicode/U+00EF)|LATIN SMALL LETTER I WITH DIAERESIS|
|<a name="char-latin-capital-letter-i-with-diaeresis-and-acute"></a>Ḯ|[U+1E2E](https://www.compart.com/en/unicode/U+1E2E)|LATIN CAPITAL LETTER I WITH DIAERESIS AND ACUTE|
|<a name="char-latin-small-letter-i-with-diaeresis-and-acute"></a>ḯ|[U+1E2F](https://www.compart.com/en/unicode/U+1E2F)|LATIN SMALL LETTER I WITH DIAERESIS AND ACUTE|
|<a name="char-latin-capital-letter-i-with-hook-above"></a>Ỉ|[U+1EC8](https://www.compart.com/en/unicode/U+1EC8)|LATIN CAPITAL LETTER I WITH HOOK ABOVE|
|<a name="char-latin-small-letter-i-with-hook-above"></a>ỉ|[U+1EC9](https://www.compart.com/en/unicode/U+1EC9)|LATIN SMALL LETTER I WITH HOOK ABOVE|
|<a name="char-latin-capital-letter-i-with-caron"></a>Ǐ|[U+01CF](https://www.compart.com/en/unicode/U+01CF)|LATIN CAPITAL LETTER I WITH CARON|
|<a name="char-latin-small-letter-i-with-caron"></a>ǐ|[U+01D0](https://www.compart.com/en/unicode/U+01D0)|LATIN SMALL LETTER I WITH CARON|
|<a name="char-latin-capital-letter-i-with-double-grave"></a>Ȉ|[U+0208](https://www.compart.com/en/unicode/U+0208)|LATIN CAPITAL LETTER I WITH DOUBLE GRAVE|
|<a name="char-latin-small-letter-i-with-double-grave"></a>ȉ|[U+0209](https://www.compart.com/en/unicode/U+0209)|LATIN SMALL LETTER I WITH DOUBLE GRAVE|
|<a name="char-latin-capital-letter-i-with-inverted-breve"></a>Ȋ|[U+020A](https://www.compart.com/en/unicode/U+020A)|LATIN CAPITAL LETTER I WITH INVERTED BREVE|
|<a name="char-latin-small-letter-i-with-inverted-breve"></a>ȋ|[U+020B](https://www.compart.com/en/unicode/U+020B)|LATIN SMALL LETTER I WITH INVERTED BREVE|
|<a name="char-latin-capital-letter-i-with-dot-below"></a>Ị|[U+1ECA](https://www.compart.com/en/unicode/U+1ECA)|LATIN CAPITAL LETTER I WITH DOT BELOW|
|<a name="char-latin-small-letter-i-with-dot-below"></a>ị|[U+1ECB](https://www.compart.com/en/unicode/U+1ECB)|LATIN SMALL LETTER I WITH DOT BELOW|
|<a name="char-latin-capital-letter-i-with-ogonek"></a>Į|[U+012E](https://www.compart.com/en/unicode/U+012E)|LATIN CAPITAL LETTER I WITH OGONEK|
|<a name="char-latin-small-letter-i-with-ogonek"></a>į|[U+012F](https://www.compart.com/en/unicode/U+012F)|LATIN SMALL LETTER I WITH OGONEK|
|<a name="char-latin-capital-letter-i-with-tilde-below"></a>Ḭ|[U+1E2C](https://www.compart.com/en/unicode/U+1E2C)|LATIN CAPITAL LETTER I WITH TILDE BELOW|
|<a name="char-latin-small-letter-i-with-tilde-below"></a>ḭ|[U+1E2D](https://www.compart.com/en/unicode/U+1E2D)|LATIN SMALL LETTER I WITH TILDE BELOW|
|<a name="char-latin-capital-letter-j-with-circumflex"></a>Ĵ|[U+0134](https://www.compart.com/en/unicode/U+0134)|LATIN CAPITAL LETTER J WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-j-with-circumflex"></a>ĵ|[U+0135](https://www.compart.com/en/unicode/U+0135)|LATIN SMALL LETTER J WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-j-with-caron"></a>ǰ|[U+01F0](https://www.compart.com/en/unicode/U+01F0)|LATIN SMALL LETTER J WITH CARON|
|<a name="char-latin-capital-letter-k-with-acute"></a>Ḱ|[U+1E30](https://www.compart.com/en/unicode/U+1E30)|LATIN CAPITAL LETTER K WITH ACUTE|
|<a name="char-latin-small-letter-k-with-acute"></a>ḱ|[U+1E31](https://www.compart.com/en/unicode/U+1E31)|LATIN SMALL LETTER K WITH ACUTE|
|<a name="char-latin-capital-letter-k-with-caron"></a>Ǩ|[U+01E8](https://www.compart.com/en/unicode/U+01E8)|LATIN CAPITAL LETTER K WITH CARON|
|<a name="char-latin-small-letter-k-with-caron"></a>ǩ|[U+01E9](https://www.compart.com/en/unicode/U+01E9)|LATIN SMALL LETTER K WITH CARON|
|<a name="char-latin-capital-letter-k-with-dot-below"></a>Ḳ|[U+1E32](https://www.compart.com/en/unicode/U+1E32)|LATIN CAPITAL LETTER K WITH DOT BELOW|
|<a name="char-latin-small-letter-k-with-dot-below"></a>ḳ|[U+1E33](https://www.compart.com/en/unicode/U+1E33)|LATIN SMALL LETTER K WITH DOT BELOW|
|<a name="char-latin-capital-letter-k-with-cedilla"></a>Ķ|[U+0136](https://www.compart.com/en/unicode/U+0136)|LATIN CAPITAL LETTER K WITH CEDILLA|
|<a name="char-latin-small-letter-k-with-cedilla"></a>ķ|[U+0137](https://www.compart.com/en/unicode/U+0137)|LATIN SMALL LETTER K WITH CEDILLA|
|<a name="char-latin-capital-letter-k-with-line-below"></a>Ḵ|[U+1E34](https://www.compart.com/en/unicode/U+1E34)|LATIN CAPITAL LETTER K WITH LINE BELOW|
|<a name="char-latin-small-letter-k-with-line-below"></a>ḵ|[U+1E35](https://www.compart.com/en/unicode/U+1E35)|LATIN SMALL LETTER K WITH LINE BELOW|
|<a name="char-latin-capital-letter-l-with-acute"></a>Ĺ|[U+0139](https://www.compart.com/en/unicode/U+0139)|LATIN CAPITAL LETTER L WITH ACUTE|
|<a name="char-latin-small-letter-l-with-acute"></a>ĺ|[U+013A](https://www.compart.com/en/unicode/U+013A)|LATIN SMALL LETTER L WITH ACUTE|
|<a name="char-latin-capital-letter-l-with-caron"></a>Ľ|[U+013D](https://www.compart.com/en/unicode/U+013D)|LATIN CAPITAL LETTER L WITH CARON|
|<a name="char-latin-small-letter-l-with-caron"></a>ľ|[U+013E](https://www.compart.com/en/unicode/U+013E)|LATIN SMALL LETTER L WITH CARON|
|<a name="char-latin-capital-letter-l-with-dot-below"></a>Ḷ|[U+1E36](https://www.compart.com/en/unicode/U+1E36)|LATIN CAPITAL LETTER L WITH DOT BELOW|
|<a name="char-latin-small-letter-l-with-dot-below"></a>ḷ|[U+1E37](https://www.compart.com/en/unicode/U+1E37)|LATIN SMALL LETTER L WITH DOT BELOW|
|<a name="char-latin-capital-letter-l-with-dot-below-and-macron"></a>Ḹ|[U+1E38](https://www.compart.com/en/unicode/U+1E38)|LATIN CAPITAL LETTER L WITH DOT BELOW AND MACRON|
|<a name="char-latin-small-letter-l-with-dot-below-and-macron"></a>ḹ|[U+1E39](https://www.compart.com/en/unicode/U+1E39)|LATIN SMALL LETTER L WITH DOT BELOW AND MACRON|
|<a name="char-latin-capital-letter-l-with-cedilla"></a>Ļ|[U+013B](https://www.compart.com/en/unicode/U+013B)|LATIN CAPITAL LETTER L WITH CEDILLA|
|<a name="char-latin-small-letter-l-with-cedilla"></a>ļ|[U+013C](https://www.compart.com/en/unicode/U+013C)|LATIN SMALL LETTER L WITH CEDILLA|
|<a name="char-latin-capital-letter-l-with-circumflex-below"></a>Ḽ|[U+1E3C](https://www.compart.com/en/unicode/U+1E3C)|LATIN CAPITAL LETTER L WITH CIRCUMFLEX BELOW|
|<a name="char-latin-small-letter-l-with-circumflex-below"></a>ḽ|[U+1E3D](https://www.compart.com/en/unicode/U+1E3D)|LATIN SMALL LETTER L WITH CIRCUMFLEX BELOW|
|<a name="char-latin-capital-letter-l-with-line-below"></a>Ḻ|[U+1E3A](https://www.compart.com/en/unicode/U+1E3A)|LATIN CAPITAL LETTER L WITH LINE BELOW|
|<a name="char-latin-small-letter-l-with-line-below"></a>ḻ|[U+1E3B](https://www.compart.com/en/unicode/U+1E3B)|LATIN SMALL LETTER L WITH LINE BELOW|
|<a name="char-latin-capital-letter-m-with-acute"></a>Ḿ|[U+1E3E](https://www.compart.com/en/unicode/U+1E3E)|LATIN CAPITAL LETTER M WITH ACUTE|
|<a name="char-latin-small-letter-m-with-acute"></a>ḿ|[U+1E3F](https://www.compart.com/en/unicode/U+1E3F)|LATIN SMALL LETTER M WITH ACUTE|
|<a name="char-latin-capital-letter-m-with-dot-above"></a>Ṁ|[U+1E40](https://www.compart.com/en/unicode/U+1E40)|LATIN CAPITAL LETTER M WITH DOT ABOVE|
|<a name="char-latin-small-letter-m-with-dot-above"></a>ṁ|[U+1E41](https://www.compart.com/en/unicode/U+1E41)|LATIN SMALL LETTER M WITH DOT ABOVE|
|<a name="char-latin-capital-letter-m-with-dot-below"></a>Ṃ|[U+1E42](https://www.compart.com/en/unicode/U+1E42)|LATIN CAPITAL LETTER M WITH DOT BELOW|
|<a name="char-latin-small-letter-m-with-dot-below"></a>ṃ|[U+1E43](https://www.compart.com/en/unicode/U+1E43)|LATIN SMALL LETTER M WITH DOT BELOW|
|<a name="char-latin-capital-letter-n-with-grave"></a>Ǹ|[U+01F8](https://www.compart.com/en/unicode/U+01F8)|LATIN CAPITAL LETTER N WITH GRAVE|
|<a name="char-latin-small-letter-n-with-grave"></a>ǹ|[U+01F9](https://www.compart.com/en/unicode/U+01F9)|LATIN SMALL LETTER N WITH GRAVE|
|<a name="char-latin-capital-letter-n-with-acute"></a>Ń|[U+0143](https://www.compart.com/en/unicode/U+0143)|LATIN CAPITAL LETTER N WITH ACUTE|
|<a name="char-latin-small-letter-n-with-acute"></a>ń|[U+0144](https://www.compart.com/en/unicode/U+0144)|LATIN SMALL LETTER N WITH ACUTE|
|<a name="char-latin-capital-letter-n-with-tilde"></a>Ñ|[U+00D1](https://www.compart.com/en/unicode/U+00D1)|LATIN CAPITAL LETTER N WITH TILDE|
|<a name="char-latin-small-letter-n-with-tilde"></a>ñ|[U+00F1](https://www.compart.com/en/unicode/U+00F1)|LATIN SMALL LETTER N WITH TILDE|
|<a name="char-latin-capital-letter-n-with-dot-above"></a>Ṅ|[U+1E44](https://www.compart.com/en/unicode/U+1E44)|LATIN CAPITAL LETTER N WITH DOT ABOVE|
|<a name="char-latin-small-letter-n-with-dot-above"></a>ṅ|[U+1E45](https://www.compart.com/en/unicode/U+1E45)|LATIN SMALL LETTER N WITH DOT ABOVE|
|<a name="char-latin-capital-letter-n-with-caron"></a>Ň|[U+0147](https://www.compart.com/en/unicode/U+0147)|LATIN CAPITAL LETTER N WITH CARON|
|<a name="char-latin-small-letter-n-with-caron"></a>ň|[U+0148](https://www.compart.com/en/unicode/U+0148)|LATIN SMALL LETTER N WITH CARON|
|<a name="char-latin-capital-letter-n-with-dot-below"></a>Ṇ|[U+1E46](https://www.compart.com/en/unicode/U+1E46)|LATIN CAPITAL LETTER N WITH DOT BELOW|
|<a name="char-latin-small-letter-n-with-dot-below"></a>ṇ|[U+1E47](https://www.compart.com/en/unicode/U+1E47)|LATIN SMALL LETTER N WITH DOT BELOW|
|<a name="char-latin-capital-letter-n-with-cedilla"></a>Ņ|[U+0145](https://www.compart.com/en/unicode/U+0145)|LATIN CAPITAL LETTER N WITH CEDILLA|
|<a name="char-latin-small-letter-n-with-cedilla"></a>ņ|[U+0146](https://www.compart.com/en/unicode/U+0146)|LATIN SMALL LETTER N WITH CEDILLA|
|<a name="char-latin-capital-letter-n-with-circumflex-below"></a>Ṋ|[U+1E4A](https://www.compart.com/en/unicode/U+1E4A)|LATIN CAPITAL LETTER N WITH CIRCUMFLEX BELOW|
|<a name="char-latin-small-letter-n-with-circumflex-below"></a>ṋ|[U+1E4B](https://www.compart.com/en/unicode/U+1E4B)|LATIN SMALL LETTER N WITH CIRCUMFLEX BELOW|
|<a name="char-latin-capital-letter-n-with-line-below"></a>Ṉ|[U+1E48](https://www.compart.com/en/unicode/U+1E48)|LATIN CAPITAL LETTER N WITH LINE BELOW|
|<a name="char-latin-small-letter-n-with-line-below"></a>ṉ|[U+1E49](https://www.compart.com/en/unicode/U+1E49)|LATIN SMALL LETTER N WITH LINE BELOW|
|<a name="char-latin-capital-letter-o-with-grave"></a>Ò|[U+00D2](https://www.compart.com/en/unicode/U+00D2)|LATIN CAPITAL LETTER O WITH GRAVE|
|<a name="char-latin-small-letter-o-with-grave"></a>ò|[U+00F2](https://www.compart.com/en/unicode/U+00F2)|LATIN SMALL LETTER O WITH GRAVE|
|<a name="char-latin-capital-letter-o-with-acute"></a>Ó|[U+00D3](https://www.compart.com/en/unicode/U+00D3)|LATIN CAPITAL LETTER O WITH ACUTE|
|<a name="char-latin-small-letter-o-with-acute"></a>ó|[U+00F3](https://www.compart.com/en/unicode/U+00F3)|LATIN SMALL LETTER O WITH ACUTE|
|<a name="char-latin-capital-letter-o-with-circumflex"></a>Ô|[U+00D4](https://www.compart.com/en/unicode/U+00D4)|LATIN CAPITAL LETTER O WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-o-with-circumflex"></a>ô|[U+00F4](https://www.compart.com/en/unicode/U+00F4)|LATIN SMALL LETTER O WITH CIRCUMFLEX|
|<a name="char-latin-capital-letter-o-with-circumflex-and-grave"></a>Ồ|[U+1ED2](https://www.compart.com/en/unicode/U+1ED2)|LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND GRAVE|
|<a name="char-latin-small-letter-o-with-circumflex-and-grave"></a>ồ|[U+1ED3](https://www.compart.com/en/unicode/U+1ED3)|LATIN SMALL LETTER O WITH CIRCUMFLEX AND GRAVE|
|<a name="char-latin-capital-letter-o-with-circumflex-and-acute"></a>Ố|[U+1ED0](https://www.compart.com/en/unicode/U+1ED0)|LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND ACUTE|
|<a name="char-latin-small-letter-o-with-circumflex-and-acute"></a>ố|[U+1ED1](https://www.compart.com/en/unicode/U+1ED1)|LATIN SMALL LETTER O WITH CIRCUMFLEX AND ACUTE|
|<a name="char-latin-capital-letter-o-with-circumflex-and-tilde"></a>Ỗ|[U+1ED6](https://www.compart.com/en/unicode/U+1ED6)|LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND TILDE|
|<a name="char-latin-small-letter-o-with-circumflex-and-tilde"></a>ỗ|[U+1ED7](https://www.compart.com/en/unicode/U+1ED7)|LATIN SMALL LETTER O WITH CIRCUMFLEX AND TILDE|
|<a name="char-latin-capital-letter-o-with-circumflex-and-hook-above"></a>Ổ|[U+1ED4](https://www.compart.com/en/unicode/U+1ED4)|LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE|
|<a name="char-latin-small-letter-o-with-circumflex-and-hook-above"></a>ổ|[U+1ED5](https://www.compart.com/en/unicode/U+1ED5)|LATIN SMALL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE|
|<a name="char-latin-capital-letter-o-with-tilde"></a>Õ|[U+00D5](https://www.compart.com/en/unicode/U+00D5)|LATIN CAPITAL LETTER O WITH TILDE|
|<a name="char-latin-small-letter-o-with-tilde"></a>õ|[U+00F5](https://www.compart.com/en/unicode/U+00F5)|LATIN SMALL LETTER O WITH TILDE|
|<a name="char-latin-capital-letter-o-with-tilde-and-acute"></a>Ṍ|[U+1E4C](https://www.compart.com/en/unicode/U+1E4C)|LATIN CAPITAL LETTER O WITH TILDE AND ACUTE|
|<a name="char-latin-small-letter-o-with-tilde-and-acute"></a>ṍ|[U+1E4D](https://www.compart.com/en/unicode/U+1E4D)|LATIN SMALL LETTER O WITH TILDE AND ACUTE|
|<a name="char-latin-capital-letter-o-with-tilde-and-macron"></a>Ȭ|[U+022C](https://www.compart.com/en/unicode/U+022C)|LATIN CAPITAL LETTER O WITH TILDE AND MACRON|
|<a name="char-latin-small-letter-o-with-tilde-and-macron"></a>ȭ|[U+022D](https://www.compart.com/en/unicode/U+022D)|LATIN SMALL LETTER O WITH TILDE AND MACRON|
|<a name="char-latin-capital-letter-o-with-tilde-and-diaeresis"></a>Ṏ|[U+1E4E](https://www.compart.com/en/unicode/U+1E4E)|LATIN CAPITAL LETTER O WITH TILDE AND DIAERESIS|
|<a name="char-latin-small-letter-o-with-tilde-and-diaeresis"></a>ṏ|[U+1E4F](https://www.compart.com/en/unicode/U+1E4F)|LATIN SMALL LETTER O WITH TILDE AND DIAERESIS|
|<a name="char-latin-capital-letter-o-with-macron"></a>Ō|[U+014C](https://www.compart.com/en/unicode/U+014C)|LATIN CAPITAL LETTER O WITH MACRON|
|<a name="char-latin-small-letter-o-with-macron"></a>ō|[U+014D](https://www.compart.com/en/unicode/U+014D)|LATIN SMALL LETTER O WITH MACRON|
|<a name="char-latin-capital-letter-o-with-macron-and-grave"></a>Ṑ|[U+1E50](https://www.compart.com/en/unicode/U+1E50)|LATIN CAPITAL LETTER O WITH MACRON AND GRAVE|
|<a name="char-latin-small-letter-o-with-macron-and-grave"></a>ṑ|[U+1E51](https://www.compart.com/en/unicode/U+1E51)|LATIN SMALL LETTER O WITH MACRON AND GRAVE|
|<a name="char-latin-capital-letter-o-with-macron-and-acute"></a>Ṓ|[U+1E52](https://www.compart.com/en/unicode/U+1E52)|LATIN CAPITAL LETTER O WITH MACRON AND ACUTE|
|<a name="char-latin-small-letter-o-with-macron-and-acute"></a>ṓ|[U+1E53](https://www.compart.com/en/unicode/U+1E53)|LATIN SMALL LETTER O WITH MACRON AND ACUTE|
|<a name="char-latin-capital-letter-o-with-breve"></a>Ŏ|[U+014E](https://www.compart.com/en/unicode/U+014E)|LATIN CAPITAL LETTER O WITH BREVE|
|<a name="char-latin-small-letter-o-with-breve"></a>ŏ|[U+014F](https://www.compart.com/en/unicode/U+014F)|LATIN SMALL LETTER O WITH BREVE|
|<a name="char-latin-capital-letter-o-with-dot-above"></a>Ȯ|[U+022E](https://www.compart.com/en/unicode/U+022E)|LATIN CAPITAL LETTER O WITH DOT ABOVE|
|<a name="char-latin-small-letter-o-with-dot-above"></a>ȯ|[U+022F](https://www.compart.com/en/unicode/U+022F)|LATIN SMALL LETTER O WITH DOT ABOVE|
|<a name="char-latin-capital-letter-o-with-dot-above-and-macron"></a>Ȱ|[U+0230](https://www.compart.com/en/unicode/U+0230)|LATIN CAPITAL LETTER O WITH DOT ABOVE AND MACRON|
|<a name="char-latin-small-letter-o-with-dot-above-and-macron"></a>ȱ|[U+0231](https://www.compart.com/en/unicode/U+0231)|LATIN SMALL LETTER O WITH DOT ABOVE AND MACRON|
|<a name="char-latin-capital-letter-o-with-diaeresis"></a>Ö|[U+00D6](https://www.compart.com/en/unicode/U+00D6)|LATIN CAPITAL LETTER O WITH DIAERESIS|
|<a name="char-latin-small-letter-o-with-diaeresis"></a>ö|[U+00F6](https://www.compart.com/en/unicode/U+00F6)|LATIN SMALL LETTER O WITH DIAERESIS|
|<a name="char-latin-capital-letter-o-with-diaeresis-and-macron"></a>Ȫ|[U+022A](https://www.compart.com/en/unicode/U+022A)|LATIN CAPITAL LETTER O WITH DIAERESIS AND MACRON|
|<a name="char-latin-small-letter-o-with-diaeresis-and-macron"></a>ȫ|[U+022B](https://www.compart.com/en/unicode/U+022B)|LATIN SMALL LETTER O WITH DIAERESIS AND MACRON|
|<a name="char-latin-capital-letter-o-with-hook-above"></a>Ỏ|[U+1ECE](https://www.compart.com/en/unicode/U+1ECE)|LATIN CAPITAL LETTER O WITH HOOK ABOVE|
|<a name="char-latin-small-letter-o-with-hook-above"></a>ỏ|[U+1ECF](https://www.compart.com/en/unicode/U+1ECF)|LATIN SMALL LETTER O WITH HOOK ABOVE|
|<a name="char-latin-capital-letter-o-with-double-acute"></a>Ő|[U+0150](https://www.compart.com/en/unicode/U+0150)|LATIN CAPITAL LETTER O WITH DOUBLE ACUTE|
|<a name="char-latin-small-letter-o-with-double-acute"></a>ő|[U+0151](https://www.compart.com/en/unicode/U+0151)|LATIN SMALL LETTER O WITH DOUBLE ACUTE|
|<a name="char-latin-capital-letter-o-with-caron"></a>Ǒ|[U+01D1](https://www.compart.com/en/unicode/U+01D1)|LATIN CAPITAL LETTER O WITH CARON|
|<a name="char-latin-small-letter-o-with-caron"></a>ǒ|[U+01D2](https://www.compart.com/en/unicode/U+01D2)|LATIN SMALL LETTER O WITH CARON|
|<a name="char-latin-capital-letter-o-with-double-grave"></a>Ȍ|[U+020C](https://www.compart.com/en/unicode/U+020C)|LATIN CAPITAL LETTER O WITH DOUBLE GRAVE|
|<a name="char-latin-small-letter-o-with-double-grave"></a>ȍ|[U+020D](https://www.compart.com/en/unicode/U+020D)|LATIN SMALL LETTER O WITH DOUBLE GRAVE|
|<a name="char-latin-capital-letter-o-with-inverted-breve"></a>Ȏ|[U+020E](https://www.compart.com/en/unicode/U+020E)|LATIN CAPITAL LETTER O WITH INVERTED BREVE|
|<a name="char-latin-small-letter-o-with-inverted-breve"></a>ȏ|[U+020F](https://www.compart.com/en/unicode/U+020F)|LATIN SMALL LETTER O WITH INVERTED BREVE|
|<a name="char-latin-capital-letter-o-with-horn"></a>Ơ|[U+01A0](https://www.compart.com/en/unicode/U+01A0)|LATIN CAPITAL LETTER O WITH HORN|
|<a name="char-latin-capital-letter-o-with-horn"></a>Ơ|[U+01A0](https://www.compart.com/en/unicode/U+01A0)|LATIN CAPITAL LETTER O WITH HORN|
|<a name="char-latin-small-letter-o-with-horn"></a>ơ|[U+01A1](https://www.compart.com/en/unicode/U+01A1)|LATIN SMALL LETTER O WITH HORN|
|<a name="char-latin-small-letter-o-with-horn"></a>ơ|[U+01A1](https://www.compart.com/en/unicode/U+01A1)|LATIN SMALL LETTER O WITH HORN|
|<a name="char-latin-capital-letter-o-with-horn-and-grave"></a>Ờ|[U+1EDC](https://www.compart.com/en/unicode/U+1EDC)|LATIN CAPITAL LETTER O WITH HORN AND GRAVE|
|<a name="char-latin-small-letter-o-with-horn-and-grave"></a>ờ|[U+1EDD](https://www.compart.com/en/unicode/U+1EDD)|LATIN SMALL LETTER O WITH HORN AND GRAVE|
|<a name="char-latin-capital-letter-o-with-horn-and-acute"></a>Ớ|[U+1EDA](https://www.compart.com/en/unicode/U+1EDA)|LATIN CAPITAL LETTER O WITH HORN AND ACUTE|
|<a name="char-latin-small-letter-o-with-horn-and-acute"></a>ớ|[U+1EDB](https://www.compart.com/en/unicode/U+1EDB)|LATIN SMALL LETTER O WITH HORN AND ACUTE|
|<a name="char-latin-capital-letter-o-with-horn-and-tilde"></a>Ỡ|[U+1EE0](https://www.compart.com/en/unicode/U+1EE0)|LATIN CAPITAL LETTER O WITH HORN AND TILDE|
|<a name="char-latin-small-letter-o-with-horn-and-tilde"></a>ỡ|[U+1EE1](https://www.compart.com/en/unicode/U+1EE1)|LATIN SMALL LETTER O WITH HORN AND TILDE|
|<a name="char-latin-capital-letter-o-with-horn-and-hook-above"></a>Ở|[U+1EDE](https://www.compart.com/en/unicode/U+1EDE)|LATIN CAPITAL LETTER O WITH HORN AND HOOK ABOVE|
|<a name="char-latin-small-letter-o-with-horn-and-hook-above"></a>ở|[U+1EDF](https://www.compart.com/en/unicode/U+1EDF)|LATIN SMALL LETTER O WITH HORN AND HOOK ABOVE|
|<a name="char-latin-capital-letter-o-with-horn-and-dot-below"></a>Ợ|[U+1EE2](https://www.compart.com/en/unicode/U+1EE2)|LATIN CAPITAL LETTER O WITH HORN AND DOT BELOW|
|<a name="char-latin-small-letter-o-with-horn-and-dot-below"></a>ợ|[U+1EE3](https://www.compart.com/en/unicode/U+1EE3)|LATIN SMALL LETTER O WITH HORN AND DOT BELOW|
|<a name="char-latin-capital-letter-o-with-dot-below"></a>Ọ|[U+1ECC](https://www.compart.com/en/unicode/U+1ECC)|LATIN CAPITAL LETTER O WITH DOT BELOW|
|<a name="char-latin-small-letter-o-with-dot-below"></a>ọ|[U+1ECD](https://www.compart.com/en/unicode/U+1ECD)|LATIN SMALL LETTER O WITH DOT BELOW|
|<a name="char-latin-capital-letter-o-with-circumflex-and-dot-below"></a>Ộ|[U+1ED8](https://www.compart.com/en/unicode/U+1ED8)|LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND DOT BELOW|
|<a name="char-latin-small-letter-o-with-circumflex-and-dot-below"></a>ộ|[U+1ED9](https://www.compart.com/en/unicode/U+1ED9)|LATIN SMALL LETTER O WITH CIRCUMFLEX AND DOT BELOW|
|<a name="char-latin-capital-letter-o-with-ogonek"></a>Ǫ|[U+01EA](https://www.compart.com/en/unicode/U+01EA)|LATIN CAPITAL LETTER O WITH OGONEK|
|<a name="char-latin-small-letter-o-with-ogonek"></a>ǫ|[U+01EB](https://www.compart.com/en/unicode/U+01EB)|LATIN SMALL LETTER O WITH OGONEK|
|<a name="char-latin-capital-letter-o-with-ogonek-and-macron"></a>Ǭ|[U+01EC](https://www.compart.com/en/unicode/U+01EC)|LATIN CAPITAL LETTER O WITH OGONEK AND MACRON|
|<a name="char-latin-small-letter-o-with-ogonek-and-macron"></a>ǭ|[U+01ED](https://www.compart.com/en/unicode/U+01ED)|LATIN SMALL LETTER O WITH OGONEK AND MACRON|
|<a name="char-latin-capital-letter-p-with-acute"></a>Ṕ|[U+1E54](https://www.compart.com/en/unicode/U+1E54)|LATIN CAPITAL LETTER P WITH ACUTE|
|<a name="char-latin-small-letter-p-with-acute"></a>ṕ|[U+1E55](https://www.compart.com/en/unicode/U+1E55)|LATIN SMALL LETTER P WITH ACUTE|
|<a name="char-latin-capital-letter-p-with-dot-above"></a>Ṗ|[U+1E56](https://www.compart.com/en/unicode/U+1E56)|LATIN CAPITAL LETTER P WITH DOT ABOVE|
|<a name="char-latin-small-letter-p-with-dot-above"></a>ṗ|[U+1E57](https://www.compart.com/en/unicode/U+1E57)|LATIN SMALL LETTER P WITH DOT ABOVE|
|<a name="char-latin-capital-letter-r-with-acute"></a>Ŕ|[U+0154](https://www.compart.com/en/unicode/U+0154)|LATIN CAPITAL LETTER R WITH ACUTE|
|<a name="char-latin-small-letter-r-with-acute"></a>ŕ|[U+0155](https://www.compart.com/en/unicode/U+0155)|LATIN SMALL LETTER R WITH ACUTE|
|<a name="char-latin-capital-letter-r-with-dot-above"></a>Ṙ|[U+1E58](https://www.compart.com/en/unicode/U+1E58)|LATIN CAPITAL LETTER R WITH DOT ABOVE|
|<a name="char-latin-small-letter-r-with-dot-above"></a>ṙ|[U+1E59](https://www.compart.com/en/unicode/U+1E59)|LATIN SMALL LETTER R WITH DOT ABOVE|
|<a name="char-latin-capital-letter-r-with-caron"></a>Ř|[U+0158](https://www.compart.com/en/unicode/U+0158)|LATIN CAPITAL LETTER R WITH CARON|
|<a name="char-latin-small-letter-r-with-caron"></a>ř|[U+0159](https://www.compart.com/en/unicode/U+0159)|LATIN SMALL LETTER R WITH CARON|
|<a name="char-latin-capital-letter-r-with-double-grave"></a>Ȑ|[U+0210](https://www.compart.com/en/unicode/U+0210)|LATIN CAPITAL LETTER R WITH DOUBLE GRAVE|
|<a name="char-latin-small-letter-r-with-double-grave"></a>ȑ|[U+0211](https://www.compart.com/en/unicode/U+0211)|LATIN SMALL LETTER R WITH DOUBLE GRAVE|
|<a name="char-latin-capital-letter-r-with-inverted-breve"></a>Ȓ|[U+0212](https://www.compart.com/en/unicode/U+0212)|LATIN CAPITAL LETTER R WITH INVERTED BREVE|
|<a name="char-latin-small-letter-r-with-inverted-breve"></a>ȓ|[U+0213](https://www.compart.com/en/unicode/U+0213)|LATIN SMALL LETTER R WITH INVERTED BREVE|
|<a name="char-latin-capital-letter-r-with-dot-below"></a>Ṛ|[U+1E5A](https://www.compart.com/en/unicode/U+1E5A)|LATIN CAPITAL LETTER R WITH DOT BELOW|
|<a name="char-latin-small-letter-r-with-dot-below"></a>ṛ|[U+1E5B](https://www.compart.com/en/unicode/U+1E5B)|LATIN SMALL LETTER R WITH DOT BELOW|
|<a name="char-latin-capital-letter-r-with-dot-below-and-macron"></a>Ṝ|[U+1E5C](https://www.compart.com/en/unicode/U+1E5C)|LATIN CAPITAL LETTER R WITH DOT BELOW AND MACRON|
|<a name="char-latin-small-letter-r-with-dot-below-and-macron"></a>ṝ|[U+1E5D](https://www.compart.com/en/unicode/U+1E5D)|LATIN SMALL LETTER R WITH DOT BELOW AND MACRON|
|<a name="char-latin-capital-letter-r-with-cedilla"></a>Ŗ|[U+0156](https://www.compart.com/en/unicode/U+0156)|LATIN CAPITAL LETTER R WITH CEDILLA|
|<a name="char-latin-small-letter-r-with-cedilla"></a>ŗ|[U+0157](https://www.compart.com/en/unicode/U+0157)|LATIN SMALL LETTER R WITH CEDILLA|
|<a name="char-latin-capital-letter-r-with-line-below"></a>Ṟ|[U+1E5E](https://www.compart.com/en/unicode/U+1E5E)|LATIN CAPITAL LETTER R WITH LINE BELOW|
|<a name="char-latin-small-letter-r-with-line-below"></a>ṟ|[U+1E5F](https://www.compart.com/en/unicode/U+1E5F)|LATIN SMALL LETTER R WITH LINE BELOW|
|<a name="char-latin-capital-letter-s-with-acute"></a>Ś|[U+015A](https://www.compart.com/en/unicode/U+015A)|LATIN CAPITAL LETTER S WITH ACUTE|
|<a name="char-latin-small-letter-s-with-acute"></a>ś|[U+015B](https://www.compart.com/en/unicode/U+015B)|LATIN SMALL LETTER S WITH ACUTE|
|<a name="char-latin-capital-letter-s-with-acute-and-dot-above"></a>Ṥ|[U+1E64](https://www.compart.com/en/unicode/U+1E64)|LATIN CAPITAL LETTER S WITH ACUTE AND DOT ABOVE|
|<a name="char-latin-small-letter-s-with-acute-and-dot-above"></a>ṥ|[U+1E65](https://www.compart.com/en/unicode/U+1E65)|LATIN SMALL LETTER S WITH ACUTE AND DOT ABOVE|
|<a name="char-latin-capital-letter-s-with-circumflex"></a>Ŝ|[U+015C](https://www.compart.com/en/unicode/U+015C)|LATIN CAPITAL LETTER S WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-s-with-circumflex"></a>ŝ|[U+015D](https://www.compart.com/en/unicode/U+015D)|LATIN SMALL LETTER S WITH CIRCUMFLEX|
|<a name="char-latin-capital-letter-s-with-dot-above"></a>Ṡ|[U+1E60](https://www.compart.com/en/unicode/U+1E60)|LATIN CAPITAL LETTER S WITH DOT ABOVE|
|<a name="char-latin-small-letter-s-with-dot-above"></a>ṡ|[U+1E61](https://www.compart.com/en/unicode/U+1E61)|LATIN SMALL LETTER S WITH DOT ABOVE|
|<a name="char-latin-capital-letter-s-with-caron"></a>Š|[U+0160](https://www.compart.com/en/unicode/U+0160)|LATIN CAPITAL LETTER S WITH CARON|
|<a name="char-latin-small-letter-s-with-caron"></a>š|[U+0161](https://www.compart.com/en/unicode/U+0161)|LATIN SMALL LETTER S WITH CARON|
|<a name="char-latin-capital-letter-s-with-caron-and-dot-above"></a>Ṧ|[U+1E66](https://www.compart.com/en/unicode/U+1E66)|LATIN CAPITAL LETTER S WITH CARON AND DOT ABOVE|
|<a name="char-latin-small-letter-s-with-caron-and-dot-above"></a>ṧ|[U+1E67](https://www.compart.com/en/unicode/U+1E67)|LATIN SMALL LETTER S WITH CARON AND DOT ABOVE|
|<a name="char-latin-capital-letter-s-with-dot-below"></a>Ṣ|[U+1E62](https://www.compart.com/en/unicode/U+1E62)|LATIN CAPITAL LETTER S WITH DOT BELOW|
|<a name="char-latin-small-letter-s-with-dot-below"></a>ṣ|[U+1E63](https://www.compart.com/en/unicode/U+1E63)|LATIN SMALL LETTER S WITH DOT BELOW|
|<a name="char-latin-capital-letter-s-with-dot-below-and-dot-above"></a>Ṩ|[U+1E68](https://www.compart.com/en/unicode/U+1E68)|LATIN CAPITAL LETTER S WITH DOT BELOW AND DOT ABOVE|
|<a name="char-latin-small-letter-s-with-dot-below-and-dot-above"></a>ṩ|[U+1E69](https://www.compart.com/en/unicode/U+1E69)|LATIN SMALL LETTER S WITH DOT BELOW AND DOT ABOVE|
|<a name="char-latin-capital-letter-s-with-comma-below"></a>Ș|[U+0218](https://www.compart.com/en/unicode/U+0218)|LATIN CAPITAL LETTER S WITH COMMA BELOW|
|<a name="char-latin-capital-letter-s-with-comma-below"></a>Ș|[U+0218](https://www.compart.com/en/unicode/U+0218)|LATIN CAPITAL LETTER S WITH COMMA BELOW|
|<a name="char-latin-small-letter-s-with-comma-below"></a>ș|[U+0219](https://www.compart.com/en/unicode/U+0219)|LATIN SMALL LETTER S WITH COMMA BELOW|
|<a name="char-latin-small-letter-s-with-comma-below"></a>ș|[U+0219](https://www.compart.com/en/unicode/U+0219)|LATIN SMALL LETTER S WITH COMMA BELOW|
|<a name="char-latin-capital-letter-s-with-cedilla"></a>Ş|[U+015E](https://www.compart.com/en/unicode/U+015E)|LATIN CAPITAL LETTER S WITH CEDILLA|
|<a name="char-latin-small-letter-s-with-cedilla"></a>ş|[U+015F](https://www.compart.com/en/unicode/U+015F)|LATIN SMALL LETTER S WITH CEDILLA|
|<a name="char-latin-capital-letter-t-with-dot-above"></a>Ṫ|[U+1E6A](https://www.compart.com/en/unicode/U+1E6A)|LATIN CAPITAL LETTER T WITH DOT ABOVE|
|<a name="char-latin-small-letter-t-with-dot-above"></a>ṫ|[U+1E6B](https://www.compart.com/en/unicode/U+1E6B)|LATIN SMALL LETTER T WITH DOT ABOVE|
|<a name="char-latin-small-letter-t-with-diaeresis"></a>ẗ|[U+1E97](https://www.compart.com/en/unicode/U+1E97)|LATIN SMALL LETTER T WITH DIAERESIS|
|<a name="char-latin-capital-letter-t-with-caron"></a>Ť|[U+0164](https://www.compart.com/en/unicode/U+0164)|LATIN CAPITAL LETTER T WITH CARON|
|<a name="char-latin-small-letter-t-with-caron"></a>ť|[U+0165](https://www.compart.com/en/unicode/U+0165)|LATIN SMALL LETTER T WITH CARON|
|<a name="char-latin-capital-letter-t-with-dot-below"></a>Ṭ|[U+1E6C](https://www.compart.com/en/unicode/U+1E6C)|LATIN CAPITAL LETTER T WITH DOT BELOW|
|<a name="char-latin-small-letter-t-with-dot-below"></a>ṭ|[U+1E6D](https://www.compart.com/en/unicode/U+1E6D)|LATIN SMALL LETTER T WITH DOT BELOW|
|<a name="char-latin-capital-letter-t-with-comma-below"></a>Ț|[U+021A](https://www.compart.com/en/unicode/U+021A)|LATIN CAPITAL LETTER T WITH COMMA BELOW|
|<a name="char-latin-small-letter-t-with-comma-below"></a>ț|[U+021B](https://www.compart.com/en/unicode/U+021B)|LATIN SMALL LETTER T WITH COMMA BELOW|
|<a name="char-latin-capital-letter-t-with-cedilla"></a>Ţ|[U+0162](https://www.compart.com/en/unicode/U+0162)|LATIN CAPITAL LETTER T WITH CEDILLA|
|<a name="char-latin-small-letter-t-with-cedilla"></a>ţ|[U+0163](https://www.compart.com/en/unicode/U+0163)|LATIN SMALL LETTER T WITH CEDILLA|
|<a name="char-latin-capital-letter-t-with-circumflex-below"></a>Ṱ|[U+1E70](https://www.compart.com/en/unicode/U+1E70)|LATIN CAPITAL LETTER T WITH CIRCUMFLEX BELOW|
|<a name="char-latin-small-letter-t-with-circumflex-below"></a>ṱ|[U+1E71](https://www.compart.com/en/unicode/U+1E71)|LATIN SMALL LETTER T WITH CIRCUMFLEX BELOW|
|<a name="char-latin-capital-letter-t-with-line-below"></a>Ṯ|[U+1E6E](https://www.compart.com/en/unicode/U+1E6E)|LATIN CAPITAL LETTER T WITH LINE BELOW|
|<a name="char-latin-small-letter-t-with-line-below"></a>ṯ|[U+1E6F](https://www.compart.com/en/unicode/U+1E6F)|LATIN SMALL LETTER T WITH LINE BELOW|
|<a name="char-latin-capital-letter-u-with-grave"></a>Ù|[U+00D9](https://www.compart.com/en/unicode/U+00D9)|LATIN CAPITAL LETTER U WITH GRAVE|
|<a name="char-latin-small-letter-u-with-grave"></a>ù|[U+00F9](https://www.compart.com/en/unicode/U+00F9)|LATIN SMALL LETTER U WITH GRAVE|
|<a name="char-latin-capital-letter-u-with-acute"></a>Ú|[U+00DA](https://www.compart.com/en/unicode/U+00DA)|LATIN CAPITAL LETTER U WITH ACUTE|
|<a name="char-latin-small-letter-u-with-acute"></a>ú|[U+00FA](https://www.compart.com/en/unicode/U+00FA)|LATIN SMALL LETTER U WITH ACUTE|
|<a name="char-latin-capital-letter-u-with-circumflex"></a>Û|[U+00DB](https://www.compart.com/en/unicode/U+00DB)|LATIN CAPITAL LETTER U WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-u-with-circumflex"></a>û|[U+00FB](https://www.compart.com/en/unicode/U+00FB)|LATIN SMALL LETTER U WITH CIRCUMFLEX|
|<a name="char-latin-capital-letter-u-with-tilde"></a>Ũ|[U+0168](https://www.compart.com/en/unicode/U+0168)|LATIN CAPITAL LETTER U WITH TILDE|
|<a name="char-latin-small-letter-u-with-tilde"></a>ũ|[U+0169](https://www.compart.com/en/unicode/U+0169)|LATIN SMALL LETTER U WITH TILDE|
|<a name="char-latin-capital-letter-u-with-tilde-and-acute"></a>Ṹ|[U+1E78](https://www.compart.com/en/unicode/U+1E78)|LATIN CAPITAL LETTER U WITH TILDE AND ACUTE|
|<a name="char-latin-small-letter-u-with-tilde-and-acute"></a>ṹ|[U+1E79](https://www.compart.com/en/unicode/U+1E79)|LATIN SMALL LETTER U WITH TILDE AND ACUTE|
|<a name="char-latin-capital-letter-u-with-macron"></a>Ū|[U+016A](https://www.compart.com/en/unicode/U+016A)|LATIN CAPITAL LETTER U WITH MACRON|
|<a name="char-latin-small-letter-u-with-macron"></a>ū|[U+016B](https://www.compart.com/en/unicode/U+016B)|LATIN SMALL LETTER U WITH MACRON|
|<a name="char-latin-capital-letter-u-with-macron-and-diaeresis"></a>Ṻ|[U+1E7A](https://www.compart.com/en/unicode/U+1E7A)|LATIN CAPITAL LETTER U WITH MACRON AND DIAERESIS|
|<a name="char-latin-small-letter-u-with-macron-and-diaeresis"></a>ṻ|[U+1E7B](https://www.compart.com/en/unicode/U+1E7B)|LATIN SMALL LETTER U WITH MACRON AND DIAERESIS|
|<a name="char-latin-capital-letter-u-with-breve"></a>Ŭ|[U+016C](https://www.compart.com/en/unicode/U+016C)|LATIN CAPITAL LETTER U WITH BREVE|
|<a name="char-latin-small-letter-u-with-breve"></a>ŭ|[U+016D](https://www.compart.com/en/unicode/U+016D)|LATIN SMALL LETTER U WITH BREVE|
|<a name="char-latin-capital-letter-u-with-diaeresis"></a>Ü|[U+00DC](https://www.compart.com/en/unicode/U+00DC)|LATIN CAPITAL LETTER U WITH DIAERESIS|
|<a name="char-latin-small-letter-u-with-diaeresis"></a>ü|[U+00FC](https://www.compart.com/en/unicode/U+00FC)|LATIN SMALL LETTER U WITH DIAERESIS|
|<a name="char-latin-capital-letter-u-with-diaeresis-and-grave"></a>Ǜ|[U+01DB](https://www.compart.com/en/unicode/U+01DB)|LATIN CAPITAL LETTER U WITH DIAERESIS AND GRAVE|
|<a name="char-latin-small-letter-u-with-diaeresis-and-grave"></a>ǜ|[U+01DC](https://www.compart.com/en/unicode/U+01DC)|LATIN SMALL LETTER U WITH DIAERESIS AND GRAVE|
|<a name="char-latin-capital-letter-u-with-diaeresis-and-acute"></a>Ǘ|[U+01D7](https://www.compart.com/en/unicode/U+01D7)|LATIN CAPITAL LETTER U WITH DIAERESIS AND ACUTE|
|<a name="char-latin-small-letter-u-with-diaeresis-and-acute"></a>ǘ|[U+01D8](https://www.compart.com/en/unicode/U+01D8)|LATIN SMALL LETTER U WITH DIAERESIS AND ACUTE|
|<a name="char-latin-capital-letter-u-with-diaeresis-and-macron"></a>Ǖ|[U+01D5](https://www.compart.com/en/unicode/U+01D5)|LATIN CAPITAL LETTER U WITH DIAERESIS AND MACRON|
|<a name="char-latin-small-letter-u-with-diaeresis-and-macron"></a>ǖ|[U+01D6](https://www.compart.com/en/unicode/U+01D6)|LATIN SMALL LETTER U WITH DIAERESIS AND MACRON|
|<a name="char-latin-capital-letter-u-with-diaeresis-and-caron"></a>Ǚ|[U+01D9](https://www.compart.com/en/unicode/U+01D9)|LATIN CAPITAL LETTER U WITH DIAERESIS AND CARON|
|<a name="char-latin-small-letter-u-with-diaeresis-and-caron"></a>ǚ|[U+01DA](https://www.compart.com/en/unicode/U+01DA)|LATIN SMALL LETTER U WITH DIAERESIS AND CARON|
|<a name="char-latin-capital-letter-u-with-hook-above"></a>Ủ|[U+1EE6](https://www.compart.com/en/unicode/U+1EE6)|LATIN CAPITAL LETTER U WITH HOOK ABOVE|
|<a name="char-latin-small-letter-u-with-hook-above"></a>ủ|[U+1EE7](https://www.compart.com/en/unicode/U+1EE7)|LATIN SMALL LETTER U WITH HOOK ABOVE|
|<a name="char-latin-capital-letter-u-with-ring-above"></a>Ů|[U+016E](https://www.compart.com/en/unicode/U+016E)|LATIN CAPITAL LETTER U WITH RING ABOVE|
|<a name="char-latin-small-letter-u-with-ring-above"></a>ů|[U+016F](https://www.compart.com/en/unicode/U+016F)|LATIN SMALL LETTER U WITH RING ABOVE|
|<a name="char-latin-capital-letter-u-with-double-acute"></a>Ű|[U+0170](https://www.compart.com/en/unicode/U+0170)|LATIN CAPITAL LETTER U WITH DOUBLE ACUTE|
|<a name="char-latin-small-letter-u-with-double-acute"></a>ű|[U+0171](https://www.compart.com/en/unicode/U+0171)|LATIN SMALL LETTER U WITH DOUBLE ACUTE|
|<a name="char-latin-capital-letter-u-with-caron"></a>Ǔ|[U+01D3](https://www.compart.com/en/unicode/U+01D3)|LATIN CAPITAL LETTER U WITH CARON|
|<a name="char-latin-small-letter-u-with-caron"></a>ǔ|[U+01D4](https://www.compart.com/en/unicode/U+01D4)|LATIN SMALL LETTER U WITH CARON|
|<a name="char-latin-capital-letter-u-with-double-grave"></a>Ȕ|[U+0214](https://www.compart.com/en/unicode/U+0214)|LATIN CAPITAL LETTER U WITH DOUBLE GRAVE|
|<a name="char-latin-small-letter-u-with-double-grave"></a>ȕ|[U+0215](https://www.compart.com/en/unicode/U+0215)|LATIN SMALL LETTER U WITH DOUBLE GRAVE|
|<a name="char-latin-capital-letter-u-with-inverted-breve"></a>Ȗ|[U+0216](https://www.compart.com/en/unicode/U+0216)|LATIN CAPITAL LETTER U WITH INVERTED BREVE|
|<a name="char-latin-small-letter-u-with-inverted-breve"></a>ȗ|[U+0217](https://www.compart.com/en/unicode/U+0217)|LATIN SMALL LETTER U WITH INVERTED BREVE|
|<a name="char-latin-capital-letter-u-with-horn"></a>Ư|[U+01AF](https://www.compart.com/en/unicode/U+01AF)|LATIN CAPITAL LETTER U WITH HORN|
|<a name="char-latin-small-letter-u-with-horn"></a>ư|[U+01B0](https://www.compart.com/en/unicode/U+01B0)|LATIN SMALL LETTER U WITH HORN|
|<a name="char-latin-capital-letter-u-with-horn-and-grave"></a>Ừ|[U+1EEA](https://www.compart.com/en/unicode/U+1EEA)|LATIN CAPITAL LETTER U WITH HORN AND GRAVE|
|<a name="char-latin-small-letter-u-with-horn-and-grave"></a>ừ|[U+1EEB](https://www.compart.com/en/unicode/U+1EEB)|LATIN SMALL LETTER U WITH HORN AND GRAVE|
|<a name="char-latin-capital-letter-u-with-horn-and-acute"></a>Ứ|[U+1EE8](https://www.compart.com/en/unicode/U+1EE8)|LATIN CAPITAL LETTER U WITH HORN AND ACUTE|
|<a name="char-latin-small-letter-u-with-horn-and-acute"></a>ứ|[U+1EE9](https://www.compart.com/en/unicode/U+1EE9)|LATIN SMALL LETTER U WITH HORN AND ACUTE|
|<a name="char-latin-capital-letter-u-with-horn-and-tilde"></a>Ữ|[U+1EEE](https://www.compart.com/en/unicode/U+1EEE)|LATIN CAPITAL LETTER U WITH HORN AND TILDE|
|<a name="char-latin-small-letter-u-with-horn-and-tilde"></a>ữ|[U+1EEF](https://www.compart.com/en/unicode/U+1EEF)|LATIN SMALL LETTER U WITH HORN AND TILDE|
|<a name="char-latin-capital-letter-u-with-horn-and-hook-above"></a>Ử|[U+1EEC](https://www.compart.com/en/unicode/U+1EEC)|LATIN CAPITAL LETTER U WITH HORN AND HOOK ABOVE|
|<a name="char-latin-small-letter-u-with-horn-and-hook-above"></a>ử|[U+1EED](https://www.compart.com/en/unicode/U+1EED)|LATIN SMALL LETTER U WITH HORN AND HOOK ABOVE|
|<a name="char-latin-capital-letter-u-with-horn-and-dot-below"></a>Ự|[U+1EF0](https://www.compart.com/en/unicode/U+1EF0)|LATIN CAPITAL LETTER U WITH HORN AND DOT BELOW|
|<a name="char-latin-small-letter-u-with-horn-and-dot-below"></a>ự|[U+1EF1](https://www.compart.com/en/unicode/U+1EF1)|LATIN SMALL LETTER U WITH HORN AND DOT BELOW|
|<a name="char-latin-capital-letter-u-with-dot-below"></a>Ụ|[U+1EE4](https://www.compart.com/en/unicode/U+1EE4)|LATIN CAPITAL LETTER U WITH DOT BELOW|
|<a name="char-latin-small-letter-u-with-dot-below"></a>ụ|[U+1EE5](https://www.compart.com/en/unicode/U+1EE5)|LATIN SMALL LETTER U WITH DOT BELOW|
|<a name="char-latin-capital-letter-u-with-diaeresis-below"></a>Ṳ|[U+1E72](https://www.compart.com/en/unicode/U+1E72)|LATIN CAPITAL LETTER U WITH DIAERESIS BELOW|
|<a name="char-latin-small-letter-u-with-diaeresis-below"></a>ṳ|[U+1E73](https://www.compart.com/en/unicode/U+1E73)|LATIN SMALL LETTER U WITH DIAERESIS BELOW|
|<a name="char-latin-capital-letter-u-with-ogonek"></a>Ų|[U+0172](https://www.compart.com/en/unicode/U+0172)|LATIN CAPITAL LETTER U WITH OGONEK|
|<a name="char-latin-small-letter-u-with-ogonek"></a>ų|[U+0173](https://www.compart.com/en/unicode/U+0173)|LATIN SMALL LETTER U WITH OGONEK|
|<a name="char-latin-capital-letter-u-with-circumflex-below"></a>Ṷ|[U+1E76](https://www.compart.com/en/unicode/U+1E76)|LATIN CAPITAL LETTER U WITH CIRCUMFLEX BELOW|
|<a name="char-latin-small-letter-u-with-circumflex-below"></a>ṷ|[U+1E77](https://www.compart.com/en/unicode/U+1E77)|LATIN SMALL LETTER U WITH CIRCUMFLEX BELOW|
|<a name="char-latin-capital-letter-u-with-tilde-below"></a>Ṵ|[U+1E74](https://www.compart.com/en/unicode/U+1E74)|LATIN CAPITAL LETTER U WITH TILDE BELOW|
|<a name="char-latin-small-letter-u-with-tilde-below"></a>ṵ|[U+1E75](https://www.compart.com/en/unicode/U+1E75)|LATIN SMALL LETTER U WITH TILDE BELOW|
|<a name="char-latin-capital-letter-v-with-tilde"></a>Ṽ|[U+1E7C](https://www.compart.com/en/unicode/U+1E7C)|LATIN CAPITAL LETTER V WITH TILDE|
|<a name="char-latin-small-letter-v-with-tilde"></a>ṽ|[U+1E7D](https://www.compart.com/en/unicode/U+1E7D)|LATIN SMALL LETTER V WITH TILDE|
|<a name="char-latin-capital-letter-v-with-dot-below"></a>Ṿ|[U+1E7E](https://www.compart.com/en/unicode/U+1E7E)|LATIN CAPITAL LETTER V WITH DOT BELOW|
|<a name="char-latin-small-letter-v-with-dot-below"></a>ṿ|[U+1E7F](https://www.compart.com/en/unicode/U+1E7F)|LATIN SMALL LETTER V WITH DOT BELOW|
|<a name="char-latin-capital-letter-w"></a>W|[U+0057](https://www.compart.com/en/unicode/U+0057)|LATIN CAPITAL LETTER W|
|<a name="char-latin-small-letter-w"></a>w|[U+0077](https://www.compart.com/en/unicode/U+0077)|LATIN SMALL LETTER W|
|<a name="char-latin-capital-letter-w-with-grave"></a>Ẁ|[U+1E80](https://www.compart.com/en/unicode/U+1E80)|LATIN CAPITAL LETTER W WITH GRAVE|
|<a name="char-latin-small-letter-w-with-grave"></a>ẁ|[U+1E81](https://www.compart.com/en/unicode/U+1E81)|LATIN SMALL LETTER W WITH GRAVE|
|<a name="char-latin-capital-letter-w-with-acute"></a>Ẃ|[U+1E82](https://www.compart.com/en/unicode/U+1E82)|LATIN CAPITAL LETTER W WITH ACUTE|
|<a name="char-latin-small-letter-w-with-acute"></a>ẃ|[U+1E83](https://www.compart.com/en/unicode/U+1E83)|LATIN SMALL LETTER W WITH ACUTE|
|<a name="char-latin-capital-letter-w-with-circumflex"></a>Ŵ|[U+0174](https://www.compart.com/en/unicode/U+0174)|LATIN CAPITAL LETTER W WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-w-with-circumflex"></a>ŵ|[U+0175](https://www.compart.com/en/unicode/U+0175)|LATIN SMALL LETTER W WITH CIRCUMFLEX|
|<a name="char-latin-capital-letter-w-with-dot-above"></a>Ẇ|[U+1E86](https://www.compart.com/en/unicode/U+1E86)|LATIN CAPITAL LETTER W WITH DOT ABOVE|
|<a name="char-latin-small-letter-w-with-dot-above"></a>ẇ|[U+1E87](https://www.compart.com/en/unicode/U+1E87)|LATIN SMALL LETTER W WITH DOT ABOVE|
|<a name="char-latin-capital-letter-w-with-diaeresis"></a>Ẅ|[U+1E84](https://www.compart.com/en/unicode/U+1E84)|LATIN CAPITAL LETTER W WITH DIAERESIS|
|<a name="char-latin-small-letter-w-with-diaeresis"></a>ẅ|[U+1E85](https://www.compart.com/en/unicode/U+1E85)|LATIN SMALL LETTER W WITH DIAERESIS|
|<a name="char-latin-small-letter-w-with-ring-above"></a>ẘ|[U+1E98](https://www.compart.com/en/unicode/U+1E98)|LATIN SMALL LETTER W WITH RING ABOVE|
|<a name="char-latin-capital-letter-w-with-dot-below"></a>Ẉ|[U+1E88](https://www.compart.com/en/unicode/U+1E88)|LATIN CAPITAL LETTER W WITH DOT BELOW|
|<a name="char-latin-small-letter-w-with-dot-below"></a>ẉ|[U+1E89](https://www.compart.com/en/unicode/U+1E89)|LATIN SMALL LETTER W WITH DOT BELOW|
|<a name="char-latin-capital-letter-x-with-dot-above"></a>Ẋ|[U+1E8A](https://www.compart.com/en/unicode/U+1E8A)|LATIN CAPITAL LETTER X WITH DOT ABOVE|
|<a name="char-latin-small-letter-x-with-dot-above"></a>ẋ|[U+1E8B](https://www.compart.com/en/unicode/U+1E8B)|LATIN SMALL LETTER X WITH DOT ABOVE|
|<a name="char-latin-capital-letter-x-with-diaeresis"></a>Ẍ|[U+1E8C](https://www.compart.com/en/unicode/U+1E8C)|LATIN CAPITAL LETTER X WITH DIAERESIS|
|<a name="char-latin-small-letter-x-with-diaeresis"></a>ẍ|[U+1E8D](https://www.compart.com/en/unicode/U+1E8D)|LATIN SMALL LETTER X WITH DIAERESIS|
|<a name="char-latin-capital-letter-y-with-grave"></a>Ỳ|[U+1EF2](https://www.compart.com/en/unicode/U+1EF2)|LATIN CAPITAL LETTER Y WITH GRAVE|
|<a name="char-latin-small-letter-y-with-grave"></a>ỳ|[U+1EF3](https://www.compart.com/en/unicode/U+1EF3)|LATIN SMALL LETTER Y WITH GRAVE|
|<a name="char-latin-capital-letter-y-with-acute"></a>Ý|[U+00DD](https://www.compart.com/en/unicode/U+00DD)|LATIN CAPITAL LETTER Y WITH ACUTE|
|<a name="char-latin-small-letter-y-with-acute"></a>ý|[U+00FD](https://www.compart.com/en/unicode/U+00FD)|LATIN SMALL LETTER Y WITH ACUTE|
|<a name="char-latin-capital-letter-y-with-circumflex"></a>Ŷ|[U+0176](https://www.compart.com/en/unicode/U+0176)|LATIN CAPITAL LETTER Y WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-y-with-circumflex"></a>ŷ|[U+0177](https://www.compart.com/en/unicode/U+0177)|LATIN SMALL LETTER Y WITH CIRCUMFLEX|
|<a name="char-latin-capital-letter-y-with-tilde"></a>Ỹ|[U+1EF8](https://www.compart.com/en/unicode/U+1EF8)|LATIN CAPITAL LETTER Y WITH TILDE|
|<a name="char-latin-small-letter-y-with-tilde"></a>ỹ|[U+1EF9](https://www.compart.com/en/unicode/U+1EF9)|LATIN SMALL LETTER Y WITH TILDE|
|<a name="char-latin-capital-letter-y-with-macron"></a>Ȳ|[U+0232](https://www.compart.com/en/unicode/U+0232)|LATIN CAPITAL LETTER Y WITH MACRON|
|<a name="char-latin-small-letter-y-with-macron"></a>ȳ|[U+0233](https://www.compart.com/en/unicode/U+0233)|LATIN SMALL LETTER Y WITH MACRON|
|<a name="char-latin-capital-letter-y-with-dot-above"></a>Ẏ|[U+1E8E](https://www.compart.com/en/unicode/U+1E8E)|LATIN CAPITAL LETTER Y WITH DOT ABOVE|
|<a name="char-latin-small-letter-y-with-dot-above"></a>ẏ|[U+1E8F](https://www.compart.com/en/unicode/U+1E8F)|LATIN SMALL LETTER Y WITH DOT ABOVE|
|<a name="char-latin-capital-letter-y-with-diaeresis"></a>Ÿ|[U+0178](https://www.compart.com/en/unicode/U+0178)|LATIN CAPITAL LETTER Y WITH DIAERESIS|
|<a name="char-latin-small-letter-y-with-diaeresis"></a>ÿ|[U+00FF](https://www.compart.com/en/unicode/U+00FF)|LATIN SMALL LETTER Y WITH DIAERESIS|
|<a name="char-latin-capital-letter-y-with-hook-above"></a>Ỷ|[U+1EF6](https://www.compart.com/en/unicode/U+1EF6)|LATIN CAPITAL LETTER Y WITH HOOK ABOVE|
|<a name="char-latin-small-letter-y-with-hook-above"></a>ỷ|[U+1EF7](https://www.compart.com/en/unicode/U+1EF7)|LATIN SMALL LETTER Y WITH HOOK ABOVE|
|<a name="char-latin-small-letter-y-with-ring-above"></a>ẙ|[U+1E99](https://www.compart.com/en/unicode/U+1E99)|LATIN SMALL LETTER Y WITH RING ABOVE|
|<a name="char-latin-capital-letter-y-with-dot-below"></a>Ỵ|[U+1EF4](https://www.compart.com/en/unicode/U+1EF4)|LATIN CAPITAL LETTER Y WITH DOT BELOW|
|<a name="char-latin-small-letter-y-with-dot-below"></a>ỵ|[U+1EF5](https://www.compart.com/en/unicode/U+1EF5)|LATIN SMALL LETTER Y WITH DOT BELOW|
|<a name="char-latin-capital-letter-z-with-acute"></a>Ź|[U+0179](https://www.compart.com/en/unicode/U+0179)|LATIN CAPITAL LETTER Z WITH ACUTE|
|<a name="char-latin-small-letter-z-with-acute"></a>ź|[U+017A](https://www.compart.com/en/unicode/U+017A)|LATIN SMALL LETTER Z WITH ACUTE|
|<a name="char-latin-capital-letter-z-with-circumflex"></a>Ẑ|[U+1E90](https://www.compart.com/en/unicode/U+1E90)|LATIN CAPITAL LETTER Z WITH CIRCUMFLEX|
|<a name="char-latin-small-letter-z-with-circumflex"></a>ẑ|[U+1E91](https://www.compart.com/en/unicode/U+1E91)|LATIN SMALL LETTER Z WITH CIRCUMFLEX|
|<a name="char-latin-capital-letter-z-with-dot-above"></a>Ż|[U+017B](https://www.compart.com/en/unicode/U+017B)|LATIN CAPITAL LETTER Z WITH DOT ABOVE|
|<a name="char-latin-small-letter-z-with-dot-above"></a>ż|[U+017C](https://www.compart.com/en/unicode/U+017C)|LATIN SMALL LETTER Z WITH DOT ABOVE|
|<a name="char-latin-capital-letter-z-with-caron"></a>Ž|[U+017D](https://www.compart.com/en/unicode/U+017D)|LATIN CAPITAL LETTER Z WITH CARON|
|<a name="char-latin-small-letter-z-with-caron"></a>ž|[U+017E](https://www.compart.com/en/unicode/U+017E)|LATIN SMALL LETTER Z WITH CARON|
|<a name="char-latin-capital-letter-z-with-dot-below"></a>Ẓ|[U+1E92](https://www.compart.com/en/unicode/U+1E92)|LATIN CAPITAL LETTER Z WITH DOT BELOW|
|<a name="char-latin-small-letter-z-with-dot-below"></a>ẓ|[U+1E93](https://www.compart.com/en/unicode/U+1E93)|LATIN SMALL LETTER Z WITH DOT BELOW|
|<a name="char-latin-capital-letter-z-with-line-below"></a>Ẕ|[U+1E94](https://www.compart.com/en/unicode/U+1E94)|LATIN CAPITAL LETTER Z WITH LINE BELOW|
|<a name="char-latin-small-letter-z-with-line-below"></a>ẕ|[U+1E95](https://www.compart.com/en/unicode/U+1E95)|LATIN SMALL LETTER Z WITH LINE BELOW|
|<a name="char-latin-capital-letter-sharp-s"></a>ẞ|[U+1E9E](https://www.compart.com/en/unicode/U+1E9E)|LATIN CAPITAL LETTER SHARP S|
|<a name="char-latin-small-letter-sharp-s"></a>ß|[U+00DF](https://www.compart.com/en/unicode/U+00DF)|LATIN SMALL LETTER SHARP S|
|<a name="char-latin-capital-letter-ae"></a>Æ|[U+00C6](https://www.compart.com/en/unicode/U+00C6)|LATIN CAPITAL LETTER AE|
|<a name="char-latin-small-letter-ae"></a>æ|[U+00E6](https://www.compart.com/en/unicode/U+00E6)|LATIN SMALL LETTER AE|
|<a name="char-latin-capital-letter-ae-with-acute"></a>Ǽ|[U+01FC](https://www.compart.com/en/unicode/U+01FC)|LATIN CAPITAL LETTER AE WITH ACUTE|
|<a name="char-latin-small-letter-ae-with-acute"></a>ǽ|[U+01FD](https://www.compart.com/en/unicode/U+01FD)|LATIN SMALL LETTER AE WITH ACUTE|
|<a name="char-latin-capital-letter-ae-with-macron"></a>Ǣ|[U+01E2](https://www.compart.com/en/unicode/U+01E2)|LATIN CAPITAL LETTER AE WITH MACRON|
|<a name="char-latin-small-letter-ae-with-macron"></a>ǣ|[U+01E3](https://www.compart.com/en/unicode/U+01E3)|LATIN SMALL LETTER AE WITH MACRON|
|<a name="char-latin-capital-letter-o-with-stroke"></a>Ø|[U+00D8](https://www.compart.com/en/unicode/U+00D8)|LATIN CAPITAL LETTER O WITH STROKE|
|<a name="char-latin-small-letter-o-with-stroke"></a>ø|[U+00F8](https://www.compart.com/en/unicode/U+00F8)|LATIN SMALL LETTER O WITH STROKE|
|<a name="char-latin-capital-letter-o-with-stroke-and-acute"></a>Ǿ|[U+01FE](https://www.compart.com/en/unicode/U+01FE)|LATIN CAPITAL LETTER O WITH STROKE AND ACUTE|
|<a name="char-latin-small-letter-o-with-stroke-and-acute"></a>ǿ|[U+01FF](https://www.compart.com/en/unicode/U+01FF)|LATIN SMALL LETTER O WITH STROKE AND ACUTE|
|<a name="char-latin-capital-letter-d-with-stroke"></a>Đ|[U+0110](https://www.compart.com/en/unicode/U+0110)|LATIN CAPITAL LETTER D WITH STROKE|
|<a name="char-latin-small-letter-d-with-stroke"></a>đ|[U+0111](https://www.compart.com/en/unicode/U+0111)|LATIN SMALL LETTER D WITH STROKE|
|<a name="char-latin-capital-letter-h-with-stroke"></a>Ħ|[U+0126](https://www.compart.com/en/unicode/U+0126)|LATIN CAPITAL LETTER H WITH STROKE|
|<a name="char-latin-small-letter-h-with-stroke"></a>ħ|[U+0127](https://www.compart.com/en/unicode/U+0127)|LATIN SMALL LETTER H WITH STROKE|
|<a name="char-latin-capital-letter-l-with-middle-dot"></a>Ŀ|[U+013F](https://www.compart.com/en/unicode/U+013F)|LATIN CAPITAL LETTER L WITH MIDDLE DOT|
|<a name="char-latin-small-letter-l-with-middle-dot"></a>ŀ|[U+0140](https://www.compart.com/en/unicode/U+0140)|LATIN SMALL LETTER L WITH MIDDLE DOT|
|<a name="char-latin-capital-letter-l-with-stroke"></a>Ł|[U+0141](https://www.compart.com/en/unicode/U+0141)|LATIN CAPITAL LETTER L WITH STROKE|
|<a name="char-latin-small-letter-l-with-stroke"></a>ł|[U+0142](https://www.compart.com/en/unicode/U+0142)|LATIN SMALL LETTER L WITH STROKE|
|<a name="char-latin-capital-ligature-oe"></a>Œ|[U+0152](https://www.compart.com/en/unicode/U+0152)|LATIN CAPITAL LIGATURE OE|
|<a name="char-latin-small-ligature-oe"></a>œ|[U+0153](https://www.compart.com/en/unicode/U+0153)|LATIN SMALL LIGATURE OE|
|<a name="char-latin-capital-letter-t-with-stroke"></a>Ŧ|[U+0166](https://www.compart.com/en/unicode/U+0166)|LATIN CAPITAL LETTER T WITH STROKE|
|<a name="char-latin-small-letter-t-with-stroke"></a>ŧ|[U+0167](https://www.compart.com/en/unicode/U+0167)|LATIN SMALL LETTER T WITH STROKE|
|<a name="char-latin-capital-letter-c-with-hook"></a>Ƈ|[U+0187](https://www.compart.com/en/unicode/U+0187)|LATIN CAPITAL LETTER C WITH HOOK|
|<a name="char-latin-small-letter-c-with-hook"></a>ƈ|[U+0188](https://www.compart.com/en/unicode/U+0188)|LATIN SMALL LETTER C WITH HOOK|
|<a name="char-latin-capital-letter-f-with-hook"></a>Ƒ|[U+0191](https://www.compart.com/en/unicode/U+0191)|LATIN CAPITAL LETTER F WITH HOOK|
|<a name="char-latin-small-letter-f-with-hook"></a>ƒ|[U+0192](https://www.compart.com/en/unicode/U+0192)|LATIN SMALL LETTER F WITH HOOK|
|<a name="char-latin-capital-letter-hwair"></a>Ƕ|[U+01F6](https://www.compart.com/en/unicode/U+01F6)|LATIN CAPITAL LETTER HWAIR|
|<a name="char-latin-small-letter-hv"></a>ƕ|[U+0195](https://www.compart.com/en/unicode/U+0195)|LATIN SMALL LETTER HV|
|<a name="char-latin-capital-letter-k-with-hook"></a>Ƙ|[U+0198](https://www.compart.com/en/unicode/U+0198)|LATIN CAPITAL LETTER K WITH HOOK|
|<a name="char-latin-small-letter-k-with-hook"></a>ƙ|[U+0199](https://www.compart.com/en/unicode/U+0199)|LATIN SMALL LETTER K WITH HOOK|
|<a name="char-latin-capital-letter-l-with-bar"></a>Ƚ|[U+023D](https://www.compart.com/en/unicode/U+023D)|LATIN CAPITAL LETTER L WITH BAR|
|<a name="char-latin-small-letter-l-with-bar"></a>ƚ|[U+019A](https://www.compart.com/en/unicode/U+019A)|LATIN SMALL LETTER L WITH BAR|
|<a name="char-latin-capital-letter-p-with-hook"></a>Ƥ|[U+01A4](https://www.compart.com/en/unicode/U+01A4)|LATIN CAPITAL LETTER P WITH HOOK|
|<a name="char-latin-small-letter-p-with-hook"></a>ƥ|[U+01A5](https://www.compart.com/en/unicode/U+01A5)|LATIN SMALL LETTER P WITH HOOK|
|<a name="char-latin-capital-letter-t-with-hook"></a>Ƭ|[U+01AC](https://www.compart.com/en/unicode/U+01AC)|LATIN CAPITAL LETTER T WITH HOOK|
|<a name="char-latin-small-letter-t-with-hook"></a>ƭ|[U+01AD](https://www.compart.com/en/unicode/U+01AD)|LATIN SMALL LETTER T WITH HOOK|
|<a name="char-latin-capital-letter-y-with-hook"></a>Ƴ|[U+01B3](https://www.compart.com/en/unicode/U+01B3)|LATIN CAPITAL LETTER Y WITH HOOK|
|<a name="char-latin-small-letter-y-with-hook"></a>ƴ|[U+01B4](https://www.compart.com/en/unicode/U+01B4)|LATIN SMALL LETTER Y WITH HOOK|
|<a name="char-latin-capital-letter-g-with-stroke"></a>Ǥ|[U+01E4](https://www.compart.com/en/unicode/U+01E4)|LATIN CAPITAL LETTER G WITH STROKE|
|<a name="char-latin-small-letter-g-with-stroke"></a>ǥ|[U+01E5](https://www.compart.com/en/unicode/U+01E5)|LATIN SMALL LETTER G WITH STROKE|
|<a name="char-latin-capital-letter-r-with-stroke"></a>Ɍ|[U+024C](https://www.compart.com/en/unicode/U+024C)|LATIN CAPITAL LETTER R WITH STROKE|
|<a name="char-latin-small-letter-r-with-stroke"></a>ɍ|[U+024D](https://www.compart.com/en/unicode/U+024D)|LATIN SMALL LETTER R WITH STROKE|
|<a name="char-latin-capital-letter-b-with-hook"></a>Ɓ|[U+0181](https://www.compart.com/en/unicode/U+0181)|LATIN CAPITAL LETTER B WITH HOOK|
|<a name="char-latin-small-letter-b-with-hook"></a>ɓ|[U+0253](https://www.compart.com/en/unicode/U+0253)|LATIN SMALL LETTER B WITH HOOK|
|<a name="char-latin-capital-letter-d-with-hook"></a>Ɗ|[U+018A](https://www.compart.com/en/unicode/U+018A)|LATIN CAPITAL LETTER D WITH HOOK|
|<a name="char-latin-small-letter-d-with-hook"></a>ɗ|[U+0257](https://www.compart.com/en/unicode/U+0257)|LATIN SMALL LETTER D WITH HOOK|
|<a name="char-latin-capital-letter-schwa"></a>Ə|[U+018F](https://www.compart.com/en/unicode/U+018F)|LATIN CAPITAL LETTER SCHWA|
|<a name="char-latin-small-letter-schwa"></a>ə|[U+0259](https://www.compart.com/en/unicode/U+0259)|LATIN SMALL LETTER SCHWA|
|<a name="char-latin-capital-letter-g-with-hook"></a>Ɠ|[U+0193](https://www.compart.com/en/unicode/U+0193)|LATIN CAPITAL LETTER G WITH HOOK|
|<a name="char-latin-small-letter-g-with-hook"></a>ɠ|[U+0260](https://www.compart.com/en/unicode/U+0260)|LATIN SMALL LETTER G WITH HOOK|
|<a name="char-latin-capital-letter-i-with-stroke"></a>Ɨ|[U+0197](https://www.compart.com/en/unicode/U+0197)|LATIN CAPITAL LETTER I WITH STROKE|
|<a name="char-latin-small-letter-i-with-stroke"></a>ɨ|[U+0268](https://www.compart.com/en/unicode/U+0268)|LATIN SMALL LETTER I WITH STROKE|
|<a name="char-latin-capital-letter-u-bar"></a>Ʉ|[U+0244](https://www.compart.com/en/unicode/U+0244)|LATIN CAPITAL LETTER U BAR|
|<a name="char-latin-small-letter-u-bar"></a>ʉ|[U+0289](https://www.compart.com/en/unicode/U+0289)|LATIN SMALL LETTER U BAR|
|<a name="char-cyrillic-capital-letter-u-with-double-acute"></a>Ӳ|[U+04F2](https://www.compart.com/en/unicode/U+04F2)|CYRILLIC CAPITAL LETTER U WITH DOUBLE ACUTE|
|<a name="char-cyrillic-small-letter-u-with-double-acute"></a>ӳ|[U+04F3](https://www.compart.com/en/unicode/U+04F3)|CYRILLIC SMALL LETTER U WITH DOUBLE ACUTE|
|<a name="char-latin-small-letter-turned-ae"></a>ᴂ|[U+1D02](https://www.compart.com/en/unicode/U+1D02)|LATIN SMALL LETTER TURNED AE|
|<a name="char-latin-small-letter-ue"></a>ᵫ|[U+1D6B](https://www.compart.com/en/unicode/U+1D6B)|LATIN SMALL LETTER UE|
|<a name="char-latin-capital-letter-middle-welsh-ll"></a>Ỻ|[U+1EFA](https://www.compart.com/en/unicode/U+1EFA)|LATIN CAPITAL LETTER MIDDLE-WELSH LL|
|<a name="char-latin-small-letter-middle-welsh-ll"></a>ỻ|[U+1EFB](https://www.compart.com/en/unicode/U+1EFB)|LATIN SMALL LETTER MIDDLE-WELSH LL|
|<a name="char-l-b-bar-symbol"></a>℔|[U+2114](https://www.compart.com/en/unicode/U+2114)|L B BAR SYMBOL|
|<a name="char-turned-capital-f"></a>Ⅎ|[U+2132](https://www.compart.com/en/unicode/U+2132)|TURNED CAPITAL F|
|<a name="char-turned-small-f"></a>ⅎ|[U+214E](https://www.compart.com/en/unicode/U+214E)|TURNED SMALL F|
|<a name="char-roman-numeral-reversed-one-hundred"></a>Ↄ|[U+2183](https://www.compart.com/en/unicode/U+2183)|ROMAN NUMERAL REVERSED ONE HUNDRED|
|<a name="char-latin-small-letter-reversed-c"></a>ↄ|[U+2184](https://www.compart.com/en/unicode/U+2184)|LATIN SMALL LETTER REVERSED C|
|<a name="char-latin-capital-letter-tz"></a>Ꜩ|[U+A728](https://www.compart.com/en/unicode/U+A728)|LATIN CAPITAL LETTER TZ|
|<a name="char-latin-small-letter-tz"></a>ꜩ|[U+A729](https://www.compart.com/en/unicode/U+A729)|LATIN SMALL LETTER TZ|
|<a name="char-latin-capital-letter-aa"></a>Ꜳ|[U+A732](https://www.compart.com/en/unicode/U+A732)|LATIN CAPITAL LETTER AA|
|<a name="char-latin-small-letter-aa"></a>ꜳ|[U+A733](https://www.compart.com/en/unicode/U+A733)|LATIN SMALL LETTER AA|
|<a name="char-latin-capital-letter-ao"></a>Ꜵ|[U+A734](https://www.compart.com/en/unicode/U+A734)|LATIN CAPITAL LETTER AO|
|<a name="char-latin-small-letter-ao"></a>ꜵ|[U+A735](https://www.compart.com/en/unicode/U+A735)|LATIN SMALL LETTER AO|
|<a name="char-latin-capital-letter-au"></a>Ꜷ|[U+A736](https://www.compart.com/en/unicode/U+A736)|LATIN CAPITAL LETTER AU|
|<a name="char-latin-small-letter-au"></a>ꜷ|[U+A737](https://www.compart.com/en/unicode/U+A737)|LATIN SMALL LETTER AU|
|<a name="char-latin-capital-letter-av"></a>Ꜹ|[U+A738](https://www.compart.com/en/unicode/U+A738)|LATIN CAPITAL LETTER AV|
|<a name="char-latin-small-letter-av-with-horizontal-bar"></a>ꜻ|[U+A73B](https://www.compart.com/en/unicode/U+A73B)|LATIN SMALL LETTER AV WITH HORIZONTAL BAR|
|<a name="char-latin-capital-letter-ay"></a>Ꜽ|[U+A73C](https://www.compart.com/en/unicode/U+A73C)|LATIN CAPITAL LETTER AY|
|<a name="char-latin-small-letter-ay"></a>ꜽ|[U+A73D](https://www.compart.com/en/unicode/U+A73D)|LATIN SMALL LETTER AY|
|<a name="char-latin-capital-letter-oo"></a>Ꝏ|[U+A74E](https://www.compart.com/en/unicode/U+A74E)|LATIN CAPITAL LETTER OO|
|<a name="char-latin-small-letter-oo"></a>ꝏ|[U+A74F](https://www.compart.com/en/unicode/U+A74F)|LATIN SMALL LETTER OO|
|<a name="char-latin-capital-letter-vy"></a>Ꝡ|[U+A760](https://www.compart.com/en/unicode/U+A760)|LATIN CAPITAL LETTER VY|
|<a name="char-latin-small-letter-vy"></a>ꝡ|[U+A761](https://www.compart.com/en/unicode/U+A761)|LATIN SMALL LETTER VY|
|<a name="char-latin-small-letter-uo"></a>ꭣ|[U+AB63](https://www.compart.com/en/unicode/U+AB63)|LATIN SMALL LETTER UO|
|<a name="char-latin-small-ligature-ff"></a>ﬀ|[U+FB00](https://www.compart.com/en/unicode/U+FB00)|LATIN SMALL LIGATURE FF|
|<a name="char-latin-small-ligature-fi"></a>ﬁ|[U+FB01](https://www.compart.com/en/unicode/U+FB01)|LATIN SMALL LIGATURE FI|
|<a name="char-latin-small-ligature-fl"></a>ﬂ|[U+FB02](https://www.compart.com/en/unicode/U+FB02)|LATIN SMALL LIGATURE FL|
|<a name="char-latin-small-ligature-ffi"></a>ﬃ|[U+FB03](https://www.compart.com/en/unicode/U+FB03)|LATIN SMALL LIGATURE FFI|
|<a name="char-latin-small-ligature-ffl"></a>ﬄ|[U+FB04](https://www.compart.com/en/unicode/U+FB04)|LATIN SMALL LIGATURE FFL|
|<a name="char-latin-small-ligature-st"></a>ﬆ|[U+FB06](https://www.compart.com/en/unicode/U+FB06)|LATIN SMALL LIGATURE ST|

## Known Issues
* We'll probably never get all combining diacritics. There are hundreds, including things like [Znamenny Combining Mark Gorazdo Nizko S Kryzhem On Right](https://codepoints.net/znamenny_musical_notation).
* We're also never getting anywhere near all of Unicode, even just the "spelling" bits, as Unicode v16 now has more than 65,000 code points.
* The characters native to this system are all precomposed. As you write a character, then add diacritics, you're replacing the single code point character with another that has the diacritic, or several, in the case of stacked diacritics (and if you try to add a diacritic to a character that doesn't exist with that diacritic in Unicode as a single code point, you just get an untrans). This isn't so much a design issue, as a design decision, something for the user to be aware of. The system could try to solve for this and compose a character out of combining diacritics, when a single code point version doesn't exist, but that would just lead to confusion, especially given the next issue...
* You can star back to remove diacritics (and modifiers) in the reverse order of how you added them, and Plover will simply backtrack through the characters, effectively undoing the addition of each diacritic (and/or modifier), by re-replacing it with the simpler one it came from. If you manually compose a character, however, using the combining diacritical marks, star will simply delete the entire thing in one shot, which can be a bit jarring. I've tried every combo of glue, space suppressor, inside and outside of curly braces... Everything has its own unique set of issues. The current setup is the best so far, with the stated caveat. Backspace, at least for me, always deletes the entire character, with its combining diacritical marks, though this may be system/app dependent.


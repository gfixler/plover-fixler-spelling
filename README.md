
# Fixler Spelling for Plover
A fingerspelling system for the [Plover](https://www.openstenoproject.org/plover/) steno software.

This library currently provides quick access to 587 characters.

## Design Goals
* provide upper and lowercase letters, with some extras, like Æ/æ, and Ə/ə
* systematize writing most precomposed Latin letters with diacritics
* extend system to allow composing in combining characters
* add in other symbols, ligatures, etc., on a case-by-case basis
* include some similar alphabets (NATO, Braille, Morse, Greek, etc.)


## Notes on Design
### The Core
The core of this system is about spelling, and revolves around the Latin letters with diacritics, and alphabets that map well to and from Latin letters. That said, this library is not above including other, fun things that don't exactly fit, but also don't feel terribly out of place here.

### It's Just Outlines
Modifiers are not currently programmatic, and do not look at stroke history. This is not a Plover Python dictionary. The modifier system simply exports a JSON file filled with multi-stroke outlines that pair a base letter with one or more modifiers. This means "á" ("a with acute") is simply defined as the two-stroke outline, A*/-RP. You can't stroke KAT to write "cat", then stroke a modifier to add a diacritic to the "t" at the end of the word.

### System Letters
Because letter chords are part of the outlines with their modifiers, you must use the letter chords as defined in this library. This means if you use STK for "z", for example, and this system uses STKPW, you must use this system's version to write, e.g., the ẓ character. Currently, the way around this is to modify the Python file, and reexport the dictionary.

### Precomposed Characters
All characters defined in this system—as seen in the "Used by" lists following each modifier in the [Available Diacritics and Other Modifiers](#available-diacritics-and-other-modifiers) section below—are "precomposed" characters in Unicode, meaning they have a single code point in The Unicode Standard. Many characters not in these lists, encountered in the wild, are actually composed of a base letter, with one or more [combining characters](https://en.wikipedia.org/wiki/Combining_character) following them. For example, z with acute exists in Unicode, but currently, z with grave does not, so it's not defined in the core system here. If you see a z with grave, it's composed of small letter z (U+007A) and the combining grave diacritic (U+0323). Even characters that do have a precomposed (single code point) version often show up as [composed versions](https://en.wikipedia.org/wiki/Unicode_equivalence) of themselves. (See: [When an é is not an é](https://nation.marketo.com/t5/product-blogs/when-an-e%CC%81-is-not-an-%C3%A9-about-unicode-precomposed-vs-decomposed/ba-p/339051)).

### Stacking Modifiers
Characters with more than one modifier, like "ẫ" ("a with circumflex and tilde"), are made by stroking the letter chord, followed by each modifier chord in sequence. The order of these is based on the Unicode name, where "ẫ" (Unicode code point U+1EAB) is called "LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE", and means you stroke the circumflex modifier before the tilde modifier.


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
|![acute](images/acute.png)|![tweak](images/EU_up.png)|Shaped like the acute symbol.<BR><BR>Used in: [ǽ](https://en.wikipedia.org/wiki/%C3%86) [Ǽ](https://en.wikipedia.org/wiki/%C3%86) [á](https://en.wikipedia.org/wiki/%C3%81) [Á](https://en.wikipedia.org/wiki/%C3%81) [ć](https://en.wikipedia.org/wiki/%C4%86) [Ć](https://en.wikipedia.org/wiki/%C4%86) [é](https://en.wikipedia.org/wiki/%C3%89) [É](https://en.wikipedia.org/wiki/%C3%89) [ǵ](https://en.wikipedia.org/wiki/%C7%B4) [Ǵ](https://en.wikipedia.org/wiki/%C7%B4) [í](https://en.wikipedia.org/wiki/%C3%8D) [Í](https://en.wikipedia.org/wiki/%C3%8D) [ĺ](https://en.wikipedia.org/wiki/Acute_accent) [Ĺ](https://en.wikipedia.org/wiki/Acute_accent) [ń](https://en.wikipedia.org/wiki/%C5%83) [Ń](https://en.wikipedia.org/wiki/%C5%83) [ó](https://en.wikipedia.org/wiki/%C3%93) [Ó](https://en.wikipedia.org/wiki/%C3%93) [ǿ](https://en.wikipedia.org/wiki/%C3%98#%C7%BE) [Ǿ](https://en.wikipedia.org/wiki/%C3%98#%C7%BE) [ŕ](https://en.wikipedia.org/wiki/%C5%94) [Ŕ](https://en.wikipedia.org/wiki/%C5%94) [ś](https://en.wikipedia.org/wiki/%C5%9A) [Ś](https://en.wikipedia.org/wiki/%C5%9A) [ú](https://en.wikipedia.org/wiki/%C3%9A) [Ú](https://en.wikipedia.org/wiki/%C3%9A) [ẃ](https://en.wikipedia.org/wiki/%E1%BA%82) [Ẃ](https://en.wikipedia.org/wiki/%E1%BA%82) [ý](https://en.wikipedia.org/wiki/%C3%9D) [Ý](https://en.wikipedia.org/wiki/%C3%9D) [ź](https://en.wikipedia.org/wiki/%C5%B9) [Ź](https://en.wikipedia.org/wiki/%C5%B9) [ǽ](https://en.wikipedia.org/wiki/%C3%86) [Ǽ](https://en.wikipedia.org/wiki/%C3%86) ắ Ắ ấ Ấ ớ Ớ ố Ố ế Ế ứ Ứ ǘ Ǘ ḉ Ḉ ḗ Ḗ ḯ Ḯ ḱ Ḱ ḿ Ḿ ṍ Ṍ ṓ Ṓ ṕ Ṕ ṥ Ṥ ṹ Ṹ|
|Double Acute| |
|![acuteDoubled](images/acuteDoubled.png)|![tweak](images/E_down.png)|The acute modifier shape, with the '[extra](#modifier-tweaks)' tweak.<BR><BR>Used in: [ő](https://en.wikipedia.org/wiki/%C5%90) [Ő](https://en.wikipedia.org/wiki/%C5%90) [ű](https://en.wikipedia.org/wiki/Double_acute_accent#Letters_with_double_acute) [Ű](https://en.wikipedia.org/wiki/Double_acute_accent#Letters_with_double_acute) [ӳ](https://en.wikipedia.org/wiki/Double_acute_accent#Letters_with_double_acute) [Ӳ](https://en.wikipedia.org/wiki/Double_acute_accent#Letters_with_double_acute)|
|Breve| |
|![breve](images/breve.png)|![tweak](images/EU_up.png)|Shaped like the breve symbol.<BR><BR>Used in: [ă](https://en.wikipedia.org/wiki/%C4%82) [Ă](https://en.wikipedia.org/wiki/%C4%82) [ĕ](https://en.wikipedia.org/wiki/Breve#Letters_with_breve) [Ĕ](https://en.wikipedia.org/wiki/Breve#Letters_with_breve) [ğ](https://en.wikipedia.org/wiki/%C4%9E) [Ğ](https://en.wikipedia.org/wiki/%C4%9E) [ĭ](https://en.wikipedia.org/wiki/Breve) [Ĭ](https://en.wikipedia.org/wiki/Breve) [ŏ](https://en.wikipedia.org/wiki/Breve) [Ŏ](https://en.wikipedia.org/wiki/Breve) [ŭ](https://en.wikipedia.org/wiki/%C5%AC) [Ŭ](https://en.wikipedia.org/wiki/%C5%AC) ẳ Ẳ ẵ Ẵ ằ Ằ ắ Ắ ặ Ặ ḝ Ḝ|
|Breve Below| |
|![breveBelow](images/breveBelow.png)|![tweak](images/U_down.png)|The breve modifier shape, with the '[under](#modifier-tweaks)' tweak.<BR><BR>Used in: ḫ Ḫ|
|Breve Inverted| |
|![breveInverted](images/breveInverted.png)|![tweak](images/EU_up.png)|Shaped like the inverted breve symbol.<BR><BR>Used in: ȃ Ȃ ȇ Ȇ ȋ Ȋ ȏ Ȏ ȓ Ȓ ȗ Ȗ|
|Caron| |
|![caron](images/caron.png)|![tweak](images/EU_up.png)|Shaped like the caron symbol.<BR><BR>Used in: [ǎ](https://en.wikipedia.org/wiki/Caron) [Ǎ](https://en.wikipedia.org/wiki/Caron) [č](https://en.wikipedia.org/wiki/%C4%8C) [Č](https://en.wikipedia.org/wiki/%C4%8C) [ě](https://en.wikipedia.org/wiki/%C4%9A) [Ě](https://en.wikipedia.org/wiki/%C4%9A) [ǧ](https://en.wikipedia.org/wiki/%C7%A6) [Ǧ](https://en.wikipedia.org/wiki/%C7%A6) [ǐ](https://en.wikipedia.org/wiki/Caron) [Ǐ](https://en.wikipedia.org/wiki/Caron) [ǩ](https://en.wikipedia.org/wiki/%C7%A8) [Ǩ](https://en.wikipedia.org/wiki/%C7%A8) [ľ](https://en.wikipedia.org/wiki/%C4%BD) [Ľ](https://en.wikipedia.org/wiki/%C4%BD) [ň](https://en.wikipedia.org/wiki/%C5%87) [Ň](https://en.wikipedia.org/wiki/%C5%87) [ǒ](https://en.wikipedia.org/wiki/Caron) [Ǒ](https://en.wikipedia.org/wiki/Caron) [ř](https://en.wikipedia.org/wiki/%C5%98) [Ř](https://en.wikipedia.org/wiki/%C5%98) [ŝ](https://en.wikipedia.org/wiki/%C5%9C) [Ŝ](https://en.wikipedia.org/wiki/%C5%9C) [š](https://en.wikipedia.org/wiki/%C5%A0) [Š](https://en.wikipedia.org/wiki/%C5%A0) [ť](https://en.wikipedia.org/wiki/%C5%A4) [Ť](https://en.wikipedia.org/wiki/%C5%A4) [ǔ](https://en.wikipedia.org/wiki/Caron) [Ǔ](https://en.wikipedia.org/wiki/Caron) [ž](https://en.wikipedia.org/wiki/%C5%BD) [Ž](https://en.wikipedia.org/wiki/%C5%BD) ď Ď ȟ Ȟ ṧ Ṧ ǰ|
|Cedilla| |
|![cedilla](images/cedilla.png)|![tweak](images/EU_up.png)|Shaped like the cedilla, which hangs below the character, and curves to the left.<BR><BR>Used in: [ç](https://en.wikipedia.org/wiki/%C3%87) [Ç](https://en.wikipedia.org/wiki/%C3%87) [ȩ](https://en.wikipedia.org/wiki/Cedilla) [Ȩ](https://en.wikipedia.org/wiki/Cedilla) [ş](https://en.wikipedia.org/wiki/%C5%9E) [Ş](https://en.wikipedia.org/wiki/%C5%9E) [ţ](https://en.wikipedia.org/wiki/%C5%A2) [Ţ](https://en.wikipedia.org/wiki/%C5%A2) [ḑ](https://en.wikipedia.org/wiki/%E1%B8%90) [Ḑ](https://en.wikipedia.org/wiki/%E1%B8%90) [ģ](https://en.wikipedia.org/wiki/%C4%A2) [Ģ](https://en.wikipedia.org/wiki/%C4%A2) [ķ](https://en.wikipedia.org/wiki/%C4%B6) [Ķ](https://en.wikipedia.org/wiki/%C4%B6) [ļ](https://en.wikipedia.org/wiki/Cedilla) [Ļ](https://en.wikipedia.org/wiki/Cedilla) [ņ](https://en.wikipedia.org/wiki/Cedilla) [Ņ](https://en.wikipedia.org/wiki/Cedilla) [ŗ](https://en.wikipedia.org/wiki/Cedilla) [Ŗ](https://en.wikipedia.org/wiki/Cedilla) ḉ Ḉ ḝ Ḝ ḩ Ḩ|
|Circumflex| |
|![circumflex](images/circumflex.png)|![tweak](images/EU_up.png)|Shaped like the circumflex symbol.<BR><BR>Used in: [â](https://en.wikipedia.org/wiki/%C3%82) [Â](https://en.wikipedia.org/wiki/%C3%82) [ĉ](https://en.wikipedia.org/wiki/%C4%88) [Ĉ](https://en.wikipedia.org/wiki/%C4%88) [ḓ](https://en.wikipedia.org/wiki/Circumflex) [Ḓ](https://en.wikipedia.org/wiki/Circumflex) [ê](https://en.wikipedia.org/wiki/%C3%8A) [Ê](https://en.wikipedia.org/wiki/%C3%8A) [ĝ](https://en.wikipedia.org/wiki/%C4%9C) [Ĝ](https://en.wikipedia.org/wiki/%C4%9C) [ĥ](https://en.wikipedia.org/wiki/%C4%A4) [Ĥ](https://en.wikipedia.org/wiki/%C4%A4) [î](https://en.wikipedia.org/wiki/%C3%8E) [Î](https://en.wikipedia.org/wiki/%C3%8E) [ĵ](https://en.wikipedia.org/wiki/%C4%B4) [Ĵ](https://en.wikipedia.org/wiki/%C4%B4) [ḽ](https://en.wikipedia.org/wiki/Circumflex) [Ḽ](https://en.wikipedia.org/wiki/Circumflex) [ṋ](https://en.wikipedia.org/wiki/Circumflex) [Ṋ](https://en.wikipedia.org/wiki/Circumflex) [ô](https://en.wikipedia.org/wiki/Circumflex) [Ô](https://en.wikipedia.org/wiki/Circumflex) [ṱ](https://en.wikipedia.org/wiki/Circumflex) [Ṱ](https://en.wikipedia.org/wiki/Circumflex) [û](https://en.wikipedia.org/wiki/%C3%9B) [Û](https://en.wikipedia.org/wiki/%C3%9B) [ŵ](https://en.wikipedia.org/wiki/Circumflex) [Ŵ](https://en.wikipedia.org/wiki/Circumflex) [ŷ](https://en.wikipedia.org/wiki/Circumflex) [Ŷ](https://en.wikipedia.org/wiki/Circumflex) ậ Ậ ẩ Ẩ ẫ Ẫ ầ Ầ ấ Ấ ộ Ộ ổ Ổ ỗ Ỗ ồ Ồ ố Ố ệ Ệ ể Ể ễ Ễ ề Ề ế Ế ẑ Ẑ|
|Circumflex Below| |
|![circumflexBelow](images/circumflexBelow.png)|![tweak](images/U_down.png)|The circumflex modifier shape, with the '[under](#modifier-tweaks)' tweak.<BR><BR>Used in: ḙ Ḙ ṷ Ṷ|
|Comma Below| |
|![commaBelow](images/commaBelow.png)|![tweak](images/EU_up.png)|Chosen to mirror the shape used for the comma in the [Emily's Symbols](https://github.com/EPLHREU/emily-symbols) plugin.<BR><BR>Used in: [ș](https://en.wikipedia.org/wiki/%C8%98) [Ș](https://en.wikipedia.org/wiki/%C8%98) [ț](https://en.wikipedia.org/wiki/%C8%9A) [Ț](https://en.wikipedia.org/wiki/%C8%9A)|
|Diaeresis/Umlaut| |
|![diaeresis](images/diaeresis.png)|![tweak](images/EU_up.png)|Shaped like the diaeresis/umlaut symbols.<BR><BR>NOTE: [diaeresis](https://en.wikipedia.org/wiki/Diaeresis_(diacritic)) and [umlaut](https://en.wikipedia.org/wiki/Umlaut_(diacritic)) are distinct concepts, with separate uses, but are represented by the same Unicode code points. They are created via the same outline in this spelling system.<BR><BR>Used in: [ä](https://en.wikipedia.org/wiki/%C3%84) [Ä](https://en.wikipedia.org/wiki/%C3%84) [ǟ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [Ǟ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [ë](https://en.wikipedia.org/wiki/%C3%8B) [Ë](https://en.wikipedia.org/wiki/%C3%8B) [ï](https://en.wikipedia.org/wiki/%C3%8F) [Ï](https://en.wikipedia.org/wiki/%C3%8F) [ö](https://en.wikipedia.org/wiki/%C3%96) [Ö](https://en.wikipedia.org/wiki/%C3%96) [ȫ](https://en.wikipedia.org/wiki/%C3%96) [Ȫ](https://en.wikipedia.org/wiki/%C3%96) [ü](https://en.wikipedia.org/wiki/%C3%9C) [Ü](https://en.wikipedia.org/wiki/%C3%9C) [ẅ](https://en.wikipedia.org/wiki/Two_dots_(diacritic)) [Ẅ](https://en.wikipedia.org/wiki/Two_dots_(diacritic)) [ÿ](https://en.wikipedia.org/wiki/%C5%B8) [Ÿ](https://en.wikipedia.org/wiki/%C5%B8) ǘ Ǘ ǖ Ǖ ǚ Ǚ ǜ Ǜ ḧ Ḧ ḯ Ḯ ṏ Ṏ ṻ Ṻ ẍ Ẍ ẗ|
|Diaeresis Below| |
|![diaeresisBelow](images/diaeresisBelow.png)|![tweak](images/EU_up.png)|The diaeresis/umlaut shape, but lower.<BR><BR>Used in: ṳ Ṳ|
|Dot Above| |
|![dotAbove](images/dotAbove.png)|![tweak](images/EU_up.png)|A single key, up high, like a dot above. See dot below.<BR><BR>Used in: [ȧ](https://en.wikipedia.org/wiki/%C8%A6) [Ȧ](https://en.wikipedia.org/wiki/%C8%A6) [ċ](https://en.wikipedia.org/wiki/%C4%8A) [Ċ](https://en.wikipedia.org/wiki/%C4%8A) [ė](https://en.wikipedia.org/wiki/%C4%96) [Ė](https://en.wikipedia.org/wiki/%C4%96) [ġ](https://en.wikipedia.org/wiki/%C4%A0) [Ġ](https://en.wikipedia.org/wiki/%C4%A0) [i](https://en.wikipedia.org/wiki/%C4%B0) [İ](https://en.wikipedia.org/wiki/%C4%B0) [ṅ](https://en.wikipedia.org/wiki/%E1%B9%84) [Ṅ](https://en.wikipedia.org/wiki/%E1%B9%84) [ȯ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ȯ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ȱ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ȱ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ṡ](https://en.wikipedia.org/wiki/%E1%B9%A0) [Ṡ](https://en.wikipedia.org/wiki/%E1%B9%A0) [ẋ](https://en.wikipedia.org/wiki/%E1%BA%8A) [Ẋ](https://en.wikipedia.org/wiki/%E1%BA%8A) [ż](https://en.wikipedia.org/wiki/%C5%BB) [Ż](https://en.wikipedia.org/wiki/%C5%BB) ǡ Ǡ ḃ Ḃ ḋ Ḋ ḟ Ḟ ḣ Ḣ ṁ Ṁ ṗ Ṗ ṙ Ṙ ṥ Ṥ ṧ Ṧ ṩ Ṩ ṫ Ṫ ẇ Ẇ ẏ Ẏ|
|Dot Below| |
|![dotBelow](images/dotBelow.png)|![tweak](images/EU_up.png)|Chosen to mirror the shape used for the period in the [Emily's Symbols](https://github.com/EPLHREU/emily-symbols) plugin. A single key, down low, like a dot below. See dot above.<BR><BR>Used in: [ḅ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ḅ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ḍ](https://en.wikipedia.org/wiki/%E1%B8%8C) [Ḍ](https://en.wikipedia.org/wiki/%E1%B8%8C) [ẹ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ẹ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ḥ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ḥ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ị](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ị](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ḷ](https://en.wikipedia.org/wiki/%E1%B8%B6) [Ḷ](https://en.wikipedia.org/wiki/%E1%B8%B6) [ọ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ọ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ṛ](https://en.wikipedia.org/wiki/%E1%B9%9A) [Ṛ](https://en.wikipedia.org/wiki/%E1%B9%9A) [ș](https://en.wikipedia.org/wiki/%E1%B9%A2) [Ș](https://en.wikipedia.org/wiki/%E1%B9%A2) [ṭ](https://en.wikipedia.org/wiki/%E1%B9%AC) [Ṭ](https://en.wikipedia.org/wiki/%E1%B9%AC) [ụ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ụ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ẓ](https://en.wikipedia.org/wiki/%E1%BA%92) [Ẓ](https://en.wikipedia.org/wiki/%E1%BA%92) ỵ Ỵ ạ Ạ ặ Ặ ậ Ậ ợ Ợ ộ Ộ ệ Ệ ự Ự ḳ Ḳ ḹ Ḹ ṃ Ṃ ṇ Ṇ ṝ Ṝ ṣ Ṣ ṩ Ṩ ṿ Ṿ ẉ Ẉ|
|Grave| |
|![grave](images/grave.png)|![tweak](images/EU_up.png)|Shaped like the grave symbol.<BR><BR>Used in: [à](https://en.wikipedia.org/wiki/%C3%80) [À](https://en.wikipedia.org/wiki/%C3%80) [è](https://en.wikipedia.org/wiki/%C3%88) [È](https://en.wikipedia.org/wiki/%C3%88) [ì](https://en.wikipedia.org/wiki/%C3%8C) [Ì](https://en.wikipedia.org/wiki/%C3%8C) [ò](https://en.wikipedia.org/wiki/%C3%92) [Ò](https://en.wikipedia.org/wiki/%C3%92) [ù](https://en.wikipedia.org/wiki/Grave_accent) [Ù](https://en.wikipedia.org/wiki/Grave_accent) [ẁ](https://en.wikipedia.org/wiki/Grave_accent) [Ẁ](https://en.wikipedia.org/wiki/Grave_accent) [ỳ](https://en.wikipedia.org/wiki/Grave_accent) [Ỳ](https://en.wikipedia.org/wiki/Grave_accent) ằ Ằ ầ Ầ ờ Ờ ồ Ồ ề Ề ừ Ừ ǜ Ǜ ǹ Ǹ ḕ Ḕ ṑ Ṑ|
|Double Grave| |
|![graveDoubled](images/graveDoubled.png)|![tweak](images/E_down.png)|The grave modifier shape, with the '[extra](#modifier-tweaks)' tweak.<BR><BR>Used in: ȁ Ȁ ȅ Ȅ ȉ Ȉ ȍ Ȍ ȑ Ȑ ȕ Ȕ|
|Hook Above| |
|![hookAbove](images/hookAbove.png)|![tweak](images/EU_up.png)|Shaped like the hook above symbol, sticking up, and curling to the left.<BR><BR>Used in: ỷ Ỷ ẳ Ẳ ả Ả ẩ Ẩ ỏ Ỏ ở Ở ổ Ổ ẻ Ẻ ể Ể ỉ Ỉ ủ Ủ ử Ử|
|Hook| |
|![hook](images/hook.png)|![tweak](images/EU_up.png)|Distinct from 'hook above', which is a detached diacritic, this is for characters with an attached hook. The hook shape was chosen to match most of these characters, which either curl up, then to the right, or to the left, then down, which makes the same curve. Imagine the chord shape attaching to some at the −R, and others at the −P. Some of the visual nature of this is down to fonts and rendering, of course, and a few letters don't match up well to this chord shape, and will just have to be memorized as exceptions for now.<BR><BR>Used in: [ɓ](https://en.wikipedia.org/wiki/%C6%81) [Ɓ](https://en.wikipedia.org/wiki/%C6%81) [ƈ](https://en.wikipedia.org/wiki/%C6%87) [Ƈ](https://en.wikipedia.org/wiki/%C6%87) [ɗ](https://en.wikipedia.org/wiki/%C6%8A) [Ɗ](https://en.wikipedia.org/wiki/%C6%8A) [ƒ](https://en.wikipedia.org/wiki/%C6%91) [Ƒ](https://en.wikipedia.org/wiki/%C6%91) [ɠ](https://en.wikipedia.org/wiki/G_with_hook) [Ɠ](https://en.wikipedia.org/wiki/G_with_hook) [ƙ](https://en.wikipedia.org/wiki/%C6%98) [Ƙ](https://en.wikipedia.org/wiki/%C6%98) [ƥ](https://en.wikipedia.org/wiki/%C6%A4) [Ƥ](https://en.wikipedia.org/wiki/%C6%A4) [ƭ](https://en.wikipedia.org/wiki/%C6%AC) [Ƭ](https://en.wikipedia.org/wiki/%C6%AC) [ƴ](https://en.wikipedia.org/wiki/%C6%B3) [Ƴ](https://en.wikipedia.org/wiki/%C6%B3)|
|Horn| |
|![horn](images/horn.png)|![tweak](images/EU_up.png)|Shaped like the horn symbol, sticking out to the right and curving upward. The shape is also on the right-hand side of the modifier keys cluster, as the horn sticks out the right side of its characters.<BR><BR>Used in: [ơ](https://en.wikipedia.org/wiki/%C6%A0) [Ơ](https://en.wikipedia.org/wiki/%C6%A0) [ư](https://en.wikipedia.org/wiki/%C6%AF) [Ư](https://en.wikipedia.org/wiki/%C6%AF) [ơ](https://en.wikipedia.org/wiki/%C6%A0) [Ơ](https://en.wikipedia.org/wiki/%C6%A0) ợ Ợ ở Ở ỡ Ỡ ờ Ờ ớ Ớ ự Ự ử Ử ữ Ữ ừ Ừ ứ Ứ|
|Interpunct| |
|![interpunct](images/interpunct.png)|![tweak](images/EU_up.png)|An odd one, which joins the dot above and dot below characters. Think of it as the midpoint of the above and below dots, made by stroking both together.<BR><BR>Used in: [ŀ](https://en.wikipedia.org/wiki/Interpunct#Catalan) [Ŀ](https://en.wikipedia.org/wiki/Interpunct#Catalan)|
|Line Below| |
|![lineBelow](images/lineBelow.png)|![tweak](images/U_down.png)|When decomposed into base character + diacritic, the combining character for this set of Unicode composed characters is the macron below. Rather than use the the lower version of the chord, on the bottom row, this uses the '[under](#modifier-tweaks)' tweak with the macron shape, to respect this relation.<BR><BR>Used in: ḇ Ḇ ḏ Ḏ ḵ Ḵ ḻ Ḻ ṉ Ṉ ṟ Ṟ ṯ Ṯ ẕ Ẕ ẖ|
|Macron| |
|![macron](images/macron.png)|![tweak](images/EU_up.png)|Shaped like the macron symbol.<BR><BR>Used in: [ǣ](https://en.wikipedia.org/wiki/%C3%86) [Ǣ](https://en.wikipedia.org/wiki/%C3%86) [ǟ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [Ǟ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [ā](https://en.wikipedia.org/wiki/%C4%80) [Ā](https://en.wikipedia.org/wiki/%C4%80) [ē](https://en.wikipedia.org/wiki/Macron_(diacritic)) [Ē](https://en.wikipedia.org/wiki/Macron_(diacritic)) [ī](https://en.wikipedia.org/wiki/Macron_(diacritic)) [Ī](https://en.wikipedia.org/wiki/Macron_(diacritic)) [ȱ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ȱ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ȫ](https://en.wikipedia.org/wiki/%C3%96) [Ȫ](https://en.wikipedia.org/wiki/%C3%96) [ō](https://en.wikipedia.org/wiki/Macron_(diacritic)) [Ō](https://en.wikipedia.org/wiki/Macron_(diacritic)) [ȭ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [Ȭ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [ū](https://en.wikipedia.org/wiki/Macron_(diacritic)) [Ū](https://en.wikipedia.org/wiki/Macron_(diacritic)) [ȳ](https://en.wikipedia.org/wiki/%C8%B2) [Ȳ](https://en.wikipedia.org/wiki/%C8%B2) [ǣ](https://en.wikipedia.org/wiki/%C3%86) [Ǣ](https://en.wikipedia.org/wiki/%C3%86) ǖ Ǖ ǚ Ǚ ǡ Ǡ ǭ Ǭ ḕ Ḕ ḗ Ḗ ḡ Ḡ ḹ Ḹ ṑ Ṑ ṓ Ṓ ṝ Ṝ ṻ Ṻ|
|Ogonek| |
|![ogonek](images/ogonek.png)|![tweak](images/EU_up.png)|The ogonek, meaning 'little tail' in Polish, hangs off the bottom of its character, curling down and to the right.<BR><BR>Used in: [ą](https://en.wikipedia.org/wiki/%C4%84) [Ą](https://en.wikipedia.org/wiki/%C4%84) [ę](https://en.wikipedia.org/wiki/%C4%98) [Ę](https://en.wikipedia.org/wiki/%C4%98) [į](https://en.wikipedia.org/wiki/%C4%AE) [Į](https://en.wikipedia.org/wiki/%C4%AE) [ǫ](https://en.wikipedia.org/wiki/%C7%AA) [Ǫ](https://en.wikipedia.org/wiki/%C7%AA) [ų](https://en.wikipedia.org/wiki/%C5%B2) [Ų](https://en.wikipedia.org/wiki/%C5%B2) ǭ Ǭ|
|Ring Above| |
|![ringAbove](images/ringAbove.png)|![tweak](images/EU_up.png)|Think of this square of keys like a little circle, or ring.<BR><BR>Used in: [å](https://en.wikipedia.org/wiki/%C3%85) [Å](https://en.wikipedia.org/wiki/%C3%85) [ů](https://en.wikipedia.org/wiki/Ring_(diacritic)) [Ů](https://en.wikipedia.org/wiki/Ring_(diacritic)) ẘ ẙ|
|Ring Below| |
|![ringBelow](images/ringBelow.png)|![tweak](images/U_down.png)|The ring above modifier shape, with the '[under](#modifier-tweaks)' tweak.<BR><BR>Used in: ḁ Ḁ|
|Stroke| |
|![stroke](images/stroke.png)|![tweak](images/EU_up.png)|Like the macron, but lower, because it cuts through the character, rather than flying above it.<BR><BR>Used in: [đ](https://en.wikipedia.org/wiki/D_with_stroke) [Đ](https://en.wikipedia.org/wiki/D_with_stroke) [ǥ](https://en.wikipedia.org/wiki/G_with_stroke) [Ǥ](https://en.wikipedia.org/wiki/G_with_stroke) [ħ](https://en.wikipedia.org/wiki/H_with_stroke) [Ħ](https://en.wikipedia.org/wiki/H_with_stroke) [ɨ](https://en.wikipedia.org/wiki/I_with_bar) [Ɨ](https://en.wikipedia.org/wiki/I_with_bar) [ƚ](https://en.wikipedia.org/wiki/L_with_bar) [Ƚ](https://en.wikipedia.org/wiki/L_with_bar) [ɍ](https://en.wikipedia.org/wiki/R_with_stroke) [Ɍ](https://en.wikipedia.org/wiki/R_with_stroke) [ŧ](https://en.wikipedia.org/wiki/T_with_stroke) [Ŧ](https://en.wikipedia.org/wiki/T_with_stroke) [ʉ](https://en.wikipedia.org/wiki/U_with_bar) [Ʉ](https://en.wikipedia.org/wiki/U_with_bar)|
|Slash| |
|![slash](images/slash.png)|![tweak](images/EU_up.png)|Like the acute, but shifted, to indicate that it's lower, and cuts through the character. A bit of a stretch, as it's shifted to the right, not down, but other options were used up. Maybe think of it like moving to the right while reading this text, which eventually wraps, and takes you down a line.<BR><BR>Used in: [ł](https://en.wikipedia.org/wiki/%C5%81) [Ł](https://en.wikipedia.org/wiki/%C5%81) [ø](https://en.wikipedia.org/wiki/%C3%98) [Ø](https://en.wikipedia.org/wiki/%C3%98) [ǿ](https://en.wikipedia.org/wiki/%C3%98#%C7%BE) [Ǿ](https://en.wikipedia.org/wiki/%C3%98#%C7%BE)|
|Tilde| |
|![tilde](images/tilde.png)|![tweak](images/EU_up.png)|Shaped like the tilde symbol.<BR><BR>Used in: [ã](https://en.wikipedia.org/wiki/%C3%83) [Ã](https://en.wikipedia.org/wiki/%C3%83) [ẽ](https://en.wikipedia.org/wiki/%E1%BA%BC) [Ẽ](https://en.wikipedia.org/wiki/%E1%BA%BC) [ĩ](https://en.wikipedia.org/wiki/Tilde) [Ĩ](https://en.wikipedia.org/wiki/Tilde) [ñ](https://en.wikipedia.org/wiki/%C3%91) [Ñ](https://en.wikipedia.org/wiki/%C3%91) [õ](https://en.wikipedia.org/wiki/%C3%95) [Õ](https://en.wikipedia.org/wiki/%C3%95) [ȭ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [Ȭ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [ũ](https://en.wikipedia.org/wiki/Tilde) [Ũ](https://en.wikipedia.org/wiki/Tilde) [ỹ](https://en.wikipedia.org/wiki/Tilde) [Ỹ](https://en.wikipedia.org/wiki/Tilde) ẵ Ẵ ẫ Ẫ ỡ Ỡ ỗ Ỗ ễ Ễ ữ Ữ ṍ Ṍ ṏ Ṏ ṹ Ṹ ṽ Ṽ|
|Tilde Below| |
|![tildeBelow](images/tildeBelow.png)|![tweak](images/U_down.png)|The tilde modifier shape, with the '[under](#modifier-tweaks)' tweak.<BR><BR>Used in: ḛ Ḛ ḭ Ḭ ṵ Ṵ|
|Ligature| |
|![ligature](images/ligature.png)|![tweak](images/EU_up.png)|[Ligatures](https://en.wikipedia.org/wiki/Ligature_(writing)) are two or more graphemes joined together, as in Æ. To output an existing ligature, stroke the two letters in left-to-right order, then stroke this modifier to merge them. Think of the two vertical columns as the two graphemes being joined. For characters that modify ligatures, like the AE ligature with circumflex, or the AE ligature turned, create the ligature first, before modifying it further.<BR><BR>Used in: [ꜳ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [Ꜳ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [æ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [Æ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ꜵ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [Ꜵ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ꜷ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [Ꜷ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ꜻ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [Ꜹ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ꜽ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [Ꜽ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ﬀ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ﬃ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ﬄ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ﬁ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ﬂ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ƕ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [Ƕ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [℔](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ỻ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [Ỻ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [œ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [Œ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ꝏ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [Ꝏ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ﬆ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ꜩ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [Ꜩ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ᵫ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ꭣ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [w](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [W](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ꝡ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [Ꝡ](https://en.wikipedia.org/wiki/Ligature_(writing)#Ligatures_in_Unicode_(Latin_alphabets)) [ß](https://en.wikipedia.org/wiki/%C3%9F) [ẞ](https://en.wikipedia.org/wiki/%C3%9F)|
|Turned/Rotated| |
|![turned](images/turned.png)|![tweak](images/EU_up.png)|This modifier allows access to characters that are turned, or rotated.<BR><BR>Used in: [ə](https://en.wikipedia.org/wiki/Mid_central_vowel) [Ə](https://en.wikipedia.org/wiki/Mid_central_vowel) [ⅎ](https://en.wikipedia.org/wiki/Claudian_letters) [Ⅎ](https://en.wikipedia.org/wiki/Claudian_letters) [ᴂ](https://en.wiktionary.org/wiki/%E1%B4%82#Translingual)|
|Reversed| |
|![reversed](images/reversed.png)|![tweak](images/EU_down.png)|The turned modifier shape, with the '[inverted](#modifier-tweaks)' tweak.<BR><BR>This allows access to characters that are flipped, inverted, or reversed.<BR><BR>Used in: [ↄ](https://en.wikipedia.org/wiki/Claudian_letters) [Ↄ](https://en.wikipedia.org/wiki/Claudian_letters)|

## Character List
Here are all the characters this library exports.

Code points currently link to their associated page on [Compart](https://www.compart.com/en/about-compart)'s site.
|Char|Code Pt|Name|
|-|-|-|
|À|[U+00C0](https://www.compart.com/en/unicode/U+00C0)|LATIN CAPITAL LETTER A WITH GRAVE|
|à|[U+00E0](https://www.compart.com/en/unicode/U+00E0)|LATIN SMALL LETTER A WITH GRAVE|
|Á|[U+00C1](https://www.compart.com/en/unicode/U+00C1)|LATIN CAPITAL LETTER A WITH ACUTE|
|á|[U+00E1](https://www.compart.com/en/unicode/U+00E1)|LATIN SMALL LETTER A WITH ACUTE|
|Â|[U+00C2](https://www.compart.com/en/unicode/U+00C2)|LATIN CAPITAL LETTER A WITH CIRCUMFLEX|
|â|[U+00E2](https://www.compart.com/en/unicode/U+00E2)|LATIN SMALL LETTER A WITH CIRCUMFLEX|
|Ầ|[U+1EA6](https://www.compart.com/en/unicode/U+1EA6)|LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND GRAVE|
|ầ|[U+1EA7](https://www.compart.com/en/unicode/U+1EA7)|LATIN SMALL LETTER A WITH CIRCUMFLEX AND GRAVE|
|Ấ|[U+1EA4](https://www.compart.com/en/unicode/U+1EA4)|LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND ACUTE|
|ấ|[U+1EA5](https://www.compart.com/en/unicode/U+1EA5)|LATIN SMALL LETTER A WITH CIRCUMFLEX AND ACUTE|
|Ẫ|[U+1EAA](https://www.compart.com/en/unicode/U+1EAA)|LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND TILDE|
|ẫ|[U+1EAB](https://www.compart.com/en/unicode/U+1EAB)|LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE|
|Ẩ|[U+1EA8](https://www.compart.com/en/unicode/U+1EA8)|LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND HOOK ABOVE|
|ẩ|[U+1EA9](https://www.compart.com/en/unicode/U+1EA9)|LATIN SMALL LETTER A WITH CIRCUMFLEX AND HOOK ABOVE|
|Ã|[U+00C3](https://www.compart.com/en/unicode/U+00C3)|LATIN CAPITAL LETTER A WITH TILDE|
|ã|[U+00E3](https://www.compart.com/en/unicode/U+00E3)|LATIN SMALL LETTER A WITH TILDE|
|Ā|[U+0100](https://www.compart.com/en/unicode/U+0100)|LATIN CAPITAL LETTER A WITH MACRON|
|ā|[U+0101](https://www.compart.com/en/unicode/U+0101)|LATIN SMALL LETTER A WITH MACRON|
|Ă|[U+0102](https://www.compart.com/en/unicode/U+0102)|LATIN CAPITAL LETTER A WITH BREVE|
|ă|[U+0103](https://www.compart.com/en/unicode/U+0103)|LATIN SMALL LETTER A WITH BREVE|
|Ằ|[U+1EB0](https://www.compart.com/en/unicode/U+1EB0)|LATIN CAPITAL LETTER A WITH BREVE AND GRAVE|
|ằ|[U+1EB1](https://www.compart.com/en/unicode/U+1EB1)|LATIN SMALL LETTER A WITH BREVE AND GRAVE|
|Ắ|[U+1EAE](https://www.compart.com/en/unicode/U+1EAE)|LATIN CAPITAL LETTER A WITH BREVE AND ACUTE|
|ắ|[U+1EAF](https://www.compart.com/en/unicode/U+1EAF)|LATIN SMALL LETTER A WITH BREVE AND ACUTE|
|Ẵ|[U+1EB4](https://www.compart.com/en/unicode/U+1EB4)|LATIN CAPITAL LETTER A WITH BREVE AND TILDE|
|ẵ|[U+1EB5](https://www.compart.com/en/unicode/U+1EB5)|LATIN SMALL LETTER A WITH BREVE AND TILDE|
|Ẳ|[U+1EB2](https://www.compart.com/en/unicode/U+1EB2)|LATIN CAPITAL LETTER A WITH BREVE AND HOOK ABOVE|
|ẳ|[U+1EB3](https://www.compart.com/en/unicode/U+1EB3)|LATIN SMALL LETTER A WITH BREVE AND HOOK ABOVE|
|Ȧ|[U+0226](https://www.compart.com/en/unicode/U+0226)|LATIN CAPITAL LETTER A WITH DOT ABOVE|
|ȧ|[U+0227](https://www.compart.com/en/unicode/U+0227)|LATIN SMALL LETTER A WITH DOT ABOVE|
|Ǡ|[U+01E0](https://www.compart.com/en/unicode/U+01E0)|LATIN CAPITAL LETTER A WITH DOT ABOVE AND MACRON|
|ǡ|[U+01E1](https://www.compart.com/en/unicode/U+01E1)|LATIN SMALL LETTER A WITH DOT ABOVE AND MACRON|
|Ä|[U+00C4](https://www.compart.com/en/unicode/U+00C4)|LATIN CAPITAL LETTER A WITH DIAERESIS|
|ä|[U+00E4](https://www.compart.com/en/unicode/U+00E4)|LATIN SMALL LETTER A WITH DIAERESIS|
|Ǟ|[U+01DE](https://www.compart.com/en/unicode/U+01DE)|LATIN CAPITAL LETTER A WITH DIAERESIS AND MACRON|
|ǟ|[U+01DF](https://www.compart.com/en/unicode/U+01DF)|LATIN SMALL LETTER A WITH DIAERESIS AND MACRON|
|Ả|[U+1EA2](https://www.compart.com/en/unicode/U+1EA2)|LATIN CAPITAL LETTER A WITH HOOK ABOVE|
|ả|[U+1EA3](https://www.compart.com/en/unicode/U+1EA3)|LATIN SMALL LETTER A WITH HOOK ABOVE|
|Å|[U+00C5](https://www.compart.com/en/unicode/U+00C5)|LATIN CAPITAL LETTER A WITH RING ABOVE|
|å|[U+00E5](https://www.compart.com/en/unicode/U+00E5)|LATIN SMALL LETTER A WITH RING ABOVE|
|Ǎ|[U+01CD](https://www.compart.com/en/unicode/U+01CD)|LATIN CAPITAL LETTER A WITH CARON|
|ǎ|[U+01CE](https://www.compart.com/en/unicode/U+01CE)|LATIN SMALL LETTER A WITH CARON|
|Ȁ|[U+0200](https://www.compart.com/en/unicode/U+0200)|LATIN CAPITAL LETTER A WITH DOUBLE GRAVE|
|ȁ|[U+0201](https://www.compart.com/en/unicode/U+0201)|LATIN SMALL LETTER A WITH DOUBLE GRAVE|
|Ȃ|[U+0202](https://www.compart.com/en/unicode/U+0202)|LATIN CAPITAL LETTER A WITH INVERTED BREVE|
|ȃ|[U+0203](https://www.compart.com/en/unicode/U+0203)|LATIN SMALL LETTER A WITH INVERTED BREVE|
|Ạ|[U+1EA0](https://www.compart.com/en/unicode/U+1EA0)|LATIN CAPITAL LETTER A WITH DOT BELOW|
|ạ|[U+1EA1](https://www.compart.com/en/unicode/U+1EA1)|LATIN SMALL LETTER A WITH DOT BELOW|
|Ậ|[U+1EAC](https://www.compart.com/en/unicode/U+1EAC)|LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND DOT BELOW|
|ậ|[U+1EAD](https://www.compart.com/en/unicode/U+1EAD)|LATIN SMALL LETTER A WITH CIRCUMFLEX AND DOT BELOW|
|Ặ|[U+1EB6](https://www.compart.com/en/unicode/U+1EB6)|LATIN CAPITAL LETTER A WITH BREVE AND DOT BELOW|
|ặ|[U+1EB7](https://www.compart.com/en/unicode/U+1EB7)|LATIN SMALL LETTER A WITH BREVE AND DOT BELOW|
|Ḁ|[U+1E00](https://www.compart.com/en/unicode/U+1E00)|LATIN CAPITAL LETTER A WITH RING BELOW|
|ḁ|[U+1E01](https://www.compart.com/en/unicode/U+1E01)|LATIN SMALL LETTER A WITH RING BELOW|
|Ą|[U+0104](https://www.compart.com/en/unicode/U+0104)|LATIN CAPITAL LETTER A WITH OGONEK|
|ą|[U+0105](https://www.compart.com/en/unicode/U+0105)|LATIN SMALL LETTER A WITH OGONEK|
|Ḃ|[U+1E02](https://www.compart.com/en/unicode/U+1E02)|LATIN CAPITAL LETTER B WITH DOT ABOVE|
|ḃ|[U+1E03](https://www.compart.com/en/unicode/U+1E03)|LATIN SMALL LETTER B WITH DOT ABOVE|
|Ḅ|[U+1E04](https://www.compart.com/en/unicode/U+1E04)|LATIN CAPITAL LETTER B WITH DOT BELOW|
|ḅ|[U+1E05](https://www.compart.com/en/unicode/U+1E05)|LATIN SMALL LETTER B WITH DOT BELOW|
|Ḇ|[U+1E06](https://www.compart.com/en/unicode/U+1E06)|LATIN CAPITAL LETTER B WITH LINE BELOW|
|ḇ|[U+1E07](https://www.compart.com/en/unicode/U+1E07)|LATIN SMALL LETTER B WITH LINE BELOW|
|Ć|[U+0106](https://www.compart.com/en/unicode/U+0106)|LATIN CAPITAL LETTER C WITH ACUTE|
|ć|[U+0107](https://www.compart.com/en/unicode/U+0107)|LATIN SMALL LETTER C WITH ACUTE|
|Ĉ|[U+0108](https://www.compart.com/en/unicode/U+0108)|LATIN CAPITAL LETTER C WITH CIRCUMFLEX|
|ĉ|[U+0109](https://www.compart.com/en/unicode/U+0109)|LATIN SMALL LETTER C WITH CIRCUMFLEX|
|Ċ|[U+010A](https://www.compart.com/en/unicode/U+010A)|LATIN CAPITAL LETTER C WITH DOT ABOVE|
|ċ|[U+010B](https://www.compart.com/en/unicode/U+010B)|LATIN SMALL LETTER C WITH DOT ABOVE|
|Č|[U+010C](https://www.compart.com/en/unicode/U+010C)|LATIN CAPITAL LETTER C WITH CARON|
|č|[U+010D](https://www.compart.com/en/unicode/U+010D)|LATIN SMALL LETTER C WITH CARON|
|Ç|[U+00C7](https://www.compart.com/en/unicode/U+00C7)|LATIN CAPITAL LETTER C WITH CEDILLA|
|ç|[U+00E7](https://www.compart.com/en/unicode/U+00E7)|LATIN SMALL LETTER C WITH CEDILLA|
|Ḉ|[U+1E08](https://www.compart.com/en/unicode/U+1E08)|LATIN CAPITAL LETTER C WITH CEDILLA AND ACUTE|
|ḉ|[U+1E09](https://www.compart.com/en/unicode/U+1E09)|LATIN SMALL LETTER C WITH CEDILLA AND ACUTE|
|Ḋ|[U+1E0A](https://www.compart.com/en/unicode/U+1E0A)|LATIN CAPITAL LETTER D WITH DOT ABOVE|
|ḋ|[U+1E0B](https://www.compart.com/en/unicode/U+1E0B)|LATIN SMALL LETTER D WITH DOT ABOVE|
|Ď|[U+010E](https://www.compart.com/en/unicode/U+010E)|LATIN CAPITAL LETTER D WITH CARON|
|ď|[U+010F](https://www.compart.com/en/unicode/U+010F)|LATIN SMALL LETTER D WITH CARON|
|Ḍ|[U+1E0C](https://www.compart.com/en/unicode/U+1E0C)|LATIN CAPITAL LETTER D WITH DOT BELOW|
|ḍ|[U+1E0D](https://www.compart.com/en/unicode/U+1E0D)|LATIN SMALL LETTER D WITH DOT BELOW|
|Ḑ|[U+1E10](https://www.compart.com/en/unicode/U+1E10)|LATIN CAPITAL LETTER D WITH CEDILLA|
|ḑ|[U+1E11](https://www.compart.com/en/unicode/U+1E11)|LATIN SMALL LETTER D WITH CEDILLA|
|Ḓ|[U+1E12](https://www.compart.com/en/unicode/U+1E12)|LATIN CAPITAL LETTER D WITH CIRCUMFLEX BELOW|
|ḓ|[U+1E13](https://www.compart.com/en/unicode/U+1E13)|LATIN SMALL LETTER D WITH CIRCUMFLEX BELOW|
|Ḏ|[U+1E0E](https://www.compart.com/en/unicode/U+1E0E)|LATIN CAPITAL LETTER D WITH LINE BELOW|
|ḏ|[U+1E0F](https://www.compart.com/en/unicode/U+1E0F)|LATIN SMALL LETTER D WITH LINE BELOW|
|È|[U+00C8](https://www.compart.com/en/unicode/U+00C8)|LATIN CAPITAL LETTER E WITH GRAVE|
|è|[U+00E8](https://www.compart.com/en/unicode/U+00E8)|LATIN SMALL LETTER E WITH GRAVE|
|É|[U+00C9](https://www.compart.com/en/unicode/U+00C9)|LATIN CAPITAL LETTER E WITH ACUTE|
|é|[U+00E9](https://www.compart.com/en/unicode/U+00E9)|LATIN SMALL LETTER E WITH ACUTE|
|Ê|[U+00CA](https://www.compart.com/en/unicode/U+00CA)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX|
|ê|[U+00EA](https://www.compart.com/en/unicode/U+00EA)|LATIN SMALL LETTER E WITH CIRCUMFLEX|
|Ề|[U+1EC0](https://www.compart.com/en/unicode/U+1EC0)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND GRAVE|
|ề|[U+1EC1](https://www.compart.com/en/unicode/U+1EC1)|LATIN SMALL LETTER E WITH CIRCUMFLEX AND GRAVE|
|Ế|[U+1EBE](https://www.compart.com/en/unicode/U+1EBE)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND ACUTE|
|ế|[U+1EBF](https://www.compart.com/en/unicode/U+1EBF)|LATIN SMALL LETTER E WITH CIRCUMFLEX AND ACUTE|
|Ễ|[U+1EC4](https://www.compart.com/en/unicode/U+1EC4)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND TILDE|
|ễ|[U+1EC5](https://www.compart.com/en/unicode/U+1EC5)|LATIN SMALL LETTER E WITH CIRCUMFLEX AND TILDE|
|Ể|[U+1EC2](https://www.compart.com/en/unicode/U+1EC2)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE|
|ể|[U+1EC3](https://www.compart.com/en/unicode/U+1EC3)|LATIN SMALL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE|
|Ẽ|[U+1EBC](https://www.compart.com/en/unicode/U+1EBC)|LATIN CAPITAL LETTER E WITH TILDE|
|ẽ|[U+1EBD](https://www.compart.com/en/unicode/U+1EBD)|LATIN SMALL LETTER E WITH TILDE|
|Ē|[U+0112](https://www.compart.com/en/unicode/U+0112)|LATIN CAPITAL LETTER E WITH MACRON|
|ē|[U+0113](https://www.compart.com/en/unicode/U+0113)|LATIN SMALL LETTER E WITH MACRON|
|Ḕ|[U+1E14](https://www.compart.com/en/unicode/U+1E14)|LATIN CAPITAL LETTER E WITH MACRON AND GRAVE|
|ḕ|[U+1E15](https://www.compart.com/en/unicode/U+1E15)|LATIN SMALL LETTER E WITH MACRON AND GRAVE|
|Ḗ|[U+1E16](https://www.compart.com/en/unicode/U+1E16)|LATIN CAPITAL LETTER E WITH MACRON AND ACUTE|
|ḗ|[U+1E17](https://www.compart.com/en/unicode/U+1E17)|LATIN SMALL LETTER E WITH MACRON AND ACUTE|
|Ĕ|[U+0114](https://www.compart.com/en/unicode/U+0114)|LATIN CAPITAL LETTER E WITH BREVE|
|ĕ|[U+0115](https://www.compart.com/en/unicode/U+0115)|LATIN SMALL LETTER E WITH BREVE|
|Ė|[U+0116](https://www.compart.com/en/unicode/U+0116)|LATIN CAPITAL LETTER E WITH DOT ABOVE|
|ė|[U+0117](https://www.compart.com/en/unicode/U+0117)|LATIN SMALL LETTER E WITH DOT ABOVE|
|Ë|[U+00CB](https://www.compart.com/en/unicode/U+00CB)|LATIN CAPITAL LETTER E WITH DIAERESIS|
|ë|[U+00EB](https://www.compart.com/en/unicode/U+00EB)|LATIN SMALL LETTER E WITH DIAERESIS|
|Ẻ|[U+1EBA](https://www.compart.com/en/unicode/U+1EBA)|LATIN CAPITAL LETTER E WITH HOOK ABOVE|
|ẻ|[U+1EBB](https://www.compart.com/en/unicode/U+1EBB)|LATIN SMALL LETTER E WITH HOOK ABOVE|
|Ě|[U+011A](https://www.compart.com/en/unicode/U+011A)|LATIN CAPITAL LETTER E WITH CARON|
|ě|[U+011B](https://www.compart.com/en/unicode/U+011B)|LATIN SMALL LETTER E WITH CARON|
|Ȅ|[U+0204](https://www.compart.com/en/unicode/U+0204)|LATIN CAPITAL LETTER E WITH DOUBLE GRAVE|
|ȅ|[U+0205](https://www.compart.com/en/unicode/U+0205)|LATIN SMALL LETTER E WITH DOUBLE GRAVE|
|Ȇ|[U+0206](https://www.compart.com/en/unicode/U+0206)|LATIN CAPITAL LETTER E WITH INVERTED BREVE|
|ȇ|[U+0207](https://www.compart.com/en/unicode/U+0207)|LATIN SMALL LETTER E WITH INVERTED BREVE|
|Ẹ|[U+1EB8](https://www.compart.com/en/unicode/U+1EB8)|LATIN CAPITAL LETTER E WITH DOT BELOW|
|ẹ|[U+1EB9](https://www.compart.com/en/unicode/U+1EB9)|LATIN SMALL LETTER E WITH DOT BELOW|
|Ệ|[U+1EC6](https://www.compart.com/en/unicode/U+1EC6)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND DOT BELOW|
|ệ|[U+1EC7](https://www.compart.com/en/unicode/U+1EC7)|LATIN SMALL LETTER E WITH CIRCUMFLEX AND DOT BELOW|
|Ȩ|[U+0228](https://www.compart.com/en/unicode/U+0228)|LATIN CAPITAL LETTER E WITH CEDILLA|
|ȩ|[U+0229](https://www.compart.com/en/unicode/U+0229)|LATIN SMALL LETTER E WITH CEDILLA|
|Ḝ|[U+1E1C](https://www.compart.com/en/unicode/U+1E1C)|LATIN CAPITAL LETTER E WITH CEDILLA AND BREVE|
|ḝ|[U+1E1D](https://www.compart.com/en/unicode/U+1E1D)|LATIN SMALL LETTER E WITH CEDILLA AND BREVE|
|Ę|[U+0118](https://www.compart.com/en/unicode/U+0118)|LATIN CAPITAL LETTER E WITH OGONEK|
|ę|[U+0119](https://www.compart.com/en/unicode/U+0119)|LATIN SMALL LETTER E WITH OGONEK|
|Ḙ|[U+1E18](https://www.compart.com/en/unicode/U+1E18)|LATIN CAPITAL LETTER E WITH CIRCUMFLEX BELOW|
|ḙ|[U+1E19](https://www.compart.com/en/unicode/U+1E19)|LATIN SMALL LETTER E WITH CIRCUMFLEX BELOW|
|Ḛ|[U+1E1A](https://www.compart.com/en/unicode/U+1E1A)|LATIN CAPITAL LETTER E WITH TILDE BELOW|
|ḛ|[U+1E1B](https://www.compart.com/en/unicode/U+1E1B)|LATIN SMALL LETTER E WITH TILDE BELOW|
|Ḟ|[U+1E1E](https://www.compart.com/en/unicode/U+1E1E)|LATIN CAPITAL LETTER F WITH DOT ABOVE|
|ḟ|[U+1E1F](https://www.compart.com/en/unicode/U+1E1F)|LATIN SMALL LETTER F WITH DOT ABOVE|
|Ǵ|[U+01F4](https://www.compart.com/en/unicode/U+01F4)|LATIN CAPITAL LETTER G WITH ACUTE|
|ǵ|[U+01F5](https://www.compart.com/en/unicode/U+01F5)|LATIN SMALL LETTER G WITH ACUTE|
|Ĝ|[U+011C](https://www.compart.com/en/unicode/U+011C)|LATIN CAPITAL LETTER G WITH CIRCUMFLEX|
|ĝ|[U+011D](https://www.compart.com/en/unicode/U+011D)|LATIN SMALL LETTER G WITH CIRCUMFLEX|
|Ḡ|[U+1E20](https://www.compart.com/en/unicode/U+1E20)|LATIN CAPITAL LETTER G WITH MACRON|
|ḡ|[U+1E21](https://www.compart.com/en/unicode/U+1E21)|LATIN SMALL LETTER G WITH MACRON|
|Ğ|[U+011E](https://www.compart.com/en/unicode/U+011E)|LATIN CAPITAL LETTER G WITH BREVE|
|ğ|[U+011F](https://www.compart.com/en/unicode/U+011F)|LATIN SMALL LETTER G WITH BREVE|
|Ġ|[U+0120](https://www.compart.com/en/unicode/U+0120)|LATIN CAPITAL LETTER G WITH DOT ABOVE|
|ġ|[U+0121](https://www.compart.com/en/unicode/U+0121)|LATIN SMALL LETTER G WITH DOT ABOVE|
|Ǧ|[U+01E6](https://www.compart.com/en/unicode/U+01E6)|LATIN CAPITAL LETTER G WITH CARON|
|ǧ|[U+01E7](https://www.compart.com/en/unicode/U+01E7)|LATIN SMALL LETTER G WITH CARON|
|Ģ|[U+0122](https://www.compart.com/en/unicode/U+0122)|LATIN CAPITAL LETTER G WITH CEDILLA|
|ģ|[U+0123](https://www.compart.com/en/unicode/U+0123)|LATIN SMALL LETTER G WITH CEDILLA|
|Ĥ|[U+0124](https://www.compart.com/en/unicode/U+0124)|LATIN CAPITAL LETTER H WITH CIRCUMFLEX|
|ĥ|[U+0125](https://www.compart.com/en/unicode/U+0125)|LATIN SMALL LETTER H WITH CIRCUMFLEX|
|Ḣ|[U+1E22](https://www.compart.com/en/unicode/U+1E22)|LATIN CAPITAL LETTER H WITH DOT ABOVE|
|ḣ|[U+1E23](https://www.compart.com/en/unicode/U+1E23)|LATIN SMALL LETTER H WITH DOT ABOVE|
|Ḧ|[U+1E26](https://www.compart.com/en/unicode/U+1E26)|LATIN CAPITAL LETTER H WITH DIAERESIS|
|ḧ|[U+1E27](https://www.compart.com/en/unicode/U+1E27)|LATIN SMALL LETTER H WITH DIAERESIS|
|Ȟ|[U+021E](https://www.compart.com/en/unicode/U+021E)|LATIN CAPITAL LETTER H WITH CARON|
|ȟ|[U+021F](https://www.compart.com/en/unicode/U+021F)|LATIN SMALL LETTER H WITH CARON|
|Ḥ|[U+1E24](https://www.compart.com/en/unicode/U+1E24)|LATIN CAPITAL LETTER H WITH DOT BELOW|
|ḥ|[U+1E25](https://www.compart.com/en/unicode/U+1E25)|LATIN SMALL LETTER H WITH DOT BELOW|
|Ḩ|[U+1E28](https://www.compart.com/en/unicode/U+1E28)|LATIN CAPITAL LETTER H WITH CEDILLA|
|ḩ|[U+1E29](https://www.compart.com/en/unicode/U+1E29)|LATIN SMALL LETTER H WITH CEDILLA|
|Ḫ|[U+1E2A](https://www.compart.com/en/unicode/U+1E2A)|LATIN CAPITAL LETTER H WITH BREVE BELOW|
|ḫ|[U+1E2B](https://www.compart.com/en/unicode/U+1E2B)|LATIN SMALL LETTER H WITH BREVE BELOW|
|ẖ|[U+1E96](https://www.compart.com/en/unicode/U+1E96)|LATIN SMALL LETTER H WITH LINE BELOW|
|i|[U+0069](https://www.compart.com/en/unicode/U+0069)|LATIN SMALL LETTER I|
|Ì|[U+00CC](https://www.compart.com/en/unicode/U+00CC)|LATIN CAPITAL LETTER I WITH GRAVE|
|ì|[U+00EC](https://www.compart.com/en/unicode/U+00EC)|LATIN SMALL LETTER I WITH GRAVE|
|Í|[U+00CD](https://www.compart.com/en/unicode/U+00CD)|LATIN CAPITAL LETTER I WITH ACUTE|
|í|[U+00ED](https://www.compart.com/en/unicode/U+00ED)|LATIN SMALL LETTER I WITH ACUTE|
|Î|[U+00CE](https://www.compart.com/en/unicode/U+00CE)|LATIN CAPITAL LETTER I WITH CIRCUMFLEX|
|î|[U+00EE](https://www.compart.com/en/unicode/U+00EE)|LATIN SMALL LETTER I WITH CIRCUMFLEX|
|Ĩ|[U+0128](https://www.compart.com/en/unicode/U+0128)|LATIN CAPITAL LETTER I WITH TILDE|
|ĩ|[U+0129](https://www.compart.com/en/unicode/U+0129)|LATIN SMALL LETTER I WITH TILDE|
|Ī|[U+012A](https://www.compart.com/en/unicode/U+012A)|LATIN CAPITAL LETTER I WITH MACRON|
|ī|[U+012B](https://www.compart.com/en/unicode/U+012B)|LATIN SMALL LETTER I WITH MACRON|
|Ĭ|[U+012C](https://www.compart.com/en/unicode/U+012C)|LATIN CAPITAL LETTER I WITH BREVE|
|ĭ|[U+012D](https://www.compart.com/en/unicode/U+012D)|LATIN SMALL LETTER I WITH BREVE|
|İ|[U+0130](https://www.compart.com/en/unicode/U+0130)|LATIN CAPITAL LETTER I WITH DOT ABOVE|
|Ï|[U+00CF](https://www.compart.com/en/unicode/U+00CF)|LATIN CAPITAL LETTER I WITH DIAERESIS|
|ï|[U+00EF](https://www.compart.com/en/unicode/U+00EF)|LATIN SMALL LETTER I WITH DIAERESIS|
|Ḯ|[U+1E2E](https://www.compart.com/en/unicode/U+1E2E)|LATIN CAPITAL LETTER I WITH DIAERESIS AND ACUTE|
|ḯ|[U+1E2F](https://www.compart.com/en/unicode/U+1E2F)|LATIN SMALL LETTER I WITH DIAERESIS AND ACUTE|
|Ỉ|[U+1EC8](https://www.compart.com/en/unicode/U+1EC8)|LATIN CAPITAL LETTER I WITH HOOK ABOVE|
|ỉ|[U+1EC9](https://www.compart.com/en/unicode/U+1EC9)|LATIN SMALL LETTER I WITH HOOK ABOVE|
|Ǐ|[U+01CF](https://www.compart.com/en/unicode/U+01CF)|LATIN CAPITAL LETTER I WITH CARON|
|ǐ|[U+01D0](https://www.compart.com/en/unicode/U+01D0)|LATIN SMALL LETTER I WITH CARON|
|Ȉ|[U+0208](https://www.compart.com/en/unicode/U+0208)|LATIN CAPITAL LETTER I WITH DOUBLE GRAVE|
|ȉ|[U+0209](https://www.compart.com/en/unicode/U+0209)|LATIN SMALL LETTER I WITH DOUBLE GRAVE|
|Ȋ|[U+020A](https://www.compart.com/en/unicode/U+020A)|LATIN CAPITAL LETTER I WITH INVERTED BREVE|
|ȋ|[U+020B](https://www.compart.com/en/unicode/U+020B)|LATIN SMALL LETTER I WITH INVERTED BREVE|
|Ị|[U+1ECA](https://www.compart.com/en/unicode/U+1ECA)|LATIN CAPITAL LETTER I WITH DOT BELOW|
|ị|[U+1ECB](https://www.compart.com/en/unicode/U+1ECB)|LATIN SMALL LETTER I WITH DOT BELOW|
|Į|[U+012E](https://www.compart.com/en/unicode/U+012E)|LATIN CAPITAL LETTER I WITH OGONEK|
|į|[U+012F](https://www.compart.com/en/unicode/U+012F)|LATIN SMALL LETTER I WITH OGONEK|
|Ḭ|[U+1E2C](https://www.compart.com/en/unicode/U+1E2C)|LATIN CAPITAL LETTER I WITH TILDE BELOW|
|ḭ|[U+1E2D](https://www.compart.com/en/unicode/U+1E2D)|LATIN SMALL LETTER I WITH TILDE BELOW|
|Ĵ|[U+0134](https://www.compart.com/en/unicode/U+0134)|LATIN CAPITAL LETTER J WITH CIRCUMFLEX|
|ĵ|[U+0135](https://www.compart.com/en/unicode/U+0135)|LATIN SMALL LETTER J WITH CIRCUMFLEX|
|ǰ|[U+01F0](https://www.compart.com/en/unicode/U+01F0)|LATIN SMALL LETTER J WITH CARON|
|Ḱ|[U+1E30](https://www.compart.com/en/unicode/U+1E30)|LATIN CAPITAL LETTER K WITH ACUTE|
|ḱ|[U+1E31](https://www.compart.com/en/unicode/U+1E31)|LATIN SMALL LETTER K WITH ACUTE|
|Ǩ|[U+01E8](https://www.compart.com/en/unicode/U+01E8)|LATIN CAPITAL LETTER K WITH CARON|
|ǩ|[U+01E9](https://www.compart.com/en/unicode/U+01E9)|LATIN SMALL LETTER K WITH CARON|
|Ḳ|[U+1E32](https://www.compart.com/en/unicode/U+1E32)|LATIN CAPITAL LETTER K WITH DOT BELOW|
|ḳ|[U+1E33](https://www.compart.com/en/unicode/U+1E33)|LATIN SMALL LETTER K WITH DOT BELOW|
|Ķ|[U+0136](https://www.compart.com/en/unicode/U+0136)|LATIN CAPITAL LETTER K WITH CEDILLA|
|ķ|[U+0137](https://www.compart.com/en/unicode/U+0137)|LATIN SMALL LETTER K WITH CEDILLA|
|Ḵ|[U+1E34](https://www.compart.com/en/unicode/U+1E34)|LATIN CAPITAL LETTER K WITH LINE BELOW|
|ḵ|[U+1E35](https://www.compart.com/en/unicode/U+1E35)|LATIN SMALL LETTER K WITH LINE BELOW|
|Ĺ|[U+0139](https://www.compart.com/en/unicode/U+0139)|LATIN CAPITAL LETTER L WITH ACUTE|
|ĺ|[U+013A](https://www.compart.com/en/unicode/U+013A)|LATIN SMALL LETTER L WITH ACUTE|
|Ľ|[U+013D](https://www.compart.com/en/unicode/U+013D)|LATIN CAPITAL LETTER L WITH CARON|
|ľ|[U+013E](https://www.compart.com/en/unicode/U+013E)|LATIN SMALL LETTER L WITH CARON|
|Ḷ|[U+1E36](https://www.compart.com/en/unicode/U+1E36)|LATIN CAPITAL LETTER L WITH DOT BELOW|
|ḷ|[U+1E37](https://www.compart.com/en/unicode/U+1E37)|LATIN SMALL LETTER L WITH DOT BELOW|
|Ḹ|[U+1E38](https://www.compart.com/en/unicode/U+1E38)|LATIN CAPITAL LETTER L WITH DOT BELOW AND MACRON|
|ḹ|[U+1E39](https://www.compart.com/en/unicode/U+1E39)|LATIN SMALL LETTER L WITH DOT BELOW AND MACRON|
|Ļ|[U+013B](https://www.compart.com/en/unicode/U+013B)|LATIN CAPITAL LETTER L WITH CEDILLA|
|ļ|[U+013C](https://www.compart.com/en/unicode/U+013C)|LATIN SMALL LETTER L WITH CEDILLA|
|Ḽ|[U+1E3C](https://www.compart.com/en/unicode/U+1E3C)|LATIN CAPITAL LETTER L WITH CIRCUMFLEX BELOW|
|ḽ|[U+1E3D](https://www.compart.com/en/unicode/U+1E3D)|LATIN SMALL LETTER L WITH CIRCUMFLEX BELOW|
|Ḻ|[U+1E3A](https://www.compart.com/en/unicode/U+1E3A)|LATIN CAPITAL LETTER L WITH LINE BELOW|
|ḻ|[U+1E3B](https://www.compart.com/en/unicode/U+1E3B)|LATIN SMALL LETTER L WITH LINE BELOW|
|Ḿ|[U+1E3E](https://www.compart.com/en/unicode/U+1E3E)|LATIN CAPITAL LETTER M WITH ACUTE|
|ḿ|[U+1E3F](https://www.compart.com/en/unicode/U+1E3F)|LATIN SMALL LETTER M WITH ACUTE|
|Ṁ|[U+1E40](https://www.compart.com/en/unicode/U+1E40)|LATIN CAPITAL LETTER M WITH DOT ABOVE|
|ṁ|[U+1E41](https://www.compart.com/en/unicode/U+1E41)|LATIN SMALL LETTER M WITH DOT ABOVE|
|Ṃ|[U+1E42](https://www.compart.com/en/unicode/U+1E42)|LATIN CAPITAL LETTER M WITH DOT BELOW|
|ṃ|[U+1E43](https://www.compart.com/en/unicode/U+1E43)|LATIN SMALL LETTER M WITH DOT BELOW|
|Ǹ|[U+01F8](https://www.compart.com/en/unicode/U+01F8)|LATIN CAPITAL LETTER N WITH GRAVE|
|ǹ|[U+01F9](https://www.compart.com/en/unicode/U+01F9)|LATIN SMALL LETTER N WITH GRAVE|
|Ń|[U+0143](https://www.compart.com/en/unicode/U+0143)|LATIN CAPITAL LETTER N WITH ACUTE|
|ń|[U+0144](https://www.compart.com/en/unicode/U+0144)|LATIN SMALL LETTER N WITH ACUTE|
|Ñ|[U+00D1](https://www.compart.com/en/unicode/U+00D1)|LATIN CAPITAL LETTER N WITH TILDE|
|ñ|[U+00F1](https://www.compart.com/en/unicode/U+00F1)|LATIN SMALL LETTER N WITH TILDE|
|Ṅ|[U+1E44](https://www.compart.com/en/unicode/U+1E44)|LATIN CAPITAL LETTER N WITH DOT ABOVE|
|ṅ|[U+1E45](https://www.compart.com/en/unicode/U+1E45)|LATIN SMALL LETTER N WITH DOT ABOVE|
|Ň|[U+0147](https://www.compart.com/en/unicode/U+0147)|LATIN CAPITAL LETTER N WITH CARON|
|ň|[U+0148](https://www.compart.com/en/unicode/U+0148)|LATIN SMALL LETTER N WITH CARON|
|Ṇ|[U+1E46](https://www.compart.com/en/unicode/U+1E46)|LATIN CAPITAL LETTER N WITH DOT BELOW|
|ṇ|[U+1E47](https://www.compart.com/en/unicode/U+1E47)|LATIN SMALL LETTER N WITH DOT BELOW|
|Ņ|[U+0145](https://www.compart.com/en/unicode/U+0145)|LATIN CAPITAL LETTER N WITH CEDILLA|
|ņ|[U+0146](https://www.compart.com/en/unicode/U+0146)|LATIN SMALL LETTER N WITH CEDILLA|
|Ṋ|[U+1E4A](https://www.compart.com/en/unicode/U+1E4A)|LATIN CAPITAL LETTER N WITH CIRCUMFLEX BELOW|
|ṋ|[U+1E4B](https://www.compart.com/en/unicode/U+1E4B)|LATIN SMALL LETTER N WITH CIRCUMFLEX BELOW|
|Ṉ|[U+1E48](https://www.compart.com/en/unicode/U+1E48)|LATIN CAPITAL LETTER N WITH LINE BELOW|
|ṉ|[U+1E49](https://www.compart.com/en/unicode/U+1E49)|LATIN SMALL LETTER N WITH LINE BELOW|
|Ò|[U+00D2](https://www.compart.com/en/unicode/U+00D2)|LATIN CAPITAL LETTER O WITH GRAVE|
|ò|[U+00F2](https://www.compart.com/en/unicode/U+00F2)|LATIN SMALL LETTER O WITH GRAVE|
|Ó|[U+00D3](https://www.compart.com/en/unicode/U+00D3)|LATIN CAPITAL LETTER O WITH ACUTE|
|ó|[U+00F3](https://www.compart.com/en/unicode/U+00F3)|LATIN SMALL LETTER O WITH ACUTE|
|Ô|[U+00D4](https://www.compart.com/en/unicode/U+00D4)|LATIN CAPITAL LETTER O WITH CIRCUMFLEX|
|ô|[U+00F4](https://www.compart.com/en/unicode/U+00F4)|LATIN SMALL LETTER O WITH CIRCUMFLEX|
|Ồ|[U+1ED2](https://www.compart.com/en/unicode/U+1ED2)|LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND GRAVE|
|ồ|[U+1ED3](https://www.compart.com/en/unicode/U+1ED3)|LATIN SMALL LETTER O WITH CIRCUMFLEX AND GRAVE|
|Ố|[U+1ED0](https://www.compart.com/en/unicode/U+1ED0)|LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND ACUTE|
|ố|[U+1ED1](https://www.compart.com/en/unicode/U+1ED1)|LATIN SMALL LETTER O WITH CIRCUMFLEX AND ACUTE|
|Ỗ|[U+1ED6](https://www.compart.com/en/unicode/U+1ED6)|LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND TILDE|
|ỗ|[U+1ED7](https://www.compart.com/en/unicode/U+1ED7)|LATIN SMALL LETTER O WITH CIRCUMFLEX AND TILDE|
|Ổ|[U+1ED4](https://www.compart.com/en/unicode/U+1ED4)|LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE|
|ổ|[U+1ED5](https://www.compart.com/en/unicode/U+1ED5)|LATIN SMALL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE|
|Õ|[U+00D5](https://www.compart.com/en/unicode/U+00D5)|LATIN CAPITAL LETTER O WITH TILDE|
|õ|[U+00F5](https://www.compart.com/en/unicode/U+00F5)|LATIN SMALL LETTER O WITH TILDE|
|Ṍ|[U+1E4C](https://www.compart.com/en/unicode/U+1E4C)|LATIN CAPITAL LETTER O WITH TILDE AND ACUTE|
|ṍ|[U+1E4D](https://www.compart.com/en/unicode/U+1E4D)|LATIN SMALL LETTER O WITH TILDE AND ACUTE|
|Ȭ|[U+022C](https://www.compart.com/en/unicode/U+022C)|LATIN CAPITAL LETTER O WITH TILDE AND MACRON|
|ȭ|[U+022D](https://www.compart.com/en/unicode/U+022D)|LATIN SMALL LETTER O WITH TILDE AND MACRON|
|Ṏ|[U+1E4E](https://www.compart.com/en/unicode/U+1E4E)|LATIN CAPITAL LETTER O WITH TILDE AND DIAERESIS|
|ṏ|[U+1E4F](https://www.compart.com/en/unicode/U+1E4F)|LATIN SMALL LETTER O WITH TILDE AND DIAERESIS|
|Ō|[U+014C](https://www.compart.com/en/unicode/U+014C)|LATIN CAPITAL LETTER O WITH MACRON|
|ō|[U+014D](https://www.compart.com/en/unicode/U+014D)|LATIN SMALL LETTER O WITH MACRON|
|Ṑ|[U+1E50](https://www.compart.com/en/unicode/U+1E50)|LATIN CAPITAL LETTER O WITH MACRON AND GRAVE|
|ṑ|[U+1E51](https://www.compart.com/en/unicode/U+1E51)|LATIN SMALL LETTER O WITH MACRON AND GRAVE|
|Ṓ|[U+1E52](https://www.compart.com/en/unicode/U+1E52)|LATIN CAPITAL LETTER O WITH MACRON AND ACUTE|
|ṓ|[U+1E53](https://www.compart.com/en/unicode/U+1E53)|LATIN SMALL LETTER O WITH MACRON AND ACUTE|
|Ŏ|[U+014E](https://www.compart.com/en/unicode/U+014E)|LATIN CAPITAL LETTER O WITH BREVE|
|ŏ|[U+014F](https://www.compart.com/en/unicode/U+014F)|LATIN SMALL LETTER O WITH BREVE|
|Ȯ|[U+022E](https://www.compart.com/en/unicode/U+022E)|LATIN CAPITAL LETTER O WITH DOT ABOVE|
|ȯ|[U+022F](https://www.compart.com/en/unicode/U+022F)|LATIN SMALL LETTER O WITH DOT ABOVE|
|Ȱ|[U+0230](https://www.compart.com/en/unicode/U+0230)|LATIN CAPITAL LETTER O WITH DOT ABOVE AND MACRON|
|ȱ|[U+0231](https://www.compart.com/en/unicode/U+0231)|LATIN SMALL LETTER O WITH DOT ABOVE AND MACRON|
|Ö|[U+00D6](https://www.compart.com/en/unicode/U+00D6)|LATIN CAPITAL LETTER O WITH DIAERESIS|
|ö|[U+00F6](https://www.compart.com/en/unicode/U+00F6)|LATIN SMALL LETTER O WITH DIAERESIS|
|Ȫ|[U+022A](https://www.compart.com/en/unicode/U+022A)|LATIN CAPITAL LETTER O WITH DIAERESIS AND MACRON|
|ȫ|[U+022B](https://www.compart.com/en/unicode/U+022B)|LATIN SMALL LETTER O WITH DIAERESIS AND MACRON|
|Ỏ|[U+1ECE](https://www.compart.com/en/unicode/U+1ECE)|LATIN CAPITAL LETTER O WITH HOOK ABOVE|
|ỏ|[U+1ECF](https://www.compart.com/en/unicode/U+1ECF)|LATIN SMALL LETTER O WITH HOOK ABOVE|
|Ő|[U+0150](https://www.compart.com/en/unicode/U+0150)|LATIN CAPITAL LETTER O WITH DOUBLE ACUTE|
|ő|[U+0151](https://www.compart.com/en/unicode/U+0151)|LATIN SMALL LETTER O WITH DOUBLE ACUTE|
|Ǒ|[U+01D1](https://www.compart.com/en/unicode/U+01D1)|LATIN CAPITAL LETTER O WITH CARON|
|ǒ|[U+01D2](https://www.compart.com/en/unicode/U+01D2)|LATIN SMALL LETTER O WITH CARON|
|Ȍ|[U+020C](https://www.compart.com/en/unicode/U+020C)|LATIN CAPITAL LETTER O WITH DOUBLE GRAVE|
|ȍ|[U+020D](https://www.compart.com/en/unicode/U+020D)|LATIN SMALL LETTER O WITH DOUBLE GRAVE|
|Ȏ|[U+020E](https://www.compart.com/en/unicode/U+020E)|LATIN CAPITAL LETTER O WITH INVERTED BREVE|
|ȏ|[U+020F](https://www.compart.com/en/unicode/U+020F)|LATIN SMALL LETTER O WITH INVERTED BREVE|
|Ơ|[U+01A0](https://www.compart.com/en/unicode/U+01A0)|LATIN CAPITAL LETTER O WITH HORN|
|Ơ|[U+01A0](https://www.compart.com/en/unicode/U+01A0)|LATIN CAPITAL LETTER O WITH HORN|
|ơ|[U+01A1](https://www.compart.com/en/unicode/U+01A1)|LATIN SMALL LETTER O WITH HORN|
|ơ|[U+01A1](https://www.compart.com/en/unicode/U+01A1)|LATIN SMALL LETTER O WITH HORN|
|Ờ|[U+1EDC](https://www.compart.com/en/unicode/U+1EDC)|LATIN CAPITAL LETTER O WITH HORN AND GRAVE|
|ờ|[U+1EDD](https://www.compart.com/en/unicode/U+1EDD)|LATIN SMALL LETTER O WITH HORN AND GRAVE|
|Ớ|[U+1EDA](https://www.compart.com/en/unicode/U+1EDA)|LATIN CAPITAL LETTER O WITH HORN AND ACUTE|
|ớ|[U+1EDB](https://www.compart.com/en/unicode/U+1EDB)|LATIN SMALL LETTER O WITH HORN AND ACUTE|
|Ỡ|[U+1EE0](https://www.compart.com/en/unicode/U+1EE0)|LATIN CAPITAL LETTER O WITH HORN AND TILDE|
|ỡ|[U+1EE1](https://www.compart.com/en/unicode/U+1EE1)|LATIN SMALL LETTER O WITH HORN AND TILDE|
|Ở|[U+1EDE](https://www.compart.com/en/unicode/U+1EDE)|LATIN CAPITAL LETTER O WITH HORN AND HOOK ABOVE|
|ở|[U+1EDF](https://www.compart.com/en/unicode/U+1EDF)|LATIN SMALL LETTER O WITH HORN AND HOOK ABOVE|
|Ợ|[U+1EE2](https://www.compart.com/en/unicode/U+1EE2)|LATIN CAPITAL LETTER O WITH HORN AND DOT BELOW|
|ợ|[U+1EE3](https://www.compart.com/en/unicode/U+1EE3)|LATIN SMALL LETTER O WITH HORN AND DOT BELOW|
|Ọ|[U+1ECC](https://www.compart.com/en/unicode/U+1ECC)|LATIN CAPITAL LETTER O WITH DOT BELOW|
|ọ|[U+1ECD](https://www.compart.com/en/unicode/U+1ECD)|LATIN SMALL LETTER O WITH DOT BELOW|
|Ộ|[U+1ED8](https://www.compart.com/en/unicode/U+1ED8)|LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND DOT BELOW|
|ộ|[U+1ED9](https://www.compart.com/en/unicode/U+1ED9)|LATIN SMALL LETTER O WITH CIRCUMFLEX AND DOT BELOW|
|Ǫ|[U+01EA](https://www.compart.com/en/unicode/U+01EA)|LATIN CAPITAL LETTER O WITH OGONEK|
|ǫ|[U+01EB](https://www.compart.com/en/unicode/U+01EB)|LATIN SMALL LETTER O WITH OGONEK|
|Ǭ|[U+01EC](https://www.compart.com/en/unicode/U+01EC)|LATIN CAPITAL LETTER O WITH OGONEK AND MACRON|
|ǭ|[U+01ED](https://www.compart.com/en/unicode/U+01ED)|LATIN SMALL LETTER O WITH OGONEK AND MACRON|
|Ṕ|[U+1E54](https://www.compart.com/en/unicode/U+1E54)|LATIN CAPITAL LETTER P WITH ACUTE|
|ṕ|[U+1E55](https://www.compart.com/en/unicode/U+1E55)|LATIN SMALL LETTER P WITH ACUTE|
|Ṗ|[U+1E56](https://www.compart.com/en/unicode/U+1E56)|LATIN CAPITAL LETTER P WITH DOT ABOVE|
|ṗ|[U+1E57](https://www.compart.com/en/unicode/U+1E57)|LATIN SMALL LETTER P WITH DOT ABOVE|
|Ŕ|[U+0154](https://www.compart.com/en/unicode/U+0154)|LATIN CAPITAL LETTER R WITH ACUTE|
|ŕ|[U+0155](https://www.compart.com/en/unicode/U+0155)|LATIN SMALL LETTER R WITH ACUTE|
|Ṙ|[U+1E58](https://www.compart.com/en/unicode/U+1E58)|LATIN CAPITAL LETTER R WITH DOT ABOVE|
|ṙ|[U+1E59](https://www.compart.com/en/unicode/U+1E59)|LATIN SMALL LETTER R WITH DOT ABOVE|
|Ř|[U+0158](https://www.compart.com/en/unicode/U+0158)|LATIN CAPITAL LETTER R WITH CARON|
|ř|[U+0159](https://www.compart.com/en/unicode/U+0159)|LATIN SMALL LETTER R WITH CARON|
|Ȑ|[U+0210](https://www.compart.com/en/unicode/U+0210)|LATIN CAPITAL LETTER R WITH DOUBLE GRAVE|
|ȑ|[U+0211](https://www.compart.com/en/unicode/U+0211)|LATIN SMALL LETTER R WITH DOUBLE GRAVE|
|Ȓ|[U+0212](https://www.compart.com/en/unicode/U+0212)|LATIN CAPITAL LETTER R WITH INVERTED BREVE|
|ȓ|[U+0213](https://www.compart.com/en/unicode/U+0213)|LATIN SMALL LETTER R WITH INVERTED BREVE|
|Ṛ|[U+1E5A](https://www.compart.com/en/unicode/U+1E5A)|LATIN CAPITAL LETTER R WITH DOT BELOW|
|ṛ|[U+1E5B](https://www.compart.com/en/unicode/U+1E5B)|LATIN SMALL LETTER R WITH DOT BELOW|
|Ṝ|[U+1E5C](https://www.compart.com/en/unicode/U+1E5C)|LATIN CAPITAL LETTER R WITH DOT BELOW AND MACRON|
|ṝ|[U+1E5D](https://www.compart.com/en/unicode/U+1E5D)|LATIN SMALL LETTER R WITH DOT BELOW AND MACRON|
|Ŗ|[U+0156](https://www.compart.com/en/unicode/U+0156)|LATIN CAPITAL LETTER R WITH CEDILLA|
|ŗ|[U+0157](https://www.compart.com/en/unicode/U+0157)|LATIN SMALL LETTER R WITH CEDILLA|
|Ṟ|[U+1E5E](https://www.compart.com/en/unicode/U+1E5E)|LATIN CAPITAL LETTER R WITH LINE BELOW|
|ṟ|[U+1E5F](https://www.compart.com/en/unicode/U+1E5F)|LATIN SMALL LETTER R WITH LINE BELOW|
|Ś|[U+015A](https://www.compart.com/en/unicode/U+015A)|LATIN CAPITAL LETTER S WITH ACUTE|
|ś|[U+015B](https://www.compart.com/en/unicode/U+015B)|LATIN SMALL LETTER S WITH ACUTE|
|Ṥ|[U+1E64](https://www.compart.com/en/unicode/U+1E64)|LATIN CAPITAL LETTER S WITH ACUTE AND DOT ABOVE|
|ṥ|[U+1E65](https://www.compart.com/en/unicode/U+1E65)|LATIN SMALL LETTER S WITH ACUTE AND DOT ABOVE|
|Ŝ|[U+015C](https://www.compart.com/en/unicode/U+015C)|LATIN CAPITAL LETTER S WITH CIRCUMFLEX|
|ŝ|[U+015D](https://www.compart.com/en/unicode/U+015D)|LATIN SMALL LETTER S WITH CIRCUMFLEX|
|Ṡ|[U+1E60](https://www.compart.com/en/unicode/U+1E60)|LATIN CAPITAL LETTER S WITH DOT ABOVE|
|ṡ|[U+1E61](https://www.compart.com/en/unicode/U+1E61)|LATIN SMALL LETTER S WITH DOT ABOVE|
|Š|[U+0160](https://www.compart.com/en/unicode/U+0160)|LATIN CAPITAL LETTER S WITH CARON|
|š|[U+0161](https://www.compart.com/en/unicode/U+0161)|LATIN SMALL LETTER S WITH CARON|
|Ṧ|[U+1E66](https://www.compart.com/en/unicode/U+1E66)|LATIN CAPITAL LETTER S WITH CARON AND DOT ABOVE|
|ṧ|[U+1E67](https://www.compart.com/en/unicode/U+1E67)|LATIN SMALL LETTER S WITH CARON AND DOT ABOVE|
|Ṣ|[U+1E62](https://www.compart.com/en/unicode/U+1E62)|LATIN CAPITAL LETTER S WITH DOT BELOW|
|ṣ|[U+1E63](https://www.compart.com/en/unicode/U+1E63)|LATIN SMALL LETTER S WITH DOT BELOW|
|Ṩ|[U+1E68](https://www.compart.com/en/unicode/U+1E68)|LATIN CAPITAL LETTER S WITH DOT BELOW AND DOT ABOVE|
|ṩ|[U+1E69](https://www.compart.com/en/unicode/U+1E69)|LATIN SMALL LETTER S WITH DOT BELOW AND DOT ABOVE|
|Ș|[U+0218](https://www.compart.com/en/unicode/U+0218)|LATIN CAPITAL LETTER S WITH COMMA BELOW|
|Ș|[U+0218](https://www.compart.com/en/unicode/U+0218)|LATIN CAPITAL LETTER S WITH COMMA BELOW|
|ș|[U+0219](https://www.compart.com/en/unicode/U+0219)|LATIN SMALL LETTER S WITH COMMA BELOW|
|ș|[U+0219](https://www.compart.com/en/unicode/U+0219)|LATIN SMALL LETTER S WITH COMMA BELOW|
|Ş|[U+015E](https://www.compart.com/en/unicode/U+015E)|LATIN CAPITAL LETTER S WITH CEDILLA|
|ş|[U+015F](https://www.compart.com/en/unicode/U+015F)|LATIN SMALL LETTER S WITH CEDILLA|
|Ṫ|[U+1E6A](https://www.compart.com/en/unicode/U+1E6A)|LATIN CAPITAL LETTER T WITH DOT ABOVE|
|ṫ|[U+1E6B](https://www.compart.com/en/unicode/U+1E6B)|LATIN SMALL LETTER T WITH DOT ABOVE|
|ẗ|[U+1E97](https://www.compart.com/en/unicode/U+1E97)|LATIN SMALL LETTER T WITH DIAERESIS|
|Ť|[U+0164](https://www.compart.com/en/unicode/U+0164)|LATIN CAPITAL LETTER T WITH CARON|
|ť|[U+0165](https://www.compart.com/en/unicode/U+0165)|LATIN SMALL LETTER T WITH CARON|
|Ṭ|[U+1E6C](https://www.compart.com/en/unicode/U+1E6C)|LATIN CAPITAL LETTER T WITH DOT BELOW|
|ṭ|[U+1E6D](https://www.compart.com/en/unicode/U+1E6D)|LATIN SMALL LETTER T WITH DOT BELOW|
|Ț|[U+021A](https://www.compart.com/en/unicode/U+021A)|LATIN CAPITAL LETTER T WITH COMMA BELOW|
|ț|[U+021B](https://www.compart.com/en/unicode/U+021B)|LATIN SMALL LETTER T WITH COMMA BELOW|
|Ţ|[U+0162](https://www.compart.com/en/unicode/U+0162)|LATIN CAPITAL LETTER T WITH CEDILLA|
|ţ|[U+0163](https://www.compart.com/en/unicode/U+0163)|LATIN SMALL LETTER T WITH CEDILLA|
|Ṱ|[U+1E70](https://www.compart.com/en/unicode/U+1E70)|LATIN CAPITAL LETTER T WITH CIRCUMFLEX BELOW|
|ṱ|[U+1E71](https://www.compart.com/en/unicode/U+1E71)|LATIN SMALL LETTER T WITH CIRCUMFLEX BELOW|
|Ṯ|[U+1E6E](https://www.compart.com/en/unicode/U+1E6E)|LATIN CAPITAL LETTER T WITH LINE BELOW|
|ṯ|[U+1E6F](https://www.compart.com/en/unicode/U+1E6F)|LATIN SMALL LETTER T WITH LINE BELOW|
|Ù|[U+00D9](https://www.compart.com/en/unicode/U+00D9)|LATIN CAPITAL LETTER U WITH GRAVE|
|ù|[U+00F9](https://www.compart.com/en/unicode/U+00F9)|LATIN SMALL LETTER U WITH GRAVE|
|Ú|[U+00DA](https://www.compart.com/en/unicode/U+00DA)|LATIN CAPITAL LETTER U WITH ACUTE|
|ú|[U+00FA](https://www.compart.com/en/unicode/U+00FA)|LATIN SMALL LETTER U WITH ACUTE|
|Û|[U+00DB](https://www.compart.com/en/unicode/U+00DB)|LATIN CAPITAL LETTER U WITH CIRCUMFLEX|
|û|[U+00FB](https://www.compart.com/en/unicode/U+00FB)|LATIN SMALL LETTER U WITH CIRCUMFLEX|
|Ũ|[U+0168](https://www.compart.com/en/unicode/U+0168)|LATIN CAPITAL LETTER U WITH TILDE|
|ũ|[U+0169](https://www.compart.com/en/unicode/U+0169)|LATIN SMALL LETTER U WITH TILDE|
|Ṹ|[U+1E78](https://www.compart.com/en/unicode/U+1E78)|LATIN CAPITAL LETTER U WITH TILDE AND ACUTE|
|ṹ|[U+1E79](https://www.compart.com/en/unicode/U+1E79)|LATIN SMALL LETTER U WITH TILDE AND ACUTE|
|Ū|[U+016A](https://www.compart.com/en/unicode/U+016A)|LATIN CAPITAL LETTER U WITH MACRON|
|ū|[U+016B](https://www.compart.com/en/unicode/U+016B)|LATIN SMALL LETTER U WITH MACRON|
|Ṻ|[U+1E7A](https://www.compart.com/en/unicode/U+1E7A)|LATIN CAPITAL LETTER U WITH MACRON AND DIAERESIS|
|ṻ|[U+1E7B](https://www.compart.com/en/unicode/U+1E7B)|LATIN SMALL LETTER U WITH MACRON AND DIAERESIS|
|Ŭ|[U+016C](https://www.compart.com/en/unicode/U+016C)|LATIN CAPITAL LETTER U WITH BREVE|
|ŭ|[U+016D](https://www.compart.com/en/unicode/U+016D)|LATIN SMALL LETTER U WITH BREVE|
|Ü|[U+00DC](https://www.compart.com/en/unicode/U+00DC)|LATIN CAPITAL LETTER U WITH DIAERESIS|
|ü|[U+00FC](https://www.compart.com/en/unicode/U+00FC)|LATIN SMALL LETTER U WITH DIAERESIS|
|Ǜ|[U+01DB](https://www.compart.com/en/unicode/U+01DB)|LATIN CAPITAL LETTER U WITH DIAERESIS AND GRAVE|
|ǜ|[U+01DC](https://www.compart.com/en/unicode/U+01DC)|LATIN SMALL LETTER U WITH DIAERESIS AND GRAVE|
|Ǘ|[U+01D7](https://www.compart.com/en/unicode/U+01D7)|LATIN CAPITAL LETTER U WITH DIAERESIS AND ACUTE|
|ǘ|[U+01D8](https://www.compart.com/en/unicode/U+01D8)|LATIN SMALL LETTER U WITH DIAERESIS AND ACUTE|
|Ǖ|[U+01D5](https://www.compart.com/en/unicode/U+01D5)|LATIN CAPITAL LETTER U WITH DIAERESIS AND MACRON|
|ǖ|[U+01D6](https://www.compart.com/en/unicode/U+01D6)|LATIN SMALL LETTER U WITH DIAERESIS AND MACRON|
|Ǚ|[U+01D9](https://www.compart.com/en/unicode/U+01D9)|LATIN CAPITAL LETTER U WITH DIAERESIS AND CARON|
|ǚ|[U+01DA](https://www.compart.com/en/unicode/U+01DA)|LATIN SMALL LETTER U WITH DIAERESIS AND CARON|
|Ủ|[U+1EE6](https://www.compart.com/en/unicode/U+1EE6)|LATIN CAPITAL LETTER U WITH HOOK ABOVE|
|ủ|[U+1EE7](https://www.compart.com/en/unicode/U+1EE7)|LATIN SMALL LETTER U WITH HOOK ABOVE|
|Ů|[U+016E](https://www.compart.com/en/unicode/U+016E)|LATIN CAPITAL LETTER U WITH RING ABOVE|
|ů|[U+016F](https://www.compart.com/en/unicode/U+016F)|LATIN SMALL LETTER U WITH RING ABOVE|
|Ű|[U+0170](https://www.compart.com/en/unicode/U+0170)|LATIN CAPITAL LETTER U WITH DOUBLE ACUTE|
|ű|[U+0171](https://www.compart.com/en/unicode/U+0171)|LATIN SMALL LETTER U WITH DOUBLE ACUTE|
|Ǔ|[U+01D3](https://www.compart.com/en/unicode/U+01D3)|LATIN CAPITAL LETTER U WITH CARON|
|ǔ|[U+01D4](https://www.compart.com/en/unicode/U+01D4)|LATIN SMALL LETTER U WITH CARON|
|Ȕ|[U+0214](https://www.compart.com/en/unicode/U+0214)|LATIN CAPITAL LETTER U WITH DOUBLE GRAVE|
|ȕ|[U+0215](https://www.compart.com/en/unicode/U+0215)|LATIN SMALL LETTER U WITH DOUBLE GRAVE|
|Ȗ|[U+0216](https://www.compart.com/en/unicode/U+0216)|LATIN CAPITAL LETTER U WITH INVERTED BREVE|
|ȗ|[U+0217](https://www.compart.com/en/unicode/U+0217)|LATIN SMALL LETTER U WITH INVERTED BREVE|
|Ư|[U+01AF](https://www.compart.com/en/unicode/U+01AF)|LATIN CAPITAL LETTER U WITH HORN|
|ư|[U+01B0](https://www.compart.com/en/unicode/U+01B0)|LATIN SMALL LETTER U WITH HORN|
|Ừ|[U+1EEA](https://www.compart.com/en/unicode/U+1EEA)|LATIN CAPITAL LETTER U WITH HORN AND GRAVE|
|ừ|[U+1EEB](https://www.compart.com/en/unicode/U+1EEB)|LATIN SMALL LETTER U WITH HORN AND GRAVE|
|Ứ|[U+1EE8](https://www.compart.com/en/unicode/U+1EE8)|LATIN CAPITAL LETTER U WITH HORN AND ACUTE|
|ứ|[U+1EE9](https://www.compart.com/en/unicode/U+1EE9)|LATIN SMALL LETTER U WITH HORN AND ACUTE|
|Ữ|[U+1EEE](https://www.compart.com/en/unicode/U+1EEE)|LATIN CAPITAL LETTER U WITH HORN AND TILDE|
|ữ|[U+1EEF](https://www.compart.com/en/unicode/U+1EEF)|LATIN SMALL LETTER U WITH HORN AND TILDE|
|Ử|[U+1EEC](https://www.compart.com/en/unicode/U+1EEC)|LATIN CAPITAL LETTER U WITH HORN AND HOOK ABOVE|
|ử|[U+1EED](https://www.compart.com/en/unicode/U+1EED)|LATIN SMALL LETTER U WITH HORN AND HOOK ABOVE|
|Ự|[U+1EF0](https://www.compart.com/en/unicode/U+1EF0)|LATIN CAPITAL LETTER U WITH HORN AND DOT BELOW|
|ự|[U+1EF1](https://www.compart.com/en/unicode/U+1EF1)|LATIN SMALL LETTER U WITH HORN AND DOT BELOW|
|Ụ|[U+1EE4](https://www.compart.com/en/unicode/U+1EE4)|LATIN CAPITAL LETTER U WITH DOT BELOW|
|ụ|[U+1EE5](https://www.compart.com/en/unicode/U+1EE5)|LATIN SMALL LETTER U WITH DOT BELOW|
|Ṳ|[U+1E72](https://www.compart.com/en/unicode/U+1E72)|LATIN CAPITAL LETTER U WITH DIAERESIS BELOW|
|ṳ|[U+1E73](https://www.compart.com/en/unicode/U+1E73)|LATIN SMALL LETTER U WITH DIAERESIS BELOW|
|Ų|[U+0172](https://www.compart.com/en/unicode/U+0172)|LATIN CAPITAL LETTER U WITH OGONEK|
|ų|[U+0173](https://www.compart.com/en/unicode/U+0173)|LATIN SMALL LETTER U WITH OGONEK|
|Ṷ|[U+1E76](https://www.compart.com/en/unicode/U+1E76)|LATIN CAPITAL LETTER U WITH CIRCUMFLEX BELOW|
|ṷ|[U+1E77](https://www.compart.com/en/unicode/U+1E77)|LATIN SMALL LETTER U WITH CIRCUMFLEX BELOW|
|Ṵ|[U+1E74](https://www.compart.com/en/unicode/U+1E74)|LATIN CAPITAL LETTER U WITH TILDE BELOW|
|ṵ|[U+1E75](https://www.compart.com/en/unicode/U+1E75)|LATIN SMALL LETTER U WITH TILDE BELOW|
|Ṽ|[U+1E7C](https://www.compart.com/en/unicode/U+1E7C)|LATIN CAPITAL LETTER V WITH TILDE|
|ṽ|[U+1E7D](https://www.compart.com/en/unicode/U+1E7D)|LATIN SMALL LETTER V WITH TILDE|
|Ṿ|[U+1E7E](https://www.compart.com/en/unicode/U+1E7E)|LATIN CAPITAL LETTER V WITH DOT BELOW|
|ṿ|[U+1E7F](https://www.compart.com/en/unicode/U+1E7F)|LATIN SMALL LETTER V WITH DOT BELOW|
|W|[U+0057](https://www.compart.com/en/unicode/U+0057)|LATIN CAPITAL LETTER W|
|w|[U+0077](https://www.compart.com/en/unicode/U+0077)|LATIN SMALL LETTER W|
|Ẁ|[U+1E80](https://www.compart.com/en/unicode/U+1E80)|LATIN CAPITAL LETTER W WITH GRAVE|
|ẁ|[U+1E81](https://www.compart.com/en/unicode/U+1E81)|LATIN SMALL LETTER W WITH GRAVE|
|Ẃ|[U+1E82](https://www.compart.com/en/unicode/U+1E82)|LATIN CAPITAL LETTER W WITH ACUTE|
|ẃ|[U+1E83](https://www.compart.com/en/unicode/U+1E83)|LATIN SMALL LETTER W WITH ACUTE|
|Ŵ|[U+0174](https://www.compart.com/en/unicode/U+0174)|LATIN CAPITAL LETTER W WITH CIRCUMFLEX|
|ŵ|[U+0175](https://www.compart.com/en/unicode/U+0175)|LATIN SMALL LETTER W WITH CIRCUMFLEX|
|Ẇ|[U+1E86](https://www.compart.com/en/unicode/U+1E86)|LATIN CAPITAL LETTER W WITH DOT ABOVE|
|ẇ|[U+1E87](https://www.compart.com/en/unicode/U+1E87)|LATIN SMALL LETTER W WITH DOT ABOVE|
|Ẅ|[U+1E84](https://www.compart.com/en/unicode/U+1E84)|LATIN CAPITAL LETTER W WITH DIAERESIS|
|ẅ|[U+1E85](https://www.compart.com/en/unicode/U+1E85)|LATIN SMALL LETTER W WITH DIAERESIS|
|ẘ|[U+1E98](https://www.compart.com/en/unicode/U+1E98)|LATIN SMALL LETTER W WITH RING ABOVE|
|Ẉ|[U+1E88](https://www.compart.com/en/unicode/U+1E88)|LATIN CAPITAL LETTER W WITH DOT BELOW|
|ẉ|[U+1E89](https://www.compart.com/en/unicode/U+1E89)|LATIN SMALL LETTER W WITH DOT BELOW|
|Ẋ|[U+1E8A](https://www.compart.com/en/unicode/U+1E8A)|LATIN CAPITAL LETTER X WITH DOT ABOVE|
|ẋ|[U+1E8B](https://www.compart.com/en/unicode/U+1E8B)|LATIN SMALL LETTER X WITH DOT ABOVE|
|Ẍ|[U+1E8C](https://www.compart.com/en/unicode/U+1E8C)|LATIN CAPITAL LETTER X WITH DIAERESIS|
|ẍ|[U+1E8D](https://www.compart.com/en/unicode/U+1E8D)|LATIN SMALL LETTER X WITH DIAERESIS|
|Ỳ|[U+1EF2](https://www.compart.com/en/unicode/U+1EF2)|LATIN CAPITAL LETTER Y WITH GRAVE|
|ỳ|[U+1EF3](https://www.compart.com/en/unicode/U+1EF3)|LATIN SMALL LETTER Y WITH GRAVE|
|Ý|[U+00DD](https://www.compart.com/en/unicode/U+00DD)|LATIN CAPITAL LETTER Y WITH ACUTE|
|ý|[U+00FD](https://www.compart.com/en/unicode/U+00FD)|LATIN SMALL LETTER Y WITH ACUTE|
|Ŷ|[U+0176](https://www.compart.com/en/unicode/U+0176)|LATIN CAPITAL LETTER Y WITH CIRCUMFLEX|
|ŷ|[U+0177](https://www.compart.com/en/unicode/U+0177)|LATIN SMALL LETTER Y WITH CIRCUMFLEX|
|Ỹ|[U+1EF8](https://www.compart.com/en/unicode/U+1EF8)|LATIN CAPITAL LETTER Y WITH TILDE|
|ỹ|[U+1EF9](https://www.compart.com/en/unicode/U+1EF9)|LATIN SMALL LETTER Y WITH TILDE|
|Ȳ|[U+0232](https://www.compart.com/en/unicode/U+0232)|LATIN CAPITAL LETTER Y WITH MACRON|
|ȳ|[U+0233](https://www.compart.com/en/unicode/U+0233)|LATIN SMALL LETTER Y WITH MACRON|
|Ẏ|[U+1E8E](https://www.compart.com/en/unicode/U+1E8E)|LATIN CAPITAL LETTER Y WITH DOT ABOVE|
|ẏ|[U+1E8F](https://www.compart.com/en/unicode/U+1E8F)|LATIN SMALL LETTER Y WITH DOT ABOVE|
|Ÿ|[U+0178](https://www.compart.com/en/unicode/U+0178)|LATIN CAPITAL LETTER Y WITH DIAERESIS|
|ÿ|[U+00FF](https://www.compart.com/en/unicode/U+00FF)|LATIN SMALL LETTER Y WITH DIAERESIS|
|Ỷ|[U+1EF6](https://www.compart.com/en/unicode/U+1EF6)|LATIN CAPITAL LETTER Y WITH HOOK ABOVE|
|ỷ|[U+1EF7](https://www.compart.com/en/unicode/U+1EF7)|LATIN SMALL LETTER Y WITH HOOK ABOVE|
|ẙ|[U+1E99](https://www.compart.com/en/unicode/U+1E99)|LATIN SMALL LETTER Y WITH RING ABOVE|
|Ỵ|[U+1EF4](https://www.compart.com/en/unicode/U+1EF4)|LATIN CAPITAL LETTER Y WITH DOT BELOW|
|ỵ|[U+1EF5](https://www.compart.com/en/unicode/U+1EF5)|LATIN SMALL LETTER Y WITH DOT BELOW|
|Ź|[U+0179](https://www.compart.com/en/unicode/U+0179)|LATIN CAPITAL LETTER Z WITH ACUTE|
|ź|[U+017A](https://www.compart.com/en/unicode/U+017A)|LATIN SMALL LETTER Z WITH ACUTE|
|Ẑ|[U+1E90](https://www.compart.com/en/unicode/U+1E90)|LATIN CAPITAL LETTER Z WITH CIRCUMFLEX|
|ẑ|[U+1E91](https://www.compart.com/en/unicode/U+1E91)|LATIN SMALL LETTER Z WITH CIRCUMFLEX|
|Ż|[U+017B](https://www.compart.com/en/unicode/U+017B)|LATIN CAPITAL LETTER Z WITH DOT ABOVE|
|ż|[U+017C](https://www.compart.com/en/unicode/U+017C)|LATIN SMALL LETTER Z WITH DOT ABOVE|
|Ž|[U+017D](https://www.compart.com/en/unicode/U+017D)|LATIN CAPITAL LETTER Z WITH CARON|
|ž|[U+017E](https://www.compart.com/en/unicode/U+017E)|LATIN SMALL LETTER Z WITH CARON|
|Ẓ|[U+1E92](https://www.compart.com/en/unicode/U+1E92)|LATIN CAPITAL LETTER Z WITH DOT BELOW|
|ẓ|[U+1E93](https://www.compart.com/en/unicode/U+1E93)|LATIN SMALL LETTER Z WITH DOT BELOW|
|Ẕ|[U+1E94](https://www.compart.com/en/unicode/U+1E94)|LATIN CAPITAL LETTER Z WITH LINE BELOW|
|ẕ|[U+1E95](https://www.compart.com/en/unicode/U+1E95)|LATIN SMALL LETTER Z WITH LINE BELOW|
|ẞ|[U+1E9E](https://www.compart.com/en/unicode/U+1E9E)|LATIN CAPITAL LETTER SHARP S|
|ß|[U+00DF](https://www.compart.com/en/unicode/U+00DF)|LATIN SMALL LETTER SHARP S|
|Æ|[U+00C6](https://www.compart.com/en/unicode/U+00C6)|LATIN CAPITAL LETTER AE|
|æ|[U+00E6](https://www.compart.com/en/unicode/U+00E6)|LATIN SMALL LETTER AE|
|Ǽ|[U+01FC](https://www.compart.com/en/unicode/U+01FC)|LATIN CAPITAL LETTER AE WITH ACUTE|
|Ǽ|[U+01FC](https://www.compart.com/en/unicode/U+01FC)|LATIN CAPITAL LETTER AE WITH ACUTE|
|ǽ|[U+01FD](https://www.compart.com/en/unicode/U+01FD)|LATIN SMALL LETTER AE WITH ACUTE|
|ǽ|[U+01FD](https://www.compart.com/en/unicode/U+01FD)|LATIN SMALL LETTER AE WITH ACUTE|
|Ǣ|[U+01E2](https://www.compart.com/en/unicode/U+01E2)|LATIN CAPITAL LETTER AE WITH MACRON|
|Ǣ|[U+01E2](https://www.compart.com/en/unicode/U+01E2)|LATIN CAPITAL LETTER AE WITH MACRON|
|ǣ|[U+01E3](https://www.compart.com/en/unicode/U+01E3)|LATIN SMALL LETTER AE WITH MACRON|
|ǣ|[U+01E3](https://www.compart.com/en/unicode/U+01E3)|LATIN SMALL LETTER AE WITH MACRON|
|Ø|[U+00D8](https://www.compart.com/en/unicode/U+00D8)|LATIN CAPITAL LETTER O WITH STROKE|
|ø|[U+00F8](https://www.compart.com/en/unicode/U+00F8)|LATIN SMALL LETTER O WITH STROKE|
|Ǿ|[U+01FE](https://www.compart.com/en/unicode/U+01FE)|LATIN CAPITAL LETTER O WITH STROKE AND ACUTE|
|ǿ|[U+01FF](https://www.compart.com/en/unicode/U+01FF)|LATIN SMALL LETTER O WITH STROKE AND ACUTE|
|Đ|[U+0110](https://www.compart.com/en/unicode/U+0110)|LATIN CAPITAL LETTER D WITH STROKE|
|đ|[U+0111](https://www.compart.com/en/unicode/U+0111)|LATIN SMALL LETTER D WITH STROKE|
|Ħ|[U+0126](https://www.compart.com/en/unicode/U+0126)|LATIN CAPITAL LETTER H WITH STROKE|
|ħ|[U+0127](https://www.compart.com/en/unicode/U+0127)|LATIN SMALL LETTER H WITH STROKE|
|Ŀ|[U+013F](https://www.compart.com/en/unicode/U+013F)|LATIN CAPITAL LETTER L WITH MIDDLE DOT|
|ŀ|[U+0140](https://www.compart.com/en/unicode/U+0140)|LATIN SMALL LETTER L WITH MIDDLE DOT|
|Ł|[U+0141](https://www.compart.com/en/unicode/U+0141)|LATIN CAPITAL LETTER L WITH STROKE|
|ł|[U+0142](https://www.compart.com/en/unicode/U+0142)|LATIN SMALL LETTER L WITH STROKE|
|Œ|[U+0152](https://www.compart.com/en/unicode/U+0152)|LATIN CAPITAL LIGATURE OE|
|œ|[U+0153](https://www.compart.com/en/unicode/U+0153)|LATIN SMALL LIGATURE OE|
|Ŧ|[U+0166](https://www.compart.com/en/unicode/U+0166)|LATIN CAPITAL LETTER T WITH STROKE|
|ŧ|[U+0167](https://www.compart.com/en/unicode/U+0167)|LATIN SMALL LETTER T WITH STROKE|
|Ƈ|[U+0187](https://www.compart.com/en/unicode/U+0187)|LATIN CAPITAL LETTER C WITH HOOK|
|ƈ|[U+0188](https://www.compart.com/en/unicode/U+0188)|LATIN SMALL LETTER C WITH HOOK|
|Ƒ|[U+0191](https://www.compart.com/en/unicode/U+0191)|LATIN CAPITAL LETTER F WITH HOOK|
|ƒ|[U+0192](https://www.compart.com/en/unicode/U+0192)|LATIN SMALL LETTER F WITH HOOK|
|Ƕ|[U+01F6](https://www.compart.com/en/unicode/U+01F6)|LATIN CAPITAL LETTER HWAIR|
|ƕ|[U+0195](https://www.compart.com/en/unicode/U+0195)|LATIN SMALL LETTER HV|
|Ƙ|[U+0198](https://www.compart.com/en/unicode/U+0198)|LATIN CAPITAL LETTER K WITH HOOK|
|ƙ|[U+0199](https://www.compart.com/en/unicode/U+0199)|LATIN SMALL LETTER K WITH HOOK|
|Ƚ|[U+023D](https://www.compart.com/en/unicode/U+023D)|LATIN CAPITAL LETTER L WITH BAR|
|ƚ|[U+019A](https://www.compart.com/en/unicode/U+019A)|LATIN SMALL LETTER L WITH BAR|
|Ƥ|[U+01A4](https://www.compart.com/en/unicode/U+01A4)|LATIN CAPITAL LETTER P WITH HOOK|
|ƥ|[U+01A5](https://www.compart.com/en/unicode/U+01A5)|LATIN SMALL LETTER P WITH HOOK|
|Ƭ|[U+01AC](https://www.compart.com/en/unicode/U+01AC)|LATIN CAPITAL LETTER T WITH HOOK|
|ƭ|[U+01AD](https://www.compart.com/en/unicode/U+01AD)|LATIN SMALL LETTER T WITH HOOK|
|Ƴ|[U+01B3](https://www.compart.com/en/unicode/U+01B3)|LATIN CAPITAL LETTER Y WITH HOOK|
|ƴ|[U+01B4](https://www.compart.com/en/unicode/U+01B4)|LATIN SMALL LETTER Y WITH HOOK|
|Ǥ|[U+01E4](https://www.compart.com/en/unicode/U+01E4)|LATIN CAPITAL LETTER G WITH STROKE|
|ǥ|[U+01E5](https://www.compart.com/en/unicode/U+01E5)|LATIN SMALL LETTER G WITH STROKE|
|Ɍ|[U+024C](https://www.compart.com/en/unicode/U+024C)|LATIN CAPITAL LETTER R WITH STROKE|
|ɍ|[U+024D](https://www.compart.com/en/unicode/U+024D)|LATIN SMALL LETTER R WITH STROKE|
|Ɓ|[U+0181](https://www.compart.com/en/unicode/U+0181)|LATIN CAPITAL LETTER B WITH HOOK|
|ɓ|[U+0253](https://www.compart.com/en/unicode/U+0253)|LATIN SMALL LETTER B WITH HOOK|
|Ɗ|[U+018A](https://www.compart.com/en/unicode/U+018A)|LATIN CAPITAL LETTER D WITH HOOK|
|ɗ|[U+0257](https://www.compart.com/en/unicode/U+0257)|LATIN SMALL LETTER D WITH HOOK|
|Ə|[U+018F](https://www.compart.com/en/unicode/U+018F)|LATIN CAPITAL LETTER SCHWA|
|ə|[U+0259](https://www.compart.com/en/unicode/U+0259)|LATIN SMALL LETTER SCHWA|
|Ɠ|[U+0193](https://www.compart.com/en/unicode/U+0193)|LATIN CAPITAL LETTER G WITH HOOK|
|ɠ|[U+0260](https://www.compart.com/en/unicode/U+0260)|LATIN SMALL LETTER G WITH HOOK|
|Ɨ|[U+0197](https://www.compart.com/en/unicode/U+0197)|LATIN CAPITAL LETTER I WITH STROKE|
|ɨ|[U+0268](https://www.compart.com/en/unicode/U+0268)|LATIN SMALL LETTER I WITH STROKE|
|Ʉ|[U+0244](https://www.compart.com/en/unicode/U+0244)|LATIN CAPITAL LETTER U BAR|
|ʉ|[U+0289](https://www.compart.com/en/unicode/U+0289)|LATIN SMALL LETTER U BAR|
|Ӳ|[U+04F2](https://www.compart.com/en/unicode/U+04F2)|CYRILLIC CAPITAL LETTER U WITH DOUBLE ACUTE|
|ӳ|[U+04F3](https://www.compart.com/en/unicode/U+04F3)|CYRILLIC SMALL LETTER U WITH DOUBLE ACUTE|
|ᴂ|[U+1D02](https://www.compart.com/en/unicode/U+1D02)|LATIN SMALL LETTER TURNED AE|
|ᵫ|[U+1D6B](https://www.compart.com/en/unicode/U+1D6B)|LATIN SMALL LETTER UE|
|Ỻ|[U+1EFA](https://www.compart.com/en/unicode/U+1EFA)|LATIN CAPITAL LETTER MIDDLE-WELSH LL|
|ỻ|[U+1EFB](https://www.compart.com/en/unicode/U+1EFB)|LATIN SMALL LETTER MIDDLE-WELSH LL|
|℔|[U+2114](https://www.compart.com/en/unicode/U+2114)|L B BAR SYMBOL|
|Ⅎ|[U+2132](https://www.compart.com/en/unicode/U+2132)|TURNED CAPITAL F|
|ⅎ|[U+214E](https://www.compart.com/en/unicode/U+214E)|TURNED SMALL F|
|Ↄ|[U+2183](https://www.compart.com/en/unicode/U+2183)|ROMAN NUMERAL REVERSED ONE HUNDRED|
|ↄ|[U+2184](https://www.compart.com/en/unicode/U+2184)|LATIN SMALL LETTER REVERSED C|
|Ꜩ|[U+A728](https://www.compart.com/en/unicode/U+A728)|LATIN CAPITAL LETTER TZ|
|ꜩ|[U+A729](https://www.compart.com/en/unicode/U+A729)|LATIN SMALL LETTER TZ|
|Ꜳ|[U+A732](https://www.compart.com/en/unicode/U+A732)|LATIN CAPITAL LETTER AA|
|ꜳ|[U+A733](https://www.compart.com/en/unicode/U+A733)|LATIN SMALL LETTER AA|
|Ꜵ|[U+A734](https://www.compart.com/en/unicode/U+A734)|LATIN CAPITAL LETTER AO|
|ꜵ|[U+A735](https://www.compart.com/en/unicode/U+A735)|LATIN SMALL LETTER AO|
|Ꜷ|[U+A736](https://www.compart.com/en/unicode/U+A736)|LATIN CAPITAL LETTER AU|
|ꜷ|[U+A737](https://www.compart.com/en/unicode/U+A737)|LATIN SMALL LETTER AU|
|Ꜹ|[U+A738](https://www.compart.com/en/unicode/U+A738)|LATIN CAPITAL LETTER AV|
|ꜻ|[U+A73B](https://www.compart.com/en/unicode/U+A73B)|LATIN SMALL LETTER AV WITH HORIZONTAL BAR|
|Ꜽ|[U+A73C](https://www.compart.com/en/unicode/U+A73C)|LATIN CAPITAL LETTER AY|
|ꜽ|[U+A73D](https://www.compart.com/en/unicode/U+A73D)|LATIN SMALL LETTER AY|
|Ꝏ|[U+A74E](https://www.compart.com/en/unicode/U+A74E)|LATIN CAPITAL LETTER OO|
|ꝏ|[U+A74F](https://www.compart.com/en/unicode/U+A74F)|LATIN SMALL LETTER OO|
|Ꝡ|[U+A760](https://www.compart.com/en/unicode/U+A760)|LATIN CAPITAL LETTER VY|
|ꝡ|[U+A761](https://www.compart.com/en/unicode/U+A761)|LATIN SMALL LETTER VY|
|ꭣ|[U+AB63](https://www.compart.com/en/unicode/U+AB63)|LATIN SMALL LETTER UO|
|ﬀ|[U+FB00](https://www.compart.com/en/unicode/U+FB00)|LATIN SMALL LIGATURE FF|
|ﬁ|[U+FB01](https://www.compart.com/en/unicode/U+FB01)|LATIN SMALL LIGATURE FI|
|ﬂ|[U+FB02](https://www.compart.com/en/unicode/U+FB02)|LATIN SMALL LIGATURE FL|
|ﬃ|[U+FB03](https://www.compart.com/en/unicode/U+FB03)|LATIN SMALL LIGATURE FFI|
|ﬄ|[U+FB04](https://www.compart.com/en/unicode/U+FB04)|LATIN SMALL LIGATURE FFL|
|ﬆ|[U+FB06](https://www.compart.com/en/unicode/U+FB06)|LATIN SMALL LIGATURE ST|

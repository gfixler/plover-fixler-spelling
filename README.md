
# Fixler Spelling for Plover
A fingerspelling system for the [Plover](https://www.openstenoproject.org/plover/) steno software.

This library currently provides quick access to 572 characters.

## Design Goals
* provide upper and lowercase letters, with some extras, like Æ/æ, and Ə/ə
* systematize writing most precomposed Latin letters with diacritics
* extend system to allow composing in combining characters
* add in other symbols, ligatures, etc., on a case-by-case basis
* include some similar alphabets (NATO, Braille, Morse, Greek, etc.)


## Diacritic Keys
The following 6 keys are used to add diacritics.
```
🅂🅃🄿🄷 🄾 🅵🅿🅻🅃🄳
🅂🄺🅆🅁 🄾 🆁🅱🅶🅂🅉
　　　🄰🄾 🄴🅄
```


## Adding Diacritics/Modifiers
Modify base letters by stroking a diacritic or modifier outline immediately after a base letter.

For example, to get á, stroke A* for "a", then the acute modifier outline to convert it.

NOTE: Modifiers are currently precomposed with their letters. The system doesn't look back at previous output, meaning you must stroke the letter as defined, followed by any modifiers. This in turn means you must use this system's strokes for each letter, e.g. STKPW for "z", and not STK. Currently, the only way to fix this is to modify the python file, and regenerate the dictionary.


## Modifier Tweaks
Tweaks are added to a modifier stroke using the E and U keys:

    🅂🅃🄿🄷 🄾 🄵🄿🄻🅃🄳
    🅂🄺🅆🅁 🄾 🅁🄱🄶🅂🅉
    　　　🄰🄾 🅴🆄

|Tweak|Description|
|-|-|
|![EU Up](images/EU_up.png)|Neither E nor U pressed means no tweak to the modifier stroke.|
|![E Down](images/E_down.png)|Think of E as meaning "extra". This is added to acute and grave strokes to double them.|
|![U Down](images/U_down.png)|Think of U as meaning "under". This is added to various diacritic strokes to turn them into their "below" versions: breve below, circumflex below, line below, ring below, and tilde below.|
|![EU Down](images/EU_down.png)|Think of EU (the "i" chord in steno) as meaning "invert".


## Available Diacritics/Modifiers
In general, the diacritic chords are meant to visually resemble their symbols, to ease remembering them all.

For other modifiers, like rotation or inversion, an attempt was made to be memorable. See notes with each modifier.

|Pattern|Notes|
|-|-|
|Acute| |
|![acute](images/acute.png)|Shaped like the acute symbol.<BR><BR>Used in: [á](https://en.wikipedia.org/wiki/%C3%81) [Á](https://en.wikipedia.org/wiki/%C3%81) [ǻ](https://en.wikipedia.org/wiki/%C3%85#On_computers) [Ǻ](https://en.wikipedia.org/wiki/%C3%85#On_computers) [ć](https://en.wikipedia.org/wiki/%C4%86) [Ć](https://en.wikipedia.org/wiki/%C4%86) [é](https://en.wikipedia.org/wiki/%C3%89) [É](https://en.wikipedia.org/wiki/%C3%89) [ǵ](https://en.wikipedia.org/wiki/%C7%B4) [Ǵ](https://en.wikipedia.org/wiki/%C7%B4) [í](https://en.wikipedia.org/wiki/%C3%8D) [Í](https://en.wikipedia.org/wiki/%C3%8D) [ĺ](https://en.wikipedia.org/wiki/Acute_accent) [Ĺ](https://en.wikipedia.org/wiki/Acute_accent) [ń](https://en.wikipedia.org/wiki/%C5%83) [Ń](https://en.wikipedia.org/wiki/%C5%83) [ó](https://en.wikipedia.org/wiki/%C3%93) [Ó](https://en.wikipedia.org/wiki/%C3%93) [ǿ](https://en.wikipedia.org/wiki/%C3%98#%C7%BE) [Ǿ](https://en.wikipedia.org/wiki/%C3%98#%C7%BE) [ŕ](https://en.wikipedia.org/wiki/%C5%94) [Ŕ](https://en.wikipedia.org/wiki/%C5%94) [ś](https://en.wikipedia.org/wiki/%C5%9A) [Ś](https://en.wikipedia.org/wiki/%C5%9A) [ú](https://en.wikipedia.org/wiki/%C3%9A) [Ú](https://en.wikipedia.org/wiki/%C3%9A) [ẃ](https://en.wikipedia.org/wiki/%E1%BA%82) [Ẃ](https://en.wikipedia.org/wiki/%E1%BA%82) [ý](https://en.wikipedia.org/wiki/%C3%9D) [Ý](https://en.wikipedia.org/wiki/%C3%9D) [ź](https://en.wikipedia.org/wiki/%C5%B9) [Ź](https://en.wikipedia.org/wiki/%C5%B9) [ǽ](https://en.wikipedia.org/wiki/%C3%86) [Ǽ](https://en.wikipedia.org/wiki/%C3%86) [ắ](https://www.compart.com/en/unicode/U+1EAF) [Ắ](https://www.compart.com/en/unicode/U+1EAE) [ấ](https://www.compart.com/en/unicode/U+1EA5) [Ấ](https://www.compart.com/en/unicode/U+1EA4) [ớ](https://www.compart.com/en/unicode/U+1EDB) [Ớ](https://www.compart.com/en/unicode/U+1EDA) [ố](https://www.compart.com/en/unicode/U+1ED1) [Ố](https://www.compart.com/en/unicode/U+1ED0) [ế](https://www.compart.com/en/unicode/U+1EBF) [Ế](https://www.compart.com/en/unicode/U+1EBE) [ứ](https://www.compart.com/en/unicode/U+1EE9) [Ứ](https://www.compart.com/en/unicode/U+1EE8) [ǘ](https://www.compart.com/en/unicode/U+01D8) [Ǘ](https://www.compart.com/en/unicode/U+01D7) [ḉ](https://www.compart.com/en/unicode/U+1E09) [Ḉ](https://www.compart.com/en/unicode/U+1E08) [ḗ](https://www.compart.com/en/unicode/U+1E17) [Ḗ](https://www.compart.com/en/unicode/U+1E16) [ḯ](https://www.compart.com/en/unicode/U+1E2F) [Ḯ](https://www.compart.com/en/unicode/U+1E2E) [ḱ](https://www.compart.com/en/unicode/U+1E31) [Ḱ](https://www.compart.com/en/unicode/U+1E30) [ḿ](https://www.compart.com/en/unicode/U+1E3F) [Ḿ](https://www.compart.com/en/unicode/U+1E3E) [ṍ](https://www.compart.com/en/unicode/U+1E4D) [Ṍ](https://www.compart.com/en/unicode/U+1E4C) [ṓ](https://www.compart.com/en/unicode/U+1E53) [Ṓ](https://www.compart.com/en/unicode/U+1E52) [ṕ](https://www.compart.com/en/unicode/U+1E55) [Ṕ](https://www.compart.com/en/unicode/U+1E54) [ṥ](https://www.compart.com/en/unicode/U+1E65) [Ṥ](https://www.compart.com/en/unicode/U+1E64) [ṹ](https://www.compart.com/en/unicode/U+1E79) [Ṹ](https://www.compart.com/en/unicode/U+1E78)|
|Double Acute| |
|![acuteDoubled](images/acuteDoubled.png)|The acute modifier shape, with the '[extra](#modifier-tweaks)' tweak.<BR><BR>Used in: [a̋](https://en.wikipedia.org/wiki/Double_acute_accent#Letters_with_double_acute) [A̋](https://en.wikipedia.org/wiki/Double_acute_accent#Letters_with_double_acute) [ő](https://en.wikipedia.org/wiki/%C5%90) [Ő](https://en.wikipedia.org/wiki/%C5%90) [ű](https://en.wikipedia.org/wiki/Double_acute_accent#Letters_with_double_acute) [Ű](https://en.wikipedia.org/wiki/Double_acute_accent#Letters_with_double_acute) [ӳ](https://en.wikipedia.org/wiki/Double_acute_accent#Letters_with_double_acute) [Ӳ](https://en.wikipedia.org/wiki/Double_acute_accent#Letters_with_double_acute)|
|Breve| |
|![breve](images/breve.png)|Shaped like the breve symbol.<BR><BR>Used in: [ă](https://en.wikipedia.org/wiki/%C4%82) [Ă](https://en.wikipedia.org/wiki/%C4%82) [ĕ](https://en.wikipedia.org/wiki/Breve#Letters_with_breve) [Ĕ](https://en.wikipedia.org/wiki/Breve#Letters_with_breve) [ğ](https://en.wikipedia.org/wiki/%C4%9E) [Ğ](https://en.wikipedia.org/wiki/%C4%9E) [ĭ](https://en.wikipedia.org/wiki/Breve) [Ĭ](https://en.wikipedia.org/wiki/Breve) [ŏ](https://en.wikipedia.org/wiki/Breve) [Ŏ](https://en.wikipedia.org/wiki/Breve) [ŭ](https://en.wikipedia.org/wiki/%C5%AC) [Ŭ](https://en.wikipedia.org/wiki/%C5%AC) [ẳ](https://www.compart.com/en/unicode/U+1EB3) [Ẳ](https://www.compart.com/en/unicode/U+1EB2) [ẵ](https://www.compart.com/en/unicode/U+1EB5) [Ẵ](https://www.compart.com/en/unicode/U+1EB4) [ằ](https://www.compart.com/en/unicode/U+1EB1) [Ằ](https://www.compart.com/en/unicode/U+1EB0) [ắ](https://www.compart.com/en/unicode/U+1EAF) [Ắ](https://www.compart.com/en/unicode/U+1EAE) [ặ](https://www.compart.com/en/unicode/U+1EB7) [Ặ](https://www.compart.com/en/unicode/U+1EB6) [ḝ](https://www.compart.com/en/unicode/U+1E1D) [Ḝ](https://www.compart.com/en/unicode/U+1E1C)|
|Breve Below| |
|![breveBelow](images/breveBelow.png)|The breve modifier shape, with the '[under](#modifier-tweaks)' tweak.<BR><BR>Used in: [ḫ](https://www.compart.com/en/unicode/U+1E2B) [Ḫ](https://www.compart.com/en/unicode/U+1E2A)|
|Breve Inverted| |
|![breveInverted](images/breveInverted.png)|Shaped like the inverted breve symbol.<BR><BR>Used in: [ȃ](https://www.compart.com/en/unicode/U+0203) [Ȃ](https://www.compart.com/en/unicode/U+0202) [ȇ](https://www.compart.com/en/unicode/U+0207) [Ȇ](https://www.compart.com/en/unicode/U+0206) [ȋ](https://www.compart.com/en/unicode/U+020B) [Ȋ](https://www.compart.com/en/unicode/U+020A) [ȏ](https://www.compart.com/en/unicode/U+020F) [Ȏ](https://www.compart.com/en/unicode/U+020E) [ȓ](https://www.compart.com/en/unicode/U+0213) [Ȓ](https://www.compart.com/en/unicode/U+0212) [ȗ](https://www.compart.com/en/unicode/U+0217) [Ȗ](https://www.compart.com/en/unicode/U+0216)|
|Caron| |
|![caron](images/caron.png)|Shaped like the caron symbol.<BR><BR>Used in: [ǎ](https://en.wikipedia.org/wiki/Caron) [Ǎ](https://en.wikipedia.org/wiki/Caron) [č](https://en.wikipedia.org/wiki/%C4%8C) [Č](https://en.wikipedia.org/wiki/%C4%8C) [ě](https://en.wikipedia.org/wiki/%C4%9A) [Ě](https://en.wikipedia.org/wiki/%C4%9A) [ǧ](https://en.wikipedia.org/wiki/%C7%A6) [Ǧ](https://en.wikipedia.org/wiki/%C7%A6) [ǐ](https://en.wikipedia.org/wiki/Caron) [Ǐ](https://en.wikipedia.org/wiki/Caron) [ǩ](https://en.wikipedia.org/wiki/%C7%A8) [Ǩ](https://en.wikipedia.org/wiki/%C7%A8) [ľ](https://en.wikipedia.org/wiki/%C4%BD) [Ľ](https://en.wikipedia.org/wiki/%C4%BD) [ň](https://en.wikipedia.org/wiki/%C5%87) [Ň](https://en.wikipedia.org/wiki/%C5%87) [ǒ](https://en.wikipedia.org/wiki/Caron) [Ǒ](https://en.wikipedia.org/wiki/Caron) [ř](https://en.wikipedia.org/wiki/%C5%98) [Ř](https://en.wikipedia.org/wiki/%C5%98) [ŝ](https://en.wikipedia.org/wiki/%C5%9C) [Ŝ](https://en.wikipedia.org/wiki/%C5%9C) [š](https://en.wikipedia.org/wiki/%C5%A0) [Š](https://en.wikipedia.org/wiki/%C5%A0) [ť](https://en.wikipedia.org/wiki/%C5%A4) [Ť](https://en.wikipedia.org/wiki/%C5%A4) [ǔ](https://en.wikipedia.org/wiki/Caron) [Ǔ](https://en.wikipedia.org/wiki/Caron) [ž](https://en.wikipedia.org/wiki/%C5%BD) [Ž](https://en.wikipedia.org/wiki/%C5%BD) [ď](https://www.compart.com/en/unicode/U+010F) [Ď](https://www.compart.com/en/unicode/U+010E) [ȟ](https://www.compart.com/en/unicode/U+021F) [Ȟ](https://www.compart.com/en/unicode/U+021E) [ṧ](https://www.compart.com/en/unicode/U+1E67) [Ṧ](https://www.compart.com/en/unicode/U+1E66) [ǰ](https://www.compart.com/en/unicode/U+01F0)|
|Cedilla| |
|![cedilla](images/cedilla.png)|Only remaining low key (see [dot below](#dot-below), and [comma below](#comma-below)).<BR><BR>Used in: [ç](https://en.wikipedia.org/wiki/%C3%87) [Ç](https://en.wikipedia.org/wiki/%C3%87) [ȩ](https://en.wikipedia.org/wiki/Cedilla) [Ȩ](https://en.wikipedia.org/wiki/Cedilla) [i̧](https://en.wikipedia.org/wiki/Cedilla) [I̧](https://en.wikipedia.org/wiki/Cedilla) [m̧](https://en.wikipedia.org/wiki/Cedilla) [M̧](https://en.wikipedia.org/wiki/Cedilla) [o̧](https://en.wikipedia.org/wiki/Cedilla) [O̧](https://en.wikipedia.org/wiki/Cedilla) [ş](https://en.wikipedia.org/wiki/%C5%9E) [Ş](https://en.wikipedia.org/wiki/%C5%9E) [ţ](https://en.wikipedia.org/wiki/%C5%A2) [Ţ](https://en.wikipedia.org/wiki/%C5%A2) [u̧](https://en.wikipedia.org/wiki/Cedilla) [U̧](https://en.wikipedia.org/wiki/Cedilla) [ḑ](https://en.wikipedia.org/wiki/%E1%B8%90) [Ḑ](https://en.wikipedia.org/wiki/%E1%B8%90) [ģ](https://en.wikipedia.org/wiki/%C4%A2) [Ģ](https://en.wikipedia.org/wiki/%C4%A2) [ķ](https://en.wikipedia.org/wiki/%C4%B6) [Ķ](https://en.wikipedia.org/wiki/%C4%B6) [ļ](https://en.wikipedia.org/wiki/Cedilla) [Ļ](https://en.wikipedia.org/wiki/Cedilla) [ņ](https://en.wikipedia.org/wiki/Cedilla) [Ņ](https://en.wikipedia.org/wiki/Cedilla) [ŗ](https://en.wikipedia.org/wiki/Cedilla) [Ŗ](https://en.wikipedia.org/wiki/Cedilla) [ḉ](https://www.compart.com/en/unicode/U+1E09) [Ḉ](https://www.compart.com/en/unicode/U+1E08) [ḝ](https://www.compart.com/en/unicode/U+1E1D) [Ḝ](https://www.compart.com/en/unicode/U+1E1C) [ḩ](https://www.compart.com/en/unicode/U+1E29) [Ḩ](https://www.compart.com/en/unicode/U+1E28)|
|Circumflex| |
|![circumflex](images/circumflex.png)|Shaped like the circumflex symbol.<BR><BR>Used in: [â](https://en.wikipedia.org/wiki/%C3%82) [Â](https://en.wikipedia.org/wiki/%C3%82) [ĉ](https://en.wikipedia.org/wiki/%C4%88) [Ĉ](https://en.wikipedia.org/wiki/%C4%88) [ḓ](https://en.wikipedia.org/wiki/Circumflex) [Ḓ](https://en.wikipedia.org/wiki/Circumflex) [ê](https://en.wikipedia.org/wiki/%C3%8A) [Ê](https://en.wikipedia.org/wiki/%C3%8A) [ĝ](https://en.wikipedia.org/wiki/%C4%9C) [Ĝ](https://en.wikipedia.org/wiki/%C4%9C) [ĥ](https://en.wikipedia.org/wiki/%C4%A4) [Ĥ](https://en.wikipedia.org/wiki/%C4%A4) [î](https://en.wikipedia.org/wiki/%C3%8E) [Î](https://en.wikipedia.org/wiki/%C3%8E) [ĵ](https://en.wikipedia.org/wiki/%C4%B4) [Ĵ](https://en.wikipedia.org/wiki/%C4%B4) [ḽ](https://en.wikipedia.org/wiki/Circumflex) [Ḽ](https://en.wikipedia.org/wiki/Circumflex) [m̂](https://en.wikipedia.org/wiki/Circumflex) [M̂](https://en.wikipedia.org/wiki/Circumflex) [n̂](https://en.wikipedia.org/wiki/Circumflex) [N̂](https://en.wikipedia.org/wiki/Circumflex) [ṋ](https://en.wikipedia.org/wiki/Circumflex) [Ṋ](https://en.wikipedia.org/wiki/Circumflex) [ô](https://en.wikipedia.org/wiki/Circumflex) [Ô](https://en.wikipedia.org/wiki/Circumflex) [ṱ](https://en.wikipedia.org/wiki/Circumflex) [Ṱ](https://en.wikipedia.org/wiki/Circumflex) [û](https://en.wikipedia.org/wiki/%C3%9B) [Û](https://en.wikipedia.org/wiki/%C3%9B) [ŵ](https://en.wikipedia.org/wiki/Circumflex) [Ŵ](https://en.wikipedia.org/wiki/Circumflex) [ŷ](https://en.wikipedia.org/wiki/Circumflex) [Ŷ](https://en.wikipedia.org/wiki/Circumflex) [ậ](https://www.compart.com/en/unicode/U+1EAD) [Ậ](https://www.compart.com/en/unicode/U+1EAC) [ẩ](https://www.compart.com/en/unicode/U+1EA9) [Ẩ](https://www.compart.com/en/unicode/U+1EA8) [ẫ](https://www.compart.com/en/unicode/U+1EAB) [Ẫ](https://www.compart.com/en/unicode/U+1EAA) [ầ](https://www.compart.com/en/unicode/U+1EA7) [Ầ](https://www.compart.com/en/unicode/U+1EA6) [ấ](https://www.compart.com/en/unicode/U+1EA5) [Ấ](https://www.compart.com/en/unicode/U+1EA4) [ộ](https://www.compart.com/en/unicode/U+1ED9) [Ộ](https://www.compart.com/en/unicode/U+1ED8) [ổ](https://www.compart.com/en/unicode/U+1ED5) [Ổ](https://www.compart.com/en/unicode/U+1ED4) [ỗ](https://www.compart.com/en/unicode/U+1ED7) [Ỗ](https://www.compart.com/en/unicode/U+1ED6) [ồ](https://www.compart.com/en/unicode/U+1ED3) [Ồ](https://www.compart.com/en/unicode/U+1ED2) [ố](https://www.compart.com/en/unicode/U+1ED1) [Ố](https://www.compart.com/en/unicode/U+1ED0) [ệ](https://www.compart.com/en/unicode/U+1EC7) [Ệ](https://www.compart.com/en/unicode/U+1EC6) [ể](https://www.compart.com/en/unicode/U+1EC3) [Ể](https://www.compart.com/en/unicode/U+1EC2) [ễ](https://www.compart.com/en/unicode/U+1EC5) [Ễ](https://www.compart.com/en/unicode/U+1EC4) [ề](https://www.compart.com/en/unicode/U+1EC1) [Ề](https://www.compart.com/en/unicode/U+1EC0) [ế](https://www.compart.com/en/unicode/U+1EBF) [Ế](https://www.compart.com/en/unicode/U+1EBE) [ẑ](https://www.compart.com/en/unicode/U+1E91) [Ẑ](https://www.compart.com/en/unicode/U+1E90)|
|Circumflex Below| |
|![circumflexBelow](images/circumflexBelow.png)|The circumflex modifier shape, with the '[under](#modifier-tweaks)' tweak.<BR><BR>Used in: [ḙ](https://www.compart.com/en/unicode/U+1E19) [Ḙ](https://www.compart.com/en/unicode/U+1E18) [ṷ](https://www.compart.com/en/unicode/U+1E77) [Ṷ](https://www.compart.com/en/unicode/U+1E76)|
|Comma Below| |
|![commaBelow](images/commaBelow.png)|Chosen to mirror the shape used for the comma in the Emily's Symbols plugin.<BR><BR>Used in: [ș](https://en.wikipedia.org/wiki/%C8%98) [Ș](https://en.wikipedia.org/wiki/%C8%98) [ț](https://en.wikipedia.org/wiki/%C8%9A) [Ț](https://en.wikipedia.org/wiki/%C8%9A)|
|Diaeresis/Umlaut| |
|![diaeresis](images/diaeresis.png)|Shaped like the diaeresis/umlaut symbols.<BR><BR>NOTE: [diaeresis](https://en.wikipedia.org/wiki/Diaeresis_(diacritic)) and [umlaut](https://en.wikipedia.org/wiki/Umlaut_(diacritic)) are distinct concepts, with separate uses, but are represented by the same Unicode code points. They are created via the same outline in this spelling system.<BR><BR>Used in: [ä](https://en.wikipedia.org/wiki/%C3%84) [Ä](https://en.wikipedia.org/wiki/%C3%84) [ǟ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [Ǟ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [ë](https://en.wikipedia.org/wiki/%C3%8B) [Ë](https://en.wikipedia.org/wiki/%C3%8B) [ï](https://en.wikipedia.org/wiki/%C3%8F) [Ï](https://en.wikipedia.org/wiki/%C3%8F) [n̈](https://en.wikipedia.org/wiki/N%CC%88) [N̈](https://en.wikipedia.org/wiki/N%CC%88) [ö](https://en.wikipedia.org/wiki/%C3%96) [Ö](https://en.wikipedia.org/wiki/%C3%96) [ȫ](https://en.wikipedia.org/wiki/%C3%96) [Ȫ](https://en.wikipedia.org/wiki/%C3%96) [ü](https://en.wikipedia.org/wiki/%C3%9C) [Ü](https://en.wikipedia.org/wiki/%C3%9C) [ẅ](https://en.wikipedia.org/wiki/Two_dots_(diacritic)) [Ẅ](https://en.wikipedia.org/wiki/Two_dots_(diacritic)) [ÿ](https://en.wikipedia.org/wiki/%C5%B8) [Ÿ](https://en.wikipedia.org/wiki/%C5%B8) [ǘ](https://www.compart.com/en/unicode/U+01D8) [Ǘ](https://www.compart.com/en/unicode/U+01D7) [ǖ](https://www.compart.com/en/unicode/U+01D6) [Ǖ](https://www.compart.com/en/unicode/U+01D5) [ǚ](https://www.compart.com/en/unicode/U+01DA) [Ǚ](https://www.compart.com/en/unicode/U+01D9) [ǜ](https://www.compart.com/en/unicode/U+01DC) [Ǜ](https://www.compart.com/en/unicode/U+01DB) [ḧ](https://www.compart.com/en/unicode/U+1E27) [Ḧ](https://www.compart.com/en/unicode/U+1E26) [ḯ](https://www.compart.com/en/unicode/U+1E2F) [Ḯ](https://www.compart.com/en/unicode/U+1E2E) [ṏ](https://www.compart.com/en/unicode/U+1E4F) [Ṏ](https://www.compart.com/en/unicode/U+1E4E) [ṻ](https://www.compart.com/en/unicode/U+1E7B) [Ṻ](https://www.compart.com/en/unicode/U+1E7A) [ẍ](https://www.compart.com/en/unicode/U+1E8D) [Ẍ](https://www.compart.com/en/unicode/U+1E8C) [ẗ](https://www.compart.com/en/unicode/U+1E97)|
|Diaeresis Below| |
|![diaeresisBelow](images/diaeresisBelow.png)|The diaeresis/umlaut shape, but lower.<BR><BR>Used in: [ṳ](https://www.compart.com/en/unicode/U+1E73) [Ṳ](https://www.compart.com/en/unicode/U+1E72)|
|Dot Above| |
|![dotAbove](images/dotAbove.png)|A single key, up high, like a dot above.<BR><BR>Used in: [ȧ](https://en.wikipedia.org/wiki/%C8%A6) [Ȧ](https://en.wikipedia.org/wiki/%C8%A6) [ċ](https://en.wikipedia.org/wiki/%C4%8A) [Ċ](https://en.wikipedia.org/wiki/%C4%8A) [ė](https://en.wikipedia.org/wiki/%C4%96) [Ė](https://en.wikipedia.org/wiki/%C4%96) [ġ](https://en.wikipedia.org/wiki/%C4%A0) [Ġ](https://en.wikipedia.org/wiki/%C4%A0) [i](https://en.wikipedia.org/wiki/%C4%B0) [İ](https://en.wikipedia.org/wiki/%C4%B0) [ṅ](https://en.wikipedia.org/wiki/%E1%B9%84) [Ṅ](https://en.wikipedia.org/wiki/%E1%B9%84) [ȯ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ȯ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ȱ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ȱ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ṡ](https://en.wikipedia.org/wiki/%E1%B9%A0) [Ṡ](https://en.wikipedia.org/wiki/%E1%B9%A0) [ẋ](https://en.wikipedia.org/wiki/%E1%BA%8A) [Ẋ](https://en.wikipedia.org/wiki/%E1%BA%8A) [ż](https://en.wikipedia.org/wiki/%C5%BB) [Ż](https://en.wikipedia.org/wiki/%C5%BB) [ǡ](https://www.compart.com/en/unicode/U+01E1) [Ǡ](https://www.compart.com/en/unicode/U+01E0) [ḃ](https://www.compart.com/en/unicode/U+1E03) [Ḃ](https://www.compart.com/en/unicode/U+1E02) [ḋ](https://www.compart.com/en/unicode/U+1E0B) [Ḋ](https://www.compart.com/en/unicode/U+1E0A) [ḟ](https://www.compart.com/en/unicode/U+1E1F) [Ḟ](https://www.compart.com/en/unicode/U+1E1E) [ḣ](https://www.compart.com/en/unicode/U+1E23) [Ḣ](https://www.compart.com/en/unicode/U+1E22) [ṁ](https://www.compart.com/en/unicode/U+1E41) [Ṁ](https://www.compart.com/en/unicode/U+1E40) [ṗ](https://www.compart.com/en/unicode/U+1E57) [Ṗ](https://www.compart.com/en/unicode/U+1E56) [ṙ](https://www.compart.com/en/unicode/U+1E59) [Ṙ](https://www.compart.com/en/unicode/U+1E58) [ṥ](https://www.compart.com/en/unicode/U+1E65) [Ṥ](https://www.compart.com/en/unicode/U+1E64) [ṧ](https://www.compart.com/en/unicode/U+1E67) [Ṧ](https://www.compart.com/en/unicode/U+1E66) [ṩ](https://www.compart.com/en/unicode/U+1E69) [Ṩ](https://www.compart.com/en/unicode/U+1E68) [ṫ](https://www.compart.com/en/unicode/U+1E6B) [Ṫ](https://www.compart.com/en/unicode/U+1E6A) [ẇ](https://www.compart.com/en/unicode/U+1E87) [Ẇ](https://www.compart.com/en/unicode/U+1E86) [ẏ](https://www.compart.com/en/unicode/U+1E8F) [Ẏ](https://www.compart.com/en/unicode/U+1E8E)|
|Dot Below| |
|![dotBelow](images/dotBelow.png)|A single key, down low, like a dot below.<BR><BR>Used in: [ḅ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ḅ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ḍ](https://en.wikipedia.org/wiki/%E1%B8%8C) [Ḍ](https://en.wikipedia.org/wiki/%E1%B8%8C) [ẹ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ẹ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ḥ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ḥ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ị](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ị](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ḷ](https://en.wikipedia.org/wiki/%E1%B8%B6) [Ḷ](https://en.wikipedia.org/wiki/%E1%B8%B6) [ọ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ọ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ṛ](https://en.wikipedia.org/wiki/%E1%B9%9A) [Ṛ](https://en.wikipedia.org/wiki/%E1%B9%9A) [ș](https://en.wikipedia.org/wiki/%E1%B9%A2) [Ș](https://en.wikipedia.org/wiki/%E1%B9%A2) [ṭ](https://en.wikipedia.org/wiki/%E1%B9%AC) [Ṭ](https://en.wikipedia.org/wiki/%E1%B9%AC) [ụ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ụ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ẓ](https://en.wikipedia.org/wiki/%E1%BA%92) [Ẓ](https://en.wikipedia.org/wiki/%E1%BA%92) [ỵ](https://www.compart.com/en/unicode/U+1EF5) [Ỵ](https://www.compart.com/en/unicode/U+1EF4) [ạ](https://www.compart.com/en/unicode/U+1EA1) [Ạ](https://www.compart.com/en/unicode/U+1EA0) [ặ](https://www.compart.com/en/unicode/U+1EB7) [Ặ](https://www.compart.com/en/unicode/U+1EB6) [ậ](https://www.compart.com/en/unicode/U+1EAD) [Ậ](https://www.compart.com/en/unicode/U+1EAC) [ợ](https://www.compart.com/en/unicode/U+1EE3) [Ợ](https://www.compart.com/en/unicode/U+1EE2) [ộ](https://www.compart.com/en/unicode/U+1ED9) [Ộ](https://www.compart.com/en/unicode/U+1ED8) [ệ](https://www.compart.com/en/unicode/U+1EC7) [Ệ](https://www.compart.com/en/unicode/U+1EC6) [ự](https://www.compart.com/en/unicode/U+1EF1) [Ự](https://www.compart.com/en/unicode/U+1EF0) [ḳ](https://www.compart.com/en/unicode/U+1E33) [Ḳ](https://www.compart.com/en/unicode/U+1E32) [ḹ](https://www.compart.com/en/unicode/U+1E39) [Ḹ](https://www.compart.com/en/unicode/U+1E38) [ṃ](https://www.compart.com/en/unicode/U+1E43) [Ṃ](https://www.compart.com/en/unicode/U+1E42) [ṇ](https://www.compart.com/en/unicode/U+1E47) [Ṇ](https://www.compart.com/en/unicode/U+1E46) [ṝ](https://www.compart.com/en/unicode/U+1E5D) [Ṝ](https://www.compart.com/en/unicode/U+1E5C) [ṣ](https://www.compart.com/en/unicode/U+1E63) [Ṣ](https://www.compart.com/en/unicode/U+1E62) [ṩ](https://www.compart.com/en/unicode/U+1E69) [Ṩ](https://www.compart.com/en/unicode/U+1E68) [ṿ](https://www.compart.com/en/unicode/U+1E7F) [Ṿ](https://www.compart.com/en/unicode/U+1E7E) [ẉ](https://www.compart.com/en/unicode/U+1E89) [Ẉ](https://www.compart.com/en/unicode/U+1E88)|
|Grave| |
|![grave](images/grave.png)|Shaped like the grave symbol.<BR><BR>Used in: [à](https://en.wikipedia.org/wiki/%C3%80) [À](https://en.wikipedia.org/wiki/%C3%80) [è](https://en.wikipedia.org/wiki/%C3%88) [È](https://en.wikipedia.org/wiki/%C3%88) [ì](https://en.wikipedia.org/wiki/%C3%8C) [Ì](https://en.wikipedia.org/wiki/%C3%8C) [ò](https://en.wikipedia.org/wiki/%C3%92) [Ò](https://en.wikipedia.org/wiki/%C3%92) [ù](https://en.wikipedia.org/wiki/Grave_accent) [Ù](https://en.wikipedia.org/wiki/Grave_accent) [ẁ](https://en.wikipedia.org/wiki/Grave_accent) [Ẁ](https://en.wikipedia.org/wiki/Grave_accent) [ỳ](https://en.wikipedia.org/wiki/Grave_accent) [Ỳ](https://en.wikipedia.org/wiki/Grave_accent) [ằ](https://www.compart.com/en/unicode/U+1EB1) [Ằ](https://www.compart.com/en/unicode/U+1EB0) [ầ](https://www.compart.com/en/unicode/U+1EA7) [Ầ](https://www.compart.com/en/unicode/U+1EA6) [ờ](https://www.compart.com/en/unicode/U+1EDD) [Ờ](https://www.compart.com/en/unicode/U+1EDC) [ồ](https://www.compart.com/en/unicode/U+1ED3) [Ồ](https://www.compart.com/en/unicode/U+1ED2) [ề](https://www.compart.com/en/unicode/U+1EC1) [Ề](https://www.compart.com/en/unicode/U+1EC0) [ừ](https://www.compart.com/en/unicode/U+1EEB) [Ừ](https://www.compart.com/en/unicode/U+1EEA) [ǜ](https://www.compart.com/en/unicode/U+01DC) [Ǜ](https://www.compart.com/en/unicode/U+01DB) [ǹ](https://www.compart.com/en/unicode/U+01F9) [Ǹ](https://www.compart.com/en/unicode/U+01F8) [ḕ](https://www.compart.com/en/unicode/U+1E15) [Ḕ](https://www.compart.com/en/unicode/U+1E14) [ṑ](https://www.compart.com/en/unicode/U+1E51) [Ṑ](https://www.compart.com/en/unicode/U+1E50)|
|Double Grave| |
|![graveDoubled](images/graveDoubled.png)|The grave modifier shape, with the '[extra](#modifier-tweaks)' tweak.<BR><BR>Used in: [ȁ](https://www.compart.com/en/unicode/U+0201) [Ȁ](https://www.compart.com/en/unicode/U+0200) [ȅ](https://www.compart.com/en/unicode/U+0205) [Ȅ](https://www.compart.com/en/unicode/U+0204) [ȉ](https://www.compart.com/en/unicode/U+0209) [Ȉ](https://www.compart.com/en/unicode/U+0208) [ȍ](https://www.compart.com/en/unicode/U+020D) [Ȍ](https://www.compart.com/en/unicode/U+020C) [ȑ](https://www.compart.com/en/unicode/U+0211) [Ȑ](https://www.compart.com/en/unicode/U+0210) [ȕ](https://www.compart.com/en/unicode/U+0215) [Ȕ](https://www.compart.com/en/unicode/U+0214)|
|Hook Above| |
|![hookAbove](images/hookAbove.png)|Shaped like the hook above symbol, sticking up, and curling to the left.<BR><BR>Used in: [ỷ](https://www.compart.com/en/unicode/U+1EF7) [Ỷ](https://www.compart.com/en/unicode/U+1EF6) [ẳ](https://www.compart.com/en/unicode/U+1EB3) [Ẳ](https://www.compart.com/en/unicode/U+1EB2) [ả](https://www.compart.com/en/unicode/U+1EA3) [Ả](https://www.compart.com/en/unicode/U+1EA2) [ẩ](https://www.compart.com/en/unicode/U+1EA9) [Ẩ](https://www.compart.com/en/unicode/U+1EA8) [ỏ](https://www.compart.com/en/unicode/U+1ECF) [Ỏ](https://www.compart.com/en/unicode/U+1ECE) [ở](https://www.compart.com/en/unicode/U+1EDF) [Ở](https://www.compart.com/en/unicode/U+1EDE) [ổ](https://www.compart.com/en/unicode/U+1ED5) [Ổ](https://www.compart.com/en/unicode/U+1ED4) [ẻ](https://www.compart.com/en/unicode/U+1EBB) [Ẻ](https://www.compart.com/en/unicode/U+1EBA) [ể](https://www.compart.com/en/unicode/U+1EC3) [Ể](https://www.compart.com/en/unicode/U+1EC2) [ỉ](https://www.compart.com/en/unicode/U+1EC9) [Ỉ](https://www.compart.com/en/unicode/U+1EC8) [ủ](https://www.compart.com/en/unicode/U+1EE7) [Ủ](https://www.compart.com/en/unicode/U+1EE6) [ử](https://www.compart.com/en/unicode/U+1EED) [Ử](https://www.compart.com/en/unicode/U+1EEC)|
|Hook| |
|![hook](images/hook.png)|Distinct from hook above, which is a detached diacritic, this is for characters with an attached hook. The hook shape was chosen to match most of these characters, which either curl up, then to the right, or to the left, then down, which makes the same curve. Imagine the chord shape attaching to some at the –R, and others at the –P. Some of the visual nature of this is down to fonts and rendering, of course, and a few letters don't match up well to this chord shape, and will just have to be memorized as exceptions for now.<BR><BR>Used in: [ɓ](https://en.wikipedia.org/wiki/%C6%81) [Ɓ](https://en.wikipedia.org/wiki/%C6%81) [ƈ](https://en.wikipedia.org/wiki/%C6%87) [Ƈ](https://en.wikipedia.org/wiki/%C6%87) [ɗ](https://en.wikipedia.org/wiki/%C6%8A) [Ɗ](https://en.wikipedia.org/wiki/%C6%8A) [ƒ](https://en.wikipedia.org/wiki/%C6%91) [Ƒ](https://en.wikipedia.org/wiki/%C6%91) [ɠ](https://en.wikipedia.org/wiki/G_with_hook) [Ɠ](https://en.wikipedia.org/wiki/G_with_hook) [ƙ](https://en.wikipedia.org/wiki/%C6%98) [Ƙ](https://en.wikipedia.org/wiki/%C6%98) [ƥ](https://en.wikipedia.org/wiki/%C6%A4) [Ƥ](https://en.wikipedia.org/wiki/%C6%A4) [ƭ](https://en.wikipedia.org/wiki/%C6%AC) [Ƭ](https://en.wikipedia.org/wiki/%C6%AC) [ƴ](https://en.wikipedia.org/wiki/%C6%B3) [Ƴ](https://en.wikipedia.org/wiki/%C6%B3)|
|Horn| |
|![horn](images/horn.png)|Shaped like the horn symbol, sticking out to the right and curving upward. The shape is also on the right-hand side of the modifier keys cluster, as the horn sticks out the right side of it characters.<BR><BR>Used in: [ơ](https://en.wikipedia.org/wiki/%C6%A0) [Ơ](https://en.wikipedia.org/wiki/%C6%A0) [ư](https://en.wikipedia.org/wiki/%C6%AF) [Ư](https://en.wikipedia.org/wiki/%C6%AF) [ơ](https://en.wikipedia.org/wiki/%C6%A0) [Ơ](https://en.wikipedia.org/wiki/%C6%A0) [ợ](https://www.compart.com/en/unicode/U+1EE3) [Ợ](https://www.compart.com/en/unicode/U+1EE2) [ở](https://www.compart.com/en/unicode/U+1EDF) [Ở](https://www.compart.com/en/unicode/U+1EDE) [ỡ](https://www.compart.com/en/unicode/U+1EE1) [Ỡ](https://www.compart.com/en/unicode/U+1EE0) [ờ](https://www.compart.com/en/unicode/U+1EDD) [Ờ](https://www.compart.com/en/unicode/U+1EDC) [ớ](https://www.compart.com/en/unicode/U+1EDB) [Ớ](https://www.compart.com/en/unicode/U+1EDA) [ự](https://www.compart.com/en/unicode/U+1EF1) [Ự](https://www.compart.com/en/unicode/U+1EF0) [ử](https://www.compart.com/en/unicode/U+1EED) [Ử](https://www.compart.com/en/unicode/U+1EEC) [ữ](https://www.compart.com/en/unicode/U+1EEF) [Ữ](https://www.compart.com/en/unicode/U+1EEE) [ừ](https://www.compart.com/en/unicode/U+1EEB) [Ừ](https://www.compart.com/en/unicode/U+1EEA) [ứ](https://www.compart.com/en/unicode/U+1EE9) [Ứ](https://www.compart.com/en/unicode/U+1EE8)|
|Interpunct| |
|![interpunct](images/interpunct.png)|An odd one, which joins the dot above and dot below characters. Think of it as the midpoint of the above and below dots, made by stroking both together.<BR><BR>Used in: [ŀ](https://en.wikipedia.org/wiki/Interpunct#Catalan) [Ŀ](https://en.wikipedia.org/wiki/Interpunct#Catalan)|
|Line Below| |
|![lineBelow](images/lineBelow.png)|When decomposed into base character + diacritic, the combining character for this set of Unicode composed characters is the macron below. Rather than use the the lower version of the chord, on the bottom row, this uses the '[under](#modifier-tweaks)' tweak with the macron shape, to respect this relation.<BR><BR>Used in: [ḇ](https://www.compart.com/en/unicode/U+1E07) [Ḇ](https://www.compart.com/en/unicode/U+1E06) [ḏ](https://www.compart.com/en/unicode/U+1E0F) [Ḏ](https://www.compart.com/en/unicode/U+1E0E) [ḵ](https://www.compart.com/en/unicode/U+1E35) [Ḵ](https://www.compart.com/en/unicode/U+1E34) [ḻ](https://www.compart.com/en/unicode/U+1E3B) [Ḻ](https://www.compart.com/en/unicode/U+1E3A) [ṉ](https://www.compart.com/en/unicode/U+1E49) [Ṉ](https://www.compart.com/en/unicode/U+1E48) [ṟ](https://www.compart.com/en/unicode/U+1E5F) [Ṟ](https://www.compart.com/en/unicode/U+1E5E) [ṯ](https://www.compart.com/en/unicode/U+1E6F) [Ṯ](https://www.compart.com/en/unicode/U+1E6E) [ẕ](https://www.compart.com/en/unicode/U+1E95) [Ẕ](https://www.compart.com/en/unicode/U+1E94) [ẖ](https://www.compart.com/en/unicode/U+1E96)|
|Macron| |
|![macron](images/macron.png)|Shaped like the macron symbol.<BR><BR>Used in: [ǟ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [Ǟ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [ā](https://en.wikipedia.org/wiki/%C4%80) [Ā](https://en.wikipedia.org/wiki/%C4%80) [ē](https://en.wikipedia.org/wiki/Macron_(diacritic)) [Ē](https://en.wikipedia.org/wiki/Macron_(diacritic)) [ī](https://en.wikipedia.org/wiki/Macron_(diacritic)) [Ī](https://en.wikipedia.org/wiki/Macron_(diacritic)) [m̄](https://en.wikipedia.org/wiki/Macron_(diacritic)) [M̄](https://en.wikipedia.org/wiki/Macron_(diacritic)) [n̄](https://en.wikipedia.org/wiki/Macron_(diacritic)) [N̄](https://en.wikipedia.org/wiki/Macron_(diacritic)) [ȱ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [Ȱ](https://en.wikipedia.org/wiki/Dot_(diacritic)) [ȫ](https://en.wikipedia.org/wiki/%C3%96) [Ȫ](https://en.wikipedia.org/wiki/%C3%96) [ō](https://en.wikipedia.org/wiki/Macron_(diacritic)) [Ō](https://en.wikipedia.org/wiki/Macron_(diacritic)) [ȭ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [Ȭ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [p̄](https://en.wikipedia.org/wiki/Macron_(diacritic)#Letter_extension) [P̄](https://en.wikipedia.org/wiki/Macron_(diacritic)#Letter_extension) [ū](https://en.wikipedia.org/wiki/Macron_(diacritic)) [Ū](https://en.wikipedia.org/wiki/Macron_(diacritic)) [ȳ](https://en.wikipedia.org/wiki/%C8%B2) [Ȳ](https://en.wikipedia.org/wiki/%C8%B2) [ǣ](https://en.wikipedia.org/wiki/%C3%86) [Ǣ](https://en.wikipedia.org/wiki/%C3%86) [ǖ](https://www.compart.com/en/unicode/U+01D6) [Ǖ](https://www.compart.com/en/unicode/U+01D5) [ǚ](https://www.compart.com/en/unicode/U+01DA) [Ǚ](https://www.compart.com/en/unicode/U+01D9) [ǡ](https://www.compart.com/en/unicode/U+01E1) [Ǡ](https://www.compart.com/en/unicode/U+01E0) [ǭ](https://www.compart.com/en/unicode/U+01ED) [Ǭ](https://www.compart.com/en/unicode/U+01EC) [ḕ](https://www.compart.com/en/unicode/U+1E15) [Ḕ](https://www.compart.com/en/unicode/U+1E14) [ḗ](https://www.compart.com/en/unicode/U+1E17) [Ḗ](https://www.compart.com/en/unicode/U+1E16) [ḡ](https://www.compart.com/en/unicode/U+1E21) [Ḡ](https://www.compart.com/en/unicode/U+1E20) [ḹ](https://www.compart.com/en/unicode/U+1E39) [Ḹ](https://www.compart.com/en/unicode/U+1E38) [ṑ](https://www.compart.com/en/unicode/U+1E51) [Ṑ](https://www.compart.com/en/unicode/U+1E50) [ṓ](https://www.compart.com/en/unicode/U+1E53) [Ṓ](https://www.compart.com/en/unicode/U+1E52) [ṝ](https://www.compart.com/en/unicode/U+1E5D) [Ṝ](https://www.compart.com/en/unicode/U+1E5C) [ṻ](https://www.compart.com/en/unicode/U+1E7B) [Ṻ](https://www.compart.com/en/unicode/U+1E7A)|
|Ogonek| |
|![ogonek](images/ogonek.png)|The ogonek, meaning 'little tail' in Polish, hangs off the bottom of its character, curling down and to the right.<BR><BR>Used in: [ą](https://en.wikipedia.org/wiki/%C4%84) [Ą](https://en.wikipedia.org/wiki/%C4%84) [ę](https://en.wikipedia.org/wiki/%C4%98) [Ę](https://en.wikipedia.org/wiki/%C4%98) [į](https://en.wikipedia.org/wiki/%C4%AE) [Į](https://en.wikipedia.org/wiki/%C4%AE) [ǫ](https://en.wikipedia.org/wiki/%C7%AA) [Ǫ](https://en.wikipedia.org/wiki/%C7%AA) [ų](https://en.wikipedia.org/wiki/%C5%B2) [Ų](https://en.wikipedia.org/wiki/%C5%B2) [y̨](https://en.wikipedia.org/wiki/Ogonek) [Y̨](https://en.wikipedia.org/wiki/Ogonek) [ǭ](https://www.compart.com/en/unicode/U+01ED) [Ǭ](https://www.compart.com/en/unicode/U+01EC)|
|Ring Above| |
|![ringAbove](images/ringAbove.png)|Think of this square of keys like a little circle, or ring.<BR><BR>Used in: [å](https://en.wikipedia.org/wiki/%C3%85) [Å](https://en.wikipedia.org/wiki/%C3%85) [ǻ](https://en.wikipedia.org/wiki/%C3%85#On_computers) [Ǻ](https://en.wikipedia.org/wiki/%C3%85#On_computers) [ů](https://en.wikipedia.org/wiki/Ring_(diacritic)) [Ů](https://en.wikipedia.org/wiki/Ring_(diacritic)) [ẘ](https://www.compart.com/en/unicode/U+1E98) [ẙ](https://www.compart.com/en/unicode/U+1E99)|
|Ring Below| |
|![ringBelow](images/ringBelow.png)|The ring above modifier shape, with the '[under](#modifier-tweaks)' tweak.<BR><BR>Used in: [ḁ](https://www.compart.com/en/unicode/U+1E01) [Ḁ](https://www.compart.com/en/unicode/U+1E00)|
|Stroke| |
|![stroke](images/stroke.png)|Like the macron, but lower, because it cuts through the character, rather than flying above it.<BR><BR>Used in: [đ](https://en.wikipedia.org/wiki/D_with_stroke) [Đ](https://en.wikipedia.org/wiki/D_with_stroke) [ǥ](https://en.wikipedia.org/wiki/G_with_stroke) [Ǥ](https://en.wikipedia.org/wiki/G_with_stroke) [ħ](https://en.wikipedia.org/wiki/H_with_stroke) [Ħ](https://en.wikipedia.org/wiki/H_with_stroke) [ɨ](https://en.wikipedia.org/wiki/I_with_bar) [Ɨ](https://en.wikipedia.org/wiki/I_with_bar) [ƚ](https://en.wikipedia.org/wiki/L_with_bar) [Ƚ](https://en.wikipedia.org/wiki/L_with_bar) [ɍ](https://en.wikipedia.org/wiki/R_with_stroke) [Ɍ](https://en.wikipedia.org/wiki/R_with_stroke) [ŧ](https://en.wikipedia.org/wiki/T_with_stroke) [Ŧ](https://en.wikipedia.org/wiki/T_with_stroke) [ʉ](https://en.wikipedia.org/wiki/U_with_bar) [Ʉ](https://en.wikipedia.org/wiki/U_with_bar)|
|Slash| |
|![slash](images/slash.png)|Like the acute, but shifted, to indicate that it's lower, and cuts through the character. A bit of a stretch, as it's shifted to the right, not down, but other options were used up. Maybe think of it like moving to the right while reading this text, which eventually wraps, and takes you down a line.<BR><BR>Used in: [ł](https://en.wikipedia.org/wiki/%C5%81) [Ł](https://en.wikipedia.org/wiki/%C5%81) [ø](https://en.wikipedia.org/wiki/%C3%98) [Ø](https://en.wikipedia.org/wiki/%C3%98) [ǿ](https://en.wikipedia.org/wiki/%C3%98#%C7%BE) [Ǿ](https://en.wikipedia.org/wiki/%C3%98#%C7%BE)|
|Tilde| |
|![tilde](images/tilde.png)|Shaped like the tilde symbol.<BR><BR>Used in: [ã](https://en.wikipedia.org/wiki/%C3%83) [Ã](https://en.wikipedia.org/wiki/%C3%83) [ẽ](https://en.wikipedia.org/wiki/%E1%BA%BC) [Ẽ](https://en.wikipedia.org/wiki/%E1%BA%BC) [g̃](https://en.wikipedia.org/wiki/G%CC%83) [G̃](https://en.wikipedia.org/wiki/G%CC%83) [ĩ](https://en.wikipedia.org/wiki/Tilde) [Ĩ](https://en.wikipedia.org/wiki/Tilde) [ñ](https://en.wikipedia.org/wiki/%C3%91) [Ñ](https://en.wikipedia.org/wiki/%C3%91) [õ](https://en.wikipedia.org/wiki/%C3%95) [Õ](https://en.wikipedia.org/wiki/%C3%95) [ȭ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [Ȭ](https://en.wikipedia.org/wiki/Livonian_language#Alphabet) [ũ](https://en.wikipedia.org/wiki/Tilde) [Ũ](https://en.wikipedia.org/wiki/Tilde) [ỹ](https://en.wikipedia.org/wiki/Tilde) [Ỹ](https://en.wikipedia.org/wiki/Tilde) [ẵ](https://www.compart.com/en/unicode/U+1EB5) [Ẵ](https://www.compart.com/en/unicode/U+1EB4) [ẫ](https://www.compart.com/en/unicode/U+1EAB) [Ẫ](https://www.compart.com/en/unicode/U+1EAA) [ỡ](https://www.compart.com/en/unicode/U+1EE1) [Ỡ](https://www.compart.com/en/unicode/U+1EE0) [ỗ](https://www.compart.com/en/unicode/U+1ED7) [Ỗ](https://www.compart.com/en/unicode/U+1ED6) [ễ](https://www.compart.com/en/unicode/U+1EC5) [Ễ](https://www.compart.com/en/unicode/U+1EC4) [ữ](https://www.compart.com/en/unicode/U+1EEF) [Ữ](https://www.compart.com/en/unicode/U+1EEE) [ṍ](https://www.compart.com/en/unicode/U+1E4D) [Ṍ](https://www.compart.com/en/unicode/U+1E4C) [ṏ](https://www.compart.com/en/unicode/U+1E4F) [Ṏ](https://www.compart.com/en/unicode/U+1E4E) [ṹ](https://www.compart.com/en/unicode/U+1E79) [Ṹ](https://www.compart.com/en/unicode/U+1E78) [ṽ](https://www.compart.com/en/unicode/U+1E7D) [Ṽ](https://www.compart.com/en/unicode/U+1E7C)|
|Tilde Below| |
|![tildeBelow](images/tildeBelow.png)|The tilde modifier shape, with the '[under](#modifier-tweaks)' tweak.<BR><BR>Used in: [ḛ](https://www.compart.com/en/unicode/U+1E1B) [Ḛ](https://www.compart.com/en/unicode/U+1E1A) [ḭ](https://www.compart.com/en/unicode/U+1E2D) [Ḭ](https://www.compart.com/en/unicode/U+1E2C) [ṵ](https://www.compart.com/en/unicode/U+1E75) [Ṵ](https://www.compart.com/en/unicode/U+1E74)|
|Turned/Rotated| |
|![turned](images/turned.png)|<BR><BR>Used in: [ⅎ](https://en.wikipedia.org/wiki/Claudian_letters) [Ⅎ](https://en.wikipedia.org/wiki/Claudian_letters) [ᴂ](https://en.wiktionary.org/wiki/%E1%B4%82#Translingual)|
|Reversed| |
|![reversed](images/reversed.png)|<BR><BR>Used in: [ↄ](https://en.wikipedia.org/wiki/Claudian_letters) [Ↄ](https://en.wikipedia.org/wiki/Claudian_letters)|

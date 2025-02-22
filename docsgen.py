from PIL import Image, ImageDraw, ImageFont

from fixspell import modifiers


defaultKeyOpts = {
    "keyWidth": 57,
    "keyHeight": 57,

    "draft": 6,
    "draftOffset": 2,

    "outerRadius": 5,
    "innerRadius": 3,

    "outlineWidth": 1,

    "backgroundCol": "white",
    "keysFrameCol": "#EEEEEE",

    "outerOutlineUp": "black",
    "outerOutlineDown": "black",
    "innerOutlineUp": "#BBBBBB",
    "innerOutlineDown": "#009900",

    "upColorDark": "#CCCCCC",
    "upColorLight": "#FCFCFC",
    "dnColorDark": "#00AA00",
    "dnColorLight": "#46CD34",
}

def genKey (label, pressed=False, topRow=False, **kwargs):
    width = kwargs["keyWidth"]
    height = kwargs["keyHeight"]
    bgCol = kwargs["backgroundCol"]

    image = Image.new("RGB", (width, height), bgCol)
    draw = ImageDraw.Draw(image)

    border = kwargs["outerOutlineDown" if pressed else "outerOutlineUp"]
    rad = kwargs["outerRadius"]
    stroke = kwargs["outlineWidth"]
    col = kwargs["dnColorDark" if pressed else "upColorDark"]
    dims = (0, 0, width - (stroke / 2), height - (stroke / 2))
    opts = {"fill":col, "outline":border, "width":stroke, "radius":rad}
    draw.rounded_rectangle(dims, **opts)

    draft = kwargs["draft"]
    draftOffset = kwargs["draftOffset"]

    offset = draftOffset * (1 if topRow else -1)
    x = draft
    y = draft + offset
    w = width - draft
    h = height - draft + offset
    border = kwargs["innerOutlineDown" if pressed else "innerOutlineUp"]
    stroke = kwargs["outlineWidth"]
    rad = kwargs["innerRadius"]
    col = kwargs["dnColorLight" if pressed else "upColorLight"]
    dims = (x, y, w - (stroke / 2), h - (stroke / 2))
    opts = {"fill":col, "outline":border, "width":stroke, "radius":rad}
    draw.rounded_rectangle(dims, **opts)

    font = ImageFont.truetype('Arial', 16)
    _, _, tw, th = draw.textbbox((0, 0), label, font)
    dims = ((width-tw) / 2, (height-th) / 2 + offset)
    draw.text(dims, label, font=font, fill="black")

    return image


def genDiacriticStrokeImage (s="", **kwargs):
    F = genKey("F", "F" in s, True, **kwargs)
    R = genKey("R", "R" in s, **kwargs)
    P = genKey("P", "P" in s, True, **kwargs)
    B = genKey("B", "B" in s, **kwargs)
    L = genKey("L", "L" in s, True, **kwargs)
    G = genKey("G", "G" in s, **kwargs)

    kw = F.width
    kh = F.height
    w = kw * 3
    h = kw * 2
    x = 0
    y = 0
    image = Image.new("RGB", (w, h))
    image.paste(F, (x, y))
    image.paste(R, (x, y + kw))
    image.paste(P, (x + kw, y))
    image.paste(B, (x + kw, y + kh))
    image.paste(L, (x + kw * 2, y))
    image.paste(G, (x + kw * 2, y + kh))

    return image

def genDiacriticImages ():
    for modName, modStroke in modifiers.items():
        image = genDiacriticStrokeImage(modStroke, **defaultKeyOpts)
        image.save("images/" + modName + ".png", "PNG")

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
![test](http://garyfixler.com/fixlerSpelling/board.png)

## Adding Diacritics
Add diacritics to letters by stroking a chord from the diacritic keys after stroking a letter chord.

In general, the chord used is meant to visually resemble, the diacritic being added.

NOTE: The chords are pre-built, and don't work with Plover's stroke history. This means you must use the chord specified for each letter in this system, before following up with a diacritic stroke. Currently, if you want to use a different stroke for a letter (e.g. STK instead of STKPW for z), you must change it in the python file. This limitation may be addressed at some point.

## Available Diacritics
"""

def generateReadme ():
    print(readmeTop)
    print("|Pattern|Notes|")
    print("|-|-|")
    for diacriticName, combiningMark in combiningMarks.items():
        print("|" + diacriticName.capitalize() + "| |")
        img = "![" + diacriticName + "](images/" + diacriticName + ".png)"
        print("|" + img + "|" + diacriticName + "|")


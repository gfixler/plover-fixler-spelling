from PIL import Image, ImageDraw, ImageFont, ImageFilter

from fixspell import modifiers


northKey = (0, 2)
southKey = (0, -2)
eastKey = (-2, 0)
westKey = (2, 0)

defaultKeyOpts = {
    "unit": 57,

    "topFaceShrink": 6,
    "topFaceOffset": northKey,

    "outerRadius": 5,
    "innerRadius": 3,

    "outlineWidth": 1,

    "frameMargin": 5,
    "frameRadius": 8,

    "backgroundCol": "white",
    "frameCol": "#EEEEEE",

    "keyOutlineCol": "black",
}

defaultKeyCols = {
    "light": "#FCFCFC",
    "dark": "#CCCCCC",
    "ridge": "#BBBBBB",
}

modifierKeyCols = {
    "light": "#46CD34",
    "dark": "#00AA00",
    "ridge": "#009900",
}

tweakKeyCols = {
    "light": "#BF69EE",
    "dark": "#A24ED1",
    "ridge": "#9146BC",
}

def genKey (label, keyCols=defaultKeyCols, keyOpts=defaultKeyOpts):
    smoothing = 8

    unit = keyOpts["unit"] * smoothing
    bgCol = keyOpts["frameCol"]

    image = Image.new("RGB", (unit, unit), bgCol)
    draw = ImageDraw.Draw(image)

    borderCol = keyOpts["keyOutlineCol"]
    stroke = keyOpts["outlineWidth"] * smoothing
    rad = keyOpts["outerRadius"] * smoothing
    col = keyCols["dark"]
    dims = (0, 0, unit - (stroke / 2), unit - (stroke / 2))
    opts = {"fill":col, "outline":borderCol, "width":stroke, "radius":rad}
    draw.rounded_rectangle(dims, **opts)

    topFaceShrink = keyOpts["topFaceShrink"] * smoothing
    xOffset, yOffset = keyOpts["topFaceOffset"]

    xOffset *= smoothing
    yOffset *= smoothing
    x = topFaceShrink + xOffset
    y = topFaceShrink + yOffset
    w = unit - topFaceShrink + xOffset
    h = unit - topFaceShrink + yOffset
    ridgeCol = keyCols["ridge"]
    stroke = keyOpts["outlineWidth"] * smoothing
    rad = keyOpts["innerRadius"] * smoothing
    col = keyCols["light"]
    dims = (x, y, w - (stroke / 2), h - (stroke / 2))
    opts = {"fill":col, "outline":ridgeCol, "width":stroke, "radius":rad}
    draw.rounded_rectangle(dims, **opts)

    font = ImageFont.truetype('Arial', 14 * smoothing)
    _, _, tw, th = draw.textbbox((0, 0), label, font)
    dims = ((unit-tw) / 2 + xOffset, (unit-th) / 2 + yOffset)
    draw.text(dims, label, font=font, fill="black")

    downRes = image.resize((image.width // smoothing, image.height // smoothing), resample=Image.LANCZOS)

    return downRes


def genDiacriticStrokeImage (stroke="", keyOpts=defaultKeyOpts):
    pressed = lambda k: modifierKeyCols if k in stroke else defaultKeyCols
    north = {"topFaceOffset": northKey}
    south = {"topFaceOffset": southKey}
    west = {"topFaceOffset": westKey}
    east = {"topFaceOffset": eastKey}

    F = genKey("F", pressed("F"), keyOpts | north)
    R = genKey("R", pressed("R"), keyOpts | south)
    P = genKey("P", pressed("P"), keyOpts | north)
    B = genKey("B", pressed("B"), keyOpts | south)
    L = genKey("L", pressed("L"), keyOpts | north)
    G = genKey("G", pressed("G"), keyOpts | south)

    pressed = lambda k: tweakKeyCols if k in stroke else defaultKeyCols
    E = genKey("E", pressed("E"), keyOpts | west)
    U = genKey("U", pressed("U"), keyOpts | east)

    kw = F.width
    kh = F.height

    margin = 8
    w = kw * 3 + margin * 2
    h = kh * 2 + margin * 2
    x = margin
    y = margin

    bgCol = keyOpts["backgroundCol"]
    image = Image.new("RGB", (w, h), bgCol)
    draw = ImageDraw.Draw(image)

    rad = keyOpts["frameRadius"]
    col = keyOpts["frameCol"]
    dims = (0, 0, image.width, image.height)
    opts = {"fill":col, "radius":rad}
    draw.rounded_rectangle(dims, **opts)

    image.paste(F, (x, y))
    image.paste(R, (x, y + kw))
    image.paste(P, (x + kw, y))
    image.paste(B, (x + kw, y + kh))
    image.paste(L, (x + kw * 2, y))
    image.paste(G, (x + kw * 2, y + kh))

    return image

def genDiacriticImages ():
    for modName, modData in modifiers.items():
        image = genDiacriticStrokeImage(modData["outline"])
        image.save("images/" + modName + ".png", "PNG")

def genTweakStrokeImage (stroke="", keyOpts=defaultKeyOpts):
    pressed = lambda k: tweakKeyCols if k in stroke else defaultKeyCols
    west = {"topFaceOffset": westKey}
    east = {"topFaceOffset": eastKey}

    E = genKey("E", pressed("E"), keyOpts | west)
    U = genKey("U", pressed("U"), keyOpts | east)

    kw = E.width
    kh = E.height

    margin = 8
    w = kw * 2 + margin * 2
    h = kh * 1 + margin * 2
    x = margin
    y = margin

    bgCol = keyOpts["backgroundCol"]
    image = Image.new("RGB", (w, h), bgCol)
    draw = ImageDraw.Draw(image)

    rad = keyOpts["frameRadius"]
    col = keyOpts["frameCol"]
    dims = (0, 0, image.width, image.height)
    opts = {"fill":col, "radius":rad}
    draw.rounded_rectangle(dims, **opts)

    image.paste(E, (x, y))
    image.paste(U, (x + kw, y))

    return image

def genTweakImages ():
    genTweakStrokeImage("").save("images/EU_up.png", "PNG")
    genTweakStrokeImage("E").save("images/E_down.png", "PNG")
    genTweakStrokeImage("U").save("images/U_down.png", "PNG")
    genTweakStrokeImage("EU").save("images/EU_down.png", "PNG")

if __name__ == "__main__":
    genDiacriticImages()
    genTweakImages()


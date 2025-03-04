from PIL import Image, ImageDraw, ImageFont, ImageFilter

from fixspell import modifiers


defaultKeyOpts = {
    "unit": 57,

    "faceMargin": 6,

    "faceOffsetX": 0,
    "faceOffsetY": 0,

    "baseCornerRadius": 5,
    "faceCornerRadius": 3,

    "outlineWidth": 1,

    "frameMargin": 5,
    "frameRadius": 8,
}

defaultKeyCols = {
    "backgroundCol": "white",
    "frameCol": "#EEEEEE",
    "keyOutlineCol": "black",

    "light": "#FCFCFC",
    "dark": "#CCCCCC",
    "ridge": "#BBBBBB",
}

modifierKeyCols = defaultKeyCols | {
    "light": "#46CD34",
    "dark": "#00AA00",
    "ridge": "#009900",
}

tweakKeyCols = defaultKeyCols | {
    "light": "#BF69EE",
    "dark": "#A24ED1",
    "ridge": "#9146BC",
}

def genKey (label, keyOpts=defaultKeyOpts, keyCols=defaultKeyCols):
    smoothing = 8

    unit = keyOpts["unit"] * smoothing
    bgCol = keyCols["frameCol"]

    image = Image.new("RGB", (unit, unit), bgCol)
    draw = ImageDraw.Draw(image)

    col = keyCols["dark"]
    borderCol = keyCols["keyOutlineCol"]
    stroke = keyOpts["outlineWidth"] * smoothing
    rad = keyOpts["baseCornerRadius"] * smoothing
    dims = (0, 0, unit - (stroke / 2), unit - (stroke / 2))
    opts = {"fill":col, "outline":borderCol, "width":stroke, "radius":rad}
    draw.rounded_rectangle(dims, **opts)

    faceMargin = keyOpts["faceMargin"] * smoothing
    xOffset = keyOpts["faceOffsetX"]
    yOffset = keyOpts["faceOffsetY"]

    xOffset *= smoothing
    yOffset *= smoothing
    x = faceMargin + xOffset
    y = faceMargin + yOffset
    w = unit - faceMargin + xOffset
    h = unit - faceMargin + yOffset
    col = keyCols["light"]
    ridgeCol = keyCols["ridge"]
    stroke = keyOpts["outlineWidth"] * smoothing
    rad = keyOpts["faceCornerRadius"] * smoothing
    dims = (x, y, w - (stroke / 2), h - (stroke / 2))
    opts = {"fill":col, "outline":ridgeCol, "width":stroke, "radius":rad}
    draw.rounded_rectangle(dims, **opts)

    font = ImageFont.truetype('Arial', 14 * smoothing)
    _, _, tw, th = draw.textbbox((0, 0), label, font)
    dims = ((unit-tw) / 2 + xOffset, (unit-th) / 2 + yOffset)
    draw.text(dims, label, font=font, fill="black")

    downRes = image.resize((image.width // smoothing, image.height // smoothing), resample=Image.LANCZOS)

    return downRes


def genDiacriticStrokeImage (stroke="", keyOpts=defaultKeyOpts, keyCols=defaultKeyCols):
    pressed = lambda k: modifierKeyCols if k in stroke else defaultKeyCols

    north = {"faceOffsetY": 2}
    south = {"faceOffsetY": -2}
    east = {"faceOffsetX": -2}
    west = {"faceOffsetX": 2}

    F = genKey("F", keyOpts | north, pressed("F"))
    R = genKey("R", keyOpts | south, pressed("R"))
    P = genKey("P", keyOpts | north, pressed("P"))
    B = genKey("B", keyOpts | south, pressed("B"))
    L = genKey("L", keyOpts | north, pressed("L"))
    G = genKey("G", keyOpts | south, pressed("G"))

    kw = F.width
    kh = F.height

    margin = 8
    w = kw * 3 + margin * 2
    h = kh * 2 + margin * 2
    x = margin
    y = margin

    bgCol = keyCols["backgroundCol"]
    image = Image.new("RGB", (w, h), bgCol)
    draw = ImageDraw.Draw(image)

    col = keyCols["frameCol"]
    rad = keyOpts["frameRadius"]
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

def genTweakStrokeImage (stroke="", keyOpts=defaultKeyOpts, keyCols=defaultKeyCols):
    pressed = lambda k: tweakKeyCols if k in stroke else defaultKeyCols

    east = {"faceOffsetX": -2}
    west = {"faceOffsetX": 2}

    E = genKey("E", keyOpts | west, pressed("E"))
    U = genKey("U", keyOpts | east, pressed("U"))

    kw = E.width
    kh = E.height

    margin = 8
    w = kw * 2 + margin * 2
    h = kh * 1 + margin * 2
    x = margin
    y = margin

    bgCol = keyCols["backgroundCol"]
    image = Image.new("RGB", (w, h), bgCol)
    draw = ImageDraw.Draw(image)

    rad = keyOpts["frameRadius"]
    col = keyCols["frameCol"]
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


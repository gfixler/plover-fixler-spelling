from PIL import Image, ImageDraw, ImageFont, ImageFilter

from fixspell import modifiers


defaultKeyOpts = {
    "keyWidth": 57,
    "keyHeight": 57,

    "draft": 6,
    "draftOffset": 2,

    "outerRadius": 5,
    "innerRadius": 3,

    "outlineWidth": 1,

    "frameMargin": 5,
    "frameRadius": 8,

    "backgroundCol": "white",
    "frameCol": "#EEEEEE",

    "keyOutlineCol": "black",

    "keyLightCol": "#FCFCFC",
    "keyDarkCol": "#CCCCCC",
    "keyRidgeCol": "#BBBBBB",

    "modLightCol": "#46CD34",
    "modDarkCol": "#00AA00",
    "modRidgeCol": "#009900",

    "tweakLightCol": "#BF69EE",
    "tweakDarkCol": "#A24ED1",
    "tweakRidgeCol": "#9146BC",
}

def genKey (label, keyType="key", topRow=False, **kwargs):
    upResFactor = 8

    width = kwargs["keyWidth"] * upResFactor
    height = kwargs["keyHeight"] * upResFactor
    bgCol = kwargs["frameCol"]

    image = Image.new("RGB", (width, height), bgCol)
    draw = ImageDraw.Draw(image)

    border = kwargs["keyOutlineCol"]
    stroke = kwargs["outlineWidth"] * upResFactor
    rad = kwargs["outerRadius"] * upResFactor
    col = kwargs[keyType + "DarkCol"]
    dims = (0, 0, width - (stroke / 2), height - (stroke / 2))
    opts = {"fill":col, "outline":border, "width":stroke, "radius":rad}
    draw.rounded_rectangle(dims, **opts)

    draft = kwargs["draft"] * upResFactor
    draftOffset = kwargs["draftOffset"] * upResFactor

    offset = draftOffset * (1 if topRow else -1)
    x = draft
    y = draft + offset
    w = width - draft
    h = height - draft + offset
    border = kwargs[keyType + "RidgeCol"]
    stroke = kwargs["outlineWidth"] * upResFactor
    rad = kwargs["innerRadius"] * upResFactor
    col = kwargs[keyType + "LightCol"]
    dims = (x, y, w - (stroke / 2), h - (stroke / 2))
    opts = {"fill":col, "outline":border, "width":stroke, "radius":rad}
    draw.rounded_rectangle(dims, **opts)

    font = ImageFont.truetype('Arial', 14 * upResFactor)
    _, _, tw, th = draw.textbbox((0, 0), label, font)
    dims = ((width-tw) / 2, (height-th) / 2 + offset)
    draw.text(dims, label, font=font, fill="black")

    downRes = image.resize((image.width // upResFactor, image.height // upResFactor), resample=Image.LANCZOS)

    return downRes


def genDiacriticStrokeImage (stroke="", **kwargs):
    pressed = lambda k: "mod" if k in stroke else "key"
    F = genKey("F", pressed("F"), True, **kwargs)
    R = genKey("R", pressed("R"), **kwargs)
    P = genKey("P", pressed("P"), True, **kwargs)
    B = genKey("B", pressed("B"), **kwargs)
    L = genKey("L", pressed("L"), True, **kwargs)
    G = genKey("G", pressed("G"), **kwargs)

    pressed = lambda k: "tweak" if k in stroke else "key"
    E = genKey("E", pressed("E"), ** kwargs)
    U = genKey("U", pressed("U"), ** kwargs)

    kw = F.width
    kh = F.height

    tweaked = "E" in stroke or "U" in stroke
    margin = 8
    w = kw * 3 + margin * 2
    h = kw * (4 if tweaked else 2) + margin * 2
    x = margin
    y = margin

    bgCol = kwargs["backgroundCol"]
    image = Image.new("RGB", (w, h), bgCol)
    draw = ImageDraw.Draw(image)

    rad = kwargs["frameRadius"]
    col = kwargs["frameCol"]
    dims = (0, 0, image.width, image.height)
    opts = {"fill":col, "radius":rad}
    draw.rounded_rectangle(dims, **opts)

    image.paste(F, (x, y))
    image.paste(R, (x, y + kw))
    image.paste(P, (x + kw, y))
    image.paste(B, (x + kw, y + kh))
    image.paste(L, (x + kw * 2, y))
    image.paste(G, (x + kw * 2, y + kh))

    if "E" in stroke or "U" in stroke:
        image.paste(E, (x, y + kh * 3))
        image.paste(U, (x + kw, y + kh * 3))

    return image

def genDiacriticImages ():
    for modName, modStroke in modifiers.items():
        image = genDiacriticStrokeImage(modStroke, **defaultKeyOpts)
        image.save("images/" + modName + ".png", "PNG")

if __name__ == "__main__":
    genDiacriticImages()


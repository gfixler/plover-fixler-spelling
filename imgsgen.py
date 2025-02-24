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
}

def genKey (label, pressed=False, topRow=False, **kwargs):
    upResFactor = 8

    width = kwargs["keyWidth"] * upResFactor
    height = kwargs["keyHeight"] * upResFactor
    bgCol = kwargs["frameCol"]

    image = Image.new("RGB", (width, height), bgCol)
    draw = ImageDraw.Draw(image)

    border = kwargs["keyOutlineCol"]
    stroke = kwargs["outlineWidth"] * upResFactor
    rad = kwargs["outerRadius"] * upResFactor
    col = kwargs["modDarkCol" if pressed else "keyDarkCol"]
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
    border = kwargs["modRidgeCol" if pressed else "keyRidgeCol"]
    stroke = kwargs["outlineWidth"] * upResFactor
    rad = kwargs["innerRadius"] * upResFactor
    col = kwargs["modLightCol" if pressed else "keyLightCol"]
    dims = (x, y, w - (stroke / 2), h - (stroke / 2))
    opts = {"fill":col, "outline":border, "width":stroke, "radius":rad}
    draw.rounded_rectangle(dims, **opts)

    font = ImageFont.truetype('Arial', 14 * upResFactor)
    _, _, tw, th = draw.textbbox((0, 0), label, font)
    dims = ((width-tw) / 2, (height-th) / 2 + offset)
    draw.text(dims, label, font=font, fill="black")

    downRes = image.resize((image.width // upResFactor, image.height // upResFactor), resample=Image.LANCZOS)

    return downRes


def genDiacriticStrokeImage (s="", **kwargs):
    F = genKey("F", "F" in s, True, **kwargs)
    R = genKey("R", "R" in s, **kwargs)
    P = genKey("P", "P" in s, True, **kwargs)
    B = genKey("B", "B" in s, **kwargs)
    L = genKey("L", "L" in s, True, **kwargs)
    G = genKey("G", "G" in s, **kwargs)

    kw = F.width
    kh = F.height

    margin = 8
    w = kw * 3 + margin * 2
    h = kw * 2 + margin * 2
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

    return image

def genDiacriticImages ():
    for modName, modStroke in modifiers.items():
        image = genDiacriticStrokeImage(modStroke, **defaultKeyOpts)
        image.save("images/" + modName + ".png", "PNG")



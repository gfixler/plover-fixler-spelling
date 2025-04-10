from PIL import Image, ImageDraw, ImageFont, ImageFilter
from dataclasses import dataclass

from fixspell import MODIFIERS


# functional helpers
fst = lambda pair: pair[0]
snd = lambda pair: pair[1]


# helpful coordinates
ORIGIN = (0, 0)
UNIT = (1, 1)

# direction key top "leans"
NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)


# key options
@dataclass
class KeyOpts:
    """
    Default key options.
    """
    unit: int = 57
    size: tuple = (1, 1)
    faceMargin: int = 6
    shiftBy: int = 2
    shiftDir: tuple = NORTH
    baseRad: int = 5
    faceRad: int = 3
    outlineWidth: int = 1
    frameMargin: int = 5
    frameRadius: int = 8
    typeface: str = "Arial"
    fontSize: int = 14


# key colors
@dataclass
class KeyCols:
    """
    Default key colors.
    """
    bg = (255, 255, 255, 0)
    frame: str = "#EEEEEE"
    border: str = "black"
    font: str = "black"
    light: str = "#FCFCFC"
    dark: str = "#CCCCCC"
    ridge: str = "#BBBBBB"

defaultKeyCols = KeyCols()

modifierKeyCols = KeyCols(
    light = "#46CD34",
    dark = "#00AA00",
    ridge = "#009900",
)

tweakKeyCols = KeyCols(
    light = "#BF69EE",
    dark = "#A24ED1",
    ridge = "#9146BC",
)


# default key
@dataclass
class Key:
    label: str = ""
    pos: tuple = ORIGIN
    shift: tuple = NORTH
    size: tuple = UNIT
    cols: dict = KeyCols()


def genKey (label, opts=None, cols=None, smoothing=8):
    """
    Takes a key label, and optional options, colors, and smoothing value.
    Returns an image of keyboard key.

    opts, cols, and smoothing will use sensible defaults if not passed.
    """
    # if nothing passed, use defaults
    opts = opts or KeyOpts()
    cols = cols or KeyCols()

    # scale up all dimensions if smoothing requires it
    # drawing large, and scaling at the end, makes a smoother image
    if smoothing > 1:
        opts = KeyOpts(**{k: v * smoothing if isinstance(v, int) else v for k, v in vars(opts).items()})

    unitsWide, unitsHigh = opts.size

    # create an image and a drawing context for it
    image = Image.new("RGBA", (opts.unit * unitsWide, opts.unit * unitsHigh), cols.bg)
    draw = ImageDraw.Draw(image)

    # draw the key base
    dims = (0, 0, opts.unit * unitsWide - 1, opts.unit * unitsHigh - 1)
    rectOpts = {
        "fill": cols.dark,
        "outline": cols.border,
        "width": opts.outlineWidth,
        "radius": opts.baseRad
    }
    draw.rounded_rectangle(dims, **rectOpts)

    # set up top face shift, if any
    shiftX, shiftY = opts.shiftDir
    xShift = shiftX * opts.shiftBy
    yShift = shiftY * opts.shiftBy

    # draw the key face
    x = opts.faceMargin + xShift
    y = opts.faceMargin + yShift
    w = opts.unit * unitsWide - opts.faceMargin + xShift
    h = opts.unit * unitsHigh - opts.faceMargin + yShift
    dims = (x, y, w - 1, h - 1)
    rectOpts = {
        "fill": cols.light,
        "outline": cols.ridge,
        "width": opts.outlineWidth,
        "radius": opts.faceRad
    }
    draw.rounded_rectangle(dims, **rectOpts)

    # add the label to the key
    font = ImageFont.truetype(opts.typeface, opts.fontSize)
    _, _, tw, th = draw.textbbox((0, 0), label, font)
    dims = ((opts.unit * unitsWide - tw) / 2 + xShift, (opts.unit * unitsHigh - th) / 2 + yShift)
    draw.text(dims, label, font=font, fill="black")

    # if smoothing, we scaled up, so scale back down, and get antialiased
    if smoothing > 1:
        newWidth = image.width // smoothing
        newHeight = image.height // smoothing
        final = image.resize((newWidth, newHeight), resample=Image.LANCZOS)
    else:
        final = image

    return final


stenoKeys = [
    ("S", (0,0),  EAST, (1,2)),
    ("T", (1,0), SOUTH,  UNIT),
    ("K", (1,1), NORTH,  UNIT),
    ("P", (2,0), SOUTH,  UNIT),
    ("W", (2,1), NORTH,  UNIT),
    ("H", (3,0), SOUTH,  UNIT),
    ("R", (3,1), NORTH,  UNIT),
    ("A", (2,2),  EAST,  UNIT),
    ("O", (3,2),  WEST,  UNIT),
    ("*", (4,0), (0,0), (1,2)),
    ("E", (5,2),  EAST,  UNIT),
    ("U", (6,2),  WEST,  UNIT),
    ("F", (5,0), SOUTH,  UNIT),
    ("R", (5,1), NORTH,  UNIT),
    ("P", (6,0), SOUTH,  UNIT),
    ("B", (6,1), NORTH,  UNIT),
    ("L", (7,0), SOUTH,  UNIT),
    ("G", (7,1), NORTH,  UNIT),
    ("T", (8,0), SOUTH,  UNIT),
    ("S", (8,1), NORTH,  UNIT),
    ("D", (9,0), SOUTH,  UNIT),
    ("Z", (9,1), NORTH,  UNIT),
]


def buildKeyboard (kbdKeys):
    return [Key(*k) for k in kbdKeys]

def renderKeyboard (keys):
    minX = minY = float('inf')
    maxX = maxY = float('-inf')

    renders = []
    for key in keys:
        x, y = key.pos

        options = {
            "shiftDir": key.shift,
            "size": key.size,
        }
        opts = KeyOpts(**options)
        keyImg = genKey(key.label, opts, key.cols)
        imgW, imgH = keyImg.size

        keyX = x * imgW
        keyY = y * imgH

        minX = min(minX, keyX)
        minY = min(minY, keyY)
        maxX = max(maxX, keyX + imgW)
        maxY = max(maxY, keyY + imgH)

        renders.append((keyImg, keyX, keyY))

    image = Image.new("RGBA", (maxX - minX, maxY - minY), (255, 255, 255, 0))

    for keyImg, x, y in renders:
        image.paste(keyImg, (x - minX, y - minY))

    return image

# def genDiacriticStrokeImage (stroke="", keyOpts=defaultKeyOpts, keyCols=defaultKeyCols):
#     pressed = lambda k: modifierKeyCols if k in stroke else defaultKeyCols

#     north = {"faceOffsetY": 2}
#     south = {"faceOffsetY": -2}
#     east = {"faceOffsetX": -2}
#     west = {"faceOffsetX": 2}

#     F = genKey("F", keyOpts | north, pressed("F"))
#     R = genKey("R", keyOpts | south, pressed("R"))
#     P = genKey("P", keyOpts | north, pressed("P"))
#     B = genKey("B", keyOpts | south, pressed("B"))
#     L = genKey("L", keyOpts | north, pressed("L"))
#     G = genKey("G", keyOpts | south, pressed("G"))

#     kw = F.width
#     kh = F.height

#     margin = 8
#     w = kw * 3 + margin * 2
#     h = kh * 2 + margin * 2
#     x = margin
#     y = margin

#     bgCol = keyCols["bg"]
#     image = Image.new("RGBA", (w, h), bgCol)
#     draw = ImageDraw.Draw(image)

#     col = keyCols["frame"]
#     rad = opts.frameRadius
#     dims = (0, 0, image.width, image.height)
#     opts = {"fill":col, "radius":rad}
#     draw.rounded_rectangle(dims, **opts)

#     image.paste(F, (x, y))
#     image.paste(R, (x, y + kw))
#     image.paste(P, (x + kw, y))
#     image.paste(B, (x + kw, y + kh))
#     image.paste(L, (x + kw * 2, y))
#     image.paste(G, (x + kw * 2, y + kh))

#     return image

# def genDiacriticImages ():
#     for modName, modData in MODIFIERS.items():
#         image = genDiacriticStrokeImage(modData["outline"])
#         image.save("images/" + modName + ".png", "PNG")

# def genTweakStrokeImage (stroke="", keyOpts=defaultKeyOpts, keyCols=defaultKeyCols):
#     pressed = lambda k: tweakKeyCols if k in stroke else defaultKeyCols

#     east = {"faceOffsetX": -2}
#     west = {"faceOffsetX": 2}

#     E = genKey("E", keyOpts | west, pressed("E"))
#     U = genKey("U", keyOpts | east, pressed("U"))

#     kw = E.width
#     kh = E.height

#     margin = 8
#     w = kw * 2 + margin * 2
#     h = kh * 1 + margin * 2
#     x = margin
#     y = margin

#     bgCol = keyCols["bg"]
#     image = Image.new("RGBA", (w, h), bgCol)
#     draw = ImageDraw.Draw(image)

#     rad = keyOpts["frameRadius"]
#     col = keyCols["frame"]
#     dims = (0, 0, image.width, image.height)
#     opts = {"fill":col, "radius":rad}
#     draw.rounded_rectangle(dims, **opts)

#     image.paste(E, (x, y))
#     image.paste(U, (x + kw, y))

#     return image

# def genTweakImages ():
#     genTweakStrokeImage("").save("images/EU_up.png", "PNG")
#     genTweakStrokeImage("E").save("images/E_down.png", "PNG")
#     genTweakStrokeImage("U").save("images/U_down.png", "PNG")
#     genTweakStrokeImage("EU").save("images/EU_down.png", "PNG")

# if __name__ == "__main__":
#     genDiacriticImages()
#     genTweakImages()


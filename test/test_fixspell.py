import unittest

from fixspell import *


S = T = K = P = W = H = R = A = O = DASH = STAR = E = U = F = B = L = G = D = Z = [True]
s = t = k = p = w = h = r = a = o = dash = star = e = u = f = b = l = g = d = z = [False]
LHS = S + T + K + P + W + H + R
lhs = s + t + k + p + w + h + r
AO = A + O
ao = a + o
EU = E + U
eu = e + u
RHS = F + R + P + B + L + G + T + S + D + Z
rhs = f + r + p + b + l + g + t + s + d + z


class Test_parseStroke (unittest.TestCase):

    def test_starOnly (self):
        self.assertEqual(parseStroke("*"), lhs + ao + dash + STAR + eu + rhs)

    def test_leftHandKeys (self):
        self.assertEqual(parseStroke("SKPR"), S + t + K + P + w + h + R + ao + dash + star + eu + rhs)

    def test_vowels (self):
        self.assertEqual(parseStroke("AEU"), lhs + A + o + dash + star + EU + rhs)

    def test_rightHandKeys (self):
        self.assertEqual(parseStroke("-RPLGS"), lhs + ao + DASH + star + eu + f + R + P + b + L + G + t + S + d + z)

    def test_leftHandAndVowels (self):
        self.assertEqual(parseStroke("TPWROU"), s + T + k + P + W + h + R + a + O + dash + star + e + U + rhs)

    def test_rightHandAndVowels (self):
        self.assertEqual(parseStroke("EFGTS"), lhs + ao + star + dash + E + u + F + r + p + b + l + G + T + S + d + z)

    def test_wholeKeyboard (self):
        self.assertEqual(parseStroke("KPRO*ERPGTSZ"), s + t + K + P + w + h + R + a + O + dash + STAR + E + u + f + R + P + b + l + G + T + S + d + Z)


class Test_mergeStrokes (unittest.TestCase):

    def test_leftHandMerges (self):
        a = "STPR"
        b = "THR"
        result = mergeStrokes(a, b)
        expected = parseStroke("STPHR")
        self.assertEqual(result, expected)

    def test_rightHandMerges (self):
        a = "-FBGT"
        b = "-FRPDZ"
        result = mergeStrokes(a, b)
        expected = parseStroke("-FRPBGTDZ")
        self.assertEqual(result, expected)

    def test_vowels (self):
        a = "AE"
        b = "AOE"
        result = mergeStrokes(a, b)
        expected = parseStroke("AOE")
        self.assertEqual(result, expected)

    def test_starAndDash (self):
        """
        Star and dash can live together in a stroke.
        It's only when the stroke is rendered that star overwrites dash.
        """
        a = "STR-PLS"
        b = "STA*ET"
        result = mergeStrokes(a, b)
        expected = parseStroke("STRA-*EPLTS")
        self.assertEqual(result, expected)

    def test_skeletons (self):
        a = "STR-L"
        b = "KR-FLS"
        result = mergeStrokes(a, b)
        expected = parseStroke("STKR-FLS")
        self.assertEqual(result, expected)


class Test_renderStroke (unittest.TestCase):

    def test_starOnly (self):
        result = renderStroke(parseStroke("*"))
        self.assertEqual(result, "*")

    def test_lhs (self):
        stroke = "STKR"
        result = renderStroke(parseStroke(stroke))
        self.assertEqual(result, stroke)

    def test_rhs (self):
        stroke = "-RPLTS"
        result = renderStroke(parseStroke(stroke))
        self.assertEqual(result, stroke)

    def test_vowels (self):
        stroke = "OEU"
        result = renderStroke(parseStroke(stroke))
        self.assertEqual(result, stroke)

    def test_bigChord (self):
        stroke = "KPROERPLGTDZ"
        result = renderStroke(parseStroke(stroke))
        self.assertEqual(result, stroke)

    def test_everythingStroke (self):
        stroke = "STKPWHRAO*EUFRPBLGTSDZ"
        result = renderStroke(parseStroke(stroke))
        self.assertEqual(result, stroke)

    def test_skeletonStroke (self):
        stroke = "STR-RPLS"
        result = renderStroke(parseStroke(stroke))
        self.assertEqual(result, stroke)


testEmptyAlphabetData = {
    "minStroke": "",
    "majStroke": "",
    "letters": [],
}

testAlphabetData = {
    "minStroke": "-DZ",
    "majStroke": "*DZ",
    "letters": [
        {
            "majuscule": "💤",
            "minuscule": "🦓",
            "strokes": ["STKPW", "STK"],
        },
        {
            "majuscule": "👴",
            "minuscule": "👶",
            "strokes": ["O"],
        },
    ]
}

class Test_buildAlphabet (unittest.TestCase):

    def test_handlesEmptyAlphabetData (self):
        self.assertEqual(buildAlphabet(testEmptyAlphabetData), {})

    def test_buildingAlphabet (self):
        result = buildAlphabet(testAlphabetData)
        expected = {
            "🦓": ["STKPW-DZ", "STK-DZ"],
            "💤": ["STKPW*DZ", "STK*DZ"],
            "👶": ["ODZ"],
            "👴": ["O*DZ"],
        }
        self.assertEqual(result, expected)


class Test_buildModCharOutlines (unittest.TestCase):

    def test_worksForAToAAcute (self):
        result = buildModCharOutlines(latinAlphabet, ("a", "á"), ["-RP"])
        expected = ("á", [["A*", "-RP"]])
        self.assertEqual(result, expected)

    def test_zeToImaginaryLigature (self):
        result = buildModCharOutlines(latinAlphabet, ("ze", "🦓"), ["-FRLG"])
        expected = ("🦓", [["STKPW*", "*E", "-FRLG"], ["STK*", "*E", "-FRLG"]])
        self.assertEqual(result, expected)


modifier_aWithAcute = {
    "minuscule": ("a", "á"),
    "majuscule": ("A", "Á"),
    "modifiers": ["acute"],
}

modifier_aeLigature = {
    "minuscule": ("ae", "æ"),
    "majuscule": ("AE", "Æ"),
    "modifiers": ["ligature"],
}

modifier_aeLigatureWithAcute = {
    "minuscule": ("ae", "ǽ"),
    "majuscule": ("AE", "Ǽ"),
    "modifiers": ["ligature", "acute"],
}


class Test_createOutlines (unittest.TestCase):

    def test_aWithAcute (self):
        result = createOutlines(latinAlphabet, modifier_aWithAcute)
        expected = (("á", [["A*", "-RP"]]), ("Á", [["A*P", "-RP"]]))
        self.assertEqual(result, expected)

    def test_aeLigature (self):
        result = createOutlines(latinAlphabet, modifier_aeLigature)
        expected = (("æ", [["A*", "*E", "-FRLG"]]), ("Æ", [["A*P", "*EP", "-FRLG"]]))
        self.assertEqual(result, expected)

    def test_aeLigatureWithAcute (self):
        result = createOutlines(latinAlphabet, modifier_aeLigatureWithAcute)
        expected = (("ǽ", [["A*", "*E", "-FRLG", "-RP"]]), ("Ǽ", [["A*P", "*EP", "-FRLG", "-RP"]]))
        self.assertEqual(result, expected)


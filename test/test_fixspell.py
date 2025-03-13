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


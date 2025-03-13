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

from toBinaryOne import toSingleBinaryByte
import unittest
from encryption import seeder, enCrypt

class TestBinary(unittest.TestCase):
    def test_tobinary(self):
        result = toSingleBinaryByte("andrew stinks12345784654606478917309271-4327041-2356216!@#$%&*()+^_")
        self.assertEqual(result, 21889554)
    def test_seedGen(self):
        testSeeder = seeder() 
        self.assertIsInstance(testSeeder.genSeed("andrew"), float)
    def test_cipherGen(self):
        Testdict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25,'A': 26, 'B': 27, 'C': 28, 'D': 29, 'E': 30, 'F': 31, 'G': 32,'H': 33, 'I': 34, 'J': 35, 'K': 36, 'L': 37, 'M': 38, 'N': 39,'O': 40, 'P': 41, 'Q': 42, 'R': 43, 'S': 44, 'T': 45, 'U': 46,'V': 47, 'W': 48, 'X': 49, 'Y': 50, 'Z': 51}
        testenCrypt = enCrypt()
        cipher = testenCrypt.genCipher("NO")
        self.assertIsInstance(cipher, dict)
        self.assertEqual(cipher.keys(), Testdict.keys())
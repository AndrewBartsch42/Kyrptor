from toBinaryOne import toSingleBinaryByte
import unittest
from encryption import kryptor

class TestBinary(unittest.TestCase):
    def test_tobinary(self):
        result = toSingleBinaryByte("andrew stinks12345784654606478917309271-4327041-2356216!@#$%&*()+^_")
        self.assertEqual(result, 21889554)
    def test_seedGen(self):
        testKryptor = kryptor
        testSeedValue = 0.01745240643 
        self.assertEqual(testKryptor.seedMath(1), testSeedValue)
import random
from toBinaryOne import toSingleBinaryByte
import math


class seeder():
    def __init__(self):
        pass
    def seedMath(self, input):
        random.seed(input)
        delta = random.randint(1, 10)
        return float((math.sqrt(42*math.pow(math.pi, math.e)*input))/math.sqrt(math.e))/delta

    def genSeed(self, message):
        seed = toSingleBinaryByte(message)
        return(self.seedMath(seed) * math.pow(10,len(message)))


class enCrypt():
    def __init__(self):
        self.alphabet = [  'a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
        self.cipher = {}
        self.encryptedMessage = []
    def genCipher(self, message):
        random.seed(seeder.genSeed(self, message))
        for i in self.alphabet:
            self.cipher[i] = random.randint(1, len(self.alphabet))
        return self.cipher


testDict = {"a": 1}
testDict2 = {"a": 2}

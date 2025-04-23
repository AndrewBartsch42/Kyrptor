import random
from toBinaryOne import toSingleBinaryByte
import math


class seeder():
    def __init__(self):
        pass
    def seedMath(self, input):
        random.seed(input)
        delta = random.randint(1, 10)
        return float((math.sqrt(42*math.pow(math.pi, math.e)*input))/math.sqrt(math.e))/delta #use this function to generate a large number

    def genSeed(self, message):
        seed = toSingleBinaryByte(message)
        return(self.seedMath(seed) * math.pow(10,len(message)))


class enCrypt():
    def __init__(self):
        self.alphabet = [    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ':', ';', '<', '=', '>', '?', '@', '_', '^', ]
        self.cipher = {}
        self.encryptedMessage = []
        self.seed = 0
        self.delim = ""
    def genCipher(self, message):
        seedGen = seeder() # add a seeder object for seeding of the random function
        self.seed = seedGen.genSeed(message) # store the seed for later output
        random.seed(self.seed) # seed the random function
        for i in self.alphabet: # for each character in the alphabet array
            characterLength = random.randint(3, 7) #generate the random character length 
            characterValue = ""
            while characterLength > 0: #generate the character 
                characterValue = characterValue + self.alphabet[random.randint(0, len(self.alphabet)-1)]
                characterLength -= 1
            self.cipher[i] = characterValue # add the character to the dictionary 
        self.delim += self.alphabet[random.randint(0,len(self.alphabet)-1)]  
        return self.cipher # return the cipher
    def encryptMessage(self, message): # encrypts the message
        encryptedMessage = ""
        for i in message:
            encryptedMessage += self.cipher[i]
        return encryptedMessage
    
    def getSeed(self):
        return self.seed
    
    def getDelim(self):
        return self.delim

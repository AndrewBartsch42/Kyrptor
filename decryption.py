import random

class deCrypt():
    def __init__(self, key):
        self.alphabet = [    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ':', ';', '<', '=', '>', '?', '@', '_']
        self.cipher = {}
        self.delimCharacters = ['^', '}', '{']
        self.key = key
    def genCipher(self):
        random.seed(self.key)
        for i in self.alphabet: # for each character in the alphabet array
            characterLength = random.randint(3, 7) #generate the random character length 
            characterValue = ""
            while characterLength > 0: #generate the character 
                characterValue = characterValue + self.alphabet[random.randint(0, len(self.alphabet)-1)]
                characterLength -= 1
            self.cipher[i] = characterValue # add the character to the dictionary 
        return self.cipher # return the cipher
    def getKey(self):
        return self.key
    def deCrypt(self, encryptedMessage):
        self.genCipher()
        invertCipher = {v: k for k, v in self.cipher.items()} #https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping
        decryptedMessage = "" #stores the decrypted message in progress
        charBuffer = ""

        for i in encryptedMessage:
            if i == self.delimCharacters[0] or i == self.delimCharacters[1] or i == self.delimCharacters[2]: #stops the adding to the charBuffer and tries to find the buffer value in the inverted cipher
                decryptedMessage += invertCipher[charBuffer] # adds the value of the key which is the charbuffer value from the inverted cipher
                charBuffer = "" # clears the charbuffer for next character
            else:
                charBuffer += i # adds the single char to the charbuffer until the delim character is hit
        return decryptedMessage # returns the decrypted message
    

    
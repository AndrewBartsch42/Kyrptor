class HTMLstorage():
    def __init__(self):
        self.msg = ""
        self.seed = None
        self.encryptedMSG = ""
    def setmsg(self, msg):
        self.msg = msg
    def setseed(self, seed):
        self.seed = seed
    def setencryptedMSG(self, msg):
        self.encryptedMSG = msg
    def clear(self):
        self.msg = ""
        self.seed = None
        self.encryptedMSG = ""


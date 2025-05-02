from flask import Flask, render_template, request #https://www.youtube.com/watch?v=RuSH-DEmwEg flask tutorial
from encryption import enCrypt
from decryption import deCrypt
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        link = request.form.get('link')
        if link == "encrypt":
            return encryption()
        elif link == "decrypt":
            return decryption()
    return render_template('index.html')
def encryption():
    encryptor = enCrypt()
    if request.method == "POST":
        msg = str(request.form.get("MSG"))
        encryptedMSG = encryptor.encryptMessage(msg)
    return render_template('encrypt.html', text=encryptedMSG, key=encryptor.getSeed())
def decryption():
    if request.method == "POST":
        encryptedMsg = str(request.form.get("encryptedMSG"))
        seed = request.form.get("key", float)
        decryptor = deCrypt(seed)
        msg = decryptor.deCrypt(encryptedMsg)
    return render_template('decrypt.html')
if __name__ == '__main__':
    app.run(debug=True)
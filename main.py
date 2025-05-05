from flask import Flask, render_template, request, redirect, url_for#https://www.youtube.com/watch?v=RuSH-DEmwEg flask tutorial
from encryption import enCrypt
from decryption import deCrypt
from storage import HTMLstorage
app = Flask(__name__)

storage = HTMLstorage()

@app.route("/", methods=['POST', 'GET'])
def index():
    storage.clear()
    if request.method == "POST":
        link = request.form.get('link')
        if link == "encrypt":
            print("encryption request")
            return encrypt()
        elif link == "decrypt":
            print("decryption request")
            return decrypt()
        elif link == "output":
            return encryptedoutput()
    return render_template('index.html')
@app.route("/encrypt.html", methods=['POST', 'GET'])
def encrypt():
    encryptor = enCrypt()
    if request.method == "POST":
        print("grabbbing start variable")
        if 'encrypt' in request.form:
            startVal = request.form["encrypt"]
            if startVal == 'Start':
                msg = str(request.form.get("MSG"))
                encryptedMSG = encryptor.encryptMessage(msg)
                storage.setencryptedMSG(encryptedMSG)
                storage.setseed(encryptor.getSeed())
                print(encryptor.getSeed())
                return encryptedoutput()
    return render_template('encrypt.html')
@app.route("/decrypt.html", methods=["POST", "GET"])
def decrypt():
    if request.method == "POST":
        if 'decrypt' in request.form:
            startVal = request.form["decrypt"]
            if startVal == "start":
                encryptedMsg = str(request.form.get("encryptedMSG"))
                seed = request.form.get("key", type=float)
                decryptor = deCrypt(seed)
                msg = decryptor.deCrypt(encryptedMsg)
                storage.setmsg(msg)
                print("going to decrypted output")
                return decryptedoutput()
    return render_template("decrypt.html")
@app.route("/output.html", methods=['POST', 'GET'])
def decryptedoutput():
    if request.method == "POST":
        if "Home" in request.form:
            home = request.form["Home"]
            if home == "Back":
                return redirect(url_for('/'))
    return render_template("output.html", text=storage.msg)
def encryptedoutput():
    if request.method == "POST":
        if "Home" in request.form:
            home = request.form["Home"]
            if home == "Back":
                return redirect(url_for('/'))
    return render_template("output.html", key=storage.seed, text=storage.encryptedMSG)
if __name__ == '__main__':
    app.run(debug=True)
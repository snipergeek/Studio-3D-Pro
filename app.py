from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/devis", methods=["POST"])
def devis():
    nom = request.form["nom"]
    email = request.form["email"]
    details = request.form["details"]
    print(f"Nouvelle demande de devis : {nom} - {email} - {details}")
    return f"Merci {nom}, votre demande de devis a été envoyée !"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1408525023660212374/hthxrBdNCDontFV-N4umcXP8mdXORIaXA7TrsDXQwvZqYovMY4fI1l0tyo_e4V9ENQ2o"

avis_list = []

@app.route("/", methods=["GET", "POST"])
def home():
    global avis_list

    if request.method == "POST":
        type_form = request.form.get("type")

        # Avis
        if type_form == "avis":
            nom = request.form["nom"]
            note = request.form["note"]
            commentaire = request.form["commentaire"]
            avis_list.append({"nom": nom, "note": note, "commentaire": commentaire})
            return '', 204

        # Contact
        elif type_form == "contact":
            nom = request.form["nom"]
            email = request.form["email"]
            message = request.form["message"]
            data = {"content": f"**Contact**\nNom: {nom}\nEmail: {email}\nMessage: {message}"}
            requests.post(DISCORD_WEBHOOK_URL, json=data)
            return '', 204

        # Devis
        elif type_form == "devis":
            produit = request.form["produit"]
            nom = request.form["nom"]
            email = request.form["email"]
            message = request.form.get("message", "")
            data = {"content": f"**Demande de devis**\nProduit: {produit}\nNom: {nom}\nEmail: {email}\nMessage: {message}"}
            requests.post(DISCORD_WEBHOOK_URL, json=data)
            return '', 204

    return render_template("index.html", avis_list=avis_list)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template_string, request, send_from_directory

app = Flask(__name__)

# Route pour le CSS dans le même dossier
@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

# Page principale
@app.route("/")
def home():
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return render_template_string(html_content)

# Formulaire devis
@app.route("/devis", methods=["POST"])
def devis():
    nom = request.form["nom"]
    email = request.form["email"]
    details = request.form["details"]
    print(f"Nouvelle demande de devis : {nom} - {email} - {details}")
    return f"Merci {nom}, votre demande de devis a été envoyée !"

if __name__ == "__main__":
    app.run(debug=True)

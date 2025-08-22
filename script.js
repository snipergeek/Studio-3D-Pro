// Défilement fluide
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({ behavior: "smooth" });
    });
});

// Fonction pour AJAX
function ajaxForm(selector, msgSelector) {
    document.querySelector(selector).addEventListener("submit", function(e) {
        e.preventDefault();
        let form = e.target;
        let formData = new FormData(form);

        fetch("/", { method: "POST", body: formData })
        .then(res => {
            form.reset();
            if(msgSelector) document.querySelector(msgSelector).textContent = "✅ Envoyé !";
        })
        .catch(err => {
            if(msgSelector) document.querySelector(msgSelector).textContent = "❌ Erreur";
        });
    });
}

// Formulaires Contact
ajaxForm(".contact-form", ".contact-msg");

// Formulaires Avis
ajaxForm(".avis-form", ".avis-msg");

// Formulaires Devis
document.querySelectorAll(".devis-form").forEach((form, i) => {
    form.addEventListener("submit", function(e){
        e.preventDefault();
        let formData = new FormData(form);
        formData.append("type", "devis");
        fetch("/", { method: "POST", body: formData })
        .then(res => { form.reset(); form.nextElementSibling.textContent = "✅ Demande envoyée !"; })
        .catch(err => { form.nextElementSibling.textContent = "❌ Erreur"; });
    });
});

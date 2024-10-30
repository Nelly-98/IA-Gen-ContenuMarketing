import streamlit as st
import openai
import json
import os
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()
# Récupérer la clé API OpenAI depuis les variables d'environnement
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("La clé API OpenAI est manquante. Veuillez la configurer dans les secrets ou les variables d'environnement.")
else:
    # Code qui utilise la clé API OpenAI
    st.write("Clé API chargée avec succès (mais pas affichée pour des raisons de sécurité).")



# Lire le fichier CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Charger le fichier styles.css
load_css("styles/style.css")



# Initialisation de l'historique
if "history" not in st.session_state:
    st.session_state["history"] = []

# Titre de l'application
st.title("Générateur de Contenu Marketing Automatisé")

# Ajouter une sélection de langue
language = st.selectbox("Choisissez la langue :", ["Français", "Anglais", "Espagnol", "Allemand"])

# Prompt de l'utilisateur
prompt = st.text_area("Entrez votre idée de contenu ou mot-clé :")

# Sélection du ton
tone = st.selectbox("Choisissez le ton du contenu :", ["Formel", "Décontracté", "Technique", "Persuasif"])

# Sélection du type de contenu
content_type = st.selectbox("Type de contenu :", ["Article", "Post sur les réseaux sociaux", "Email"])

# Longueur du contenu
length = st.slider("Choisissez la longueur du contenu (en mots) :", min_value=50, max_value=500, step=50)

# Bouton pour générer le contenu
if st.button("Générer le contenu"):
    if prompt:
        # Adapter le prompt en fonction de la langue choisie
        if language == "Français":
            lang_prefix = "Écrire en français :"
        elif language == "Anglais":
            lang_prefix = "Write in English:"
        elif language == "Espagnol":
            lang_prefix = "Escribir en español :"
        elif language == "Allemand":
            lang_prefix = "Schreiben auf Deutsch :"
        
        # Construire le prompt final pour l'API OpenAI
        final_prompt = f"{lang_prefix} {tone} : {prompt}. Type : {content_type}. Longueur : {length} mots."

        # Appeler l'API OpenAI pour générer le texte
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=final_prompt,
            max_tokens=length,
            temperature=0.7,
        )
        # Extraire le texte généré
        generated_text = response.choices[0].text.strip()

        # Ajouter le contenu généré à l'historique
        st.session_state["history"].append({
            "prompt": prompt,
            "generated_text": generated_text,
            "language": language,
            "tone": tone,
            "content_type": content_type,
            "length": length
        })

        # Afficher le résultat généré
        st.write("### Contenu généré :")
        st.write(generated_text)
    else:
        st.warning("Veuillez entrer une idée de contenu.")

# Fonction pour télécharger l'historique
def download_history():
    json_data = json.dumps(st.session_state["history"], indent=4)
    st.download_button(
        label="Télécharger l'historique",
        data=json_data,
        file_name="historique_contenus.json",
        mime="application/json"
    )

# Afficher l'historique dans la sidebar avec des options de filtrage
st.sidebar.title("Historique des contenus générés")
if st.session_state["history"]:
    # Options de filtrage
    filter_language = st.sidebar.selectbox("Filtrer par langue :", ["Toutes"] + list({entry["language"] for entry in st.session_state["history"]}))
    filter_tone = st.sidebar.selectbox("Filtrer par ton :", ["Tous"] + list({entry["tone"] for entry in st.session_state["history"]}))
    filter_content_type = st.sidebar.selectbox("Filtrer par type de contenu :", ["Tous"] + list({entry["content_type"] for entry in st.session_state["history"]}))
    
    # Appliquer les filtres
    filtered_history = [
        entry for entry in st.session_state["history"]
        if (filter_language == "Toutes" or entry["language"] == filter_language) and
           (filter_tone == "Tous" or entry["tone"] == filter_tone) and
           (filter_content_type == "Tous" or entry["content_type"] == filter_content_type)
    ]
    
    for i, entry in enumerate(filtered_history):
        with st.sidebar.expander(f"Contenu {i+1} ({entry['language']})"):
            st.write(f"**Prompt :** {entry['prompt']}")
            st.write(f"**Ton :** {entry['tone']}")
            st.write(f"**Type :** {entry['content_type']}")
            st.write(f"**Longueur :** {entry['length']} mots")
            st.write(f"**Contenu généré :** {entry['generated_text']}")

    # Ajouter un bouton pour effacer l'historique
    if st.sidebar.button("Effacer l'historique"):
        st.session_state["history"].clear()
        st.sidebar.success("Historique effacé avec succès.")
    
    # Ajouter l'option de téléchargement
    download_history()
else:
    st.sidebar.write("Aucun historique disponible.")

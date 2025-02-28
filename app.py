import json
import streamlit as st

# -----------------------------
# FONCTIONS DE CHARGEMENT / SAUVEGARDE
# -----------------------------
def load_qcm(file_path: str):
    """
    Lit un fichier JSON et retourne son contenu sous forme de liste (ou dict).
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_qcm(file_path: str, qcm_data):
    """
    Écrit le contenu qcm_data dans un fichier JSON.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(qcm_data, file, indent=4, ensure_ascii=False)


# -----------------------------
# CHARGEMENT DES 6 QCM
# -----------------------------
# Mettez ici les chemins de vos fichiers JSON.
qcm_file_2021 = "qcm_2021.json"
qcm_file_2022 = "qcm_2022.json"
qcm_file_2023 = "qcm_2023.json"
qcm_file_2024 = "qcm_2024.json"
qcm_file_supp1 = "qcm_100_questions.json"
qcm_file_supp2 = "qcm_2_GPT_100.json"

# On charge chaque fichier en mémoire
qcm_2021_data = load_qcm(qcm_file_2021)
qcm_2022_data = load_qcm(qcm_file_2022)
qcm_2023_data = load_qcm(qcm_file_2023)
qcm_2024_data = load_qcm(qcm_file_2024)
qcm_supp1_data = load_qcm(qcm_file_supp1)
qcm_supp2_data = load_qcm(qcm_file_supp2)

# On crée un dictionnaire pour faire le lien entre
# le nom du QCM dans la sidebar et son contenu
qcm_collection = {
    "QCM 2021": qcm_2021_data,
    "QCM 2022": qcm_2022_data,
    "QCM 2023": qcm_2023_data,
    "QCM 2024": qcm_2024_data,
    "QCM Supplémentaire 1": qcm_supp1_data,
    "QCM Supplémentaire 2": qcm_supp2_data
}

# De la même façon, on crée un mapping entre le nom du QCM
# et le chemin du fichier correspondant pour pouvoir
# sauvegarder après correction
qcm_file_mapping = {
    "QCM 2021": qcm_file_2021,
    "QCM 2022": qcm_file_2022,
    "QCM 2023": qcm_file_2023,
    "QCM 2024": qcm_file_2024,
    "QCM Supplémentaire 1": qcm_file_supp1,
    "QCM Supplémentaire 2": qcm_file_supp2
}

# -----------------------------
# INTERFACE STREAMLIT
# -----------------------------
st.title("QCM d'évaluation")

# Sélection du QCM
selected_qcm = st.sidebar.selectbox(
    "Choisissez le QCM :",
    list(qcm_collection.keys())
)

# Récupération de la liste de questions correspondant au QCM choisi
questions = qcm_collection[selected_qcm]

st.header(f"{selected_qcm}")

# Initialisation du score et du résumé des erreurs
score = 0
wrong_summary = []

# On parcourt toutes les questions du QCM
for idx, q in enumerate(questions):
    # Affichage de la question
    st.markdown(f"**{q['question']}**")

    # Pour forcer l'utilisateur à sélectionner un choix
    placeholder_text = "Faites un choix"
    all_options = [placeholder_text] + list(q["options"].keys())

    # Affichage du radio button
    answer = st.radio(
        "Votre réponse :",
        all_options,
        index=0,
        key=f"q{idx}_{selected_qcm}"  # on ajoute le QCM dans la clé pour éviter les collisions
    )

    # Affichage du détail des propositions
    st.markdown("\n".join([f"- **{k}** : {v}" for k, v in q["options"].items()]))

    # Vérification de la réponse
    if answer == placeholder_text:
        st.warning("Veuillez sélectionner une option.")
    else:
        if answer == q["correct"]:
            st.success(f"Correct ! Votre réponse : {answer} - {q['options'][answer]}")
            score += 1
        else:
            st.error(
                f"Faux. Votre réponse : {answer} - {q['options'][answer]}. "
                f"La bonne réponse est : {q['correct']} - {q['options'][q['correct']]}"
            )
            # On stocke l'erreur pour l'affichage final
            wrong_summary.append({
                "index": idx,
                "question": q["question"],
                "your_answer": answer,
                "your_answer_text": q["options"].get(answer, "Réponse invalide"),
                "correct": q["correct"],
                "correct_text": q["options"][q["correct"]]
            })

            # Bouton de correction
            if st.button("Corriger la réponse", key=f"correct_btn_{idx}_{selected_qcm}"):
                new_correct = st.selectbox(
                    "Sélectionnez la bonne réponse :",
                    list(q["options"].keys()),
                    key=f"new_correct_{idx}_{selected_qcm}"
                )
                if st.button("Enregistrer la correction", key=f"save_correct_{idx}_{selected_qcm}"):
                    # On met à jour la bonne réponse
                    q["correct"] = new_correct
                    # Sauvegarde du QCM dans le fichier correspondant
                    save_qcm(qcm_file_mapping[selected_qcm], questions)
                    st.success("Correction enregistrée avec succès !")

    st.write("---")

# -----------------------------
# AFFICHAGE DU SCORE FINAL
# -----------------------------
total_questions = len(questions)
if total_questions > 0:
    percentage = (score / total_questions) * 100
    score_out_of_20 = (percentage * 20) / 100
else:
    percentage = 0
    score_out_of_20 = 0

st.subheader(f"Score final : {score} / {total_questions}")
st.subheader(f"Note en pourcentage : {percentage:.2f} %")
st.subheader(f"Note sur 20 : {score_out_of_20:.2f} / 20")

# -----------------------------
# RÉCAPITULATIF DES QUESTIONS INCORRECTES
# -----------------------------
if wrong_summary:
    st.header("Récapitulatif des questions incorrectes")
    for item in wrong_summary:
        st.markdown(f"**{item['question']}**")
        st.write(f"Votre réponse : {item['your_answer']} - {item['your_answer_text']}")
        st.write(f"Bonne réponse : {item['correct']} - {item['correct_text']}")
        st.write("---")

# -----------------------------
# TÉLÉCHARGEMENT DU FICHIER JSON MIS À JOUR
# -----------------------------
# On propose le téléchargement du QCM sélectionné (celui qui est affiché).
# Les corrections sont déjà prises en compte dans la liste 'questions'.
updated_json = json.dumps(questions, indent=4, ensure_ascii=False)
file_name = f"{selected_qcm.replace(' ', '_').lower()}_updated.json"

st.download_button(
    label="Télécharger le QCM mis à jour",
    data=updated_json,
    file_name=file_name,
    mime="application/json"
)

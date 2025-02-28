import json
import os
import streamlit as st

# -----------------------------------------------------------------
# FONCTIONS DE CHARGEMENT / SAUVEGARDE
# -----------------------------------------------------------------
def load_qcm(file_path):
    """
    Lit un fichier JSON et retourne son contenu sous forme de liste de questions.
    Gère les erreurs de fichier manquant ou JSON invalide.
    """
    if not os.path.exists(file_path):
        st.warning(f"Fichier introuvable : {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        st.error(f"Erreur JSON dans {file_path} : {e}")
        return []

    # Vérifie que data est bien une liste
    if not isinstance(data, list):
        st.error(f"Le fichier {file_path} ne contient pas un tableau JSON.")
        return []

    # Contrôle minimal : chaque question doit avoir "question", "options", "correct"
    cleaned_data = []
    for idx, item in enumerate(data):
        if (
            isinstance(item, dict)
            and "question" in item
            and "options" in item
            and "correct" in item
            and isinstance(item["options"], dict)
        ):
            cleaned_data.append(item)
        else:
            st.warning(f"Élément n°{idx} ignoré (format invalide) dans {file_path}.")

    return cleaned_data


def save_qcm(file_path, qcm_data):
    """
    Sauvegarde le QCM (liste de questions) dans un fichier JSON, en UTF-8.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(qcm_data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        st.error(f"Impossible d'enregistrer le fichier {file_path} : {e}")


# -----------------------------------------------------------------
# CHEMINS VERS LES FICHIERS QCM
# -----------------------------------------------------------------
qcm_file_2021 = "qcm_2021.json"
qcm_file_2022 = "qcm_2022.json"
qcm_file_2023 = "qcm_2023.json"
qcm_file_2024 = "qcm_2024.json"
qcm_file_supp1 = "qcm_100_questions.json"
qcm_file_supp2 = "qcm_2_GPT_100.json"

# -----------------------------------------------------------------
# CHARGEMENT DES 6 QCM
# -----------------------------------------------------------------
qcm_2021_data = load_qcm(qcm_file_2021)
qcm_2022_data = load_qcm(qcm_file_2022)
qcm_2023_data = load_qcm(qcm_file_2023)
qcm_2024_data = load_qcm(qcm_file_2024)
qcm_supp1_data = load_qcm(qcm_file_supp1)
qcm_supp2_data = load_qcm(qcm_file_supp2)

qcm_collection = {
    "QCM 2021": qcm_2021_data,
    "QCM 2022": qcm_2022_data,
    "QCM 2023": qcm_2023_data,
    "QCM 2024": qcm_2024_data,
    "QCM Supplémentaire 1": qcm_supp1_data,
    "QCM Supplémentaire 2": qcm_supp2_data
}

qcm_file_mapping = {
    "QCM 2021": qcm_file_2021,
    "QCM 2022": qcm_file_2022,
    "QCM 2023": qcm_file_2023,
    "QCM 2024": qcm_file_2024,
    "QCM Supplémentaire 1": qcm_file_supp1,
    "QCM Supplémentaire 2": qcm_file_supp2
}

# -----------------------------------------------------------------
# INTERFACE STREAMLIT
# -----------------------------------------------------------------
st.title("QCM d'évaluation")

# Sélection du QCM
selected_qcm = st.sidebar.selectbox(
    "Choisissez le QCM :",
    list(qcm_collection.keys())
)

# Récupération des questions
questions = qcm_collection[selected_qcm]
st.header(f"{selected_qcm}")

# Si le QCM est vide (ou introuvable), on arrête là
if not questions:
    st.warning(f"Aucune question à afficher pour {selected_qcm}.")
    st.stop()

# Initialisation du score et du résumé des erreurs
score = 0
wrong_summary = []

# Pour stocker les réponses de l'utilisateur, on utilise la session State
# La clé "user_answers_{selected_qcm}" contiendra un dict question_index -> réponse
state_key = f"user_answers_{selected_qcm}"
if state_key not in st.session_state:
    st.session_state[state_key] = {}

# -----------------------------------------------------------------
# AFFICHAGE DE CHAQUE QUESTION + CORRECTION
# -----------------------------------------------------------------
for idx, q in enumerate(questions):
    # Titre de la question
    st.markdown(f"**{q['question']}**")

    # Liste des choix
    placeholder_text = "Faites un choix"
    all_options = [placeholder_text] + list(q["options"].keys())

    # Récupération de la réponse en session_state (si déjà choisie)
    current_answer = st.session_state[state_key].get(idx, placeholder_text)

    # Radio pour choisir la réponse
    chosen_answer = st.radio(
        label="Votre réponse :",
        options=all_options,
        index=all_options.index(current_answer) if current_answer in all_options else 0,
        key=f"radio_{selected_qcm}_{idx}"
    )

    # Mémorise la réponse choisie dans la session
    st.session_state[state_key][idx] = chosen_answer

    # Affiche toutes les options en clair
    for letter, desc in q["options"].items():
        st.markdown(f"- **{letter}** : {desc}")

    # Si l'utilisateur a choisi une option
    if chosen_answer != placeholder_text:
        if chosen_answer == q["correct"]:
            st.success(f"Correct ! Votre réponse : {chosen_answer} - {q['options'][chosen_answer]}")
            score += 1
        else:
            st.error(
                f"Faux. Votre réponse : {chosen_answer} - {q['options'][chosen_answer]}. "
                f"La bonne réponse officielle est : {q['correct']} - {q['options'][q['correct']]}"
            )
            wrong_summary.append({
                "index": idx,
                "question": q["question"],
                "your_answer": chosen_answer,
                "your_answer_text": q["options"][chosen_answer],
                "correct": q["correct"],
                "correct_text": q["options"][q["correct"]]
            })

        # -----------------------------------------------------------------
        # BOUTON POUR CORRIGER LA "BONNE RÉPONSE" DANS LE JSON
        # -----------------------------------------------------------------
        # Si on estime que la "bonne réponse" officielle est fausse
        # on permet à l'utilisateur de la modifier.
        with st.expander("Corriger la bonne réponse officielle"):
            st.write("Sélectionnez la nouvelle réponse correcte ci-dessous :")
            new_correct = st.selectbox(
                "Nouvelle bonne réponse :",
                list(q["options"].keys()),
                key=f"new_correct_{selected_qcm}_{idx}"
            )
            if st.button("Enregistrer la correction", key=f"save_correct_{selected_qcm}_{idx}"):
                q["correct"] = new_correct
                save_qcm(qcm_file_mapping[selected_qcm], questions)
                st.success("Nouvelle réponse officielle enregistrée !")

    st.write("---")

# -----------------------------------------------------------------
# SCORE FINAL
# -----------------------------------------------------------------
total_questions = len(questions)
percentage = (score / total_questions) * 100 if total_questions else 0
score_out_of_20 = (percentage * 20) / 100

st.subheader(f"Score final : {score} / {total_questions}")
st.subheader(f"Note en pourcentage : {percentage:.2f} %")
st.subheader(f"Note sur 20 : {score_out_of_20:.2f} / 20")

# -----------------------------------------------------------------
# RÉCAPITULATIF DES ERREURS
# -----------------------------------------------------------------
if wrong_summary:
    st.header("Récapitulatif des questions incorrectes")
    for item in wrong_summary:
        st.markdown(f"**{item['question']}**")
        st.write(f"Votre réponse : {item['your_answer']} - {item['your_answer_text']}")
        st.write(f"Bonne réponse : {item['correct']} - {item['correct_text']}")
        st.write("---")

# -----------------------------------------------------------------
# TÉLÉCHARGEMENT DU QCM ACTUEL
# -----------------------------------------------------------------
# On propose le téléchargement du JSON mis à jour (avec corrections)
updated_json = json.dumps(questions, indent=4, ensure_ascii=False)
file_name = f"{selected_qcm.replace(' ', '_').lower()}_updated.json"

st.download_button(
    label="Télécharger le QCM mis à jour",
    data=updated_json,
    file_name=file_name,
    mime="application/json"
)

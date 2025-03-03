import json
import os
import streamlit as st
import base64
import requests

# -----------------------------------------------------------------
# FONCTIONS DE CHARGEMENT / SAUVEGARDE
# -----------------------------------------------------------------
def load_qcm(file_path):
    if not os.path.exists(file_path):
        st.warning(f"Fichier introuvable : {file_path}")
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        st.error(f"Erreur JSON dans {file_path} : {e}")
        return []
    if not isinstance(data, list):
        st.error(f"Le fichier {file_path} ne contient pas un tableau JSON.")
        return []
    cleaned_data = []
    for idx, item in enumerate(data):
        if (isinstance(item, dict)
            and "question" in item
            and "options" in item
            and "correct" in item
            and isinstance(item["options"], dict)):
            cleaned_data.append(item)
        else:
            st.warning(f"Élément n°{idx} ignoré (format invalide) dans {file_path}.")
    return cleaned_data

def save_qcm(file_path, qcm_data):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(qcm_data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        st.error(f"Impossible d'enregistrer le fichier {file_path} : {e}")

# -----------------------------------------------------------------
# FONCTION POUR PUSH SUR GITHUB (MODIFICATION AJOUTÉE)
# -----------------------------------------------------------------
def push_to_github(updated_json, commit_message, github_owner, github_repo, github_file_path, branch="main"):
    """
    Pousse le fichier JSON mis à jour sur GitHub via l'API GitHub.
    La clé est récupérée via st.secrets.
    """
    # Récupération de la clé depuis les secrets de Streamlit
    github_token = st.secrets["GITHUB_TOKEN"]
    url = f"https://api.github.com/repos/{github_owner}/{github_repo}/contents/{github_file_path}"
    headers = {"Authorization": f"token {github_token}"}

    # Obtenir le SHA actuel du fichier (s'il existe)
    get_response = requests.get(url, headers=headers)
    if get_response.status_code == 200:
        file_info = get_response.json()
        sha = file_info["sha"]
    else:
        sha = None

    payload = {
        "message": commit_message,
        "content": base64.b64encode(updated_json.encode("utf-8")).decode("utf-8"),
        "branch": branch
    }
    if sha:
        payload["sha"] = sha

    response = requests.put(url, headers=headers, json=payload)
    return response

# -----------------------------------------------------------------
# CHEMINS VERS LES FICHIERS QCM
# -----------------------------------------------------------------
qcm_file_2021 = "qcm_2021.json"
qcm_file_2022 = "qcm_2022.json"
qcm_file_2023 = "qcm_2023.json"
qcm_file_2024 = "qcm_2024.json"

qcm_2021_data = load_qcm(qcm_file_2021)
qcm_2022_data = load_qcm(qcm_file_2022)
qcm_2023_data = load_qcm(qcm_file_2023)
qcm_2024_data = load_qcm(qcm_file_2024)

qcm_collection = {
    "QCM 2021": qcm_2021_data,
    "QCM 2022": qcm_2022_data,
    "QCM 2023": qcm_2023_data,
    "QCM 2024": qcm_2024_data,
}

qcm_file_mapping = {
    "QCM 2021": qcm_file_2021,
    "QCM 2022": qcm_file_2022,
    "QCM 2023": qcm_file_2023,
    "QCM 2024": qcm_file_2024,
}

# -----------------------------------------------------------------
# INTERFACE STREAMLIT
# -----------------------------------------------------------------
st.title("QCM d'évaluation")

selected_qcm = st.sidebar.selectbox("Choisissez le QCM :", list(qcm_collection.keys()))
questions = qcm_collection[selected_qcm]
st.header(f"{selected_qcm}")

if not questions:
    st.warning(f"Aucune question à afficher pour {selected_qcm}.")
    st.stop()

score = 0
wrong_summary = []

state_key = f"user_answers_{selected_qcm}"
if state_key not in st.session_state:
    st.session_state[state_key] = {}

for idx, q in enumerate(questions):
    st.markdown(f"**{q['question']}**")
    placeholder_text = "Faites un choix"
    all_options = [placeholder_text] + list(q["options"].keys())
    current_answer = st.session_state[state_key].get(idx, placeholder_text)
    chosen_answer = st.radio(
        label="Votre réponse :",
        options=all_options,
        index=all_options.index(current_answer) if current_answer in all_options else 0,
        key=f"radio_{selected_qcm}_{idx}"
    )
    st.session_state[state_key][idx] = chosen_answer

    for letter, desc in q["options"].items():
        st.markdown(f"- **{letter}** : {desc}")

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

        with st.expander("Corriger la bonne réponse officielle"):
            st.write("Sélectionnez la nouvelle réponse correcte ci-dessous :")
            new_correct = st.selectbox("Nouvelle bonne réponse :", list(q["options"].keys()), key=f"new_correct_{selected_qcm}_{idx}")
            if st.button("Enregistrer la correction", key=f"save_correct_{selected_qcm}_{idx}"):
                q["correct"] = new_correct
                save_qcm(qcm_file_mapping[selected_qcm], questions)
                st.success("Nouvelle réponse officielle enregistrée !")
    st.write("---")

total_questions = len(questions)
percentage = (score / total_questions) * 100 if total_questions else 0
score_out_of_20 = (percentage * 20) / 100

st.subheader(f"Score final : {score} / {total_questions}")
st.subheader(f"Note en pourcentage : {percentage:.2f} %")
st.subheader(f"Note sur 20 : {score_out_of_20:.2f} / 20")

if wrong_summary:
    st.header("Récapitulatif des questions incorrectes")
    for item in wrong_summary:
        st.markdown(f"**{item['question']}**")
        st.write(f"Votre réponse : {item['your_answer']} - {item['your_answer_text']}")
        st.write(f"Bonne réponse : {item['correct']} - {item['correct_text']}")
        st.write("---")

updated_json = json.dumps(questions, indent=4, ensure_ascii=False)
# Utilisation du nom de fichier original tel que défini dans qcm_file_mapping
file_name = qcm_file_mapping[selected_qcm]

# -----------------------------------------------------------------
# BOUTON POUR PUSH SUR GITHUB
# -----------------------------------------------------------------
if st.button("mettre à jour la correction (ne mettez pas de corrections fausses svp 🙏)"):
    github_owner = "sebastienHussons"
    github_repo = "qcm_CG"
    commit_message = "Mise à jour du QCM via Streamlit App"

    response = push_to_github(updated_json, commit_message, github_owner, github_repo, file_name)
    if response is not None and response.status_code in [200, 201]:
        st.success("Le fichier JSON a été mis à jour sur GitHub avec succès !")
    else:
        error_text = response.text if response is not None else "Aucune réponse"
        st.error(f"Erreur lors de la mise à jour sur GitHub : {error_text}")

# -----------------------------------------------------------------
# BOUTON DE TÉLÉCHARGEMENT DU QCM ACTUEL
# -----------------------------------------------------------------
st.download_button(
    label="Télécharger le JSON du QCM mis à jour",
    data=updated_json,
    file_name=file_name,
    mime="application/json"
)

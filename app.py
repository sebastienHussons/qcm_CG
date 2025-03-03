import json
import os
import streamlit as st
import base64
import requests

def push_to_github(updated_json, commit_message, github_owner, github_repo, github_file_path, branch="main"):
    """
    Met à jour le fichier sur GitHub en utilisant l'API GitHub.
    La clé est récupérée depuis les secrets de Streamlit.
    """
    # Récupère la clé stockée dans les secrets de Streamlit
    github_token = st.secrets["GITHUB_TOKEN"]
    
    url = f"https://api.github.com/repos/{github_owner}/{github_repo}/contents/{github_file_path}"
    headers = {"Authorization": f"token {github_token}"}

    # Récupérer le SHA du fichier existant (si présent)
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
# Exemple d'utilisation dans ton app Streamlit
# -----------------------------------------------------------------

# Paramètres GitHub à configurer (remplace par tes infos)
github_owner = "ton_nom_d_utilisateur"
github_repo = "ton_repertoire"
# Par exemple, pour sauvegarder dans le même fichier que celui généré par ton app
github_file_path = f"{selected_qcm.replace(' ', '_').lower()}_updated.json"
commit_message = "Mise à jour du QCM via Streamlit App"

if st.button("Pousser la correction sur GitHub"):
    response = push_to_github(updated_json, commit_message, github_owner, github_repo, github_file_path)
    if response is not None and response.status_code in [200, 201]:
        st.success("Le fichier JSON a été mis à jour sur GitHub avec succès !")
    else:
        error_text = response.text if response is not None else "Aucune réponse"
        st.error(f"Erreur lors de la mise à jour sur GitHub : {error_text}")

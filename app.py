# app.py
# ===========

import streamlit as st
from qcm2022 import questions  # On importe la liste "questions" depuis qcm2022.py

st.title("QCM d'évaluation - Session 2022")

# On utilise le session_state pour mémoriser si l'utilisateur a validé ses réponses
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Formulaire principal pour le QCM
with st.form("qcm_form"):
    st.write("Répondez aux questions ci-dessous. Une fois validé, vous ne pourrez plus modifier vos réponses.")
    
    # Dictionnaire pour stocker les réponses de l'utilisateur
    user_answers = {}
    
    for idx, q in enumerate(questions):
        st.markdown(f"**{q['question']}**")
        # Création d'un bouton radio pour chaque question (désactivé si déjà soumis)
        answer = st.radio(
            "Votre réponse :",
            options=list(q["options"].keys()),
            key=f"q{idx}",
            disabled=st.session_state.submitted
        )
        # Affiche le texte de chaque option
        st.markdown(", ".join([f"**{k}** : {v}" for k, v in q["options"].items()]))
        user_answers[idx] = answer
        st.write("---")
    
    # Bouton de validation
    submitted = st.form_submit_button("Valider mes réponses")
    if submitted:
        st.session_state.submitted = True

# Si le formulaire est validé, on affiche la correction et le score
if st.session_state.submitted:
    score = 0
    st.header("Correction et Résultats")
    
    for idx, q in enumerate(questions):
        user_ans = st.session_state.get(f"q{idx}")
        correct_ans = q["correct"]
        
        # Rappel de la question
        st.markdown(f"**{q['question']}**")
        
        # Affichage de la réponse de l'utilisateur
        if user_ans in q["options"]:
            st.write("Votre réponse :", user_ans, "-", q["options"][user_ans])
        else:
            st.write("Votre réponse : Non répondu")
        
        # Vérification
        if user_ans == correct_ans:
            st.success("Correct")
            score += 1
        else:
            st.error(f"Faux. La bonne réponse est : {correct_ans} - {q['options'][correct_ans]}")
        
        st.write("---")
    
    # Calcul du score
    total_questions = len(questions)
    percentage = (score / total_questions) * 100
    score_out_of_20 = (percentage * 20) / 100
    
    # Affichage des résultats
    st.subheader(f"Score final : {score} / {total_questions}")
    st.subheader(f"Note en pourcentage : {percentage:.2f} %")
    st.subheader(f"Note sur 20 : {score_out_of_20:.2f} / 20")

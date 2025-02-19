import streamlit as st

# Définition des QCM
# ------------------

# QCM 2022 (exemple complet avec quelques questions, complète avec tes 100 questions)
qcm2022 = [
    {
        "question": "1. Lors des jeux olympiques de 2024, les épreuves de surf devraient se dérouler à :",
        "options": {"A": "Lacanau", "B": "Tahiti", "C": "Hossegor", "D": "Biarritz"},
        "correct": "B"
    },
    {
        "question": "2. Dans quelle fiction rencontre-t-on des « marcheurs blancs » ?",
        "options": {"A": "Les Randonneurs", "B": "Blanche-Neige et les Sept Nains", "C": "Le Trône de fer", "D": "Star Treck"},
        "correct": "C"
    },
    {
        "question": "3. Que sont les fleurs de Bach ?",
        "options": {"A": "Des suites musicales", "B": "Des plantes typiques de la région de Leipzig", "C": "Des remèdes", "D": "Un recueil de poèmes"},
        "correct": "C"
    },
    {
        "question": "4. Qu'est-ce que le petit verdot ?",
        "options": {"A": "Un invertébré vermiforme", "B": "Une variété de raisin", "C": "Un objet hypothétique en astrophysique", "D": "Un personnage de « la guerre des boutons »"},
        "correct": "B"
    },
    {
        "question": "5. Le livre 'Le choc des civilisations' a été écrit par :",
        "options": {"A": "Samuel Huntington", "B": "Hiram Hutchinson", "C": "James Parkinson", "D": "Georges Huntington"},
        "correct": "A"
    },
    # ... ajoute ici les 95 autres questions pour QCM 2022
]

# QCM 2023 (exemple minimal, à compléter avec tes questions)
qcm2023 = [
    {
        "question": "1. Exemple QCM 2023 – Question 1",
        "options": {"A": "Option 1", "B": "Option 2", "C": "Option 3", "D": "Option 4"},
        "correct": "A"
    },
    {
        "question": "2. Exemple QCM 2023 – Question 2",
        "options": {"A": "Option A", "B": "Option B", "C": "Option C", "D": "Option D"},
        "correct": "B"
    },
    # ... ajoute ici les autres questions pour QCM 2023
]

# QCM 2024 (exemple minimal, à compléter avec tes questions)
qcm2024 = [
    {
        "question": "1. Exemple QCM 2024 – Question 1",
        "options": {"A": "Réponse 1", "B": "Réponse 2", "C": "Réponse 3", "D": "Réponse 4"},
        "correct": "C"
    },
    {
        "question": "2. Exemple QCM 2024 – Question 2",
        "options": {"A": "Réponse A", "B": "Réponse B", "C": "Réponse C", "D": "Réponse D"},
        "correct": "D"
    },
    # ... ajoute ici les autres questions pour QCM 2024
]

# Regroupement des QCM dans un dictionnaire pour la sélection
qcm_collection = {
    "QCM 2022": qcm2022,
    "QCM 2023": qcm2023,
    "QCM 2024": qcm2024
}

# ------------------
# Interface Streamlit
# ------------------

# Sidebar pour sélectionner le QCM
selected_qcm = st.sidebar.selectbox("Choisissez le QCM :", list(qcm_collection.keys()))
questions = qcm_collection[selected_qcm]

st.title(f"QCM d'évaluation - {selected_qcm}")

# On utilise le session_state pour savoir si les réponses ont été validées
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Formulaire du QCM
with st.form("qcm_form"):
    st.write("Répondez aux questions ci-dessous. Une fois validé, vous ne pourrez plus modifier vos réponses.")
    user_answers = {}
    for idx, q in enumerate(questions):
        st.markdown(f"**{q['question']}**")
        # Bouton radio pour choisir la réponse
        answer = st.radio(
            "Votre réponse :",
            options=list(q["options"].keys()),
            key=f"q{idx}",
            disabled=st.session_state.submitted
        )
        # Affichage du détail des options
        st.markdown(", ".join([f"**{k}** : {v}" for k, v in q["options"].items()]))
        user_answers[idx] = answer
        st.write("---")
    submitted = st.form_submit_button("Valider mes réponses")
    if submitted:
        st.session_state.submitted = True

# Affichage de la correction et du score une fois validé
if st.session_state.submitted:
    score = 0
    st.header("Correction et Résultats")
    for idx, q in enumerate(questions):
        user_ans = st.session_state.get(f"q{idx}")
        correct_ans = q["correct"]
        st.markdown(f"**{q['question']}**")
        if user_ans in q["options"]:
            st.write("Votre réponse :", user_ans, "-", q["options"][user_ans])
        else:
            st.write("Votre réponse : Non répondu")
        if user_ans == correct_ans:
            st.success("Correct")
            score += 1
        else:
            st.error(f"Faux. La bonne réponse est : {correct_ans} - {q['options'][correct_ans]}")
        st.write("---")
    total_questions = len(questions)
    percentage = (score / total_questions) * 100
    score_out_of_20 = (percentage * 20) / 100
    st.subheader(f"Score final : {score} / {total_questions}")
    st.subheader(f"Note en pourcentage : {percentage:.2f} %")
    st.subheader(f"Note sur 20 : {score_out_of_20:.2f} / 20")

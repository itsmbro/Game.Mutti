import streamlit as st
import random
import time

st.set_page_config(page_title="Trivia Game", layout="centered")

# ---------- COLORI E STILE ----------
st.markdown(
    """
    <style>
        .main { background-color: #fefefe; }
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            padding: 0.6em 1em;
            font-size: 1.1em;
            border-radius: 8px;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        .correct { color: green; font-weight: bold; font-size: 1.3em; }
        .wrong { color: red; font-weight: bold; font-size: 1.3em; }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- DATABASE DOMANDE ----------









quiz_db = {
    "Scienza": [
        {
            "question": "Qual è la particella elementare che ha carica negativa?",
            "options": [
                "Protone",
                "Elettrone",
                "Neutrone",
                "Quark"
            ],
            "answer": "Elettrone"
        },
        {
            "question": "Quale pianeta è il più caldo del sistema solare?",
            "options": [
                "Venere",
                "Mercurio",
                "Giove",
                "Marte"
            ],
            "answer": "Venere"
        },
        {
            "question": "Qual è la formula chimica dell'acqua?",
            "options": [
                "H2O",
                "CO2",
                "NaCl",
                "O2"
            ],
            "answer": "H2O"
        },
        {
            "question": "Qual è la funzione dei globuli rossi?",
            "options": [
                "Difendere il corpo",
                "Trasportare ossigeno",
                "Coagulare il sangue",
                "Produrre anticorpi"
            ],
            "answer": "Trasportare ossigeno"
        },
        {
            "question": "Cosa misura un sismografo?",
            "options": [
                "Temperatura",
                "Pressione",
                "Movimenti della terra",
                "Umidità"
            ],
            "answer": "Movimenti della terra"
        },
        {
            "question": "Quale organo del corpo umano produce l'insulina?",
            "options": [
                "Fegato",
                "Pancreas",
                "Milza",
                "Cuore"
            ],
            "answer": "Pancreas"
        }
    ],
    "Matematica": [
        {
            "question": "Quanto fa 7 × 8?",
            "options": [
                "54",
                "56",
                "58",
                "60"
            ],
            "answer": "56"
        },
        {
            "question": "Qual è il numero primo più piccolo?",
            "options": [
                "0",
                "1",
                "2",
                "3"
            ],
            "answer": "2"
        },
        {
            "question": "Quanto vale π (pi greco) approssimato?",
            "options": [
                "2.14",
                "3.14",
                "4.13",
                "5.12"
            ],
            "answer": "3.14"
        },
        {
            "question": "Quanto fa la radice quadrata di 81?",
            "options": [
                "7",
                "8",
                "9",
                "10"
            ],
            "answer": "9"
        },
        {
            "question": "Qual è il risultato di 12 ÷ 4?",
            "options": [
                "2",
                "3",
                "4",
                "5"
            ],
            "answer": "3"
        },
        {
            "question": "Cosa rappresenta il simbolo %?",
            "options": [
                "Divisione",
                "Moltiplicazione",
                "Percentuale",
                "Sottrazione"
            ],
            "answer": "Percentuale"
        }
    ],
    "Geografia": [
        {
            "question": "Qual è la capitale del Canada?",
            "options": [
                "Toronto",
                "Vancouver",
                "Ottawa",
                "Montreal"
            ],
            "answer": "Ottawa"
        },
        {
            "question": "Qual è il deserto più grande al mondo?",
            "options": [
                "Sahara",
                "Antartide",
                "Gobi",
                "Kalahari"
            ],
            "answer": "Antartide"
        },
        {
            "question": "Dove si trova il monte Everest?",
            "options": [
                "India",
                "Nepal",
                "Cina",
                "Pakistan"
            ],
            "answer": "Nepal"
        },
        {
            "question": "In quale continente si trova il fiume Nilo?",
            "options": [
                "Asia",
                "America",
                "Africa",
                "Europa"
            ],
            "answer": "Africa"
        },
        {
            "question": "Qual è la capitale dell’Australia?",
            "options": [
                "Sydney",
                "Melbourne",
                "Canberra",
                "Perth"
            ],
            "answer": "Canberra"
        },
        {
            "question": "Quale nazione ha la maggiore popolazione al mondo?",
            "options": [
                "India",
                "USA",
                "Cina",
                "Russia"
            ],
            "answer": "India"
        }
    ],
    "Storia": [
        {
            "question": "Chi era il primo imperatore romano?",
            "options": [
                "Cesare",
                "Augusto",
                "Nerone",
                "Traiano"
            ],
            "answer": "Augusto"
        },
        {
            "question": "In quale anno cadde l’Impero Romano d’Occidente?",
            "options": [
                "395",
                "410",
                "476",
                "500"
            ],
            "answer": "476"
        },
        {
            "question": "Chi scoprì l’America nel 1492?",
            "options": [
                "Magellano",
                "Cristoforo Colombo",
                "Amerigo Vespucci",
                "Vasco da Gama"
            ],
            "answer": "Cristoforo Colombo"
        },
        {
            "question": "Chi fu il dittatore italiano durante la Seconda Guerra Mondiale?",
            "options": [
                "Mussolini",
                "Hitler",
                "Stalin",
                "Churchill"
            ],
            "answer": "Mussolini"
        },
        {
            "question": "In quale anno avvenne la Rivoluzione Francese?",
            "options": [
                "1776",
                "1789",
                "1812",
                "1848"
            ],
            "answer": "1789"
        },
        {
            "question": "Quale civiltà costruì le piramidi di Giza?",
            "options": [
                "Romani",
                "Maya",
                "Egizi",
                "Greci"
            ],
            "answer": "Egizi"
        }
    ]
}







# ---------- INIZIALIZZAZIONE ----------
if "category" not in st.session_state:
    st.session_state.category = None
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
if "current_quiz" not in st.session_state:
    st.session_state.current_quiz = None
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_feedback" not in st.session_state:
    st.session_state.show_feedback = False


# ---------- FUNZIONI ----------
def next_question():
    quiz_list = quiz_db[st.session_state.category]
    st.session_state.current_quiz = random.choice(quiz_list)
    st.session_state.quiz_index += 1
    st.session_state.show_feedback = False


def restart_game():
    st.session_state.category = None
    st.session_state.quiz_index = 0
    st.session_state.score = 0
    st.session_state.current_quiz = None
    st.session_state.show_feedback = False


# ---------- UI ----------
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎯 Trivia Quiz per iPad</h1>", unsafe_allow_html=True)

if st.session_state.category is None:
    st.subheader("Scegli una categoria:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧬 Scienza"):
            st.session_state.category = "Scienza"
            next_question()
    with col2:
        if st.button("🧮 Matematica"):
            st.session_state.category = "Matematica"
            next_question()
    col3, col4 = st.columns(2)
    with col3:
        if st.button("🌍 Geografia"):
            st.session_state.category = "Geografia"
            next_question()
    with col4:
        if st.button("🏛️ Storia"):
            st.session_state.category = "Storia"
            next_question()
else:
    st.markdown(f"<h3 style='color: #2196F3;'>Categoria: {st.session_state.category}</h3>", unsafe_allow_html=True)
    quiz = st.session_state.current_quiz
    st.write(f"**Domanda {st.session_state.quiz_index}:** {quiz['question']}")

    answer = st.radio("Scegli una risposta:", quiz["options"], index=None)

    if "verify_clicked" not in st.session_state:
    st.session_state.verify_clicked = False

if not st.session_state.show_feedback:
    if st.button("Verifica", key="verify_button") and answer:
        st.session_state.show_feedback = True
        st.session_state.verify_clicked = True
        if answer == quiz["answer"]:
            st.session_state.score += 1
else:
    if st.session_state.verify_clicked:
        if answer == quiz["answer"]:
            st.markdown("<div class='correct'>✅ Corretto!</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='wrong'>❌ Sbagliato! La risposta giusta era: <b>{quiz['answer']}</b></div>", unsafe_allow_html=True)

        if st.button("➡️ Prossima domanda", key="next_question"):
            next_question()
            st.session_state.verify_clicked = False

    st.markdown(f"<br><div style='text-align:center; font-size:1.1em;'>Punteggio: <b>{st.session_state.score}</b></div>", unsafe_allow_html=True)
    st.markdown("---")
    if st.button("🔁 Rinizia"):
        restart_game()

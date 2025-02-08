import streamlit as st
from utils import specialMessage




questions = [
        {
            "question": "Did you like the letter?",
            "options": ["yes 👍", 
                        "no 👎", 
                        "could've done better..."],
            "correct": "yes 👍",
            "correctAnswer": "I know lol im just him 😎",
            "wrongAnswer": "damn..."
        },
        {
            "question": "What is one thing I love most about you?",
            "options": ["your kind heart and beautiful soul ❤️", 
                        "ass 🍑", 
                        "toes 🤪"],
            "correct": "toes 🤪",
            "correctAnswer": "",
            "wrongAnswer": "❌Close 👌 Try Again!❌"
        },
        {
            "question": "Who is my celebrity crush?",
            "options": ["i break up with you 💔", 
                        "Sydney Sweeney"],
            "correct": "Sydney Sweeney",
            "correctAnswer": "NAAAAAH dont worry bubinka baby bae shawty",
            "wrongAnswer": "Dont break up with me please 😥"
        }
    ]

############################
def quizFunction(questions):
############################
    # st.markdown(
    # """
    # <style>
    # div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    # font-size: 32px;
    # }
    # </style>
    # """, unsafe_allow_html=True)

    if "questionIndex" not in st.session_state:
        st.session_state.questionIndex = 0
        st.session_state.selected = None


    index = st.session_state.questionIndex
    question = questions[index]

    specialMessage(question['question'], 40)

    # Display answer choices
    answer = st.radio("", question["options"], key=f"q{index}")

    # Submit button to check answer
    if st.button("Submit"):
        st.session_state.selected = answer

    # Show feedback only after an answer is selected
    if st.session_state.selected:
        if st.session_state.selected == question["correct"]:
            if question["correct"] == "toes 🤪":
                st.image('toes.jpg', width=200)
            else:
                specialMessage(question["correctAnswer"], 20)
        else:
            specialMessage(question["wrongAnswer"], 20)

        # Move to next question when "Next" button is clicked
        if index + 1 < len(questions):
            if st.button("Next Question"):
                st.session_state.questionIndex += 1
                st.session_state.selected = None  # Reset answer
                st.rerun()  # Correct way to refresh UI
        else:
            specialMessage("Now time for the important thing...", 40)
            if st.button("WHAT IS IT??"):
                st.session_state.startQuiz = False
                st.session_state.askValentine = True
                st.rerun()
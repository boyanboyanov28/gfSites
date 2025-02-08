import streamlit as st
from quiz import quizFunction, questions
from utils import specialMessage, setBackground, showBalloons, showGif
from valentine import valentineQuestion


if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "wrongPassword" not in st.session_state:  
    st.session_state.wrongPassword = None
if "startQuiz" not in st.session_state:  
    st.session_state.startQuiz = False
if "askValentine" not in st.session_state: 
    st.session_state.askValentine = False
if "balloons" not in st.session_state:
    st.session_state.balloons = True
if "showGifOnly" not in st.session_state:
    st.session_state.showGifOnly = False

####################
def checkPassword():
####################
    if st.session_state.password_input == 'balloons':
        st.session_state.authenticated = True
        st.session_state.startQuiz = True
    else:
        st.session_state.wrongPassword = True


def main():
    if not st.session_state.authenticated:
        specialMessage("Hi, Bubka ❤️", 50)
        specialMessage("I made something special for you. Hint: Use the letter and mirror 👀", 30)

        st.text_input("Enter Password:", type="password", key="password_input", on_change=checkPassword)
        if st.session_state.wrongPassword:
            st.error("Wrong password! I thought you're better than this...")


    if st.session_state.startQuiz:
        showBalloons()
        quizFunction(questions)


    if st.session_state.askValentine:
        valentineQuestion()

    if st.session_state.showGifOnly:
        showGif()

main()

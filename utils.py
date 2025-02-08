import os
import streamlit as st
import base64


##################################
def specialMessage(message, size):
##################################
    st.markdown(
        f"<p style='color:#AF3232; text-shadow: 2px 2px 4px grey; font-size: {size}px;'>"
        f"{message}"
        "</p>", unsafe_allow_html=True)


#############################
def stylesForValentinePage():
#############################
    st.markdown(
        """
        <style>
            body {
                background-color: #ffdde1;
                background-image: linear-gradient(45deg, #ffdde1, #ee9ca7);
                color: white;
                text-align: center;
            }
            .big-text {
                font-size: 36px;
                font-weight: bold;
                color: #fff;
                text-shadow: 2px 2px 8px #ff4081;
            }
            .heart {
                font-size: 50px;
                color: red;
                text-align: center;
                animation: pulse 1.5s infinite;
            }
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.2); }
                100% { transform: scale(1); }
            }
            .button-container {
                display: flex;
                justify-content: center;
                gap: 20px;
                margin-top: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .pink-container {
            background-color: #ffb6c1;  /* Light pink */
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 10px rgba(255, 20, 147, 0.3);  /* Soft pink shadow */
        }
        </style>
        """,
        unsafe_allow_html=True
    )


#############################    
def setBackground(imageFile):
#############################
    with open(imageFile, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()  # Encode image to base64
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


###################
def showBalloons():
###################
    if st.session_state.balloons:
        st.balloons()
        st.session_state.balloons = False


##############
def showGif():
##############
    specialMessage('That is the right answer 😚', 40)
    st.markdown("![Alt Text](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmxzd3ZuMXh4NXJhYXFsdWRzczBteWIzcGI3a3E1djcwMTlicHI2YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NxC8VtyxqhMtpLoEEN/giphy.gif)")

# st.markdown(
#     """
#     <style>
#     @keyframes float {
#         0% {transform: translateY(0px);}
#         50% {transform: translateY(-20px);}
#         100% {transform: translateY(0px);}
#     }
#     .heart {
#         position: absolute;
#         font-size: 30px;
#         color: red;
#         animation: float 1s infinite ease-in-out;
#     }
#     </style>
#     <div class="heart">❤️</div>
#     <div class="heart" style="left: 30px; top: 50px;">❤️</div>
#     <div class="heart" style="left: 60px; top: 100px;">❤️</div>
#     """,
#     unsafe_allow_html=True
# )
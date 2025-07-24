import streamlit as st
from streamlit_chat import message

# Add custom CSS for pink background and styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4);
        color: #4b3f2f;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 0 1rem;
    }
    .stTextInput > div > div > input {
        font-size: 18px;
        padding: 12px;
        border-radius: 10px;
        border: 2px solid #ff69b4;
        background-color: #fff0f6;
    }
    div.stButton > button {
        background-color: #ff69b4;
        color: white;
        font-weight: 600;
        border-radius: 10px;
        padding: 12px 25px;
        border: none;
        transition: background-color 0.3s ease;
        margin-top: 10px;
    }
    div.stButton > button:hover {
        background-color: #ff1493;
        cursor: pointer;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Happy Birthday My MONKEYYYY🎂")
st.markdown(
    "Welcome to YOUR special chatbot  :p   this chatbot was made specially for you, you get to ask him anything about us and he will let you know my answers.. dont be too smart ofc its just a mini app for your birthday"
)

# Initialize session state to store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Loving messages dictionary
loving_messages = {
    "how much do you love me": "are you dumb what kinda question is that, ofc i love you, you're the best thing ever happened to me and id never wanna leave you :3",
    "why do you love me": "Because of who you are, youre the kindest soul ive even met. (also bcz ur hot)",
    "tell me a secret": "I nut to the thought of u + i want money",
    "what's the plan for my birthday": "To spend the whole night making you happy and feeling loved. :>",
}

# Input area
user_input = st.text_input("DROP YOUR QUESTION:")

def get_response(question):
    question = question.lower().strip()
    if question in loving_messages:
        return loving_messages[question]
    elif question == "":
        return "Ask me something sweetie 💕"
    else:
        return "I love you so much, more than words can say! ❤️"

# When user submits
if st.button("ASK"):
    if user_input:
        # Add user message to history
        st.session_state.history.append({"user": user_input})
        # Get bot response and add it to history
        response = get_response(user_input)
        st.session_state.history.append({"bot": response})

# Display chat messages using streamlit-chat
for chat in st.session_state.history:
    if "user" in chat:
        message(chat["user"], is_user=True)
    else:
        message(chat["bot"])

# Fun birthday button to celebrate!
if st.button("YIPIEEEE 🎉"):
    st.balloons()
    st.success("Happy Birthdayyy")

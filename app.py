import streamlit as st
import base64
from streamlit_chat import message

# --- Set Background Image ---
def set_background(image_file):
    with open(image_file, "rb") as img:
        bg_bytes = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg_bytes}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        .popup-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0, 0, 0, 0.5);
            z-index: 9998;
        }}
        .gift-popup {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 0 20px #ff94d6;
            border: 4px solid #ff5ebc;
            z-index: 9999;
            max-width: 350px;
            max-height: 90vh;
            overflow-y: auto;
            text-align: center;
        }}
        .close-btn {{
            background-color: #ff5ebc;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 8px 20px;
            cursor: pointer;
            font-weight: bold;
            margin-top: 15px;
            font-size: 16px;
        }}
        .stDeployButton, .st-emotion-cache-1y4p8pa {{
            display: none !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

set_background("bg.jpg")

# --- Balloons on First Load ---
if "loaded_once" not in st.session_state:
    st.session_state.loaded_once = True
    st.balloons()

# --- Title and Intro ---
st.title("Happy Birthday My MONKEYYYY🎂")
st.markdown(
    "Welcome to YOUR special chatbot :p this chatbot was made specially for you. "
    "You get to ask him anything about us and he will let you know my answers.. "
    "**Don’t be too smart ofc, it’s just a mini app for your birthday 💖**"
)

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "show_gift" not in st.session_state:
    st.session_state.show_gift = False

# --- Loving Replies ---
loving_messages = {
    "how much do you love me": "are you dumb what kinda question is that, ofc i love you, you're the best thing ever happened to me and id never wanna leave you :3",
    "why do you love me": "Because of who you are, youre the kindest soul ive even met. (also bcz ur hot)",
    "tell me a secret": "I nut to the thought of u + i want money",
    "what's the plan for my birthday": "To spend the whole night making you happy and feeling loved. :>"
}

# --- Input Box ---
user_input = st.text_input("DROP YOUR QUESTION:", key="input_text")

# --- Ask Button BELOW input ---
ask_pressed = st.button("Ask")

# --- Generate Response ---
if ask_pressed and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    question = user_input.lower().strip()

    if question in loving_messages:
        reply = loving_messages[question]
    elif "gift" in question:
        reply = "You already opened it, didn’t you? 😉"
    elif "who made you" in question:
        reply = "Someone who really really loves you 💕"
    else:
        reply = "sorry i didnt prepare the bot to answer this"

    st.session_state.messages.append({"role": "assistant", "content": reply})

# --- Chat History ---
for i, msg in enumerate(st.session_state.messages):
    is_user = msg["role"] == "user"
    message(msg["content"], is_user=is_user, key=str(i))

# --- Gift Button ---
if st.button("🎁 Your Gift"):
    st.session_state.show_gift = True

# --- Gift Popup ---
if st.session_state.show_gift:
    gift_data = base64.b64encode(open("gift.jpg", "rb").read()).decode()
    st.markdown(f"""
    <div class="popup-overlay"></div>
    <div class="gift-popup">
        <img src="data:image/jpeg;base64,{gift_data}" width="325" style="max-height:75vh; object-fit:contain;" />
        <div style="margin-top: 20px;">
            <form action="" method="post">
                <button name="close_gift" class="close-btn">⬅️ Back</button>
            </form>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.query_params.get("close_gift") is not None:
        st.session_state.show_gift = False
        st.rerun()

# --- Add Space Before Video ---
st.markdown("<div style='height: 700px;'></div>", unsafe_allow_html=True)

# --- Birthday Video (make sure it's mp4) ---
try:
    with open("gift2.mp4", "rb") as video_file:
        video_bytes = video_file.read()
    st.video(video_bytes)
except FileNotFoundError:
    st.warning("Video file not found. Please convert `gift2.MOV` to `gift2.mp4`.")

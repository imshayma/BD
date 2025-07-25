import streamlit as st
import base64
from streamlit_chat import message

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
            background: rgba(0,0,0,0.5);
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
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("bg.jpg")

# Read URL query params
query_params = st.experimental_get_query_params()
gift_param = query_params.get("gift", ["0"])[0]
play_video_param = query_params.get("playvideo", ["0"])[0]

# Initialize session state for messages and popup
if "messages" not in st.session_state:
    st.session_state.messages = []

if "show_gift" not in st.session_state:
    st.session_state.show_gift = False

if "play_video" not in st.session_state:
    st.session_state.play_video = False

# Sync session state with URL params
if gift_param == "1":
    st.session_state.show_gift = True
else:
    st.session_state.show_gift = False

if play_video_param == "1":
    st.session_state.play_video = True
else:
    st.session_state.play_video = False

# --- Intro ---
st.title("Happy Birthday My MONKEYYYY🎂")
st.markdown(
    "Welcome to YOUR special chatbot :p this chatbot was made specially for you. "
    "You get to ask him anything about us and he will let you know my answers.. "
    "**Don’t be too smart ofc, it’s just a mini app for your birthday 💖**"
)

loving_messages = {
    "how much do you love me": "are you dumb what kinda question is that, ofc i love you, you're the best thing ever happened to me and id never wanna leave you :3",
    "why do you love me": "Because of who you are, youre the kindest soul ive even met. (also bcz ur hot)",
    "tell me a secret": "I nut to the thought of u + i want money",
    "what's the plan for my birthday": "To spend the whole night making you happy and feeling loved. :>"
}

# --- Chat Input + Ask button ---
# We'll create a form to hold input + button (so enter doesn't submit automatically)
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("DROP YOUR QUESTION:")
    submitted = st.form_submit_button("Ask")

if submitted and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    question = user_input.lower().strip()

    if question in loving_messages:
        reply = loving_messages[question]
    elif "gift" in question:
        reply = "You already opened it, didn’t you? 😉"
    elif "who made you" in question:
        reply = "Someone who really really loves you 💕"
    else:
        reply = "That's so sweet of you to say 🥺"

    st.session_state.messages.append({"role": "assistant", "content": reply})

# --- Display chat history ---
for i, msg in enumerate(st.session_state.messages):
    is_user = msg["role"] == "user"
    message(msg["content"], is_user=is_user, key=str(i))

# --- Buttons side by side: Gift and Heart ---
col1, col2 = st.columns([1,1])

with col1:
    if st.button("🎁 Your Gift"):
        st.experimental_set_query_params(gift="1")
        st.experimental_rerun()

with col2:
    if st.button("❤️"):
        st.experimental_set_query_params(playvideo="1")
        st.experimental_rerun()

# --- Gift popup ---
if st.session_state.show_gift:
    gift_data = base64.b64encode(open("gift.jpg", "rb").read()).decode()
    popup_html = f"""
    <div class="popup-overlay"></div>
    <div class="gift-popup">
        <img src="data:image/jpeg;base64,{gift_data}" width="325" style="max-height:75vh; object-fit:contain;" />
        <button class="close-btn" onclick="
            const url = new URL(window.location);
            url.searchParams.delete('gift');
            window.history.replaceState(null, '', url);
            window.location.reload();
        ">Close Gift 🎁</button>
    </div>
    """
    st.markdown(popup_html, unsafe_allow_html=True)

# --- Video popup ---
if st.session_state.play_video:
    video_file = open("gift2.MOV", "rb").read()
    st.video(video_file, format="video/mp4", start_time=0)  # Streamlit handles MOV but mp4 is more universal; if issues, convert MOV to mp4

    # Also add a "Close Video" button to stop it and remove URL param
    if st.button("Close Video ❤️"):
        st.experimental_set_query_params()
        st.experimental_rerun()

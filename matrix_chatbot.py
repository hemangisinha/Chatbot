import streamlit as st
from openai import OpenAI

# Setup Streamlit page config
st.set_page_config(
    page_title="Matrix Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto",
)

# Custom CSS for Matrix rain background
matrix_bg = """
<style>
body {
  background-color: black;
  color: #00FF41;
  background-image: url('https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif');
  background-size: cover;
}
textarea, input, .stButton>button {
  background-color: #000;
  color: #00FF41;
  border-color: #00FF41;
}
</style>
"""

st.markdown(matrix_bg, unsafe_allow_html=True)

st.title("💻 My Chatbot")
st.write("Talk to your AI — in 100 words or less 🌧️")

# API key input
api_key = st.text_input(
    "🔑 Enter your OpenAI API Key:", 
    type="password",
    help="Your API key is safe — it is not stored."
)

# User input
prompt = st.text_area("💬 Your Message:", placeholder="Enter your prompt here...")

if st.button("Send"):
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not prompt.strip():
        st.warning("Please enter a message to send.")
    else:
        client = OpenAI(api_key=api_key)
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a poetic, concise chatbot. All responses must be under 100 words."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            reply = response.choices[0].message.content.strip()
            if len(reply.split()) > 100:
                reply = "⚠️ Oops! Response exceeded 100 words. Please try again."
            st.text_area("🤖 AI says:", value=reply, height=200)
        except Exception as e:
            st.error(f"Error: {e}")

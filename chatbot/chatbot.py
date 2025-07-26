import streamlit as st
from anthropic import Anthropic

API_KEY = "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"
client=Anthropic(api_key=API_KEY)

st.set_page_config(page_title="claude chatbot", page_icon="👌")
st.title("claud chatbot")
st.markdown("Ask anything and get Claude reply using Anthropic's LLM.")

# --- Session State to Store Chat ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
user_input = st.text_input("You", "")

# --- Send to Claude & Get Response ---
def ask_claude(prompt):
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

# --- When User Submits a Question ---
if st.button("Send") and user_input:
    st.session_state.chat_history.append(("You", user_input))
    with st.spinner("Claude is thinking..."):
        reply = ask_claude(user_input)
        st.session_state.chat_history.append(("Claude", reply))

# --- Display Chat History ---
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
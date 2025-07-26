import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os

# API Key
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# Streamlit UI
st.set_page_config(page_title="Memory Chatbot 🤖", page_icon="🧠")
st.title("🧠 Memory ChatBot with LangChain")

# Model + Memory
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

# Session state to persist chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_query = st.text_input("You:", "")

if st.button("Send") and user_query:
    response = conversation.predict(input=user_query)
    st.session_state.chat_history.append(("You", user_query))
    st.session_state.chat_history.append(("Bot", response))

# Display chat history
for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os

#step 1: API key
os.environ["OPENAI_API_KEY"]="your-api-key"

#step 2: Define the model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

#step3: create a memory object

memory = ConversationBufferMemory()

#step 4: create conversion chain with memory

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

#step 5: Interactive loop
print("ChatBot is ready! (type 'exit' to quit)\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = conversation.predict(input=user_input)
    print(f"Bot: {response}\n")
    
    
    
    
    
    
    
    
    
    
    
    
    

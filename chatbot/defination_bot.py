# definition_bot.py

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os

# ✅ Step 1: Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"  # Replace this

# ✅ Step 2: Define Prompt Template
template = """
You are a helpful dictionary assistant.
Explain the word or concept "{concept}" in a simple and clear way suitable for a 12-year-old.
"""

prompt = PromptTemplate(
    input_variables=["concept"],
    template=template
)

# ✅ Step 3: Choose LLM (OpenAI's ChatGPT)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)

# ✅ Step 4: Create a Chain (Prompt + LLM)
chain = LLMChain(prompt=prompt, llm=llm)

# ✅ Step 5: Run the Chain with User Input
if __name__ == "__main__":
    concept = input("Enter a word or concept to define: ")
    definition = chain.run(concept=concept)
    
    print("\n📚 Definition:")
    print(definition)

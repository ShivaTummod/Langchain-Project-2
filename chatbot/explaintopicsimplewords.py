from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMchain
import os

#set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

template = """
You are a helpful and friendly teacher.
Explain the topic "{topic}" in a simple and beginner-friendly way.
Avoid jargon. Make it easy to understand.
"""
prompt = PromptTemplate(
    input_vairables = ["topic"],
    template = template
)

llm = ChatOpenAI(mosel_name="gpt-3.5-turbo", temperature =0.7)

chain = LLMchain(llm=llm, prompt=prompt)

if __name__ == "__main__":
    user_topic = input("Enter a topic to explain:")
    explanation = chain.run(topic=user_topic)
    print("\n explanation:")
    print(explanation)
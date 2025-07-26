

# choose language model
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(model_name ="gpt-3.5-turbo", temperature=0.5)

import os
os.environ["OPENAI_API_KEY"] = "my-api-key"

#create a prompt template
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in simple words:\n\n{text}\n\nSummary:"
)

#create an LLMChain
from langchain.chains import LLMChain
summarization_chain=LLMChain(llm=llm, prompt=prompt)
# LLMChain connects the LLM with your prompt logic to produce answers.

#run the summarizer
input_text="LangChain is a powerful framework that allows you to build applications..."
response= summarization_chain.run(text=input_text)
print(response)
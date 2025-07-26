from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

#step 1: create a prompt Template
prompt = PromptTemplate(
    input_vairables = ["name"],
    template = "wrie a short poem for {name}",
)

#step 2: Load a chatgpt model
llm = ChatOpenAI()

#step 3: create a chain (prompt + LLM)
chain = LLMChain(prompt=prompt, llm=llm)

#step 4: Run the chain with input
result = chain.run("shiva")
print(result)

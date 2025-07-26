from langchain.prompts import PromptTemplate

#define a prompt template with placeholder
template = """
You are an expert teacher.
Explain the topic "{topic}" in simple words suitable for beginner.
"""
#Step 2: create a prompt template object
prompt = PromptTemplate(
    input_variables=["topic"],
    template = template
)

#step3: use the template to format a prompt
final_prompt = prompt.format(topic="quantum computing")

print(final_prompt)









from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

llm = ChatOpenAI(model="gpt-3.5-turbo")

# Create the LLM chain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain with user input
response = chain.run(topic="machine learning")
print(response)

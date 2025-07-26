# main.py
import os
from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 🔐 Set your Hugging Face Token here
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"


# ✅ Define a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short paragraph about {topic}"
)

# ✅ Load Hugging Face model (must be text-generation type)
llm = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-beta",  # Try this model (you can change it)
    model_kwargs={"temperature": 0.7, "max_new_tokens": 200}
)

# ✅ Build LangChain
chain = LLMChain(llm=llm, prompt=prompt)

# ✅ Run it
result = chain.run("Artificial Intelligence")
print(result)

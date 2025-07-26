

# generator.py
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceHub
import os

# Set Hugging Face Token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

def generate_custom_resume(resume_text, jd_text):
    prompt = PromptTemplate(
        input_variables=["resume", "jd"],
        template="""
You are an expert resume writer. Improve and tailor the following resume to match the given job description.

Resume:
{resume}

Job Description:
{jd}

Tailored Resume:
"""
    )

    llm = HuggingFaceHub(
        repo_id="HuggingFaceH4/zephyr-7b-beta",  # ✅ Proper text-generation model
        model_kwargs={"temperature": 0.7, "max_new_tokens": 1024}
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(resume=resume_text, jd=jd_text)

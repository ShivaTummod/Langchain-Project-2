import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ✅ SentencePiece-free multilingual translation model
model_name = "facebook/nllb-200-distilled-600M"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Language codes for NLLB
source_lang = "eng_Latn"
target_lang = "hin_Deva"

# Streamlit app
st.title("English to Hindi Translator (No SentencePiece / No Conda)")
input_text = st.text_input("Enter English text")

if input_text:
    # Add language token and tokenize
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    inputs["forced_bos_token_id"] = tokenizer.lang_code_to_id[target_lang]

    # Generate and decode output
    outputs = model.generate(**inputs)
    hindi_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Show result
    st.success("Hindi Translation:")
    st.write(hindi_output)

import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Model that does not use SentencePiece
model_name = "facebook/nllb-200-distilled-600M"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Language codes for NLLB-200
source_lang = "eng_Latn"
target_lang = "hin_Deva"

# Streamlit UI
st.title("English to Hindi Translator (No SentencePiece / No Conda)")
text = st.text_input("Enter English text")

if text:
    tokenizer.src_lang = source_lang
    encoded = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    # ✅ Correct way to get BOS token ID
    bos_token_id = tokenizer.convert_tokens_to_ids("▁" + target_lang)

    # Generate translation
    generated = model.generate(**encoded, forced_bos_token_id=bos_token_id)
    hindi_translation = tokenizer.decode(generated[0], skip_special_tokens=True)

    st.success("Hindi Translation:")
    st.write(hindi_translation)

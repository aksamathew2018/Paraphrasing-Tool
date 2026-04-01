import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

@st.cache_resource
def load_model():
    model_name = "humarin/chatgpt_paraphraser_on_T5_base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

def paraphrase_text(text):
    input_text = "paraphrase: " + text + " </s>"

    encoding = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True)

    outputs = model.generate(
        input_ids=encoding["input_ids"],
        attention_mask=encoding["attention_mask"],
        max_length=128,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
        no_repeat_ngram_size=2,
        num_return_sequences=5
    )

    paraphrases = [tokenizer.decode(o, skip_special_tokens=True).strip() for o in outputs]

    clean = [p for p in paraphrases if len(p.split()) > 5 and p.lower() != text.lower()]

    best = clean[0] if clean else paraphrases[0]
    best = best.strip()
    best = best[0].upper() + best[1:]

    return best

st.title("📝 AI Paraphrasing Tool")
user_input = st.text_area("Enter text")

if st.button("Paraphrase"):
    if user_input.strip() == "":
        st.warning("Please enter text")
    else:
        with st.spinner("Generating..."):
            result = paraphrase_text(user_input)

        st.success(result)



# 🧠 AI Paraphrasing Tool

This project is a simple AI-powered paraphrasing tool built using **Streamlit** and **Hugging Face Transformers**. It takes user input text and generates a paraphrased version using a pre-trained NLP model.

---

## 🚀 Features

* Accepts user input text
* Generates paraphrased output using a transformer model
* Simple and interactive UI using Streamlit
* Fast and lightweight setup

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Hugging Face Transformers
* PyTorch

---

## 📦 Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/ai-paraphrasing-tool.git
cd ai-paraphrasing-tool
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install manually:

```bash
pip install streamlit transformers sentencepiece torch
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

---

## 📄 Project Structure

```
ai-paraphrasing-tool/
│
├── app.py               # Main Streamlit app
├── model/               # (Optional) Saved model files
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## 🤖 Model Used

* `humarin/chatgpt_paraphraser_on_T5_base`

This model is based on the **T5 architecture** and is fine-tuned for paraphrasing tasks.

---

## ⚠️ Current Status

❌ Deployment is **not completed yet**

* The app runs locally
* Not hosted on Streamlit Cloud / Hugging Face Spaces yet

---

## 🌐 Future Improvements

* Deploy on Streamlit Cloud
* Improve paraphrasing quality
* Add multiple paraphrase options
* Add text length control
* UI improvements

---

## 📌 Notes

* Output quality may vary depending on input sentence
* Short or unclear sentences may give poor paraphrasing results

---

## 🙌 Acknowledgements

* Hugging Face Transformers
* Streamlit
--

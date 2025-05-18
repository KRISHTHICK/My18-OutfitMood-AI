# My18-OutfitMood-AI
Gen Ai

Here’s a **new fashion-related AI project** topic with **full code**, clear explanation, and instructions to run it locally in **VS Code** and deploy on **GitHub**.

---

## 👗 Project Title: **OutfitMood AI - Mood-Based Fashion Recommender**

### 🎯 Objective:

Build an AI-powered app that recommends outfits based on the user’s mood and weather conditions. It combines emotion analysis + weather data + fashion style matching to offer personalized suggestions.

---

### 💡 Features:

* Mood input via text (e.g., “I feel energetic and confident”)
* Weather condition input (manual or auto fetch – optional)
* AI recommends outfit styles, colors, and accessories
* Suggests matching captions and hashtags for Instagram
* Built using Streamlit, LangChain, and HuggingFace

---

## 🧱 Folder Structure:

```
OutfitMood-AI/
├── app.py
├── requirements.txt
├── README.md
```

---

## 📦 `requirements.txt`

```txt
streamlit
langchain
transformers
torch
sentence-transformers
```

---

## 🚀 `app.py` – Full Code

```python
import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import SimpleSequentialChain

# 1. Page Configuration
st.set_page_config(page_title="OutfitMood AI", layout="centered")

# 2. Title
st.title("👗 OutfitMood AI")
st.subheader("Get outfit ideas based on your mood and weather 🌦️")

# 3. Mood and Weather Input
mood = st.text_area("💬 Describe your current mood:", placeholder="e.g., I feel happy and energetic")
weather = st.selectbox("🌤️ What's the weather like?", ["Sunny", "Cloudy", "Rainy", "Cold", "Hot", "Windy"])

# 4. Initialize Ollama LLM (make sure it's running locally)
llm = Ollama(model="tinyllama")

# 5. Outfit Suggestion Chain
outfit_prompt = PromptTemplate(
    input_variables=["mood", "weather"],
    template="Suggest a fashionable outfit for someone who feels {mood} during a {weather} day. Include clothing, color suggestions, and accessories."
)
outfit_chain = LLMChain(llm=llm, prompt=outfit_prompt)

# 6. Caption Generator
caption_prompt = PromptTemplate(
    input_variables=["mood"],
    template="Create a trendy Instagram caption with emojis and hashtags for someone feeling {mood} and dressed fashionably."
)
caption_chain = LLMChain(llm=llm, prompt=caption_prompt)

# 7. Run the chains
if st.button("🎨 Generate Outfit Recommendation"):
    with st.spinner("Thinking..."):
        outfit = outfit_chain.run(mood=mood, weather=weather)
        caption = caption_chain.run(mood=mood)

    st.markdown("### 👚 Outfit Suggestion:")
    st.success(outfit)

    st.markdown("### 📝 Instagram Caption & Hashtags:")
    st.info(caption)
```

---

## 📖 `README.md`

````markdown
# 👗 OutfitMood AI - Mood & Weather Based Fashion Recommender

This is an AI-powered app that recommends outfits based on the user's **mood** and **weather condition**.

## ✨ Features
- Personalized fashion recommendations
- Weather-aware style suggestions
- Trendy caption & hashtag generator

## 🛠️ Tech Stack
- Python
- Streamlit
- LangChain
- HuggingFace/Ollama LLMs

## 🚀 How to Run Locally in VS Code

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/OutfitMood-AI.git
cd OutfitMood-AI
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Make Sure Ollama is Running Locally

Start TinyLLaMA or any supported model:

```bash
ollama run tinyllama
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

## ✅ Output

* 🧥 Outfit suggestion with styling tips
* 📸 Caption and hashtags for social media

## 📌 Example Mood Inputs

* “I feel relaxed and calm”
* “I’m excited and energetic”
* “Feeling classy and confident today”

## 📬 Contact

Built by [Your Name](https://github.com/your-username) – Fashion + AI enthusiast

```

---

Would you like me to:
- Add image upload and outfit match next?
- Include actual sample output screenshots for the GitHub repo?

Let me know and I’ll extend the features!
```

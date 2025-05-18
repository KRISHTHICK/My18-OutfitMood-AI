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

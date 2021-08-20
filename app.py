import os
import openai
import streamlit as st

openai.api_key = os.getenv("OAPI")

response = openai.Completion.create(
  engine="davinci",
  prompt=st.text_input("AMA, symptoms?", "I am having fever"),
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)
st.write(response)

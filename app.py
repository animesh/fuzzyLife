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
term=st.text_input("AMA, symptoms?", "fever")
term=term.rsplit(' ', 1)[-1]#"fever"
#term="headache"
qMesh="https://id.nlm.nih.gov/mesh/lookup/descriptor?label="+term+"&match=exact&limit=1"
import requests
rMesh = requests.get(qMesh,headers={'user-agent':'Python'}).json()
qCTD="http://ctdbase.org/detail.go?type=disease&acc=MESH%3A"+rMesh[0].get('resource').rsplit('/', 1)[-1]
rCTD = requests.get(qCTD,headers={'user-agent':'Python'}).text
name=rCTD[rCTD.find("gridrow0"):rCTD.find("td")]
name=rCTD[rCTD.find("<td class=\"gridrow0\">"):-1]
name=name[len("<td class=\"gridrow0\">"):name.find(".")]
name=name.strip()
name=name.replace("\n","")
name=name.replace("\r","")
st.write(name,[rCTD])
#https://id.nlm.nih.gov/mesh/lookup/descriptor?label=headache&match=contains&limit=50
#http://ctdbase.org/detail.go?type=disease&acc=MESH%3AD005334

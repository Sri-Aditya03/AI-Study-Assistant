import streamlit as st
from chains.study_chains import study_chain

st.title("AI Study Assistant")

topic = st.text_input("Enter a topic: ")

if st.button("Explain"):

    response = study_chain.invoke({
        "topic":topic
    })

    st.write(response)
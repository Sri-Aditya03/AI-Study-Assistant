import streamlit as st

from langchain_core.messages import HumanMessage, AIMessage

from chains.study_chains import study_chain

st.title("AI Study Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:

    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)

# User input
user_input = st.chat_input("Ask something...")

if user_input:

    # Display user message
    with st.chat_message("Human"):
        st.markdown(user_input)

    # Invoke chain
    response = study_chain.invoke({
        "chat_history": st.session_state.chat_history,
        "input": user_input
    })

    # Display AI response
    with st.chat_message("AI"):
        st.markdown(response)

    # Save messages into memory
    st.session_state.chat_history.append(
        HumanMessage(content=user_input)
    )

    st.session_state.chat_history.append(
        AIMessage(content=response)
    )
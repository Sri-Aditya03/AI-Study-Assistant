from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

study_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a helpful AI study assistant.
            Explain concepts in beginner-friendly terms.
            """
        ),

        MessagesPlaceholder(variable_name="chat_history"),

        (
            "human",
            "{input}"
        )
    ]
)
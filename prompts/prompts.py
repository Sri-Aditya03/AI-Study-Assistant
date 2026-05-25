from langchain_core.prompts import ChatPromptTemplate

study_prompt = ChatPromptTemplate.from_template(
     """
    You are a helpful AI study assistant.

    Explain the following topic in simple beginner-friendly terms.

    Topic: {topic}

    Give:
    1. Simple explanation
    2. Real-world analogy
    3. Important points to remember
    """
)
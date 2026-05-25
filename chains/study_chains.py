import os
from dotenv import load_dotenv 
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompts.prompts import study_prompt

load_dotenv()

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0.7
)

parser = StrOutputParser()

study_chain = study_prompt | llm | parser


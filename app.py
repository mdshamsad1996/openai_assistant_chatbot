import warnings

warnings.filterwarnings('ignore')

import streamlit as st
from langchain_openai import ChatOpenAI
from retriever import ensemble_retriever

from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

from langchain.prompts import ChatPromptTemplate

from  src.prompt import *



llm = ChatOpenAI(model_name="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_template(template)
output_parser=StrOutputParser()



# Function to generate chatbot response
def generate_response(user_input):

    rag_chain = (
        {"context": ensemble_retriever,  "question": RunnablePassthrough()}
        | prompt
        | llm
        | output_parser
    ) 
    response = rag_chain.invoke(user_input)
    print(response)
    return response




# Streamlit UI
st.title("Simple Chatbot Application")

# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# User input
user_input = st.text_input("You:", key="input", max_chars=1000)

if st.button("Submit"):

    # If the user submits input
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response from LLM
    bot_response = generate_response(user_input)
    
    # Append bot response to the chat history
    st.session_state.messages.append({"role": "bot", "content": bot_response})

    st.write(bot_response)


if st.button("Clear Chat"):
    st.session_state.messages = []

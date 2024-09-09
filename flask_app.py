from flask import Flask, request, jsonify
import warnings
from langchain_openai import ChatOpenAI
from retriever import ensemble_retriever
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from src.prompt import template

# Initialize the Flask app
app = Flask(__name__)

warnings.filterwarnings('ignore')

# Initialize the LLM and prompt template
llm = ChatOpenAI(model_name="gpt-3.5-turbo")
prompt = ChatPromptTemplate.from_template(template)
output_parser = StrOutputParser()

# Function to generate chatbot response
def generate_response(user_input):
    rag_chain = (
        {"context": ensemble_retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | output_parser
    )
    response = rag_chain.invoke(user_input)
    return response


@app.route("/")
def hello():
    return "Connection Established"

# Route for chat interaction
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("user_input")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # Generate response from LLM
    bot_response = generate_response(user_input)
    
    return jsonify({"response": bot_response})

# Route to clear chat history (just a placeholder for compatibility)
@app.route("/clear", methods=["POST"])
def clear_chat():
    # You can implement any session clearing logic if needed
    return jsonify({"message": "Chat cleared"})


if __name__ == "__main__":
    app.run(debug=True)

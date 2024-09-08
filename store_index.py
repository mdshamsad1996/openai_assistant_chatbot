from langchain_pinecone import PineconeVectorStore
from src.helper import create_documents
from langchain.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()


os.environ['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ['PINECONE_API_KEY']= PINECONE_API_KEY

index_name ="pdf-program-index"
embedding_model = OpenAIEmbeddings()

# pc = pinecone(api_key=PINECONE_API_KEY)
documents = create_documents()

# if index_name not in pc.list_indexes().names():

#     pinecone.create_index(index_name, dimension=1536)

# vector_store = PineconeVectorStore.from_documents(documents, embedding_model, index_name = index_name)



vector_store = PineconeVectorStore(embedding = embedding_model, index_name = index_name)
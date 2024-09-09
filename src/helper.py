import os
from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document


def load_pdf_file(directory_folder):
    """Load pdf file from directory"""
    pdf_files = [os.path.join(directory_folder,file_name) for file_name in os.listdir(directory_folder) \
            if os.path.isfile(os.path.join(directory_folder,file_name))]
    
    return pdf_files



def load_pdf_content():

    """Load pdf content in dict format"""

    pdf_files = load_pdf_file("data")
    documents_dict = {}

    for pdf_file in pdf_files:
        loader = PyPDFLoader(pdf_file)
        documents = loader.load()

        doc_key = pdf_file.split("/")[1]
        documents_dict[doc_key] = documents

    return documents_dict


def create_documents():

    """Create a document"""

    documents_dict = load_pdf_content()
    documents = []

    for filename, docs in documents_dict.items():
        content = "".join([doc.page_content for doc in docs])

        documents.append(Document(page_content=content, metadata={"source": filename}))
        
    return documents
    
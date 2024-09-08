from langchain.retrievers import EnsembleRetriever
from langchain.retrievers import BM25Retriever
from store_index import vector_store, documents

bm25_retriever = BM25Retriever.from_documents(documents)

vectore_store_retriever = vector_store.as_retriever()

vectore_store_retriever.search_kwargs = {"k":1}
bm25_retriever.k = 1

ensemble_retriever = EnsembleRetriever(retrievers=[vectore_store_retriever, bm25_retriever], weights=[0.3, 0.7])

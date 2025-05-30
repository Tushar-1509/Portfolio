
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="memory_store", embedding_function=embedding)

def update_context(doc, metadata):
    vectorstore.add_texts([doc], metadatas=[metadata])

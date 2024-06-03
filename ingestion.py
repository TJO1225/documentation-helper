from dotenv import load_dotenv

load_dotenv()

import os
<<<<<<< HEAD

from langchain_community.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings


INDEX_NAME = "langchain-doc-index"
=======
from langchain.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone

from consts import INDEX_NAME

pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENVIRONMENT_REGION"],
)
>>>>>>> 41d2a9b09c7260fe6a37cc9d5eb62bdf15cc118a

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


<<<<<<< HEAD
def ingest_docs():
    loader = ReadTheDocsLoader(
        "langchain-docs/api.python.langchain.com/en/latest/chains",
        encoding="utf-8",  # Specify UTF-8 encoding
    )

    raw_documents = loader.load()
    print(f"loaded {len(raw_documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_documents)
=======
def ingest_docs() -> None:
    loader = ReadTheDocsLoader(path="langchain-docs/langchain.readthedocs.io/en/latest")
    raw_documents = loader.load()
    print(f"loaded {len(raw_documents) }documents")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=100, separators=["\n\n", "\n", " ", ""]
    )
    documents = text_splitter.split_documents(documents=raw_documents)
    print(f"Splitted into {len(documents)} chunks")

>>>>>>> 41d2a9b09c7260fe6a37cc9d5eb62bdf15cc118a
    for doc in documents:
        old_path = doc.metadata["source"]
        new_url = old_path.replace("langchain-docs", "https:/")
        doc.metadata.update({"source": new_url})

<<<<<<< HEAD
    print(f"Going to add {len(documents)} to Pinecone")
    PineconeVectorStore.from_documents(documents, embeddings, index_name=INDEX_NAME)
    print("****Loading to vectorstore done ***")
=======
    print(f"Going to insert {len(documents)} to Pinecone")
    embeddings = OpenAIEmbeddings()
    Pinecone.from_documents(documents, embeddings, index_name=INDEX_NAME)
    print("****** Added to Pinecone vectorstore vectors")
>>>>>>> 41d2a9b09c7260fe6a37cc9d5eb62bdf15cc118a


if __name__ == "__main__":
    ingest_docs()

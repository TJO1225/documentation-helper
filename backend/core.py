from dotenv import load_dotenv
<<<<<<< HEAD
=======

load_dotenv()

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

import os
from typing import Any, Dict, List
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores.pinecone import Pinecone as PineconeLangChain
from pinecone import Pinecone
>>>>>>> 41d2a9b09c7260fe6a37cc9d5eb62bdf15cc118a

load_dotenv()

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from typing import Any, Dict, List
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_pinecone import PineconeVectorStore

<<<<<<< HEAD
=======
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
>>>>>>> 41d2a9b09c7260fe6a37cc9d5eb62bdf15cc118a

INDEX_NAME = "langchain-doc-index"


def run_llm(query: str, chat_history: List[Dict[str, Any]] = []):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
<<<<<<< HEAD
    docsearch = PineconeVectorStore(embedding=embeddings, index_name=INDEX_NAME)

=======
    docsearch = PineconeLangChain.from_existing_index(
        embedding=embeddings,
        index_name=INDEX_NAME,
    )
>>>>>>> 41d2a9b09c7260fe6a37cc9d5eb62bdf15cc118a
    chat = ChatOpenAI(
        verbose=True,
        temperature=0,
    )

    qa = ConversationalRetrievalChain.from_llm(
        llm=chat, retriever=docsearch.as_retriever(), return_source_documents=True
    )
    return qa.invoke({"question": query, "chat_history": chat_history})
<<<<<<< HEAD


if __name__ == "__main__":
    print(run_llm(query="What is Langchain?"))
=======
>>>>>>> 41d2a9b09c7260fe6a37cc9d5eb62bdf15cc118a

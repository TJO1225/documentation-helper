from typing import Set

from backend.core import run_llm
import streamlit as st
from streamlit_chat import message
<<<<<<< HEAD


def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string


st.header("LangChain🦜🔗 Udemy Course- Helper Bot")
if (
    "chat_answers_history" not in st.session_state
    and "user_prompt_history" not in st.session_state
    and "chat_history" not in st.session_state
):
    st.session_state["chat_answers_history"] = []
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_history"] = []


prompt = st.text_input("Prompt", placeholder="Enter your message here...") or st.button(
    "Submit"
)

if prompt:
    with st.spinner("Generating response..."):
        generated_response = run_llm(
            query=prompt, chat_history=st.session_state["chat_history"]
        )

        sources = set(
            [doc.metadata["source"] for doc in generated_response["source_documents"]]
        )
        formatted_response = (
            f"{generated_response['answer']} \n\n {create_sources_string(sources)}"
        )

        st.session_state.chat_history.append((prompt, generated_response["answer"]))
        st.session_state.user_prompt_history.append(prompt)
        st.session_state.chat_answers_history.append(formatted_response)

=======

st.header("LangChain Udemy Course- Documentation Helper Bot")


prompt = st.text_input("Prompt", placeholder="Enter your prompt here..")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []


def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string


if prompt:
    with st.spinner("Generating response.."):
        generated_response = run_llm(query=prompt)
        sources = set(
            [doc.metadata["source"] for doc in generated_response["source_documents"]]
        )

        formatted_response = (
            f"{generated_response['result']} \n\n {create_sources_string(sources)}"
        )

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)

>>>>>>> 41d2a9b09c7260fe6a37cc9d5eb62bdf15cc118a
if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
<<<<<<< HEAD
        message(
            user_query,
            is_user=True,
        )
=======
        message(user_query, is_user=True)
>>>>>>> 41d2a9b09c7260fe6a37cc9d5eb62bdf15cc118a
        message(generated_response)

"""Ask a question to the notion database."""
import faiss
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
import pickle

st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

#parser = argparse.ArgumentParser(description='Ask a question to the notion DB.')
#parser.add_argument('question', type=str, help='The question to ask the notion DB')
#args = parser.parse_args()

# Load the LangChain.
def search_and_answer(message: str) -> str:
    index = faiss.read_index("docs.index")

    with open("faiss_store.pkl", "rb") as f:
        store = pickle.load(f)

    store.index = index
    chain = RetrievalQAWithSourcesChain.from_chain_type(llm=ChatOpenAI(temperature=0), retriever=store.as_retriever())
    result = chain({"question": str(prompt)})
    answer = str(result['answer'])
    return answer

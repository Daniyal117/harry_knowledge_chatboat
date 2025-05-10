import streamlit as st
from query_engine import query_book  # Import your query function

# 🎨 Set Streamlit Page Configuration
st.set_page_config(page_title="Harry Potter Chatbot", layout="wide")

# 🏠 App Title
st.title("🧙‍♂️ Harry Potter Knowledge Chatbot")
st.write("Ask anything about the wizarding world! ⚡")

# 🛠️ Initialize Session State for Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 📌 Display Chat History
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(chat["query"])  # Display user query
    with st.chat_message("assistant"):
        st.markdown(chat["response"])  # Display bot response

# ✨ User Input
query_text = st.chat_input("Ask your question...")

# 🚀 Process the Query
if query_text:
    with st.chat_message("user"):
        st.markdown(query_text)  # Show user input

    with st.spinner("Thinking... 🧠"):
        relevant_text = query_book(query_text)  # Query the system

    with st.chat_message("assistant"):
        st.markdown(relevant_text)  # Show AI response

    # ✅ Store conversation history
    st.session_state.chat_history.append({"query": query_text, "response": relevant_text})



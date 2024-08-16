import streamlit as st
from llm_chains import load_normal_chain, chatChain
from langchain.memory import StreamlitChatMessageHistory


def load_chain(chat_history):
    return load_normal_chain(chat_history)

def clear_input_field():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""

def set_send_input():
    st.session_state.send_input = True
    clear_input_field()

def main():
    st.title("MindSpring")
    chat_container = st.container()

    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        st.session_state.user_question = ""

    # Ensure StreamlitChatMessageHistory is correctly initialized
    chat_history = StreamlitChatMessageHistory(key="history")
    llm_chain = load_chain(chat_history)

    user_input = st.text_input("Type your message here", key="user_input", on_change=set_send_input)
    send_button = st.button("Send", key="send_button")

    if send_button or st.session_state.send_input:
        if st.session_state.user_question !="":

            with chat_container:
                llm_response = llm_chain.run(st.session_state.user_question)
                st.session_state.user_question=""

            # Clear input field and reset send_input state
            st.session_state.user_question = ""

    if chat_history.messages != []:
            with chat_container:
                st.write("Chat History:")
                for message in chat_history.messages:
                  st.chat_message("message.type").write(message.content)

if __name__ == "__main__":
    main()

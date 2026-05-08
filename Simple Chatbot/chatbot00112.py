import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv(override=True)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful, smart, and friendly AI assistant. "
            "Answer the user's questions clearly and accurately. "
            "Be concise but thorough. "
            "If you don't know something, say so honestly. "
            "Support markdown formatting in your responses.",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{user_input}"),
    ]
)

llm = ChatGroq(model="llama-3.3-70b-versatile", GROQ_API_KEY=GROQ_API_KEY)

parser = StrOutputParser()

chain = template | llm | parser


def get_batman_response(user_input: str, chat_history: list) -> str:
    response = chain.invoke(
        {
            "user_input": user_input,
            "chat_history": chat_history,
        }
    )
    return response


st.set_page_config(page_title="AI Chat Assistant")

st.markdown(
    """
    <style>
        body { background-color: #0a0a0a; }
        .stApp { background-color: #0d0d0d; }
        .chat-box {
            background: #111;
            border: 1px solid #333;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 10px;
        }
        .user-msg {
            background: #1a1a2e;
            color: #c9d1d9;
            padding: 10px 14px;
            border-radius: 10px 10px 2px 10px;
            margin: 6px 0;
            text-align: right;
        }
        .batman-msg {
            background: #1c1c1c;
            color: #e0c060;
            border-left: 3px solid #e0c060;
            padding: 10px 14px;
            border-radius: 2px 10px 10px 10px;
            margin: 6px 0;
        }
        .batman-label { font-size: 11px; color: #888; margin-bottom: 2px; }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown("## AI Chat Assistant")
st.markdown("*Powered by Groq — Ask me anything!*")
st.divider()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "display_history" not in st.session_state:
    st.session_state.display_history = []

for role, message in st.session_state.display_history:
    if role == "user":
        st.markdown(
            f"""
            <div class="chat-box">
                <div class="batman-label">You</div>
                <div class="user-msg">{message}</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="chat-box">
                <div class="batman-label">Batman</div>
                <div class="batman-msg">{message}</div>
            </div>
        """,
            unsafe_allow_html=True,
        )

col1, col2 = st.columns([5, 1])

with col1:
    user_input = st.text_input(
        label="",
        placeholder="Speak to the Dark Knight...",
        label_visibility="collapsed",
        key="input_box",
    )
with col2:
    send = st.button("Send", use_container_width=True)

if send and user_input.strip():

    with st.spinner("Ai is watching..."):
        bot_reply = get_batman_response(
            user_input=user_input, chat_history=st.session_state.chat_history
        )

    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.session_state.chat_history.append(AIMessage(content=bot_reply))

    st.session_state.display_history.append(("user", user_input))
    st.session_state.display_history.append(("Ai", bot_reply))

    st.rerun()

if st.session_state.display_history:
    st.divider()
    if st.button("Clear Conversation"):
        st.session_state.chat_history = []
        st.session_state.display_history = []
        st.rerun()

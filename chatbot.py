import os
import streamlit as st
import requests

# ==========================================================
# 🔐 GROQ API KEY (FREE TIER, NO BILLING)
# ==========================================================
GROQ_API_KEY = "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"

if not GROQ_API_KEY:
    st.error("❌ Set GROQ_API_KEY as environment variable")
    st.stop()

# ==========================================================
# 📂 KT DOC
# ==========================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KT_DOC_PATH = os.path.join(BASE_DIR, "kt_doc.txt")

if not os.path.exists(KT_DOC_PATH):
    st.error("❌ kt_doc.txt not found")
    st.stop()

with open(KT_DOC_PATH, "r", encoding="utf-8") as f:
    KT_CONTENT = f.read()

# ==========================================================
# 🧠 KT PROMPT
# ==========================================================
KT_SYSTEM_PROMPT = """
You are a Knowledge Transfer (KT) Giver.

Explain step by step.
Assume the user is new.
Use examples.
Mention common mistakes.
Be honest if info is missing.
"""

# ==========================================================
# 🤖 CHAT FUNCTION (GROQ)
# ==========================================================
def ask_kt_bot(question: str) -> str:
    prompt = f"""
{KT_SYSTEM_PROMPT}

KT Documentation:
{KT_CONTENT}

User Question:
{question}
"""

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.3-70b-versatile",  # Updated model
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3
            },
            timeout=60
        )

        data = response.json()

        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        elif "error" in data:
            return f"⚠ API Error: {data['error']}"
        else:
            return f"⚠ Unexpected API response: {data}"

    except requests.exceptions.RequestException as e:
        return f"⚠ Request failed: {e}"

# ==========================================================
# 🎨 UI
# ==========================================================
st.set_page_config(page_title="KT Chatbot")
st.title("📘 KT Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

question = st.chat_input("Ask your KT question...")

if question:
    st.session_state.chat_history.append(
        {"role": "user", "content": question}
    )

    with st.spinner("KT giver thinking..."):
        answer = ask_kt_bot(question)

    st.session_state.chat_history.append(
        {"role": "assistant", "content": answer}
    )

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
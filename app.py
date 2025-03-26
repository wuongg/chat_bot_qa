import torch
from Faiss import retrieve_text_faiss
from model import generate_answer_fast
import streamlit as st
import time

# Cấu hình giao diện
st.set_page_config(page_title="Chatbot Luật Giao Thông 🚦", page_icon="🚗")

# Hiển thị tiêu đề
st.markdown(
    "<h1 style='text-align: center; color: #ff5733;'>🚦 Chatbot Luật Giao Thông</h1>",
    unsafe_allow_html=True
)

# Khởi tạo lịch sử chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị lịch sử chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Nhận đầu vào từ người dùng
if prompt := st.chat_input("Nhập câu hỏi của bạn tại đây..."):
    # Hiển thị tin nhắn người dùng
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"**🧑‍💼 Bạn:** {prompt}")

    # Xử lý phản hồi chatbot
    with st.chat_message("assistant"):
        with st.spinner("🤖 Đang xử lý..."):
            context = retrieve_text_faiss(prompt)
            answer = generate_answer_fast(prompt, context)

        # Hiệu ứng gõ chữ
        full_response = ""
        response_container = st.empty()
        for char in answer:
            full_response += char
            time.sleep(0.02)  # Giả lập thời gian gõ chữ
            response_container.markdown(f"**🤖 Chatbot:** {full_response}")

    # Lưu phản hồi vào lịch sử
    st.session_state.messages.append({"role": "assistant", "content": answer})

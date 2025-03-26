# Sử dụng Python 3.9 làm base image
FROM python:3.12

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy toàn bộ mã nguồn vào container
COPY . .

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Cài đặt wget để tải mô hình
RUN apt-get update && apt-get install -y wget

RUN wget -O tinyllama-1.1b-chat-v1.0.Q8_0.gguf "https://github.com/wuongg/chat_bot_qa/releases/download/v1.0.0/tinyllama-1.1b-chat-v1.0.Q8_0.gguf"

RUN rm tinyllama-1.1b-chat-v1.0.Q8_0.gguf

# Mở cổng 8501 (mặc định của Streamlit)
EXPOSE 8501

# Chạy ứng dụng
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

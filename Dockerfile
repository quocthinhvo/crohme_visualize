FROM python:3.10

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 9000

# Chạy ứng dụng
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
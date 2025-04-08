FROM python:3.9-slim
RUN apt update && apt install -y curl
COPY app.py .
RUN pip install flask
CMD ["python", "app.py"]

FROM python:3.11-slim
WORKDIR /app
COPY writer.py .
RUN pip install redis
CMD ["python", "writer.py"]
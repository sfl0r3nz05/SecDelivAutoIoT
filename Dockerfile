FROM python:alpine3.17
RUN pip install flask
WORKDIR /app
COPY app.py .
ENTRYPOINT ["python", "app.py"]
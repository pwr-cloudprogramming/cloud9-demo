FROM python:3.10-alpine

WORKDIR /app

RUN pip install flask flask_cors

COPY src/ /app

ENTRYPOINT ["python3"]
CMD ["app.py"]

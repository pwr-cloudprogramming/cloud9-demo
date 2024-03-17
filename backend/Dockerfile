FROM python:3.10-alpine

WORKDIR /app

RUN pip install flask flask_cors

COPY src/ .

ENTRYPOINT ["python3"]
CMD ["app.py"]

FROM python:3.10-alpine

WORKDIR /app

COPY src/ .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]

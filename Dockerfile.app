FROM python:3.9-slim

WORKDIR /app

RUN apt update -y && apt install -y build-essential libpq-dev

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

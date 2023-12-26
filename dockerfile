FROM python:3.11.7

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    python3-pip

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt --no-cache-dir
RUN pip install pandas --no-cache-dir

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

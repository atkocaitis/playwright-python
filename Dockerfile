FROM python:3.11

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && playwright install --with-deps

COPY . /app

CMD ["pytest", "tests", "-n 3"]
FROM python:3.10-slim

WORKDIR /betting

COPY ./requirements.txt ./
COPY ./alembic.ini ./

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY ./app /betting/app

CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV CONFIG_PATH=config.json

COPY config.json /app/config.json
COPY ./app /app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
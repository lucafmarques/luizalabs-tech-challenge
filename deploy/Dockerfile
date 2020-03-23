FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7


COPY app/config.json /app/config.json
COPY app /app

ENV CONFIG_PATH=${CONFIG_FILE:-config.json}

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends libc-dev

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "dom_checker/main.py" ]
FROM python:alpine
RUN apk add --update --no-cache libc-dev gcc libxslt-dev
WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt
COPY app /app
ENTRYPOINT ["./vinmonopolet.py"]

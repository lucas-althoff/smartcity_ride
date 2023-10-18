FROM python:3.10.11

WORKDIR /code
COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENV PYTHONUNBUFFERED True
COPY backend /code/backend
COPY entrypoint.sh /code/entrypoint.sh

RUN chmod +x /code/entrypoint.sh

CMD ["/code/entrypoint.sh"]

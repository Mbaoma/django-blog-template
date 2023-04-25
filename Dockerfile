FROM python:alpine3.17

WORKDIR /app

COPY . ./app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r ./app/requirements.txt

CMD ["python", "./app/tutorial/manage.py", "runserver"] 
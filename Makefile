install:
    pip install -r requirements.txt

migrate:
    python manage.py migrate

run:
    docker compose up



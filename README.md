# Project Heritage API

[![Travis CI][build-badge]][build]
[![GNU][license-badge]][license]

---

> A server for Project Heritage application

## Prerequisites

- Python v 3.6
- Postgresql
- Python virtaulenv
- pip
- graphql
- heroku

## Installation

```bash
create virtualenv
source venv/bin/activate
pip install -r requirements.txt
mv example.env .env
python manage.py migrate
python manage.py runserver
```

## Database Schema

<img src="project-heritage-db.png">

## Deployment

> We are using heroku to deploy

```bash
heroku login
heroku create demo-bootcamp
heroku addons:create heroku-postgresql:hobby-dev
heroku run python manage.py migrate
heroku config:set DJANGO_SECRET_KEY=`./manage.py generate_secret_key`
heroku run python manage.py migrate

```

## Author

> [Dennis Kamau](mailto:denniskamau3@gmail.com)

### Contributors

> [Victor Kariuki](mailto:karizvic@gmail.com)


## License

> MIT License

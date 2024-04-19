# Auth Otomari API


### Project Description:

Welcome to my project! This README provides an overview of the functionality
and features available in my application.

### Features

1. **User Registration:** Users can sign up for an account on our platform by
providing necessary details such as email and password.
2. **Two-Factor Authentication (2FA):** To enhance security, I've implemented
two-factor authentication, requiring users to provide a second form of
verification, typically a code sent to their email, in
addition to their password, during login.
3. **User Account Management:** Once registered, users have the ability to manage
their accounts.
4. **Admin Profile Editing:** Administrators have the authority to modify user
   profiles as needed.

### Technologies Used:

[![pre-commit](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3111/)
[![pre-commit](https://img.shields.io/badge/Django-3.2-092E20?logo=django&logoColor=white)](https://docs.djangoproject.com/en/4.2/releases/3.2/)
[![pre-commit](https://img.shields.io/badge/Django_REST_framework-3.12-800000?logo=djangorestramework&logoColor=white)](https://www.django-rest-framework.org/community/3.12-announcement/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![celery](https://img.shields.io/badge/celery-5.3.6-37814A?logo=celery&logoColor=white)](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)
[![redis](https://img.shields.io/badge/redis-5.0.3-DC382D?logo=redis&logoColor=white)](https://redis-py.readthedocs.io/en/stable/)

### Getting Started:

1. **Installation:** Clone the repository to your local machine.
2. **Environment Setup:** In the root of the project, create a .env file. You can use
the provided .env.example file as a template. Make sure to fill in the
necessary environment variables with your configuration.
3. **Docker Compose:** Navigate to the project directory and run below commands to launch the application using Docker Compose.

```bash
docker compose build
docker compose up
```

4. **Accessing the Application:** Once Docker Compose has finished setting up the
environment, you can access the application by visiting http://localhost/api/v1/

### API Usage:

You can send requests to the API endpoints at https://auth.otomari.ru/api/v1. Follow the API
documentation for available endpoints and parameters.

### API documentation:

https://auth.otomari.ru/redoc/

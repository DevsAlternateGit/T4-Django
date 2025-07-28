# Django Commands

This document provides a quick reference for common Django commands.

## Check Django version  <font color="red">(Most important check before running any command)</font>

```bash
python -m django --version
```

## To create a new Django project

```bash
python -m django startproject project_name
```

## To create a new Django app

Remember to run this command inside your Django project directory.

```bash
python manage.py startapp app_name
```

Also make sure to add the app to your `INSTALLED_APPS` in `settings.py`.

## To run the Django development server

```bash
python manage.py runserver
```

## To apply migrations

```bash
python manage.py migrate
```

## To create migrations for your models

```bash
python manage.py makemigrations
```

## To create a superuser

```bash
python manage.py createsuperuser
```

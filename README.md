Description

Это веб-приложение онлайн-каталог для библиотеки, где пользователи могут просматривать 
доступные книги и управлять своими учетными записями.

-----------------------------------------------------------------------------------------

Dependencies

poetry 1.8.3

python 3.12

-----------------------------------------------------------------------------------------

Clone repository

git clone https://github.com/MikhailKaz/Locallibrary.git

-----------------------------------------------------------------------------------------

Create enviroment

install python3
 
python -m venv venv

source venv/bin/activate

-----------------------------------------------------------------------------------------

Install Dependencies

1. Install Poetry

pip install pipx

pipx install poetry

poetry init

2. Install Django and Django Rest Framework

poetry add django djangorestframework

-----------------------------------------------------------------------------------------

Start server 

python3 manage.py runserver

-----------------------------------------------------------------------------------------

Migrations

python3 manage.py makemigrations

python3 manage.py migrate

-----------------------------------------------------------------------------------------



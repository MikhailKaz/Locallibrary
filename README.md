# LocalLibrary

Это веб-приложение онлайн-каталог для библиотеки, где пользователи могут просматривать 
доступные книги и управлять своими учетными записями.

## Dependencies

- `poetry 1.8.3`
- `python 3.12`

# Clone repository

```bash
git clone https://github.com/MikhailKaz/Locallibrary.git
```


## Install Dependencies

```bash
pip install poetry==1.8.3
poetry install
```

## Start server 

```bash
poetry run python3 manage.py runserver
```

## Migrations

```bash
poetry run python3 manage.py makemigrations
poetry run python3 manage.py migrate
```

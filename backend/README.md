# Backend

## MakeMigrations

```shell
docker-compose exec backend python manage.py makemigrations
```

## Install Packages

```shell
docker-compose exec backend pipenv install <package name>
```

パッケージ追加後に

```shell
docker-compose up --build
```
または
```shell
docker-compose build
```
でrebuildしてください．

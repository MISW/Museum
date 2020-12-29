# misw-museum

みすミュージアム。サークル内の個人成果物を公開するWebアプリケーションです。

## Install

- docker
- docker-compose

## Setup

### 1. Clone

```bash
$ git clone https://github.com/MISW/misw-museum.git
$ cd misw-meseum
```

### 2. Edit `.env` from `.env.example`

### 3. docker build

```bash
$ docker-compose build
```

## Usage

### Start container

```bash
$ docker-compose up -d
```

### Stop container

```bash
$ docker-compose down
```

### Logging

```bash
$ docker-compose logs -f
```

### Migration

```bash
$ docker exec misw-museum_web python manage.py migrate
```

### Create superuser

```bash
$ docker exec misw-museum_web python manage.py createsuperuser
```
もし，
```
Superuser creation skipped due to not running in a TTY. You can run `manage.py createsuperuser` in your project to create one manually.
```
とエラーがでる場合は
```
$ docker exec -it misw-museum_web bash
root@************:/app# python manage.py createsuperuser
root@************:/app# exit
```
でお願いします．

## Git setup

```bash
$ git checkout -b <my branch name>
```

## Git usage

```bash
$ git add -A
$ git commit -m <my commit message>
$ git pull origin develop
$ git push origin <my branch name>
```

## Documentation

### モデル設計

- [/docs/specification.md](./docs/specification.md)

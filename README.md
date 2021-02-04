# MISW Museum

みすミュージアム。サークル内の個人成果物を公開するWebアプリケーションです。

## Install

- docker
- docker-compose

## Setup

### 1. Clone

```bash
git clone https://github.com/MISW/Museum.git
cd misw-meseum
```

### 2. Edit `dev.env` from `dev.env.example`

### 3. docker build

```bash
docker-compose build
```

## Usage

### Start container

```bash
docker-compose up -d
```

### Stop container

```bash
docker-compose down
```

### Logging

```bash
docker-compose logs -f
```

### Migrate

```bash
docker-compose exec backend python manage.py migrate
```

### Create superuser

```bash
docker-compose exec backend python manage.py createsuperuser
```

## Git setup

```bash
git checkout -b <my branch name> develop
```

## Git usage

```bash
git add -A
git commit -m <my commit message>
git pull origin develop
git push origin <my branch name>
```

## Documentation

### モデル設計

- [/docs/specification.md](./docs/specification.md)


## For Interal developers

[dev.env for internal developers](https://misw.kibe.la/notes/4248)

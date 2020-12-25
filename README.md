# misw-gamecenter

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


## Document

`docs/` 下に置いていきたい．
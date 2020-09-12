# misw-gamecenter

## Install

```bash
$ pip install pipenv
$ pipenv install
```

## Usage

```bash
$ docker-compose up -d
($ docker-compose up -d --build)
$ docker exec misw-gamecenter_web_1 python manage.py migrate
```
以下のコマンドでコンテナ内に入ることができますが、入ったままで（root権限のままで）`git`を使わないでください。
permission関係で`git`が壊れます。
```bash
$ docker exec -it misw-gamecenter_web_1 bash
```

## How to show logs

```bash
$ docker-compose logs
```
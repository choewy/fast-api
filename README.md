# FastAPI

## Description

- OS : Ubuntu 20.04
- python-version: 3.10

## venv

### Create venv

```
$ python3.10 -m venv .venv
```

### Activate .venv

```
$ pwd
{ .venv's ROOT }

$ source { .venv's ROOT }/bin/activate
```

## Application

### Packages Install

```
$ pip install -r requirements.txt
```

### Run Application

```
$ uvicorn main:app --reload --host=0.0.0.0 --port=5000
```

### API Document

- [http://localhost:5000/docs](http://localhost:5000/docs)
- [http://localhost:5000/redoc](http://localhost:5000/redoc)

## Others

### Create requirements.txt

```
$ pip freeze > requirements.txt
```

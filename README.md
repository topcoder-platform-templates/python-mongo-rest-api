# Python Mongodb Starter Pack

## Prerequisites
1. Python 3.x
2. Mongodb
3. docker & docker-compose

## Configuration

Located under the yaml file.

- **MONGODB_URL** Mongodb connection url

the config value can be set through environment variable **MONGODB_URL**.

## Local Running

Go to app folder.

Install requirements:

```bash
pip install -r requirements.txt
```

Run application

```bash
python app.py
```

or override with environment variable

```bash
MONGODB_URL=xxx python app.py
```


## Docker compose Running

Run:
```bash
docker-compose up --build
```


## Test and Verification

Import the postman collection in docs folder to test and verify.
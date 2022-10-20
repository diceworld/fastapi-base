Fast API base
===============

## 1. 개요

1. 기능 정의
    - Fast API 앱 개발을 위한 기본 구조
    - https://github.com/teamhide/fastapi-boilerplate 참고

2. 기술 스택
    - Python 3.9.5
    - fastapi 0.85.0
    - uvicorn 0.18.3
    - SQLAlchemy 1.4.41

## 2. 설치 및 설정

### 2 - 1. mysql 설정

1. 도커를 이용한 mysql 설치
    - docker pull mysql:5.7.20
    - docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=db_password -d -p 3306:3306 mysql:latest

2. 스키마 생성
    - CREATE SCHEMA `schema` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;

3. 유저 생성
    - grant all privileges on schema.* to 'db_user'@'%' identified by 'db_password';

4. 테이블 생성
    - alembic revision --autogenerate -m "init database"
    - alembic upgrade head

### 2 - 2. python 설정

1. poetry 설치
    - pip install poetry

2. package 설치
    - poetry install

3. 실행
    - python main.py --env:prod

4. API 문서
    - http://127.0.0.1:8000/docs
    - http://127.0.0.1:8000/redoc

## 3. 참고

1. FastAPI 공식 사이트
    - https://fastapi.tiangolo.com/ko/

2. FastAPI boilerplate
    - https://github.com/teamhide/fastapi-boilerplate

3. FastAPI SQLAlchemy Session
    - https://medium.com/wantedjobs/fastapi%EC%97%90%EC%84%9C-sqlalchemy-session-다루는-방법-118150b87efa

4. Python Poetry
    - https://python-poetry.org/
    - https://chacha95.github.io/2021-03-27-python7/

5. alembic migration
    - https://blog.neonkid.xyz/m/257

# Airbnb Clone

Cloning Airbnb with Pyton, Django, Tailwind

## Create git

1. github에 repository 생성
2. 생성한 repository url 복사 ex) https://github.com/kanakan12/airbnb-clone
3. 개발 경로로 이동 ex) vscode - airbnb-clone
4. $ git init
5. $ git remote add origin [url]
6. $ git add .
7. $ git commit -m "커밋 내용"
8. touch로 파일 생성 가능 ex) $ touch README.md / $ touch .gitignore
9. $ git push origin master // github 주소에 push

## pipenv isntall

1. $ brew install pipenv // 가상환경 설치 ex) node.js의 npm같은 것

## evn setting

1. $ pipenv --three // python3 버전 사용
2. $ pipenv shell // python 가상환경 실행

## Django, flake8, black install

1. $ pipenv install Django==[version] // version: 2.2.5 사용 중
2. $ pipenv install flake8 // Linter: 에러가 발생하는 부분을 감지
3. $ pipenv install black // formatter: format code

## run python server

1. $ python [file] runserver // file: manage.py 사용 중
2. $ python [file] migrate // file: manage.py 사용 중 // 하나의 상태에서 다른 상태로, 다른 데이터 유형으로 바꿈
3. $ python [file] createsuperuser // file: manage.py 사용 중 // 관리자용 계정 생성

## django-admin startapp

1. $ django-admin startapp [file] // file: 복수형으로 사용할 것 ex) users, reviews
2. $ rm -rf [file] // file: 삭제할 file name

## python migration

1. $ python [file] makemigrations // migration 생성
2. $ python [file] migrate // file: manage.py 사용 중 // 하나의 상태에서 다른 상태로, 다른 데이터 유형으로 바꿈

## django core

1. $ django-admin startapp core

## django country

1. $ pipenv install django-countries
2. $ add django_countries to 'INSTALLED_APPS' // THIRD_PARTY_APPS

## django translation

1. $ django-admin makemessages --locale=es // 번역하기 위한 언어 setting ex) es=spanish
2. $ dajngo-admin compilemessages

## aws 

1. $ pipenv install awsebcli --dev
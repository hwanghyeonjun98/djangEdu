# 2. Django 프로젝트 만들기

## 2-1 프로젝트 생성
1. 터미널에서 <code>$ django-admin startproject [프로젝트명] [프로젝트 생성 경로]</code> 실행<br/>
<small>프로젝트 경로 이동 후 실행 또는 프로젝트 생성 경로에 자세히</small>
2. <code>$ python manage.py runserver</code> 실행(django 서버 실행)
프로젝트 생성 후 아래 디렉토리 생성
<pre>
ROOT
│  db.sqlite3
│  manage.py
│  README.md
│
├─firstdjango
│  │  asgi.py  # 서버 배표관련
│  │  settings.py  # 프로젝트 설정
│  │  urls.py  # URL 매핑 관련
│  │  wsgi.py  # 서버 배표관련
│  │  __init__.py
│  │
│  └─__pycache__
│          settings.cpython-39.pyc
│          urls.cpython-39.pyc
│          wsgi.cpython-39.pyc
│          __init__.cpython-39.pyc
</pre>

## 2-2 앱 생성
1. 터미널에서 <code>$ django-admin startapp [앱이름]</code> 실행
실행 후 디텍토리
<pre>
ROOT
│  db.sqlite3
│  manage.py
│  README.md
│
├─first
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  tests.py
│  │  views.py
│  │  __init__.py
│  │
│  ├─migrations
│  │  │  __init__.py
│  │  │
│  │  └─__pycache__
│  │          __init__.cpython-39.pyc
│  │
│  └─__pycache__
│          admin.cpython-39.pyc
│          apps.cpython-39.pyc
│          models.cpython-39.pyc
│          urls.cpython-39.pyc
│          views.cpython-39.pyc
│          __init__.cpython-39.pyc
│
├─firstdjango
│  │  asgi.py
│  │  settings.py
│  │  urls.py
│  │  wsgi.py
│  │  __init__.py
│  │
│  └─__pycache__
│          settings.cpython-39.pyc
│          urls.cpython-39.pyc
│          wsgi.cpython-39.pyc
│          __init__.cpython-39.pyc
</pre>
# 4. URL 매핑 하기

- URL 매핑과 매핑한 URL을 사용하기 위한 template 설정

## 4-1 여러 페이지 URL 매핑

1. views.py에 웹페이지를 띄우기 위해 아래 코드 생성
	- 함수를 여러개 만들어 주면 된다.

```python
from django.http import HttpResponse


def index(req):
	return HttpResponse('Hello World')


def select(req):
	return HttpResponse('Hello World')


def result(req):
	return HttpResponse('Hello World')
```

2. APP 디렉토리에 urls.py 생성 아래 예시 처럼 작성
	- <code>path(매핑 URL, views, name=[화면이름])</code>
	- url 매핑을 효율적으로 관리하기 위해 urls.py를 생성해서 관리 해도됨
	- url 매핑에 path variable이 필요할 경우 <code>path('select/<int:year>', view, name=[view_name])</code>으로 작성
	- url 매핑에 정규식이 필요한 경우 <code>re_path(r'^select/(?P<year>[0-9]/$', view, name=[view_name])</code>으로
	  작성

```python
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index')
	, path('select/', views.select, name='select')
	, path('result/', views.result, name='result')
]
```

3. APP 디렉토리에 매핑한 url을 사용 하기 위해 프로젝트 디렉토리에 있는 urls.py 변경
	- 다른 곳에 url 매핑을 가져오기 위해 urls import에 include추가
	- <code>path())</code> 메소드에 <code>path(''[매핑 URL], include([url 매핑 파일]))</code>으로 작성

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('first.urls')),
	path('admin/', admin.site.urls)
]
```

### 4-2 template 만들기

1. app 디렉토리에 templates 디렉토리 만들기
2. templates 디렉토리에 html 문서 생성
3. views.py에서 원하는 페이지에 <code>from django.template import loader</code> 후 <br/> <code>
   loader.get_template([템플릿경로,템플릿파일])</code> 추가
	- context는 html에 변수로 넘기기 위해 작성 딕셔너리 타입으로 넘김
	- return 문에는 html을 랜더링 하기 위해 render 메소드를 사용, context와 request를 같이 넘겨준다.

```python
from django.http import HttpResponse
from django.template import loader


def index(req):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context, req))
```

4. templates에 생성한 html body안에 아래와 같이 작성

- Django에서는 a tag 사용 시 <br/>
  ```html
   <a href="url">링크</a>
  ```
  아닌<br/>
  ```html
  <a href="{% url 'url_name' %}">랑크</a>
  ```
  혈식으로 작성

```html
<!doctype html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Document</title>
</head>
<body>
	<h1>메인페이지</h1>

	<a href="{% url 'select' %}">시작하기</a>
</body>
</html>
```

5. setting.py에서 INSTALLED_APPS 리스트에 실행할 APP 이름 추가
	- templates를 사용하기 위해 settings.py INSTALLED_APPS 리스트에 APP 디렉토리명 추가

```python
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	['app 이름'],  # 추가
]
```
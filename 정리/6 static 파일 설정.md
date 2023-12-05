# 5. static 파일 설정

1. settings.py에서 아래와 같은 내용을 추가한다.

```python
import os

# ...

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]
```

2. html 상단에 <code>{% load static %}</code> 추가 하고 img tag에 src에 예시처럼 작성
	- 반듯이 <code>{% load static %}</code>을 상단에 선언 해야 된다.
	- 이미지 파일 뿐만 아니라 css, js 파일도 같은 방식으로 작성

```html
{% load static %}
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
</head>
<body>
	<h1>메인페이지</h1>
	<img src="{% static 'first/sunrays-8283601_1280.jpg' %}" alt="sunrays-8283601_1280.jpg">
	<p>{{ cur_date }}</p>
	<p>{{ cur_date|date:'Y년 m월 d일 H시 i분 s초' }}</p>
	{# 변수를 쓰기위해서는 {{ }} 안에 context에 설정한 변수를 작성 #}
	{# 변수 뒤에 '|'를 붙이고 타입을 쓰면 포맷팅도 가능 #}

	<a href="{% url 'select' %}">시작하기</a>
</body>
</html>
```

### 추가 내용

- 레이아웃이 같고 일부분이 다르면 <code>{% block [블록 이름] %} {% endblock %}</code>을 사이를 통해 원하는 부분을 바꿀수 있다.
- block은 하나에 템플릿에 하나만 가능하다. 여러개를 할려면 block 대신 <code>{% include [불러올 html] %}</code>
	- 예시)
		- 영역 불러오기

		    ```html
			 {% load static %}
			 <!DOCTYPE html>
			 <html lang="ko">
			 <head>
				<meta charset="UTF-8">
				<title>로또번호</title>
				<link rel="stylesheet" href="{% static 'first/style.css' %}">
			 </head>
			 <body>
				{% block content %}
				{% endblock %}
			 </body>
			 </html>
			```
		- 내용 정의
		  ```html
		  {% extends 'first/base.html' %} {{ extends를 사용해 집어 넣기 원하는 파일 선택 }}
		  {% load static %}
		  {% block content %} {{ block content 시작 선언 }}
		  <h1>메인페이지</h1>
		  <img src="{% static 'first/sunrays-8283601_1280.jpg' %}" alt="sunrays-8283601_1280.jpg">
		  <p>{{ cur_date }}</p>
		  <p>{{ cur_date|date:'Y년 m월 d일 H시 i분 s초' }}</p>
		  
		  <a href="{% url 'select' %}">시작하기</a>
		  {% endblock %} {{ block content 끝 선언 }}
		  ```
from django.db import models


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField() # 긴문자열 저장

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	# num_stars = models.IntegerField() # 숫자형 자료 저장
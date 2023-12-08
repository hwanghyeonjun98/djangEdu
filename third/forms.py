from django.forms import ModelForm
from django import forms
from .models import Restaurant, Review
from django.utils.translation import gettext_lazy as _

REVIEW_PIONT = (
	('1', 1),
	('2', 2),
	('3', 3),
	('4', 4),
	('5', 5)
)


class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['point', 'comment', 'restaurant']
		labels = {
			'point': _('평점'),
			'comment': _('리뷰'),
		}
		help_texts = {
			'point': _('평점을 입력해주세요.'),
			'comment': _('리뷰를 입력해주세요.'),
		}
		widgets = {
			'restaurant': forms.HiddenInput(),
			'point': forms.Select(choices=REVIEW_PIONT),
			'comment': forms.Textarea()
		}


class RestaurantForm(ModelForm):
	class Meta:
		model = Restaurant
		fields = ['name', 'addr']
		labels = {
			'name': _('이름'),
			'addr': _('주소'),
		}
		help_texts = {
			'name': _('음식점 이름을 입력해주세요.'),
			'addr': _('음식점 주소를 입력해주세요.'),
		}
		error_messages = {
			'name': {'max_length': _('이름이 너무 깁니다. 30자 이내로 작성해주세요.')}
		}

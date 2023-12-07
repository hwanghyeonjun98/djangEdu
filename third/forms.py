from django.forms import ModelForm
from .models import Restaurant
from django.utils.translation import gettext_lazy as _


class RestaurantForm(ModelForm):
	class Meta:
		model = Restaurant
		fields = ['name', 'addr']
		labels = {
			'name': _('이름'),
			'addr': _('주소'),
		}
		help_texts={
			'name': _('음식점 이름을 입력해주세요.'),
			'addr': _('음식점 주소를 입력해주세요.'),
		}
		error_messages  = {
			'name' : {'max_length': _('이름이 너무 깁니다. 30자 이내로 작성해주세요.')}
		}

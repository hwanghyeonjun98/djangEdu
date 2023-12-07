from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from third.forms import RestaurantForm
from third.models import Restaurant


# Create your views here.
def list(req):
	rastaurants = Restaurant.objects.all().order_by('-id')
	paginator = Paginator(rastaurants, 5)

	page = req.GET.get('page')
	items = paginator.get_page(page)

	context = {
		'rastaurants': items
	}
	return render(req, 'third/list.html', context)


def create(req):
	if req.method == 'POST':
		form = RestaurantForm(req.POST)
		if form.is_valid():
			new_item = form.save()
		return HttpResponseRedirect('/third/list/')

	form = RestaurantForm()
	context = {
		'form': form
	}

	return render(req, 'third/create.html', context)


def update(req):
	if req.method == 'POST' and 'id' in req.POST:
		# item = Restaurant.objects.get(pk=req.POST.get('id'))
		item = get_object_or_404(Restaurant, pk=req.POST['id'])
		form = RestaurantForm(req.POST, instance=item)
		if form.is_valid():
			item = form.save()
	elif req.method == 'GET':
		# item = Restaurant.objects.get(pk=req.GET.get('id'))
		item = get_object_or_404(Restaurant, pk=req.GET['id'])
		form = RestaurantForm(instance=item)
		return render(req, 'third/update.html', {'form': form})

	return HttpResponseRedirect('/third/list/')


def detail(req):
	if 'id' in req.GET:
		item = get_object_or_404(Restaurant, pk=req.GET.get('id'))
		return render(req, 'third/detail.html', {'item': item})


def delete(req):
	if 'id' in req.GET:
		item = get_object_or_404(Restaurant, pk=req.GET.get('id'))
		item.delete()

	return HttpResponseRedirect('/third/list/')

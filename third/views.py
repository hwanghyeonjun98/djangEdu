from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from third.forms import RestaurantForm, ReviewForm
from third.models import Restaurant, Review
from django.db.models import Count, Avg


# Create your views here.
def list(req):
	rastaurants = Restaurant.objects.all().order_by('-id').annotate(reviews_count=Count('review')).annotate(point_avg=Avg('review__point'))
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


def detail(req, id):
	if id is not None:
		item = get_object_or_404(Restaurant, pk=id)
		reviews = Review.objects.filter(restaurant=item).all()
		return render(req, 'third/detail.html', {'item': item, 'reviews': reviews})


def delete(req):
	if 'id' in req.GET:
		item = get_object_or_404(Restaurant, pk=req.GET.get('id'))
		item.delete()

	return HttpResponseRedirect('/third/list/')


def review_create(req, restaurant_id):
	if req.method == 'POST':
		form = ReviewForm(req.POST)
		if form.is_valid():
			new_item = form.save()
		return redirect('restaurant-detail', id=restaurant_id)

	item = get_object_or_404(Restaurant, pk=restaurant_id)
	form = ReviewForm(initial={'restaurant': item})
	return render(req, 'third/review_create.html', {'form': form, 'item': item})


def review_delete(req, restaurant_id, review_id):
	item = get_object_or_404(Review, pk=review_id)
	item.delete()

	return redirect('restaurant-detail', id=restaurant_id)


def review_list(req):
	reviews = Review.objects.all().select_related().order_by('-created_at')
	paginator = Paginator(reviews, 10)

	page = req.GET.get('page')
	items = paginator.get_page(page)

	context = {
		'reviews': items,
		'test': reviews
	}

	return render(req, 'third/review_list.html', context)

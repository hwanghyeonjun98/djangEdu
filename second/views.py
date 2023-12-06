from django.shortcuts import render
from django.http import HttpResponseRedirect
from second.models import Post
from .forms import PostForm


# Create your views here.
def list(req):
	context = {
		'items': Post.objects.all()
	}
	return render(req, 'sencond/list.html', context)


def create(req):
	if req.method == 'POST':
		form = PostForm(req.POST)
		if form.is_valid():
			new_item = form.save()
		return HttpResponseRedirect('/second/list/')

	form = PostForm()
	return render(req, 'sencond/create.html', {'form': form})


def confirm(req):
	form = PostForm(req.POST)
	if form.is_valid():
		return render(req, 'sencond/confirm.html', {'form': form})
	return HttpResponseRedirect('/second/create/')

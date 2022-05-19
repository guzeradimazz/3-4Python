from re import template
from turtle import pos
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from matplotlib.style import context
from numpy import require
from yaml import load
from post.models import Post,Stream,Tag
from django.template import loader
from django.http import HttpResponse
from post.forms import NewPostForm
# Create your views here.

@login_required
def index(request):
    user = request.user
    posts = Stream.objects.filter(user=user)
    groups_ids = []
    for post in posts:
        groups_ids.append(post.post_id)
    post_items = Post.objects.filter(id__in=groups_ids).all().order_by('-posted')
    template = loader.get_template('index.html')
    context ={
        'post_items':post_items,
    }
    return HttpResponse(template.render(context,request))

@login_required
def NewPost(request):
    user = request.user.id
    tags_objs=[]

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tags_form = form.cleaned_data.get('tags')
            
            tags_list = list(tags_form.split(','))

            for tag in tags_list:
                t,created = Tag.objects.get_or_create(title=tag)
                tags_objs.append(t)
            p,created = Post.objects.get_or_create(picture=picture,caption=caption,user_id=user)
            p.tags.set(tags_objs)
            p.save()
            return redirect('index')
    else: 
        form = NewPostForm()
    context={
        'form':form,
    }
    return render(request,'newpost.html',context)

@login_required
def PostDetails(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	template = loader.get_template('post_details.html')

	context = {
		'post':post,
	}

	return HttpResponse(template.render(context, request))

@login_required
def tags(request,tag_slug):
    tag = get_object_or_404(Tag,slug=tag_slug)
    posts = Post.objects.filter(tags=tag).order_by('-posted')
    template = loader.get_template('tag.html')
    context={
        'posts':posts,
        'tag':tag,
    }
    return HttpResponse(template.render(context,request))
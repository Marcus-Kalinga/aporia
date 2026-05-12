from django.shortcuts import render, redirect
from.models import Post
from .forms import PostForm
def posts_view(request):
	if request.method=="POST":
		title=request.POST["title"]
		post_body=request.POST["aphorism"]
		Post.objects.create(title=title, post_body=post_body)
		return redirect(posts_view)
	else:	
		posts= Post.objects.all()
		return render(request, "posts/posts.html", {"posts":posts})
		
def posts_display(request):
	if request.method=="POST":
		#create a form object and to it pass the whole post dict
		#no need to create fields separately as above
		form=PostForm(request.POST)
		if form.is_valid():
			form.save() #if the entered data is valid, save to db?
			return redirect(posts_display)
	else:
		form= PostForm()
		posts= Post.objects.all()
		return render(request, "posts/posts.html", {
		                                        "forms":form,
		                                        "posts":posts
		                                        })			
# Create your views here.

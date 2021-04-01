from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    if request.method=='POST':#culminar tarea desde el listado
        try:
            post=Post.objects.get(id=request.POST.get('id'))
            post.estado='C'
            post.save()
            messages.success(request,'tarea cerrada exitosamente')
        except:
            return redirect('/')
        
    posts=Post.objects.all()
    return render(request,'posts.html',{'posts':posts})

def post_view(request,id):
    post=get_object_or_404(Post,id=id)
    return render(request,'postView.html',{'post':post})

def post_new(request):
    data={
        'form':PostForm(),
        'prueba':'prueba'
    }
    if request.method=='POST':
        form=PostForm(data=request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'tarea creada con exito')
                redirect(to='posts_list')
            except:
                data['mensaje']=form
    return render(request,'newPost.html',data)

def post_edit(request,id):
    post=get_object_or_404(Post,id=id)
    data={
        'form':PostForm(instance=post)
    }
    if request.method=='POST':
        form=PostForm(data=request.POST, instance=post)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'tarea modificada con exito')
                return redirect(to='posts_list')
            except:
                data['form']=form
    return render(request,'editPost.html',data)

def post_delete(request,id):
    if request.method=='POST':
        post=get_object_or_404(Post, id=id)
        post.delete()
        messages.success(request,'tarea eliminada con exito')
    
    return redirect(to='posts_list')

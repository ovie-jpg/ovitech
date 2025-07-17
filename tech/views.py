from django.shortcuts import render
from .models import Profile, Projects, Blog
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    profile= Profile.objects.get(pk=1)
    projects= Projects.objects.all()
    blogs= Blog.objects.all()
    context= {
        'profile':profile,
        'projects':projects,
        'blogs': blogs
    }
    return render(request, 'index.html', context)

def info(request, pk):
    project= Projects.objects.get(pk=pk)
    context= {
        'project':project
    }
    return render(request, 'info.html', context)

class AddProject(CreateView):
    model= Projects
    template_name= 'add-project.html'
    fields= '__all__'

class EditProject(UpdateView):
    model= Projects
    template_name= 'edit-project.html'
    fields= '__all__'

class DelProject(DeleteView):
    model= Projects
    template_name= 'delete-project.html'
    success_url= reverse_lazy('home')

class EditProfile(UpdateView):
    model= Profile
    template_name= 'edit-profile.html'
    fields= '__all__'

class AddBlog(CreateView):
    model= Blog
    template_name= 'add-blog.html'
    fields= '__all__'

class EditBlog(UpdateView):
    model= Blog
    template_name= 'edit-blog.html'
    fields= '__all__'

class DeleteBlog(DeleteView):
    model= Blog
    template_name= 'del-blog.html'
    fields= '__all__'
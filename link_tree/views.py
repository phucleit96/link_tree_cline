from django.shortcuts import render, get_object_or_404
from .models import Link, Profile
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class LinkListView(ListView):
    # query all links: Link.objects.all()
    # context = {'link':links}
    # return render(request, 'link_list.html', context)
    model = Link

class LinkCreateView(CreateView):
    # create forms.py file and form
    # check if this was a post or get request
    # return an empty form or save the form data
    model = Link
    fields = '__all__'
    success_url = reverse_lazy('link-list')
    #template called model_form, link_form html

class LinkUpdateView(UpdateView):
    # create a form
    # check if a get request or a put request
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('link-list')

class LinkDeleteView(DeleteView):
    model = Link
    # take in a id/pk of an object
    # query to db for that object
    # check if it exists -> delete the object
    # return some template or forward to user some url
    success_url = reverse_lazy('link-list')
    # form to submit to delete
    # expect a template named link_confirm_delete.html

def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        'profile': profile,
        'links': links,
    }
    return render(request, 'link_tree/profile.html', context)
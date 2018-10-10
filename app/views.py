from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.db.models import Q

from .forms import CustomUserCreationForm
from .models import Channel, Message

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('message-index'))
    return redirect(reverse_lazy('login'))
    

class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse_lazy('index')

class UserDetailView(DetailView):
    model = User

    def get_object(self):
        user = None
        if self.kwargs.get('pk'):
            user = User.objects.filter(pk=self.kwargs.get('pk')).first()
        if not user:
            user = self.request.user
        return user


class UserUpdateView(UpdateView):
    model = User

class UserDeleteView(DeleteView):
    model = User

class UserListView(ListView):
    model = User

class MessageCreateView(CreateView):
    model = Message

class NewMessageView(ListView):
    model = User

    def post(self,request):
        return reverse_lazy('message-list', kwargs={'pk':request.POST.get('user_pk')})


class MessageUpdateView(UpdateView):
    model = Message

class MessageDeleteView(DeleteView):
    model = Message

class MessageListView(ListView):
    model = Message

    def get_queryset(self):
        channel = Channel.objects.get_or_create(users = (self.request.user, User.objects.filter(pk=self.kwargs['user_pk']).first()), private = True)
        queryset = super(MessageListView, self).get_queryset()
        queryset = queryset.filter(channel=channel)
        return queryset

class MessageIndexView(ListView):
    model = Message

    template_name = 'app/message_list.html'

    
    def get_context_data(self, **kwargs):
        context = super(MessageIndexView, self).get_context_data(**kwargs)
        channels = self.request.user.channels.all()
        context['private_channels'] = []
        context['public_channels'] = []
        for i in channels:
            if i.private:
                context['private_channels'].append(i)
            else:
                context['public_channels'].append(i)

        return context
    
class ChannelCreateView(CreateView):
    model = Channel

class ChannelUpdateView(UpdateView):
    model = Channel

class ChannelDeleteView(DeleteView):
    model = Channel

class ChannelListView(ListView):
    model = Channel

class ChannelIndexView(ListView):
    model = Channel

    def get_queryset(self):
        queryset = super(ChannelIndexView, self).get_queryset()
        queryset = queryset.filter(writter=self.request.user)
        queryset_list = []
        for i in queryset:
            if i.to not in queryset_list:
                queryset_list.append(i.to)
        return queryset

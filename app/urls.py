from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #Message's url's
    
    path('mensagens/', views.MessageIndexView.as_view(), name='message-index'),
    path('mensagens/<int:user_pk>/', views.MessageListView.as_view(), name='message-list'),
    path('mensagens/new', views.NewMessageView.as_view(), name='message-new'),
    path('mensagens/<int:user_pk>/send', views.MessageCreateView.as_view(), name='message-create'),
    path('mensagens/<int:pk>/', views.MessageUpdateView.as_view(), name='message-update'),
    path('mensagens/<int:pk>/', views.MessageDeleteView.as_view(), name='message-delete'),

    #User's url's
    path('accounts/sign_up/', views.UserCreateView.as_view(), name='sign-up'),
    path('accounts/profile/', views.UserDetailView.as_view(), name='profile-detail'),
    path('accounts/<int:pk>/', views.UserDetailView.as_view(), name='profile-detail'),
    path('accounts/<int:pk>/edit', views.UserUpdateView.as_view(), name='profile-update'),
    path('accounts/<int:pk>/delete', views.UserDetailView.as_view(), name='profile-detail'),

    #Channel's url's
    path('canais/', views.ChannelIndexView.as_view(), name='channel-index'),
    path('canais/<int:user_pk>/', views.ChannelListView.as_view(), name='channel-list'),
    path('canais/<int:user_pk>/send', views.ChannelCreateView.as_view(), name='channel-create'),
    path('canais/<int:pk>/', views.ChannelUpdateView.as_view(), name='channel-update'),
    path('canais/<int:pk>/', views.ChannelDeleteView.as_view(), name='channel-delete'),
]

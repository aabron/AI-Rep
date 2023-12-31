from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/bot-action/', views.bot_action, name='bot-action'),
    path('api/login/', views.login_view, name='login'),
    path('api/logout/', views.logout_view, name='logout'),
    path('api/conversations/', views.conversation_list, name='conversation-list'),
    path('api/reamaze-webhook/', views.ReamazeWebhook.post, name='conversation-create'),
    path('api/get-statistics/', views.conversation_stats, name='conversation-stats'),
    
]


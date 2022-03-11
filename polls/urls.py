from django.urls import path

from . import views
from .views import rate, create_poll, polls

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('poll-list/', polls),
    path('poll-create/', create_poll, name="create_poll"),
    path('rate/<int:poll_id>', rate, name='rate')
]

from django.urls import path

from . import views
from .views import rate, create_poll, polls, poll_details, login, registration

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('poll-list/', polls),
    path('create-poll/', create_poll, name="create_poll"),
    path('rate/<int:poll_id>', rate, name='rate'),
    path('poll-details/<int:poll_id>', poll_details, name="poll_details"),

]
"""path('login', login, name="login_form"),
    path('registration', registration, name='registration_form')"""
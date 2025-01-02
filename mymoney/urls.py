from django.urls import path
from . import views

urlpatterns =[
    path ('register/' , views.register, name='register'),

    path ('test/' , views.test, name='test'),
    path ('' , views.main, name='main'),
    path('management/' , views.management, name='management '),
    path ('logout/' , views.logout_view, name='log_out'),
]
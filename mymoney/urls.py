from django.urls import path
from . import views

urlpatterns =[
    path ('submit/expense' , views.submit_expense, name='submit_expense'),
    path ('submit/' , views.get_info, name='Getting_information'),
    path ('register/' , views.register, name='register'),
    path ('login/' , views.login, name='login'),
    path ('test/' , views.test, name='test'),
]
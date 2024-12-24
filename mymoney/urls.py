from django.urls import path
from . import views

urlpatterns =[
    path ('management/showdata/submitexpense' , views.submit_expense, name='submit_expense'),
    path ('submit/' , views.get_info, name='Getting_information'),
    path ('register/' , views.register, name='register'),
    # path ('login/' , views.login, name='login'),
    path ('test/' , views.test, name='test'),
    path ('' , views.main, name='main'),
    path('management/showdata', views.manage_data, name='manage data'),

    path('management/' , views.get_token, name='get token'),
    path ('submit/income' , views.submit_income, name='submit income'),
    path ('lost/' , views.auth_form , name='auth form'),
    path ('lost/auth' , views.Auth, name='Show token'),
    path ('expense_added' , views.expense_added, name='expense_added'),
]
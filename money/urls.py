"""
URL configuration for MobileMoney project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name

from django.urls import path, include
from django.contrib.auth import views as auth_views

from money.views import (index_view, money_list_view,add_agent_view,add_customer_view,edit_customer_view,delete_customer_view,sign_up_view,
                         edit_agent_view, delete_agent_view,withdraw_view,edit_withdraw_view,delete_withdraw_view,deposit_view,edit_deposit_view,
                         delete_deposit_view,transfer_view,edit_transfer_view,delete_transfer_view,transaction_view)


urlpatterns = [
    path('', index_view,name='index_page'),
    path('signup/', sign_up_view, name='sign_up_page'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('money_list/', money_list_view, name='money_list_page'),
    path('add_agent/', add_agent_view, name='add_agent_page'),
    path('add_customer/', add_customer_view, name='add_customer_page'),
    path('edit_customer/<int:customer_id>/', edit_customer_view , name='edit_customer_page'),
    path('delete_customer/<int:customer_id>/', delete_customer_view, name='delete_customer_page'),
    path('edit_agent/<int:agent_id>/', edit_agent_view, name='edit_agent_page'),
    path('delete_agent/<int:agent_id>/', delete_agent_view, name='delete_agent_page'),
    path('withdraw/',withdraw_view, name='withdraw_page'),
    path('edit_withdraw/<int:withdraw_id>/',edit_withdraw_view,name='edit_withdraw_page'),
    path('delete_withdraw/<int:withdraw_id>/', delete_withdraw_view, name='delete_withdraw_page'), 
    path('deposit/',deposit_view,name='deposit_page'),
    path('edit_deposit/<int:deposit_id>/',edit_deposit_view,name='edit_deposit_page'),
    path('delete_deposit/<int:deposit_id>/',delete_deposit_view,name='delete_deposit_page'), 
    path('transfer/',transfer_view,name='transfer_page'),
    path('edit_transfer/<int:transfer_id>/',edit_transfer_view,name='edit_transfer_page'),
    path('delete_transfer/<int:transfer_id>/',delete_transfer_view,name='delete_transfer_page'),
    path('transaction/', transaction_view, name='transaction_page'),
]



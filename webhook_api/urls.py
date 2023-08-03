"""webhook_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
# webhook_api/urls.py

from django.urls import path
from webhook_app.views import AccountListCreateView, AccountRetrieveUpdateDeleteView, DestinationListCreateView, DestinationRetrieveUpdateDeleteView, DestinationByAccountView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', AccountListCreateView.as_view(), name='account-list-create'),
    path('accounts/<int:pk>/', AccountRetrieveUpdateDeleteView.as_view(),name='account-retrieve-update-delete'),
    path('destinations/', DestinationListCreateView.as_view(),name='destination-list-create'),
    path('destinations/<int:pk>/', DestinationRetrieveUpdateDeleteView.as_view(),name='destination-retrieve-update-delete'),
    path('destinations/account/<str:account_id>/',DestinationByAccountView.as_view(), name='destinations-by-account'),
]

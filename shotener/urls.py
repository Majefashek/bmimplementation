from django.urls import path
from  . import views


urlpatterns = [
    path('', views.Shotener.as_view(), name='index'),
    path("create", views.create, name="create"),
    path('<str:pk>', views.urlRedirect, name="redirect"),
]

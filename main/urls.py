from django.urls import path
from .views import index, create, detail

urlpatterns = [
    path('', index, name="index"),
    path('create/', create, name="create"),
    path('detail/', detail, name="detail"),
]

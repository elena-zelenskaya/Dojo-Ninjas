from django.urls import path
from . import views  

urlpatterns = [
    path("", views.index),
    path("new_dojo/", views.add_new_dojo),
    path("new_ninja/", views.add_new_ninja),
    path("delete/<int:number>", views.delete_dojo_and_all_its_ninjas),
]
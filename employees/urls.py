from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("home/",emp_home, name="home"),
    path("add-emp/",add_emp, name="add-emp"),
    path("delete-emp/<int:emp_id>/",delete_emp, name="delete-emp"),
    path("update-emp/<int:emp_id>/",update_emp, name="update-emp"),
    path("do-update-emp/<int:emp_id>/",do_update_emp, name="do-update-emp"),
]
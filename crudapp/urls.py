from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("register",views.registeruser,name="register"),
    path("showdetails",views.show,name="showdata"),
    path("editdetails",views.Edit,name="edit"),
    path("changed",views.change,name="change"),
    path("deletedetails",views.del_user,name="delete")

]
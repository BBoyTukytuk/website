from django.urls import path
from . import views

urlpatterns = [
    path("",views.register, name="register"),
    path("homepage",views.index, name="index"),
    path("login_view",views.login_view, name="login_view"),
    path("logout_view",views.logout_view, name="logout_view"),
    path("addcart",views.addcart, name="addcart"),
    path("add_new_plant",views.add_new_plant, name="add_new_plant"),
    path("process_payment",views.process_payment.as_view(), name="process_payment"),
    path("charge", views.charge, name='charge')
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.Usersignup, name="Usersignup"),
    path("user_login/", views.User_login, name="User_login"),
    path("logout/", views.Logout, name="Logout"),

    path("all_books/", views.Admin, name="Admin"),
    path("customers_list/", views.customers_list, name="customers_list"),
   
    path("delete_requested_books/delete_<int:myid>/", views.delete_requested_books, name="delete_requested_books"),
    path("customers_list/orders_<int:myid>/", views.orders_list, name="orders_list"),
    path("customers_list/orders_<int:myid>/data/", views.data_view, name="data"),
 
    
    path("for_users/", views.Users, name="Users"),
     
    path("checkout/", views.checkout, name="checkout"),    
]

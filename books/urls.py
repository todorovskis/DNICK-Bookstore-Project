from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('<int:id>', views.view_book, name="view_book"),
    path('<int:id>/edit', views.update_book, name="update_book"),
    path('add', views.add_book, name="add_book"),
    path('<int:id>/delete', views.delete_book, name="delete_book"),
    path('checkout/', views.checkout, name="checkout"),
    path('card/', views.card, name="card"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
]



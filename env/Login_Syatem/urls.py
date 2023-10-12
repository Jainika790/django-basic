from django.urls import path
from . import views

urlpatterns = [
    path('Homepage/', views.Homepage),
    path('IndexPage/', views.IndexPage),
    path('All_user_details/', views.AllUsers),
    path('User_details/<int:pk>', views.SingleUserDetails),
]
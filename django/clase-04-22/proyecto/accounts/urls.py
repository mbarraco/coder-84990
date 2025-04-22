from django.urls import path
from .views import UserRegisterView, UserLoginView, logout_view

app_name = "accounts"

urlpatterns = [
    path("", UserLoginView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'), 

]

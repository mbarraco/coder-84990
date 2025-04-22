from django.urls import path
from .views import UserRegisterView, UserLoginView, UserChangeView, logout_view, AvatarUpdateView

app_name = "accounts"

urlpatterns = [
    path("", UserLoginView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'), 
    # Clase 22 de Abril
    path('edit/', UserChangeView.as_view(), name='edit'),  
    path('avatar/', AvatarUpdateView.as_view(), name='upload-avatar'),
]

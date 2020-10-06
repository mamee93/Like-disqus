from django.urls import path
from  .views import signup,profile,profile_edit
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [

    path('signup',signup,name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile',profile,name='profile'),
    path('profile/edit',profile_edit,name='profile_edit'),
     

]

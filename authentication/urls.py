from django.urls import path
from authentication import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.handlelogin, name="handlelogin"),
    path('logout/', views.handlelogout, name="handlelogout"),
    path('profile/', views.user_profile, name="profile"),
    path('complete-profile/', views.complete_profile, name="completeprofile"),
    path('edit-profile/', views.edit_profile, name="editprofile"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
]
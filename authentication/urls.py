from django.urls import path
from authentication import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.handlelogin, name="handlelogin"),
    path('logout/', views.handlelogout, name="handlelogout"),
    path('profile/', views.user_profile, name="profile"),
    path('complete-profile/', views.complete_profile, name="completeprofile"),
    path('add-blood-bank/', views.add_blood_bank, name="addbloodbank"),
    path('edit-profile/', views.edit_profile, name="editprofile"),
    path('edit-bloodbank/', views.edit_bloodbank, name="editbloodbank"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    path('request-reset-email/',views.RequestResetEmailView.as_view(),name='request-reset-email'),
    path('set-new-password/<uidb64>/<token>',views.SetNewPasswordView.as_view(),name='set-new-password'),
]
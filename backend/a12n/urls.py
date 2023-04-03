from django.urls import path, include
from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path('account-confirm-email/', VerifyEmailView.as_view()),
    path('registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),
]

from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import include, path

urlpatterns = [
    path('account-confirm-email/', VerifyEmailView.as_view()),
    path('registration/account-confirm-email/<str:key>/',
         ConfirmEmailView.as_view()),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('password/reset/', PasswordResetView.as_view(),
         name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('', include('dj_rest_auth.urls')),
]

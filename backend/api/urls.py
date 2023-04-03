from allauth.account.views import ConfirmEmailView
from django.urls import path, include

from dj_rest_auth.registration.views import VerifyEmailView

authpatterns = [
    path('account-confirm-email/', VerifyEmailView.as_view()),
    path('registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),
]

urlpatterns = [
    path('auth/', include(authpatterns)),
    path('', include('api.users.urls')),
]

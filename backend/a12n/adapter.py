from allauth.account.adapter import DefaultAccountAdapter

CURRENT_VERSION = "v1"

AFTER_LOGIN_URL = f'/api/{CURRENT_VERSION}/users/'
LOGIN_URL = f"/api/{CURRENT_VERSION}/auth/login/"


class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        """После входа в систему перенаправить на"""
        return AFTER_LOGIN_URL

    def get_email_confirmation_redirect_url(self, request):
        """После подтверждения почты отправить на"""
        return LOGIN_URL

    # def get_signup_redirect_url(self, request):
    #     return LOGIN_URL


from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView, LogoutUserAPIView


urlpatterns = [
    url(r'^account/login/$',
        obtain_auth_token,
        name='auth_user_login'),
    url(r'^account/signup/$',
        CreateUserAPIView.as_view(),
        name='auth_user_create'),
    url(r'^account/logout/$',
        LogoutUserAPIView.as_view(),
        name='auth_user_logout')
]
# fe8a534dd6159d2e4956251d65d5b32aefb0a5ba

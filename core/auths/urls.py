from django.conf.urls import url
from core.auths.rest.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    url(r"^login/$", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    url(r"^token/refresh/$", TokenRefreshView.as_view(), name="token_refresh"),
]

from rest_framework import routers

from core.users.rest.views import UserViewSet

router = routers.SimpleRouter()
router.register(r"", UserViewSet)
urlpatterns = router.urls

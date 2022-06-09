from rest_framework import routers

from core.todos.rest.views import TodoViewSet

router = routers.SimpleRouter()
router.register(r"", TodoViewSet)
urlpatterns = router.urls

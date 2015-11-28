from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register("people", views.PeopleViewSet)

urlpatterns = router.urls
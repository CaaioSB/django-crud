from django.urls import include, path
from rest_framework import routers
from django_crud.marketplace.views import user, group, bicycle

router = routers.DefaultRouter()
router.register(r'users', user.UserViewSet)
router.register(r'groups', group.GroupViewSet)
router.register(r'bicycles', bicycle.BicycleViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

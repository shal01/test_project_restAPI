from rest_framework import routers

from users.viewset import UserViewSet,ProfileViewSet

app_name="users"

router=routers.DefaultRouter()

router.register(r'user',UserViewSet)

router.register(r'profiles',ProfileViewSet)
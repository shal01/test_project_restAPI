from rest_framework import routers

from users import viewset

app_name="users"

router=routers.DefaultRouter()

router.register(r'user',viewset.UserViewSet)
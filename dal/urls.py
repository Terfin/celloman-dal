from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [

]
router = DefaultRouter()
router.register('contenttype', views.ContentTypeViewSet)
router.register('permissions', views.PermissionViewSet)
router.register('groups', views.GroupViewSet)
router.register('users', views.UserViewSet)
urlpatterns += router.urls
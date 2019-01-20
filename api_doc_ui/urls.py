from rest_framework.routers import DefaultRouter

from api_doc_ui import views

router = DefaultRouter()
router.register(prefix='demo1', viewset=views.DemoAPIViewSet)

urlpatterns = router.urls

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usapp import views
from .views import AddText, SaveText, PutText, DeleteText, AddFolder, PutFolder, DeleteFolder, main_page, FolderViewSet, EditName_Text
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'folders', FolderViewSet)

urlpatterns = [
    path('', main_page.as_view(), name='main_page'),
    path('AddText/', AddText.as_view(), name='AddText'),
    path('SaveText/', SaveText.as_view(), name='SaveText'),
    path('PutText/<int:id>/', PutText.as_view(), name='PutText'),
    path('DeleteText/<int:id>/', DeleteText.as_view(), name='DeleteText'),
    path('AddFolder/', AddFolder.as_view(), name='AddFolder'),
    path('PutFolder/<int:id>/', PutFolder.as_view(), name='PutFolder'),
    path('DeleteFolder/<int:id>/', DeleteFolder.as_view(), name='DeleteFolder'),
    path('EditName_Text/<int:id>/', EditName_Text.as_view(), name='EditName_Text'),
    path('', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
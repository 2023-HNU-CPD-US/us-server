from django.urls import path
from usapp import views

urlpatterns = [
    path('reset_data/', views.reset_data, name='reset_data'),
    path('', views.main_page, name='main_page'),
    path('add_folder/', views.add_folder, name='add_folder'),
    path('add_text/', views.add_text, name='add_text'),
    path('text/<int:text_id>/', views.text_detail, name='text_detail'),
    path('text/<int:text_id>/update/', views.update_text, name='update_text'),
    path('text/<int:text_id>/delete/', views.delete_text, name='delete_text'),
]

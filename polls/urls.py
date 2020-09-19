from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.home, name='home'),
    path('list/<int:pk>/', views.delete_file, name='delete_file'),
    path('upload/', views.upload_file, name='upload_file'),
    path('list/',views.file_list, name='file_list' )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
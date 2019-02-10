
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from API.views import (
		ClassesListView,
		ClassesDetailView,
		ClassesCreateView,
		ClassesUpdateView,
		ClassesDeleteView
	)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),



		path('api/list/', ClassesListView.as_view(), name='api-list'),
    path('api/create/', ClassesCreateView.as_view(), name='api-create'),
    path('api/<int:classroom_id>/detail/', ClassesDetailView.as_view(), name='api-detail'),
    path('api/<int:classroom_id>/update/', ClassesUpdateView.as_view(), name='api-update'),
    path('api/<int:classroom_id>/delete/', ClassesDeleteView.as_view(), name='api-delete'),



]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

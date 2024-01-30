
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.ApiOverview, name='docs'),
    path('goods/', views.get_all_goods),
    path('goods/add/', views.add_good),
    path('goods/<int:pk>/delete', views.delete_good_by_id),
    path('goods/<int:pk>/update', views.update_good_by_id)
]

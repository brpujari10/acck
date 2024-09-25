from django.contrib import admin
from django.urls import path
from myapp.views import Register, Dashboard, Logout, Delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Register.as_view(), name='register'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('logout/', Logout.as_view(), name='logout'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
]
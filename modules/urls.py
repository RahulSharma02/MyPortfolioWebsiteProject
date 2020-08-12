from django.urls import path
from django.contrib import admin
from .import views


# Django admin header customs
admin.site.site_header = " Rahul Fangalia"
admin.site.site_title = " Welcome to Rahul's Dashboard"
admin.site.index_title = "Welcome to the portal"

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('projects/',views.projects,name="projects"),
    path('discover/', views.discover, name="discover"),
    # path('blog/', views.Bloghome, name="blog"),
    # path('blog/<str:username>',views.BlogList,name="blog"),
    # path('blogdetail/<int:pk>/', views.BlogDetail, name="blogdetail"),

]

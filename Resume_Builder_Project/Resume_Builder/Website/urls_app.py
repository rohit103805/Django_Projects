from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home_Page"),
    path('capture', views.capture_image, name="Capture_Image"),
    path('about_me', views.about_me, name="About Me"),
    path('template', views.template_choose, name="Template Choosing")
]
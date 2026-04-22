from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', TemplateView.as_view(template_name="About.html")),

    # About
    path('about/', TemplateView.as_view(template_name="About.html")),

    # Contact (NEW)
    path('contact/', TemplateView.as_view(template_name="Contact.html")),
]
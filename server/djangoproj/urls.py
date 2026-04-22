from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home route (fixes 404)
    path('', TemplateView.as_view(template_name="About.html")),

    # About page
    path('about/', TemplateView.as_view(template_name="About.html")),
]
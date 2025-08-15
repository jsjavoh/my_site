from django.urls import path
from .views import HomePage, AboutPage, SkillsPage, ProjectsPage, ConntactPage

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('about/',AboutPage.as_view(),name='about'),
    path('skills/', SkillsPage.as_view(),name='skills'),
    path('portfolio/', ProjectsPage.as_view(), name='portfolio'),
    path('contact/', ConntactPage.as_view(), name='contact'),
]
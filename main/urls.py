from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('yangiliklar/', views.news_list_view, name='news_list'),
    path('yangiliklar/<slug:slug>/', views.news_detail_view, name='news_detail'),
    path('rahbariyat/', views.leadership_view, name='leadership'),
    path('kafedralar/', views.departments_view, name='departments'),
    path('davlat-ramzlari/', views.state_symbols_view, name='state_symbols'),
    path('davlat-ramzlari/<str:symbol_type>/', views.state_symbols_view, name='state_symbols_detail'),
    path('litsey-tarixi-va-nizomi/', views.admission_view, name='admission'),
    path('qabul-2025-2026/', views.qabul_view, name='qabul'),
    path('fan-olimpiadalari/', views.olympiad_view, name='olympiad'),
    path('boglanish/', views.contact_view, name='contact'),
]

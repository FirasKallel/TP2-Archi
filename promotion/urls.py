from django.urls import path

from promotion import views

urlpatterns = [
    path('', views.PromotionList.as_view(), name=views.PromotionList.name),
    path('<int:pk>/', views.PromotionDetail.as_view(), name=views.PromotionDetail.name),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

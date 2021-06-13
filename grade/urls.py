from django.urls import path

from grade import views

urlpatterns = [
    path('', views.GradeList.as_view(), name=views.GradeList.name),
    path('<int:pk>/', views.GradeDetail.as_view(), name=views.GradeDetail.name),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

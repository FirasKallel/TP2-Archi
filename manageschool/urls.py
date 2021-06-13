from django.conf.urls import url, include

from manageschool.views import ApiRoot

urlpatterns = [
    url(r'^professor/', include('professor.urls')),
    url(r'^student/', include('student.urls')),
    url(r'^promotion/', include('promotion.urls')),
    url(r'^course/', include('course.urls')),
    url(r'^grade/', include('grade.urls')),
    url(r'^docs/', ApiRoot.as_view(),
        name=ApiRoot.name),
]

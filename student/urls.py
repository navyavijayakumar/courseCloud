

from django.urls import path
from student import views


urlpatterns=[
    path("register/",views.StudentCreateView.as_view(),name="student-register"),
    path("signin/",views.StudentSigninView.as_view(),name="signin"),
    path("index/",views.IndexView.as_view(),name="index"),
    path('courses/<int:pk>/',views.CourseDetailView.as_view(),name="course-detail"),
]


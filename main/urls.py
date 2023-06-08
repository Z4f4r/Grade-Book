from django.urls import path, include
from .views import (GradeViewSet, StudentViewSet, CourseViewSet, FilterCourseTitleViewSet, FilterGradeValueViewSet,
                    FilterGradeDateViewSet, FilterStudentFirstNameViewSet, SearchCourseViewSet, SearchStudentViewSet)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'student', StudentViewSet, basename='student')
router.register(r'grade', GradeViewSet, basename='grade')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/filter/course/title/<str:title>', FilterCourseTitleViewSet.as_view({'get': 'list'}),
         name='filter_course_by_title'),
    path('v1/filter/grade/value/<int:value>', FilterGradeValueViewSet.as_view({'get': 'list'}),
         name='filter_grade_by_value'),
    path('v1/filter/grade/date/', FilterGradeDateViewSet.as_view({'get': 'list'}),
         name='filter_grade_by_date'),
    path('v1/filter/student/first-name/<str:name>', FilterStudentFirstNameViewSet.as_view({'get': 'list'}),
         name='filter_student_by_first_name'),
    path('v1/search/student/<str:name>', SearchStudentViewSet.as_view({'get': 'list'}),
         name='search_student'),
    path('v1/search/course/<str:title>', SearchCourseViewSet.as_view({'get': 'list'}),
         name='search_course')
]

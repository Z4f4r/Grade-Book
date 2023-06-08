from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import Course, Student, Grade
from .serializers import CourseSerializer, StudentSerializer, GradeSerializer
from django.http import Http404


class CourseViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GradeViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class FilterCourseTitleViewSet(mixins.ListModelMixin,
                               GenericViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        title = title.capitalize()
        return Course.objects.filter(title=title)


class FilterGradeValueViewSet(mixins.ListModelMixin,
                              GenericViewSet):
    serializer_class = GradeSerializer

    def get_queryset(self):
        value = self.kwargs['value']
        if value <= 10:
            return Grade.objects.filter(value=value)
        else:
            raise Http404("Страница не найдена")


class FilterGradeDateViewSet(mixins.ListModelMixin,
                             GenericViewSet):
    serializer_class = GradeSerializer

    def get_queryset(self):
        queryset = Grade.objects.all()
        date = self.request.query_params.get('date', None)
        if date is not None:
            queryset = queryset.filter(date=date)
        else:
            raise Http404("Страница не найдена")


class FilterStudentFirstNameViewSet(mixins.ListModelMixin,
                                    GenericViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Student.objects.filter(first_name=name)


class SearchStudentViewSet(mixins.ListModelMixin,
                           GenericViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Student.objects.filter(first_name__icontains=name)


class SearchCourseViewSet(mixins.ListModelMixin,
                          GenericViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        return Course.objects.filter(title__icontains=title)


from classes.models import Classroom
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import(
	classesListSerializer,
	classesDetailSerializer,
	classesCreateUpdateSerializer
	)
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsTeacher


# Create your views here.
class ClassesListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = classesListSerializer
	permission_classes = [AllowAny,]


class ClassesDetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = classesDetailSerializer
	permission_classes = [AllowAny,]
	ookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class ClassesCreateView(CreateAPIView):
	serializer_class = classesCreateUpdateSerializer
	permission_classes = [IsAuthenticated,]

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)


class ClassesUpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = classesCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'
	permission_classes = [IsAuthenticated,IsTeacher]

class ClassesDeleteView(DestroyAPIView):
	queryset = Classroom.objects.all()
	serializer_class = classesListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'
	permission_classes = [IsAuthenticated,IsTeacher]
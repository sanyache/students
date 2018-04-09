from ..models import Student
from rest_framework import generics
from ..serializers import StudentSerializers

class StudentListAPI(generics.ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentDetailAPI(generics.RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializers
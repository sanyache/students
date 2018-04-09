from .models import Student
from  rest_framework import serializers

class StudentSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = ('first_name','last_name','ticket')
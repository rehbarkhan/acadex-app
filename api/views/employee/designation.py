from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from api.models import Designation as Model


class DesignationSer(ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class Designation(ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = DesignationSer
    filterset_fields = {
        'name' : ['icontains']
    }
# Create your views here.
from rest_framework import serializers
from rest_framework import viewsets

from api_doc_ui.models import DemoModel


class DemoModelSeriailzer(serializers.ModelSerializer):
    class Meta:
        model = DemoModel
        fields = '__all__'


class DemoAPIViewSet(viewsets.ModelViewSet):
    queryset = DemoModel.objects.all()
    serializer_class = DemoModelSeriailzer

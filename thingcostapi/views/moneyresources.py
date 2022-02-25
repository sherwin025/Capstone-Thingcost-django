from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from thingcostapi.models import MoneyResources


class ResourcesView(ViewSet):
    def retrieve(self, request, pk):
        try:
            user = MoneyResources.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except user.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
    
    def list(self, request):
        user = MoneyResources.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyResources
        fields = ("id", "url", "description")
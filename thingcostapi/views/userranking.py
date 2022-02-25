from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.forms import ValidationError

from thingcostapi.models import ItemRaking


class RankingView(ViewSet):
    def retrieve(self, request, pk):
        try:
            user = ItemRaking.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except user.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
    
    def list(self, request):
        user = ItemRaking.objects.all().order_by('ranking')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        try:
            ranking = ItemRaking.objects.get(pk=pk)
            serializer = UserSerializer(ranking, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRaking
        fields = ("id", "ranking", "item")
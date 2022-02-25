import re
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.forms import ValidationError

from thingcostapi.models import Item
from thingcostapi.models.user import AUser
from thingcostapi.models.useritemtypes import UserItemTypes


class ItemView(ViewSet):
    def retrieve(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            
            serializer = UserSerializer(item)
            return Response(serializer.data)
        except item.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
    
    def list(self, request):
        theAuser = AUser.objects.get(user=request.auth.user)
        item = Item.objects.all()
        items = item.filter(user = theAuser)
        serializer = UserSerializer(items, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        theuser = AUser.objects.get(user=request.auth.user)
        try: 
            serializer = CreateUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=theuser)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            serializer = CreateUserSerializer(item, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "price", "name", "need", "hoursneeded", "purchased", "purchaseby", "buydifficulty", "user", "useritemtype")
        depth = 1
        
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id" ,"price", "name", "need", "hoursneeded", "purchased", "purchaseby", "buydifficulty", "user", "useritemtype")
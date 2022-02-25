from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.forms import ValidationError

from thingcostapi.models import UserTipsAndTricks, AUser


class UserTipsView(ViewSet):
    def retrieve(self, request, pk):
        try:
            user = UserTipsAndTricks.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except user.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
    
    def list(self, request):
        theAuser = AUser.objects.get(user=request.auth.user)
        user = UserTipsAndTricks.objects.all()
        tips = user.filter(user_id = theAuser)
        serializer = UserSerializer(tips, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        try:
            serializer = CreateUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        item = UserTipsAndTricks.objects.get(pk=pk)
        item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTipsAndTricks
        fields = ("id", "description",  'user_id')
        
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTipsAndTricks
        fields = ( "description",  'user')
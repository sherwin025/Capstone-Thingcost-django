from pydoc import describe
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from thingcostapi.models.itemtypes import ItemType
from thingcostapi.models.moneyresources import MoneyResources
from thingcostapi.models.tipsandtricks import TipsAndTricks

from thingcostapi.models.user import AUser
from thingcostapi.models.useritemtypes import UserItemTypes
from thingcostapi.models.usermoneyresources import UserMoneyResources
from thingcostapi.models.usertipsandtricks import UserTipsAndTricks

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def login_user(request):
    '''Handles the authentication of a gamer

    Method arguments:
      request -- The full HTTP request object
    '''
    theemail = request.data['username']
    thepassword = request.data["password"]
    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(username=theemail, password=thepassword)
    
    # If authentication was successful, respond with their token
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key,
            "ThingCost_customer": authenticated_user.auser.id
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
        email=request.data['email'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        username=request.data['username'],
        password=request.data['password']
    )

    # Now save the extra info in the levelupapi_gamer table
    theuser = AUser.objects.create(
        hourlysalary=request.data['hourlysalary'],
        user=new_user
    )

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=theuser.user)
    # Return the token to the client
    data = { 'token': token.key,
            'ThingCost_customer': theuser.id}
    
    types = ItemType.objects.all()
    for type in types:
        UserItemTypes.objects.create(
            user=theuser,
            description=type.label
        )
    
    resources = MoneyResources.objects.all()
    for resource in resources:
        UserMoneyResources.objects.create(
            user=theuser,
            url= resource.url,
            description=resource.description
        )
    
    tips = TipsAndTricks.objects.all()
    for tip in tips:
        UserTipsAndTricks.objects.create(
            user=theuser,
            description=tip.description
        )
    
    return Response(data)

from django.shortcuts import render ,HttpResponse


from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle ,AnonRateThrottle
from rest_framework.decorators import api_view , permission_classes , throttle_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view()
@throttle_classes([UserRateThrottle,AnonRateThrottle])

def ping_view(request):


    return Response("pong .. server is running ...") 



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret_view(request):


    return Response({"data":"only authenticated are allowed"})
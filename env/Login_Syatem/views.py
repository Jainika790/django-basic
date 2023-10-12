from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Login_User
from .serializers import Login_User_Serializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def Homepage (request):
    return HttpResponse ("Hello and Welcome!!")
def IndexPage (request):
    return HttpResponse ("!!It's the Index Page!!")

@csrf_exempt
def AllUsers(request):
    try:
        all_users = Login_User.objects.all()
    except:
        return HttpResponse('Not Found! Sorry', status=404)
    
    if request.method == 'GET':
        users_serialized=Login_User_Serializer(all_users, many=True)
        return JsonResponse(users_serialized.data, safe=False, status=200)
    elif request.method == 'POST':
        input_data = JSONParser().parse(request)
        de_serialized=Login_User_Serializer(data=input_data)
        
        if de_serialized.is_valid():
            de_serialized.save()
            return JsonResponse(de_serialized.data, safe=False, status=200)
        else:
            return JsonResponse(de_serialized.errors, safe=False, status=400)
        
@csrf_exempt
def SingleUserDetails(request,pk):
    try:
        user=Login_User.objects.get(pk=pk)
    except:
        return HttpResponse('Sorry, this is not found',status=404)
    
    if request.method == 'GET':
        users_serialized=Login_User_Serializer(user)
        return JsonResponse(users_serialized.data, status=200)
    
    elif request.method == 'PUT':
        input_data = JSONParser().parse(request)
        de_serialized=Login_User_Serializer(user, input_data)
        
        if de_serialized.is_valid():
            de_serialized.save()
            return JsonResponse(de_serialized.data, status=200)
        else:
            return JsonResponse(de_serialized.errors, status=400)
        
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse('Successfully deleted', status=204)
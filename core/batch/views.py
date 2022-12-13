from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Enroll


@csrf_exempt
def enroll(request): 
    category = request.POST['cat']   
    username = request.POST['email']
    id = request.POST['id']
    
    record = Enroll.objects.filter(email=username)
    print(len(record))
    
    if(len(record) != 0):
            return JsonResponse({'msg': 'You are already enrolled'})
            
    else:
        instance = Enroll.create({"name":category ,"user_id" : id , "email" : username })
        instance.save()
        return JsonResponse({'msg': 'Sucessfully Enrolled'})

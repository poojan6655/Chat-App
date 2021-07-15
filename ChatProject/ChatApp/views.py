from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
from random import *
from django.http import JsonResponse
# Create your views here.

def home_fun(request):
    return render(request,"ChatApp/index.html")
    # else:
        # return render(request,"ChatApp/login.html")

def login_fun(request):
    if request.POST:
        # u_email=request.POST['EmailFromHtml']
        # u_password=request.POST['PasswordFromHtml']
        return render(request,"ChatApp/index.html")
    else:
        return render(request,"ChatApp/login.html")

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'ChatApp/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    print("11111111111111111111111111111111111111111111111111111111111111111111")
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    print("ssmskmskmks")
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
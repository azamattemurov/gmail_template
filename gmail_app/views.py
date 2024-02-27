# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def send(request):
    if request.method == "POST":
        name = request.POST.get('full-name')
        gmail = request.POST.get('gmail')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'name': name,
            'gmail': gmail,
            'subject': subject,
            'message': message
        }

        send_mail(data['subject'], message, '', ['mamajonovibrokhimjon@gmail.com'])
        return HttpResponse('Thank you gmail sending !...')
    return render(request, 'contact.html', context={})

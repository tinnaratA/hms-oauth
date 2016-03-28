from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
import json

import requests

# Create your views here.


def oauthLogin(request):
    username = request.POST.get('username', '');
    password = request.POST.get('password', '');
    client_id = request.POST.get('clientID', '');
    client_secret = request.POST.get('clientSecret', '');
    result = {'access_token': ""}

    # Search
    if request.POST.get('PIDSubmit','') != '':
        r = requests.get("http://localhost:8000/patients/id/"+request.POST.get('PID', '')+"/", headers={'Authorization':'bearer '+request.POST.get('token', '')});
        return render(request, 'client/searchMain.html', {'token': request.POST.get('token', ''), 'Plist': r.text})
    if request.POST.get('PNameSubmit','') != '':
        r = requests.get("http://localhost:8000/patients/name/"+request.POST.get('PName', '')+"/", headers={'Authorization':'bearer '+request.POST.get('token', '')});
        return render(request, 'client/searchMain.html', {'token': request.POST.get('token', ''), 'Plist': r.text})

    # If Access Token is able to use
    if request.POST.get('submission', '') != '' :
        r = requests.get("http://localhost:8000/patients/", headers={'Authorization':'bearer '+request.POST.get('token', '')});
        if 'Authentication' not in r.text:
            return render(request, 'client/searchMain.html', {'token': request.POST.get('token', ''), 'Plist':"(none)"})

    # login attempt
    if username != '' :
        response = requests.post(
            'http://localhost:8000/o/token/',
            data={
                'grant_type': 'password',
                'username': username,
                'password': password,
                'client_id': client_id,
                'client_secret': client_secret
            }
        )
        if "access_token" not in response.text:
            result = {'access_token': "ERROR"}
        else:
            result = json.loads(response.text)

    return render(request, 'client/login.html', {'token': result['access_token']})

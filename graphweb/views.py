from django.utils import timezone
import pytz
import inspect,io,os
import csv
import pyrebase
import pandas

from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

from rest_framework.views import APIView
from rest_framework.response import Response

timezone.activate(pytz.timezone("Asia/Bangkok"))
TIME = timezone.get_current_timezone().normalize(timezone.now())


def contact_upload(request):
    config = {
	"apiKey": "AIzaSyDhCyVUO2IugsNwlLEcTKW9rKTfRZPBYdw",
    "authDomain": "test2018-cafd1.firebaseapp.com",
    "databaseURL": "https://test2018-cafd1.firebaseio.com",
    "projectId": "test2018-cafd1",
    "storageBucket": "test2018-cafd1.appspot.com",
    "messagingSenderId": "578479999967"
}


    firebase = pyrebase.initialize_app(config)

    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password("meecomeback@gmail.com", "123456789")

    db = firebase.database()
    template = "contact_upload.html"
    
    prompt = {
        'order' : 'sadsadasdzxczxczxczxc'
    }

    if request.method == "GET":
        return render(request,template,prompt)
    myfile = request.FILES['file']
    fs = FileSystemStorage()
    global TIME

    strTIME = str(TIME.date())+'-'+str(TIME.time()).replace(':' , '-').replace('.', '-')+'.csv'
    filename = fs.save(strTIME, myfile)
    uploaded_file_url = fs.url(filename)
    df = pandas.read_csv(os.path.join("C:/Users/mhee/mysite/media_root", strTIME))
    # for col in df.columns:
    #     print(col)
    print(df)
    context = {}
    return render(request , template , context)

def get_data(request , *args,  **kwargs):

    data = {
        "sale":100,
        "cus":99,
    }
    return JsonResponse(data)

def analysis(request):
    
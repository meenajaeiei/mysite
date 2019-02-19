from django.utils import timezone
import pytz
import inspect,io,os
import csv
import pyrebase
import pandas
import json

from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

from rest_framework.views import APIView
from rest_framework.response import Response

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
    data = {}

    if request.method == "GET":
        return render(request,template, {"data" : data})

    dateinput = request.POST['date']
    print(dateinput)
    
    myfile = request.FILES['file']
    fs = FileSystemStorage()
    global TIME

    strTIME = str(TIME.date()).replace(':' , '-')+'.csv'
    filename = fs.save(dateinput+'.csv', myfile)
    uploaded_file_url = fs.url(filename)

    df = pandas.read_csv(os.path.join(os.path.join(BASE_DIR, 'media_root'), dateinput+'.csv'))
    # for col in df.columns:
    #     print(col)
    print(df)
    context = {}
    return render(request , template , context)


def viewgraph(request):
    return render(request , "viewgraph.html")

def setgraph(request):
    return render(request , "setgraph.html")

class ChartData(APIView):
    def get(self , request , format=None):
        labels = ["zxczxc"]
        default_items = []
        print(os.listdir(os.path.join(BASE_DIR, 'media_root')))
        dfy = pandas.read_csv(os.path.join(os.path.join(BASE_DIR, 'media_root'), "2019-02-18.csv"))

        for row in dfy.itertuples(index=True, name='Pandas'):
            tmp_dict = dict()
            tmp_dict['x'] = getattr(row, "AGE") 
            tmp_dict['y'] = getattr(row, "HEIGHT")
            default_items.append(tmp_dict)
    
        data = {
            "labels": labels,
            "default": default_items,
        }
        return(Response(data))






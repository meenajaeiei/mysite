from django.utils import timezone
import pytz
import inspect,io,os
import csv
import pyrebase
import pandas
import json

from django import forms
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
    try:
        request.session['startdate'] = request.GET['startdate']
        request.session['enddate'] = request.GET['enddate']
        pass
    except:
        return render(request , "setgraph.html")
        pass
    return render(request , "setgraph.html")

class ChartData(APIView):
    jsonfield = forms.CharField(max_length=1024)

    def get(self , request , format=None):
        print(request.session['startdate'])
        
        default_items = []
        filelist = os.listdir(os.path.join(BASE_DIR, 'media_root'))

        for fil in filelist:
            if( request.session['startdate'] <= fil[:10] and request.session['enddate'] >= fil[:10]):

                dfy = pandas.read_csv(os.path.join(os.path.join(BASE_DIR, 'media_root'), fil))

                for row in dfy.itertuples(index=True, name='Pandas'):
                    tmp_dict = dict()
                    tmp_dict['x'] = getattr(row, "AGE") 
                    tmp_dict['y'] = getattr(row, "HEIGHT")
                    default_items.append(tmp_dict)
        labels = [str(len(default_items)) +" subjects from "+ request.session['startdate']+" to "+request.session['enddate'] ]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return(Response(data))






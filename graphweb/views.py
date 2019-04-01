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
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from graphweb.models import Data,History
from .serializers import DataSerializer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
timezone.activate(pytz.timezone("Asia/Bangkok"))
TIME = timezone.get_current_timezone().normalize(timezone.now())


def contact_upload(request):

#     config = {
# 	"apiKey": "AIzaSyDhCyVUO2IugsNwlLEcTKW9rKTfRZPBYdw",
#     "authDomain": "test2018-cafd1.firebaseapp.com",
#     "databaseURL": "https://test2018-cafd1.firebaseio.com",
#     "projectId": "test2018-cafd1",
#     "storageBucket": "test2018-cafd1.appspot.com",
#     "messagingSenderId": "578479999967"
# }


#     firebase = pyrebase.initialize_app(config)

#     auth = firebase.auth()
#     user = auth.sign_in_with_email_and_password("meecomeback@gmail.com", "123456789")

#     db = firebase.database()

    template = "contact_upload.html"
    
    prompt = {
        'order' : 'sadsadasdzxczxczxczxc'
    }
    data = {}

    if request.method == "GET":
        return render(request,template, {"data" : data})

    dateinput = request.POST['date']

    if request.method == "POST":
        try:
            myfile = request.FILES['file']
            if(myfile.name[-4:]  != ".csv"):
                return render(request, "error.html" , {})

        except:
            return render(request, "error.html" , {})
        fs = FileSystemStorage()
    global TIME

    strTIME = str(TIME.date()).replace(':' , '-')+'.csv'
    filename = fs.save(dateinput+'.csv', myfile)
    uploaded_file_url = fs.url(filename).split('/')[-1]

    history_obj = History()
    history_obj.datetime_data = dateinput
    history_obj.datetime_trans = str(TIME.date()).replace(':' , '-')
    history_obj.filename = myfile.name
    history_obj.save()

    df = pandas.read_csv(os.path.join(os.path.join(BASE_DIR, 'media_root'), uploaded_file_url) ,  error_bad_lines=False )

    print(df)
    for i in range(int(df.size/df.columns.size)):
        tmp = Data(AGE=df.loc[ i , 'AGE']
        ,WEIGHT=df.loc[i , df.columns[2]]
        ,HEIGHT=df.loc[i , 'HEIGHT']
        ,FATPER=df.loc[i , 'FATPER']
        ,FATAMT=df.loc[i , 'FATAMT']
        ,FFMAMT=df.loc[i , 'FFMAMT']
        ,MSLAMT=df.loc[i , 'MSLAMT']
        ,BMI=df.loc[i , 'BMI']
        ,datetime=dateinput
        )
        tmp.save()
        #print(df.loc[i , df.columns[2]])


    #print(df) #print all of dataframe
    context = {}
    request.session['startdate'] = dateinput
    request.session['enddate'] = dateinput

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

@api_view(['GET', 'POST', ])
def graphtest(request,format=None):
    data = {
    "labels": "xczxczxc",
    "default": "asdasdasd",
    }
    return(Response(data ,  template_name='graphtest.html'))



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
                    tmp_dict['y'] = getattr(row, "BMI")
                    default_items.append(tmp_dict)
        labels = [str(len(default_items)) +" subjects from "+ request.session['startdate']+" to "+request.session['enddate'] ]
        
        #DS = Data.objects.filter(datetime__range=(request.session['startdate'], request.session['enddate']))

        data = {
            "labels": labels,
            "default": default_items,
            "datas" : serializers.serialize("json", History.published.all())
        }


        return(Response(data))

class DataList(APIView):
    def get(self , request):
        startdate = "1111-01-01"
        enddate = "1111-01-01"
        try:
            startdate = request.session['startdate']
            enddate =  request.session['enddate']
        except:
            startdate = "1111-01-01"
            enddate = "1111-01-01"
            
            
        dataall = Data.objects.filter(datetime__range=(startdate, enddate))
        serializer = DataSerializer(dataall , many=True)

        data = {
            "labels": "DATA AMOUNTS "+ str(dataall.count()),
            "dataset":serializer.data,
        }
        return Response(data)






import inspect,io 
import csv
import pyrebase
import pygal
from django.shortcuts import render

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
    csv_file = request.FILES['file']
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    count = 0
    COLUMN = []
    for col in csv.reader(io_string, delimiter = ',' , quotechar = "|"):
        if count == 90:
            break

        if count == 0:
            for zz in range(11):
                try:
                    COLUMN.append(col[zz])
                except:
                    print("EXECPT", col[zz])
                    pass
            count = count + 1
            continue
        print(col)


        for kk in range(len(COLUMN)):
            db.child("users_test_django").child(str(count)).child(str(COLUMN[kk])).set(col[kk])
        
        count = count + 1
    context = {}
    print("the count is" , count)
    print("the LEN COLUMN is" , len(COLUMN))
    return render(request , template , context)
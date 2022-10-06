from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults
#from predict.models import Contact
from django.http import HttpResponse
#here in urls.py file,views er sathe ja ache tai muloto function er name hobe
# Create your views here.
def predict(request):
    return render(request,'predict.html')

def about(request):
    return render(request,'about.html')

def predict_chances(request):
    #Reacive data from clinet or 
    #we r giving data to check male female
    if request.POST.get('action')=='post':
        long_hair = float(request.POST.get('long_hair'))
        forehead_width_cm = float(request.POST.get('forehead_width_cm'))
        forehead_height_cm = float(request.POST.get('forehead_height_cm'))
        nose_wide = float(request.POST.get('nose_wide'))
        nose_long = float(request.POST.get('nose_long'))
        lips_thin = float(request.POST.get('lips_thin'))
        distance_nose_to_lip_long = float(request.POST.get('distance_nose_to_lip_long'))
 

        model = pd.read_pickle(r"C:\Users\HP\Music\new_model1.pickle")
        result = model.predict([[long_hair,forehead_width_cm,forehead_height_cm,nose_wide,nose_long,lips_thin,distance_nose_to_lip_long]])

        gender = result[0]

        PredResults.objects.create(long_hair=long_hair, forehead_width_cm=forehead_width_cm, forehead_height_cm=forehead_height_cm,
                                   nose_wide=nose_wide,nose_long=nose_long,lips_thin=lips_thin,distance_nose_to_lip_long=distance_nose_to_lip_long,gender=gender)

        return JsonResponse({'result': gender, 'long_hair': long_hair, 'forehead_width_cm': forehead_width_cm, 'forehead_height_cm': forehead_height_cm,
                                   'nose_wide': nose_wide,'nose_long': nose_long,'lips_thin': lips_thin,'distance_nose_to_lip_long': distance_nose_to_lip_long},
                            safe=False)


#view result using results.html file
def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)

def contact(request):
    '''
    if request.method =='POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return HttpResponse("Save succesfully")'''
         

    return render (request, 'contact.html')
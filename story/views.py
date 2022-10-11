from lib2to3.pytree import convert
from urllib import response
from django.shortcuts import render
import requests
from django.http import HttpResponse, HttpResponseRedirect

import json

# Create your views here.

def showpage(request):
     return render(request,'boiler.html')

def fetch_api(request):
     api_key = '2dc8acb9c43a852b9c565557918c9e27'
     if request.method=='POST':
          query=request.POST['serch']
          movie_by_person=requests.get('https://api.themoviedb.org/3/search/person?api_key='+api_key+'&language=en-US&page=1&include_adult=false&query='+query).json()
          if movie_by_person['results']!=[]:
               person_id=movie_by_person['results'][0]['id']
               movie_of_per=requests.get('https://api.themoviedb.org/3/person/'+str(person_id)+'/movie_credits?api_key='+api_key+'&language=en-US').json()
               MOVI=movie_of_per['cast']
          if movie_by_person['results']==[]:
               return render(request,'boiler.html',{'msg':'plz give a vaild person'})
          return render(request,'boiler.html',{'res':MOVI})
      



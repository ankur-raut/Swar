from django.shortcuts import render
import pickle
import joblib
from .predict import recommend_songs
import pickle

with open('models\data.pickle', 'rb') as efile:
    data = pickle.load(efile)

# Create your views here.
def index(request):
    context={'a':1}
    return render(request,'index.html',context)

def songInput(request):
    name=request.POST['name']
    year=request.POST['year']
    year=int(year)
    d={}
    l=[]
    d['name']=name
    d['year']=year
    l.append(d)
    # print(type(l))
    print(recommend_songs(l,data))
    result=recommend_songs(l,data)
    # unique = list(result['Profession'].unique())

    return render(request,'index.html',{'result':result})

# recommend_songs([{'name': 'Blank Space', 'year':2014}], data)
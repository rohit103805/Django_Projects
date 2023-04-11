from django.shortcuts import render
from .models import Resume
import requests
import json

# Create your views here.

def home(request):
    return render(request, 'Home.html')

def capture_image(request):
    #part-1(5)
    about=request.POST['about']
    name=request.POST['identity']
    phone=int(request.POST['contact'])
    email=request.POST['gmail']
    links=request.POST['links_imp']
    #part-2(8)
    bachelors=request.POST['Bachelors']
    bcollege=request.POST['Bcollege']
    bpercent=request.POST['B_Percent']
    bpass=request.POST['B_Pass']
    stream=request.POST['Stream']
    school=request.POST['School']
    spercent=request.POST['S_Percent']
    spass=request.POST['S_Pass']
    #part-3(4)
    skill1=request.POST['sk1']
    skill2=request.POST['sk2']
    skill3=request.POST['sk3']
    skill4=request.POST['sk4']
    #part-4(4)
    exp1=request.POST['e1']
    exp2=request.POST['e2']
    exp3=request.POST['e3']
    exp4=request.POST['e4']
    try:
        ord = Resume.objects.create(phone=phone, about=about, name=name, email=email, links=links, bachelors=bachelors, bcollege=bcollege, bpercent=bpercent, bpass=bpass, stream=stream, school=school, spercent=spercent, spass=spass, skill1=skill1, skill2=skill2, skill3=skill3, skill4=skill4, exp1=exp1, exp2=exp2, exp3=exp3, exp4=exp4)
        return render(request, 'Capture_Image.html', {'phone': phone})
    except:
        person = Resume.objects.get(phone=phone)
        person.delete()
        ord = Resume.objects.create(phone=phone, about=about, name=name, email=email, links=links, bachelors=bachelors, bcollege=bcollege, bpercent=bpercent, bpass=bpass, stream=stream, school=school, spercent=spercent, spass=spass, skill1=skill1, skill2=skill2, skill3=skill3, skill4=skill4, exp1=exp1, exp2=exp2, exp3=exp3, exp4=exp4)
        return render(request, 'Capture_Image.html', {'phone': phone})

def about_me(request):
    return render(request, 'About Me.html')

def template_choose(request):
    phone=request.GET['phone']
    rec = Resume.objects.get(phone=phone)

    response = requests.get(f'https://resume-builder-c2b41-default-rtdb.firebaseio.com/{phone}.json')
    Dict = json.loads(response.text)
    #print(Dict)
    img = Dict[list(Dict.keys())[len(list(Dict.keys()))-1]]['uri']    
    #print(img)

    Skills=[]
    Skills.append(rec.skill1)
    Skills.append(rec.skill2)
    Skills.append(rec.skill3)
    Skills.append(rec.skill4)

    Exps=[]
    Exps.append(rec.exp1)
    Exps.append(rec.exp2)
    Exps.append(rec.exp3)
    Exps.append(rec.exp4)
    
    print(rec.name, rec.phone, rec.email)
    return render(request, 'Template.html', {'rec': rec, 'skills': Skills, 'exps': Exps, 'img': img})

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas
# Create your views here.

def home(request):
    return render(request,'home.html')

def regissue(request):
    mydata=Datas.objects.all()
    if(mydata!=''):
        return render(request,'issuetable.html',{'datas':mydata})
    else:
        return render(request,'issuetable.html')
    
def addData(request):
    if request.method=='POST':
        name=request.POST['name']
        issue_id=request.POST['issue_id']
        contact=request.POST['contact']
        issue=request.POST['issue']
        mail=request.POST['mail']
        
        obj=Datas()
        obj.Name=name
        obj.Issue_ID=issue_id
        obj.Issue=issue
        obj.Contact=contact
        obj.Mail=mail
        obj.save()
        mydata=Datas.objects.all()
        return redirect('regissue')
    return render(request,'issuetable.html')

def updateData(request,id):
    mydata=Datas.objects.get(id=id)
    if request.method=="POST":
        name=request.POST['name']
        issue_id=request.POST['issue_id']
        contact=request.POST['contact']
        issue=request.POST['issue']
        mail=request.POST['mail']

        mydata.Name=name
        mydata.Issue_ID=issue_id
        mydata.Issue=issue
        mydata.Contact=contact
        mydata.Mail=mail
        mydata.save()
        return redirect('regissue')
    return render(request,'update.html',{'data':mydata})

def deleteData(request,id):
    mydata=Datas.objects.get(id=id)
    mydata.delete()
    return redirect('regissue')
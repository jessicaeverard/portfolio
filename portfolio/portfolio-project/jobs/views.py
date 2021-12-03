from django.shortcuts import render, get_object_or_404 #get an object, if you cant find throw a 404
from .models import Job

def homepage(request):
    jobs = Job.objects #importing all the objects created in the model (class) job 
    return render(request, 'jobs/home.html', {'jobs':jobs}) #send back html when url is stated #dictionary is used when rendering items, name with what you what passed with the items

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id) #every model has a primary key
    return render(request, 'jobs/detail.html', {'job':job_detail})
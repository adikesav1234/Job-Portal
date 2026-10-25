from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
class JobListView(View):
    def get(self,request):
        jobs=[
        {
        "id": 1,
        "job_title": "Python Developer",
        "company_name": "TCS",
        "location": "Kochi",
        "salary": 35000,
        "job_type": "Full Time",
        "experience": "Fresher",
        "description": "Develop Python applications"
    },
    {
        "id": 2,
        "job_title": "Web Developer",
        "company": "Infosys",
        "location": "Bangalore",
        "salary": 40000,
        "experience": "1 Year"
    },
    {
        "id": 3,
        "job_title": "Data Analyst",
        "company": "Wipro",
        "location": "Chennai",
        "salary": 30000,
        "experience": "Fresher"
    },
     {
        "id": 4,
        "job_title": "UI UX Designer",
        "company_name": "Google",
        "location": "Hyderabad",
        "salary": 50000,
        "job_type": "Full Time",
        "experience": "2 Years",
        "description": "Design user-friendly interfaces"
    },
    {
        "id": 5,
        "job_title": "Digital Marketer",
        "company_name": "Zoho",
        "location": "Kochi",
        "salary": 25000,
        "job_type": "Internship",
        "experience": "Fresher",
        "description": "Manage digital marketing campaigns"
    }
        ]
        return JsonResponse(jobs,safe=False)

@method_decorator(csrf_exempt,name='dispatch')
class PeopleListView(View):
    def post(self,request):
        form_data=request.body
        data=loads(form_data)
        return JsonResponse(data)

    
        
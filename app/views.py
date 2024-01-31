from random import shuffle
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from app.models import Intership, JobPosting, WebsiteInfo


# Create your views here.
def first(req):
    website_info = WebsiteInfo.objects.first()
    service= Intership.objects.all()
    paginator = Paginator(service, 1)
    page_number = req.GET.get("page")
    job_info = paginator.get_page(page_number)
    total_page = job_info.paginator.num_pages
    records_count = Intership.objects.count()
    job_posting = JobPosting.objects.all()
    job_posting_count = JobPosting.objects.count()
    return render(req, "index.html", {
        'website_info': website_info,
        'job_info': job_info,
        'intern_count': records_count,
        'last_page': total_page,
        "totalpagelist": [n+1 for n in range(total_page)],
        'job_posting': job_posting,
        'job_count': job_posting_count
    })
    # website_info = WebsiteInfo.objects.first()
    # service= Intership.objects.all()
    # paginator=Paginator(service,2)
    # page_number=req.GET.get("page")
    # job_info=paginator.get_page(page_number)
    # total_page=job_info.paginator.num_pages
    # records_count = Intership.objects.count()
    # job_posting= JobPosting.objects.all()
    # job_posting_count= JobPosting.objects.count()
    # return render(req,"index.html",{'website_info': website_info,'job_info':job_info,'intern_count':records_count,'last_page':total_page,"totalpagelist":[n+1 for n in range(total_page)],'job_posting':job_posting,'job_count':job_posting_count})


def intern_only(req):
    service= Intership.objects.all()
    paginator=Paginator(service,2)
    page_number=req.GET.get("page")
    job_info=paginator.get_page(page_number)
    total_page=job_info.paginator.num_pages
    print(total_page)
    job_posting= JobPosting.objects.all()
    website_info = WebsiteInfo.objects.first()
    return render(req,"intern.html",{'job_info':job_info,'last_page':total_page,"totalpagelist":[n+1 for n in range(total_page)],'job_posting':job_posting,'website_info':website_info})


def job_page(req):
    return render(req,"job_page.html")

def about_page(req):
    website_info = WebsiteInfo.objects.first()
    return render(req,'about_page.html',{'logo':website_info})

def main_page(req,job_id):
    job_posting_content= Intership.objects.filter(custom_id=job_id)
    for internship in job_posting_content:
        internship.Requirments = internship.Requirments.split('.')
    Job_records = JobPosting.objects.all().order_by('id')[:10]
    job_posting_count= JobPosting.objects.count()
    Job_records3 = JobPosting.objects.all().order_by('id')[:3]
    return render(req,'job_page.html',{'job_posting_content':job_posting_content,'day_list': internship.Requirments,'Job_record':Job_records,'job_posting_count':job_posting_count,'Job_record3':Job_records3})

def main_page_job(req,id):
    job_posting_content= JobPosting.objects.filter(id=id)
    for jobPosting in job_posting_content:
        jobPosting.requirements = jobPosting.requirements.split('.')
    Job_records = JobPosting.objects.all().order_by('id')[:10]
    intern_records = Intership.objects.all().order_by('custom_id')[:10]
    job_posting_count= JobPosting.objects.count()
    job_intern_count= Intership.objects.count()
    sum=job_posting_count+job_intern_count
    return render(req,'job_page_for_job.html',{'job_posting_content':job_posting_content,"day_list": jobPosting.requirements,"intern_record":intern_records,'intern_count':job_intern_count,'job_count':job_posting_count,'sum':sum})
    

def all_job(req):
    website_info = WebsiteInfo.objects.first()
    job_records = JobPosting.objects.all()
    mixed_records =list(job_records)
    shuffle(mixed_records)
    paginator=Paginator(mixed_records,2)
    page_number=req.GET.get("page")
    job_info=paginator.get_page(page_number)
    total_page=job_info.paginator.num_pages
    job_posting= Intership.objects.all()
    return render(req,"all.html",{'website_info':website_info,'job_info':job_info,'last_page':total_page,"totalpagelist":[n+1 for n in range(total_page)],'job_posting':job_posting})


def fresher_only(req):
    service= JobPosting.objects.all()
    paginator=Paginator(service,2)
    page_number=req.GET.get("page")
    job_info=paginator.get_page(page_number)
    total_page=job_info.paginator.num_pages
    print(total_page)
    job_posting= Intership.objects.all()
    return render(req,"fresher.html",{'job_info':job_info,'last_page':total_page,"totalpagelist":[n+1 for n in range(total_page)],'job_posting':job_posting})


def search_data(req):
    search_text = req.POST.get('Search')
    print(search_text)
    jobs_by_company = JobPosting.objects.filter(company_name__icontains=search_text).order_by('published_date')
    mixed_records = list(jobs_by_company) 
    shuffle(mixed_records)
    for job in mixed_records:
        print(job.company_name, job.published_date)
    website_info = WebsiteInfo.objects.first()
    intern_posting= Intership.objects.all()
    return render(req,'search.html',{"mixed_records":mixed_records,"search":search_text,'website_info':website_info,'intern_posting':intern_posting})


    
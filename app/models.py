from django.db import models

# Create your models here.


# models.py
from django.db import models

class WebsiteInfo(models.Model):
    logo = models.ImageField(upload_to='static/img/')
    whatsapp_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    telegram_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    hero_text = models.CharField(max_length=255)
    hero_image = models.ImageField(upload_to='static/img/')
    aboutus_logo = models.ImageField(upload_to='static/img/',default='job_logo.png')
 
    def __str__(self):
        return "Website Information"
    
    
class Intership(models.Model):
    custom_id = models.AutoField(primary_key=True)
    Intership_Title=models.TextField()
    roale=models.TextField(default="devloper",blank=True, null=True)
    company_name= models.TextField() 
    published_date = models.DateTimeField(auto_now_add=True)
    published_time = models.DateTimeField(auto_now=True)
    photo_intership=models.ImageField(upload_to='static/img/intership_logo')
    Categary_post=models.TextField(max_length=50,default="fresher/experience",blank=True, null=True)
    Batch=models.CharField(max_length=40,default="Any",blank=True, null=True)
    Location=models.TextField(default="Not Specify")
    Last_day_apply=models.TextField(default="Not Specify",blank=True, null=True)
    Requirments=models.TextField(default="Bachelor’s degree in Computer Science or equivalent.Experience of Java and/or Javascript an advantage.Experience working within an Agile team an advantageFluent in English.High levels of curiosity and autonomy.Experience or knowledge of any of the following an advantage; SAP Lumira,.Experience or knowledge of any of the following an advantage; SAP Lumira, SAP Business Intelligence Platform, SAP BW, SAP HANA, SAP UI5.Preparation of unit tests.Communicate proactively, precisely & accurately.Interact with colleagues in a highly international environment.Demonstrated problem solving and solution building skills as well as the initiative to deliver results..Preparation of unit tests.You value teamwork and have excellent collaboration skills.",blank=True, null=True)
    streams=models.TextField(default="All streams/branches of B.E/B.Tech/M.E/M.Tech, MCA, and M.Sc. (CSE, IT only)",blank=True, null=True)
    Salary=models.CharField(max_length=20,default="Not Specify")
    Applly_link=models.URLField()

class JobPosting(models.Model):
    id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='static/img/jobposting', null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    experience = models.CharField(max_length=50,default="fresher/experience",blank=True, null=True)
    batch = models.CharField(max_length=50, default="Any",blank=True, null=True)
    job_location = models.CharField(max_length=255,default="Not Specify")
    last_day_to_apply = models.DateField(null=True, blank=True,default="__")
    requirements = models.TextField(default="Bachelor’s degree in Computer Science or equivalent.Experience of Java and/or Javascript an advantage.Experience working within an Agile team an advantageFluent in English.High levels of curiosity and autonomy.Experience or knowledge of any of the following an advantage; SAP Lumira,.Experience or knowledge of any of the following an advantage; SAP Lumira, SAP Business Intelligence Platform, SAP BW, SAP HANA, SAP UI5.Preparation of unit tests.Communicate proactively, precisely & accurately.Interact with colleagues in a highly international environment.Demonstrated problem solving and solution building skills as well as the initiative to deliver results..Preparation of unit tests.You value teamwork and have excellent collaboration skills.",blank=True, null=True)
    responsibilities = models.TextField(default="The responsibilities of a developer encompass a wide range of tasks throughout the software development lifecycle. Developers are primarily responsible for translating design specifications into functional and efficient code, often working collaboratively in a team. They need to possess a deep understanding of programming languages, frameworks, and development tools. Additionally, developers are tasked with debugging and troubleshooting issues, optimizing code for performance, and ensuring that the software meets quality standards through rigorous testing. Continuous learning is integral to staying updated with emerging technologies, enabling developers to adapt to evolving industry practices and contribute to the success of the projects they are involved in. Effective communication within the team and a commitment to delivering reliable and scalable solutions are crucial aspects of a developer's responsibilities.")
    position = models.CharField(max_length=50)  #inwhich tech they work means role
    salary = models.CharField(max_length=100,default="not disclosed")
    apply_link = models.URLField()

    def __str__(self):
        return self.job_title




from django.contrib import admin

from app.models import Intership, JobPosting, WebsiteInfo

# Register your models here.
class WebsiteInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'hero_text', 'logo_display', 'whatsapp_link', 'instagram_link', 'linkedin_link', 'telegram_link', 'github_link')

    def logo_display(self, obj):
        return f'<img src="{obj.logo.url}" width="50" height="50" />'
    logo_display.allow_tags = True
    logo_display.short_description = 'Logo'
admin.site.register(WebsiteInfo,WebsiteInfoAdmin)


class intership_list(admin.ModelAdmin):
    list_display = ('custom_id', 'Intership_Title', 'company_name', 'published_date', 'Location', 'Last_day_apply', 'streams', 'Salary', 'Applly_link')
    list_filter = ('Categary_post', 'Batch')  # Add filters for specific fields if needed
    search_fields = ('Intership_Title', 'company_name', 'Location')  # Add fields for searching if needed

admin.site.register(Intership, intership_list)

class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'company_name', 'published_date', 'last_day_to_apply','experience','position')
    search_fields = ('job_title', 'company_name')
    list_filter = ('category', 'experience', 'position', 'published_date')
admin.site.register(JobPosting, JobPostingAdmin)

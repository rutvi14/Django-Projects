from django.contrib import admin
from django.utils import timezone
from .models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['title','added_date','updated_date','is_published']
    search_fields = ['title','content'] #Add search bar in which you can filter out based on items specified in list
    ordering = ['title', '-updated_date']
    list_filter = ['is_published']
    prepopulated_fields = {'slug':['title']}
    readonly_fields = ['added_date', 'updated_date']
    date_hierarchy = 'updated_date'
    actions = ('make_published',)
    # fields = (      #Change layout of fields in field edit page.
    #   ('added_date','updated_date'),
    #   ('title','slug'),
    #   'content'
    #   )
    fieldsets = (
    (None, {'fields':(('added_date','updated_date'),), 'description':'Time Information'}),
    ('Must Properties', {'fields':('title','content'), 'description':'The object has to have these attributes'}),
    ('Nice to Have Properties', {'fields':(('slug','is_published'),), 'description':'If the object hasn\'t these attributes, they will be automatically generated'})
    ) #bifercate sections of fields.(Can't use fieldsets and fields together)

    def make_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f"{count} objects changed")
    make_published.short_description = 'Publish The Selected Blogs'



# admin.site.register(blog)
admin.site.site_title = 'Django Admin Panel Customization'
admin.site.site_header ='Django Admin Panel Customization'
admin.site.register(blog,BlogAdmin)

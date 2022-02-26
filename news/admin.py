from django.contrib import admin
from .models import Editor,Article,tags
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
    
admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
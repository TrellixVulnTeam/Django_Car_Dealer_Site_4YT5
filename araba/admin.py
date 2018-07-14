from django.contrib import admin
from .models import Araba
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    
    list_display= ['arabaismi','ilantarihi']
    search_fields=['arabaismi', 'ozellikler','ilantarihi']
    class Meta:
        model = Araba


admin.site.register(Araba, PostAdmin)

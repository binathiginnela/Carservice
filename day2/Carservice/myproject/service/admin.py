from django.contrib import admin
from service.models import Services,CarCategory,User

# Register your models here.
admin.site.register(Services)
admin.site.register(CarCategory)
admin.site.register(User)
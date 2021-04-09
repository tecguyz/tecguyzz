from django.contrib import admin
from . models import Trending, Latest, Featured, Deals
# Register your models here.

admin.site.register(Trending)
admin.site.register(Latest)
admin.site.register(Featured)
admin.site.register(Deals)



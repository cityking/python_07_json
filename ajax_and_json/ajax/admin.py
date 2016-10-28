from django.contrib import admin
from .models import Poem
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')
# Register your models here.
admin.site.register(Poem)

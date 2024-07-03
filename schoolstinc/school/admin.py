from django.contrib import admin
from .models import Department
from .models import Course
from .models import Enquiry
# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Enquiry)
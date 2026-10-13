from django.contrib import admin
from.models import CustomUserModel,TeacherModel,StudentBasicInfoModel,StudentEducationInfoModel
# Register your models here.
admin.site.register([CustomUserModel,TeacherModel,StudentBasicInfoModel,StudentEducationInfoModel])
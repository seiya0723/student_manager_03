from django.contrib import admin

from .models import Building,Student,Log

from .forms import LogAdminForm

from django.utils.html import format_html


class BuildingAdmin(admin.ModelAdmin):

    list_display    = ["id","name","dt","description","count_students","show_students_amount"]
    list_editable   = [ "name","dt","description" ]


    def show_students_amount(self,obj):
        return format_html('<div>' + str(obj.count_students()) + '</div>')

    show_students_amount.short_description      = "所属生徒数"


class StudentAdmin(admin.ModelAdmin):

    list_display    = ["id","name","dt","building"]
    list_editable   = [ "name","dt","building" ]


class LogAdmin(admin.ModelAdmin):
    #カスタムフォームを読み込む。
    form            = LogAdminForm

    list_display    = ["id","date","student","user"]

    list_editable   = ["date","student","user"]

    


admin.site.register(Building,BuildingAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Log,LogAdmin)


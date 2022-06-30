from django.shortcuts import render,redirect
from django.views import View

from .models import Building,Log,Student
from .forms import BuildingForm,LogForm

#DjangoMessageFrameworkをimport
from django.contrib import messages

#未ログインユーザーはアクセス拒否


#https://noauto-nolife.com/post/django-login-required-mixin/
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

import datetime

#LoginRequiredMixinを多重継承することで、未認証ユーザーをログインページへリダイレクトできる。
class IndexView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        context     = {}

        #DBからBuildingモデルのテーブルから全データを取り出す。(データは複数なので複数形)
        context["buildings"]    = Building.objects.all()
        context["today"]        = timezone.localdate()
        context["yesterday"]    = timezone.localdate() - datetime.timedelta(days=1)



        if "building" in request.GET:
            print(request.GET["building"])
            context["students"]     = Student.objects.filter(is_active=True,building=request.GET["building"]).order_by("dt")
        else:
            context["students"]     = Student.objects.filter(is_active=True).order_by("dt")

        return render(request,"student_management/index.html",context)

    def post(self, request, *args, **kwargs):

        #BuildingFormのオブジェクトを作る。(引数はPOSTメソッドで送信されたデータ全て)
        form    = BuildingForm(request.POST)

        #.is_valid()で、ここで入力されたデータが正しいかチェックしている
        #入力されたデータがルールに則っていれば、.is_valid()はTrueを返す
        if form.is_valid():
            print("バリデーションOK。書き込み")
            form.save()
        else:
            print("バリデーションNG")
            print(form.errors)
            #messages.error(request, form.errors)

        
        #TODO:この部分はビューを別にするべきかと
        copied          = request.POST.copy()
        copied["user"]  = request.user.id
        form            = LogForm(copied)

        #form    = LogForm(request.POST)

        if form.is_valid():
            print("バリデーションOK。書き込み")
            form.save()
        else:
            print("バリデーションNG")
            print(form.errors)
            #messages.error(request, form.errors)


        return redirect("student_management:index")

index   = IndexView.as_view()




#TODO:エクセルファイルを作ってDLさせる。
#https://noauto-nolife.com/post/startup-openpyxl/

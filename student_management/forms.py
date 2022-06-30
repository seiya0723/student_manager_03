from django import forms 

from .models import Building,Student,Log

#DBに書き込みする前のチェックとして、モデルを使用するフォームクラスを作るため、forms.ModelFormを継承
class BuildingForm(forms.ModelForm):
    
    #使用するモデルと、そのフィールドを指定する。
    class Meta:
        model   = Building

        #idは自動採番なので、クライアントが入力するものではない。
        #そのためバリデーション対象のフィールドとして指定する必要はない。
        #TODO:バリデーション対象のフィールドを選んで指定

        fields  = [ "name","description" ]


class LogForm(forms.ModelForm):

    class Meta:
        model   = Log
        fields  = ["date","student","user"]



#管理サイト専用のフォーム(デフォルトではis_activeがFalseの生徒まで選択できてしまう)
class LogAdminForm(forms.ModelForm):

    class Meta:
        model   = Log
        fields  = ["date","student","user"]

    #XXX:おそらくStudentモデルが変わるたびに下記はエラーを出してしまう。makemigrationsを受け付けない状態になる
    #↑admin.pyにて、このLogAdminFormを作る？

    #ChoiceFieldを使う。
    #https://www.geeksforgeeks.org/choicefield-django-forms/
    
    students            = Student.objects.filter(is_active=True).order_by("dt")
    student_choices     = []

    for s in students:
        row     = []
        row.append(s.id)
        row.append(s.name)

        student_choices.append(row)

    student     = forms.ChoiceField(choices=student_choices)





#モデルを使用しないタイプのフォームクラス。forms.Formを継承する。
"""
class YearForm(forms.Form):
    year    = IntegerField()
"""

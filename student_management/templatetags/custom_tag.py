#このcustom_tag.pyはカスタムテンプレートタグを格納するPythonファイル

from django import template
register = template.Library()

#このhello関数が、実際にテンプレート上で呼び出すカスタムテンプレートタグになる。
@register.simple_tag()
def hello():
    return "Hello"

#.simple_tag()のデコレータを使うことで、上記関数がカスタムテンプレートタグとして呼び出し可能になる。

import datetime


@register.simple_tag()
def print_date(date):

    print(date)

    #Pythonの日付の加減算処理
    date    = date - datetime.timedelta(days=1)
    return date


#第一引数は日付、第二引数はBuildingモデルクラスのオブジェクト
@register.simple_tag()
def select_date_log(date,building):

    #このlogsはLogモデルのオブジェクト
    logs    = building.logs_date(date)

    """
    for log in logs:
        print(log)
    """

    return logs


#TODO:この普通のカスタムテンプレートタグは文字列データしか返すことはできない(HTMLを返すことができない)
#もし、カスタムテンプレートタグの返り値をHTMLにしたい場合、埋め込み型カスタムテンプレートタグを作る必要がある。
@register.inclusion_tag("student_management/logs.html")
def select_date_log_html(date,building):

    #このlogsはLogモデルのオブジェクト

    context = {}
    context["logs"] = building.logs_date_custom(date)

    return context









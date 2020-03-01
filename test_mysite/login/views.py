from django.shortcuts import render,redirect
from . import models
# Create your views here.
def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "填写所有字段"
        if username and password:
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "密码错误"
            except:
                message = "用户不存在"
        return render(request, 'login/login.html', {"message": message})
    return render(request,'login/login.html')


def loginunsafe(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        import pymysql
        conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="django",charset="utf8")
        cursor = conn.cursor()
        sql_select = "select * from login_user where name = %s and password = %s" %(username,password)
        result = cursor.execute(sql_select)
        for row in cursor.fetchall():
            return redirect('/index/')
    else:
        return  render(request,'login/login.html')
def register(request):
    pass
    return render(request,'login/register.html')

def logout(request):
    pass
    return redirect('/index/')
from django.shortcuts import render, redirect, HttpResponse
from django.views import View


class LoginAuth(View):
    """登录验证"""

    def get(self,request):

        return render(request,'login.html')

    def post(self,request):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print(user,pwd)
        if user == 'root' and pwd == '123':

            request.session['username'] = user
            request.session['is_login'] = True
            if request.POST.get('mdr',None) == '1':
                # 设置超时时间，以秒为单位
                request.session.set_expiry(604800)  # 一周免登陆

            return redirect('/login/index/')
        else:
            return render(request,'login.html')

class Logout(View):
    def get(self,request):
        request.session.clear()

        return redirect('/login/')

class Index(View):

    def get(self,request):
        if request.session.get('is_login',None):
            return render(request, 'auth_index.html',{'username':request.session.get('username',None)})
        else:
            return HttpResponse('gun')
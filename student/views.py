from django.shortcuts import render,redirect
from django.views.generic import View,FormView,CreateView,TemplateView
from student.forms import StudentCreateForm,StudentLoginForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
# Create your views here.
class StudentCreateView(CreateView):
    # def get(self,request,*args,**kwargs):
    #     form_instance=StudentCreateForm()
    #     return render(request,"register.html",{"form":form_instance})
    # def post(self,request,*args,**kwargs):
    #     form_data=request.POST
    #     form_instance=StudentCreateForm(form_data)
    #     if form_instance.is_valid():
    #         form_instance.save()
    #         return redirect("student-register")
    #     return render(request,"register.html",{"form":form_instance})
    template_name="register.html"
    form_class=StudentCreateForm
    success_url=reverse_lazy("signin")

    
class StudentSigninView(FormView):
    template_name="signin.html"
    form_class=StudentLoginForm
    # def get(self,request,*args,**kwargs):
    #     form_instance=StudentLoginForm()
    #     return render(request,"signin.html",{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=StudentLoginForm(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            uname=data.get("username")
            pwd=data.get("password")        
            user_instance=authenticate(request,username=uname,password=pwd)
            if user_instance:
                login(request,user_instance)
                
                return redirect("index")
            else:
                return render(request,"signin.html",{"form":form_instance})
        else:
            return render(request,"signin.html",{"form":form_instance})
        
class IndexView(TemplateView):
    template_name="index.html"



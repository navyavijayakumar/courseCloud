from django.shortcuts import render,redirect
from django.views.generic import View
from student.forms import StudentCreateForm
# Create your views here.
class StudentCreateView(View):
    def get(self,request,*args,**kwargs):
        form_instance=StudentCreateForm()
        return render(request,"register.html",{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=StudentCreateForm(form_data)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("student-register")
        return render(request,"register.html",{"form":form_instance})
        
        
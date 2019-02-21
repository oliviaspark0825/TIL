from django.shortcuts import render, redirect
from .models import Student
# Create your views here.

def index(request):
    students = Student.objects.all()
    return render(request,'workshop19/index.html', {'students': students})
    
def new(request):
    return render(request, 'workshop19/new.html')

def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    
    
    student = Student(name=name, email=email, birthday=birthday, age=age)
    student.save()
    
    # 한줄 방법
    # board.objects.create(title=title, content=content)
  
    return redirect('/workshop19/')
def detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'workshop19/detail.html', {'student':student})
    
def delete(request,pk):
    student = Student.objects.get(pk=pk)
    # 오른쪽이 주소로 들어온 pk, # 왼쪽은 모델에 있는 pk
    student.delete()
    return redirect('/workshop19/')

def edit(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'workshop19/edit.html',{'student':student})
    
def update(request, pk):
    student = Student.objects.get(pk=pk)
    student.name = request.POST.get('name')
    student.email = request.POST.get('email')
    student.birthday = request.POST.get('birthday')
    student.age = request.POST.get('age')
    student.save()
    return redirect(f'/workshop19/{student.pk}/')
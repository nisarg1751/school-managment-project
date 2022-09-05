from django.shortcuts import render,HttpResponseRedirect
from student.forms import SignUpForm,UserForm,EditUserProfileForm,Marksform,EditOtherDetailForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from student.models import SignUpModel,Marks
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q
# Create your views here.


# Home Page 
def home(request):
    return render(request,'home.html')

# Signup Form
def signup(request):
    if request.method == 'POST':
        # usercreation form
        fm = SignUpForm(request.POST) 
        # second form
        fm1 = UserForm(request.POST,request.FILES)
        print('-----------------------FM1----------------------------------',fm1.is_valid())
        if fm.is_valid():
            fn = fm.cleaned_data['first_name']
            ln = fm.cleaned_data['last_name']
            em = fm.cleaned_data['email']
            password1 = fm.cleaned_data['password1']
            un = fm.cleaned_data['username']
            reg = User.objects.create_user(username= un,first_name = fn,last_name = ln,email = em,password = password1)
            reg.save()
            if fm1.is_valid():
                user_id = reg.id
                ph = request.POST.get('phone')
                me = request.POST.get('medium')
                image = request.FILES.get('image')
                video = request.FILES.get('video')
                stu = request.POST.getlist('study[]')
                y = ','.join(stu)
                reg1 = SignUpModel(phone=ph,medium=me,image=image,study=y,video=video,user_id = user_id)

                reg1.save()
            messages.success(request,'Your account created succesfully!!!')
            messages.info(request,'Now login and acceMarksss your account')
         
            fm  = SignUpForm()
            fm1 = UserForm()
            print(fm1.is_valid())
        else:
            messages.error(request,'please enter valid information')
    else:
        fm = SignUpForm()
        fm1 = UserForm()
    return render(request,'signup.html',{'form':fm,'form1':fm1,'x':request.user})

# Login Function
def login_form(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        # p = Paginator(user,5)
        # page_num = request.GET.get('page',1)
        # try:
        #     page = p.page(page_num)
        # except EmptyPage:
        #     page = p.page(1)

        if user is not None:
            login(request,user)
            teacher = User.objects.all()
            student = User.objects.all().exclude(is_staff = True)
            p = Paginator(student,5)
            p = Paginator(teacher,5)
            page_num = request.GET.get('page',1)
            page_num1 = request.GET.get('page1',1)
            try:
                page = p.page(page_num)
            except EmptyPage:
                page = p.page(1)
            # try:
            #     page1 = p.page(page_num1)
            # except EmptyPage:
            #     page1 = p.page(1)    
            if request.user.is_staff == True:
                return render(request,'data.html',{'user':page,'user1':page,'x':request.user})
            else:
                return render(request,'user.html',{'username':username})
        else:
            messages.error(request,'Please try again!!')
    else:
        fm = AuthenticationForm()
    return render(request,'login.html',{'form':fm})


# Logout Function
def logout_form(request):
    logout(request)
    return render(request,'home.html')

# Profile change form for user,teacher and pricipal
def userprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST,instance=request.user)
            print(request.user)
            user = User.objects.get(username=request.user)
            print(user) 
            if fm.is_valid:
                fm.save()
                messages.success(request,'Your detail updated successfully!!')
                if request.user.is_staff == True and request.user.is_superuser == True:
                    return HttpResponseRedirect('/data/')
                elif request.user.is_staff == True:
                    return HttpResponseRedirect('/data/')
                else:
                    return render(request,'user.html',{'username':request.user})
            else:
                messages.error(request,'Please try again')
                messages.info(request,'Enter valid details')
        else:
            fm = EditUserProfileForm(instance = request.user)
        return render(request,'info.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# showing all data
def data(request):
    user = User.objects.all()
    user1 = User.objects.all().exclude(is_staff = True)
    # paginator
    p = Paginator(user,5)
    c = p.num_pages
    d = p.page_range
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    # print(page)
    if request.method == 'POST':
        search = request.POST.get('search')
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',search)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',type(search))
        # se = User.objects.all().filter(username = search,first_name = search)
        que_set = (Q(username__icontains = search) | Q(first_name__icontains = search) | Q(last_name__icontains = search) | Q(email__icontains = search) | Q(id__icontains = search))
        se = User.objects.filter(que_set)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',que_set)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',se)
        return render(request,'data.html',{'search':se})

    return render(request,'data.html',{'user':page,'user1':page,'page_num':page_num,'c':c,'d':d})

# delete data function
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/data/')


# Update function for registration form
def updatedata(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = User.objects.get(pk=id)
            print('-----------------------PI ID---------------------',pi.id)
            fm = EditUserProfileForm(request.POST,instance =pi)
            try:
                pi1 = SignUpModel.objects.get(user_id = id)
                fm1 = EditOtherDetailForm(request.POST,instance=pi1)
            except:
                fm1 = EditOtherDetailForm(request.POST)
            if fm.is_valid():
                fm.save()
                if fm1.is_valid():
                    medium = request.POST['medium']
                    study = request.POST['study']
                    phone = request.POST['phone']
                    image = request.POST['image']
                    video = request.POST['video']
                    user_id = id
                    reg = SignUpModel(medium=medium,study=study,phone=phone,image=image,video=video,user_id = id)
                    reg.save()
                    messages.success(request,'data updated successfully!!')
                return HttpResponseRedirect('/data/')
            else:
                messages.error(request,'Something went wrong!!')
                return HttpResponseRedirect('userchange')
        else:
            pi = User.objects.get(pk=id)
            fm = EditUserProfileForm(instance =pi)
            try:
                pi1 = SignUpModel.objects.get(user_id = id)
                fm1 = EditOtherDetailForm(instance=pi1)
            except:
                fm1 = EditOtherDetailForm()
        return render(request,'update.html',{'form':fm,'form1':fm1})
    else:
        return HttpResponseRedirect('/login/')


# update function for marks
def marks(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = User.objects.get(pk=id)
            fm = Marksform(request.POST,instance =pi)
            if fm.is_valid():
                sci = request.POST['science']
                mat = request.POST['maths']
                hin = request.POST['hindi']
                eng = request.POST['english']
                user_id = pi.id
                reg = Marks(science=sci,maths=mat,hindi=hin,english=eng,marks_id=user_id)
                reg.save()
                messages.success(request,'data updated successfully!!')
                return HttpResponseRedirect('/data/')
            else:
                messages.error(request,'Something went wrong!!')
                return HttpResponseRedirect('userchange')
        else:
            pi = User.objects.get(pk=id)
            fm = Marksform(instance =pi)
        return render(request,'marks.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')


 
 




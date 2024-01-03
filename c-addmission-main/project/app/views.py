from django.shortcuts import render,redirect
from .models import * 
from random import randint 

# Create your views here.
def HomePage(request):
    return render(request,"app/Frontpage.html")


def AdmissionPage(request):
    return render(request,"app/Admission.html")


def SignupPage(request):
    return render(request, "app/signup.html")

def RegisterUser(request):
    fname = request.POST.get('firstname' , 'mydefaultvalue')
    lname = request.POST.get('lastname' , 'mydefaultvalue')
    email = request.POST.get('email' , 'mydefaultvalue')
    password = request.POST.get('password' , 'mydefaultvalue')
    cpassword = request.POST.get('cpassword', 'mydefaultvalue')

    user = UserMaster.objects.filter(email=email)
    
    if user :
        message = "User already exists"
        return render(request ,"app/login.html" , {'msg' : message})
    else:
        if(password==cpassword and password!=""):
           otp = randint(100000,999999)
           newuser=UserMaster.objects.create(otp = otp , email = email ,password=password)
           newcand=Can.objects.create(user_id=newuser , Firstname = fname , Lastname = lname ,)
           message = "User is registerd sucessfully "
           return render(request,"app/otppage.html" , {'msg':message} )
       
        
def OtpPage(request):
    return render(request, "app/otppage.html")

        
def OtpVerify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)

    if user :
        if user.otp == otp:
            message = "OTP verifed "
            return render(request, "app/login.html" ,{'msg' : message} )
        else:
            message = "OTP is incorrect"
            return render(request , "app/otppage.html" , {"msg" : message})
    else:
        return render(request,"app/signup.html")

def LoginPage(request):
    return render(request , "app/login.html")   


def LoginUser(request):
    email = request.POST['email']
    password = request.POST['password']

    user = UserMaster.objects.get(email=email)
    if user:
        if (user.password==password and password!=""):
            can = Can.objects.get(user_id = user)
            request.session['firstname']= can.Firstname
            request.session['lastname']= can.Lastname
            request.session['email']= user.email
            return redirect('home')
        else:
            message = "Password does not match"
            return render(request,"app/login.html" , {'msg' : message})
    else:
        message = "User does not exist"
        return render(request,"app/signup.html" , {'msg' : message})
    
def ProfilePage(request):
       user =UserMaster.objects.get(email=request.session['email'])
       can = Can.objects.get(user_id= user)
       return render(request, "app/Admission.html" , {'user':user , 'can':can})


def UpdateProfile(request):
    pk=request.session['email']
    user =UserMaster.objects.get(email=pk)
    can = Can.objects.get(user_id= user)
    can.merit_no=request.POST['merit_no']
    can.mht_cet=request.POST['mht-cet-jee']
    can.seat_no_hsc=request.POST['seat_no_hsc']
    can.marks_hsc=request.POST['marks_hsc']
    can.percentage_hsc=request.POST['percentage_hsc']
    can.name_of_board=request.POST['name_of_board']
    can.prev_clg_name=request.POST['prev_clg_name']

    can.stud_photo = request.FILES.get('pic')
    can.sign_photo = request.FILES.get('pic2')

    can.name=request.POST['stud_name']
    can.surname=request.POST.get('stud_surname')
    can.fathers_name=request.POST.get('father_name')
    can.mothers_name=request.POST['mother_name']
    can.parents_full_name=request.POST['parent_name']
    can.paddress=request.POST['p_add']
    can.pstate=request.POST['pstate']
    can.pdistrict=request.POST['pdistrict']
    can.ppincode=request.POST['ppincode']
    can.occupation=request.POST['occupation']
    can.yearly_income=request.POST['Yearly_income']
    can.pmobile=request.POST['parent_moblie']

    can.laddress=request.POST['local_add']
    can.lstate=request.POST['loc_add_state']
    can.ldistrict=request.POST['loc_add_district']
    can.lpincode=request.POST['loc_add_pincode']

    can.stud_email=request.POST['student_email']

    can.stud_mob=request.POST['student_mobile']

    can.place_of_birth=request.POST['place_of_birth']
    

    can.nationality=request.POST['nationality']

    can.mhstate=request.POST['other_state']

    can.religion=request.POST['religion']

    can.category=request.POST['category']

    can.cast=request.POST['cast']

    can.pcm_mrks=request.POST['pcm_total']

    can.phy_mrks=request.POST['physics']
    can.chem_mrks=request.POST['chemistry']
    can.maths_mrks=request.POST['maths']
    can.other_mrks=request.POST['other_marks']

    can.total_fees=request.POST['total_fees']
    can.recipt_no=request.POST['receipt_no']

    can.adhar_no=request.POST['adhar_no']
    can.pan_no=request.POST['pan_no']

    can.s_board=request.POST['s_board']
    can.s_year_of_passing=request.POST.get('s_year_of_passing' , 2019)
    can.s_mrks=request.POST['s_mrks']
    can.s_outof=request.POST['s_outof']
    can.s_percentage=request.POST['s_percentage']

    can.h_board=request.POST['h_board']
    can.h_year_of_passing=request.POST['h_year_of_passing']
    can.h_mrks=request.POST['h_mrks']
    can.h_outof=request.POST['h_outof']
    can.h_percentage=request.POST['h_percentage']

    can.hostel_fees=request.POST['hostel_fees']
    can.recipt=request.POST['hostel_receipt']
    can.save()
   # url = f'/submit/{pk}'
    return redirect('undertaking')

def AboutusPage(request):
    return render(request, "app/aboutus.html")

def UnderTakingPage(request):
    return render(request, "app/undertaking.html")


def Undertaking_name(request):
    u_name = request.POST.get('name_u','default')
    newuser = Undertaking.objects.create(uname=u_name)
    return render(request,"app/doc_upload.html")


def DocUpload(request):
    pk=request.session['email']
    user =UserMaster.objects.get(email=pk)
    can = Can.objects.get(user_id= user)
    can.allotment_photo=request.FILES.get('uploadfile1' )
    can.mht_cet_photo=request.FILES.get('uploadfile2' )
    can.ssc_photo=request.FILES.get('uploadfile3' )
    can.hsc_photo=request.FILES.get('uploadfile4')
    can.adhar_photo=request.FILES.get('uploadfile5')
    can.caste_photo=request.FILES.get('uploadfile6')
    can.c_validity_photo=request.FILES.get('uploadfile7')
    can.save()
    return render(request, "app/fees.html")


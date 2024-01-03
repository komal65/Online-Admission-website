from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    is_active = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=True)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

class Can(models.Model):
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE,null=True)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    merit_no = models.BigIntegerField(null=True)
    mht_cet = models.BigIntegerField(null=True)
    seat_no_hsc = models.BigIntegerField(null=True)
    marks_hsc = models.BigIntegerField(null=True)
    percentage_hsc = models.IntegerField(null=True)
    name_of_board = models.CharField(max_length=50,null=True)
    prev_clg_name = models.CharField(max_length=50,null=True)
    stud_photo = models.ImageField(upload_to="app/images",null=True)
    sign_photo = models.ImageField(upload_to="app/images",null=True)

    name = models.CharField(max_length=50,null=True)
    surname = models.CharField(max_length=50,null=True)
    fathers_name = models.CharField(max_length=50,null=True)
    mothers_name = models.CharField(max_length=50,null=True)
    parents_full_name = models.CharField(max_length=50,null=True)
    paddress = models.CharField(max_length=80,null=True)
    pstate = models.CharField(max_length=50,null=True)
    pdistrict =models.CharField(max_length=50,null=True)
    ppincode = models.IntegerField(null=True)
    occupation = models.CharField(max_length=50,null=True)
    yearly_income = models.BigIntegerField(null=True)
    pmobile = models.BigIntegerField(null=True)

    laddress = models.CharField(max_length=100,null=True)
    lstate = models.CharField(max_length=50,null=True)
    ldistrict =models.CharField(max_length=50,null=True)
    lpincode = models.IntegerField(null=True)

    stud_email = models.CharField(max_length=50,null=True)

    stud_mob = models.BigIntegerField(null=True)

    place_of_birth = models.CharField(max_length=50,null=True)

    nationality = models.CharField(max_length=50,null=True)

    mhstate = models.CharField(max_length=50,null=True)

    religion = models.CharField(max_length=50,null=True)

    category =models.CharField(max_length=50,null=True)

    cast = models.CharField(max_length=50,null=True)

    pcm_mrks = models.BigIntegerField(null=True)

    phy_mrks =models.BigIntegerField(null=True)
    chem_mrks = models.BigIntegerField(null=True)
    maths_mrks = models.BigIntegerField(null=True)
    other_mrks = models.BigIntegerField(null=True)

    total_fees = models.BigIntegerField(null=True)
    recipt_no = models.BigIntegerField(null=True)

    adhar_no = models.IntegerField(null=True)
    pan_no = models.IntegerField(null=True)

    s_board = models.CharField(max_length=50,null=True)
    s_year_of_passing = models.BigIntegerField(null=True)
    s_mrks = models.IntegerField(null=True)
    s_outof = models.IntegerField(null=True)
    s_percentage = models.IntegerField(null=True)

    h_board = models.CharField(max_length=50,null=True)
    h_year_of_passing = models.BigIntegerField(null=True)
    h_mrks = models.BigIntegerField(null=True)
    h_outof = models.IntegerField(null=True)
    h_percentage = models.IntegerField(null=True)

    hostel_fees = models.BigIntegerField(null=True)
    recipt = models.BigIntegerField(null=True)


    allotment_photo = models.FileField(upload_to="app/images/{}".format(stud_email),null=True)
    mht_cet_photo = models.FileField(upload_to="app/images/{}".format(stud_email),null=True)
    ssc_photo = models.FileField(upload_to="app/images/{}".format(stud_email),null=True)
    hsc_photo = models.FileField(upload_to="app/images/{}".format(stud_email),null=True)
    adhar_photo = models.FileField(upload_to="app/images/{}".format(stud_email),null=True)
    caste_photo = models.FileField(upload_to="app/images/{}".format(stud_email),null=True)
    c_validity_photo = models.FileField(upload_to="app/images/{}".format(stud_email),null=True)
    

class Undertaking(models.Model):
    uname = models.CharField(max_length=20)




        

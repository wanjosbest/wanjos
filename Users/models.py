from django.db import models
from django.contrib.auth.models import AbstractUser




#tutor register
class User(AbstractUser):
    
    email = models.EmailField(null =True, unique=True, max_length=100)
    address=models.CharField(max_length=300,null=True,blank=True)
    is_tutor=models.BooleanField(verbose_name="Tutor Status",null=True,default=True)
    # include this for a while
    is_student = models.BooleanField(verbose_name="Student Status",null=True)

    class Meta:
        verbose_name="Users"
        verbose_name_plural="Users"

    def __str__(self):
        return self.username
    

    
## add courses
class available_Courses(models.Model):
    author = models.ForeignKey(User, related_name="tutoraddcourse",on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=30,null=True)
    slug=models.SlugField(max_length=20,null=True)

    class Meta:
        verbose_name="available_Courses"
        verbose_name_plural="available Courses"
        
    def __str__(self):
        return self.title
#add course module
class coursemodule(models.Model):
    course = models.ForeignKey(available_Courses, null=True, related_name="availablecoursemodules", on_delete=models.CASCADE)
    module = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.module



    
#tutor to add live classes

class liveclass(models.Model):
   #  course = models.ForeignKey(available_Courses, related_name="liveclasscourse",on_delete=models.CASCADE,null=True)
     class_name=models.CharField(max_length=100,null=True,blank=False)
     class_description=models.TextField(max_length=1000,verbose_name="About the Live Class",null=True)
     class_link=models.CharField(max_length=255,unique=True,null=True,blank=False)
     def __str__(self):
         return self.class_name
     
#student attendance 

class studentatten(models.Model):
    student_email=models.EmailField(max_length=100, unique=True,null=True, verbose_name ="Student Email") 
    course_code = models.ForeignKey(coursemodule, related_name="courseattendance",on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=10,choices=(('P','PRESENT'),('A','ABSENT')),default='PRESENT')
    entry_time = models.DateTimeField( null=True, auto_now_add = True, auto_now = False,blank=True)
    #student_name = models.ForeignKey(User, related_name="userattendance",on_delete=models.CASCADE,null=True)

    def __str__(self):
       return f"{self.course_code}  {self.student_name} "
    
    class Meta:
        verbose_name="studentattendance"
        verbose_name_plural="Student Attendance"
 
  

class sturegistercourse(models.Model):
    course=models.ForeignKey(available_Courses, related_name="sturegcoursename",null=True, on_delete=models.CASCADE)
    email=models.CharField(max_length=50, null=True, unique=True)
    FirstName=models.CharField(max_length=50, null=True)
    LastName=models.CharField(max_length=50, null=True)
    date = models.DateTimeField(null=True, auto_now_add=True, auto_now=False)
    def __str__(self):
        return f' {self.FirstName} {self.LastName} {self.course}'


#password reset 

    

class anouncement(models.Model):
    Tutor = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=255, null=True,unique=True)
    content = models.TextField(null=True)
    date = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f'{self.title} By {self.Tutor}'
    
#Tutor create assignment and class work
class CreateAssignment(models.Model):
    Tutor = models.CharField(max_length=20, null=True)
    course= models.ForeignKey(available_Courses, related_name="createassginmentcourse", null=True,on_delete=models.CASCADE)
    title =models.CharField(max_length=255, null=True,unique=True)
    content = models.TextField(null=True)
    date = models.DateTimeField(null=True, auto_now=True)


    def __str__(self):
       return f'{self.title} assignment for {self.course}'
    
# add course timetable schedules

class coursetimetable(models.Model):
    course=models.ForeignKey(coursemodule, related_name="timetablecourse", null=True,on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    link = models.CharField(max_length=255,null=True)
      
    def __str__(self):
        return f'{self.course} {self.date}'

#add exam for courses
    
class examtimetable(models.Model):
    course=models.ForeignKey(coursemodule, related_name="timetableexam", null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    link = models.CharField(max_length=255,null=True)
      
    def __str__(self):
        return f'{self.course} {self.date}'


class PaystackPayment(models.Model):
    reference = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)






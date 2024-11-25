from rest_framework import serializers

from .models import User,available_Courses,liveclass,studentatten,sturegistercourse,anouncement,CreateAssignment,coursetimetable,examtimetable
from .models import User,available_Courses,liveclass,studentatten
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .models import PaystackPayment

class PaystackPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaystackPayment
        fields = ['reference', 'amount', 'paid']

class REGAPISerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)

    class Meta:
        model=User
        fields=("id","first_name","last_name","username","email","password","address","is_active","is_student","is_staff","is_tutor","is_superuser",)
     
    def create(self, validated_data):
        user = super(REGAPISerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class available_Courses_registrationserialization(serializers.ModelSerializer):
    class Meta:
        model=available_Courses
        fields=("id","title","slug","author",)


class liveclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = liveclass
        fields = ("class_name","class_description","class_link",)

# student attendance

class studentattendanceSerializer(serializers.ModelSerializer):
      class Meta:
          model =studentatten
          fields =("student_email","course_code","status",)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

#Reset password 



#student register course
class sturegistercourseSerializer(serializers.ModelSerializer):
      class Meta:
          model =sturegistercourse
          fields =("id",)


#tutor and admin add anouncements
class anouncementSerializer(serializers.ModelSerializer):
      class Meta:
          model =anouncement
          fields =("id","title","content",)

#tutor create assignment and class work
class CreateAssignmentSerializer(serializers.ModelSerializer):
      class Meta:
          model =CreateAssignment
          fields =("id","title","content","course")






#tutor and admin add class timetable

class coursetableSerializer(serializers.ModelSerializer):
      class Meta:
          model = coursetimetable
          fields = ("id","course","date","time","link",)

#exams timetable
class examtableSerializer(serializers.ModelSerializer):
      class Meta:
          model = examtimetable
          fields = ("id","title","course","date","time","link",)



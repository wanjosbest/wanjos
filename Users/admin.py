from django.contrib import admin

from .models import User,available_Courses,liveclass,studentatten,sturegistercourse,anouncement,CreateAssignment,coursetimetable,coursemodule,examtimetable

from .models import User,available_Courses,liveclass,studentatten


admin.site.register(User)

class available_CoursesAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
admin.site.register(available_Courses,available_CoursesAdmin)


admin.site.register(liveclass)
admin.site.register(studentatten)

admin.site.register(sturegistercourse)
admin.site.register(anouncement)
admin.site.register(CreateAssignment)
admin.site.register(coursetimetable)
admin.site.register(coursemodule)
admin.site.register(examtimetable)



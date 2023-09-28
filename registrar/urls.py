from django.urls import re_path, include

from registrar.views import courses
from registrar.views import enrollment
from registrar.views import teaching
from registrar.views import transcript
from registrar.views import certificate
from student.views import quickoverview
# from registrar.views import payment
app_name="registrar"
urlpatterns = [
    # Courses
    re_path(r'^courses$', courses.courses_page , name='courses'),
    re_path(r'^courses/(?P<category_slug>[-\w]+)/$', courses.courses_page, name='courses_list_by_category'),
    re_path(r'^course/(\d+)/$', courses.course_detail ,name='course_detail'),
    re_path(r'^enroll/(?P<id>\d+)/$', courses.enroll_course , name='enroll' ),

    re_path(r'^course/(\d+)/$', quickoverview.quickoverviews_page, name='quickoverview_page'),

    # Enrollment(s)
    re_path(r'^view/profile/enrollment$', enrollment.enrollment_page),
    re_path(r'^view/profile/', enrollment.enrollment_table),
    re_path(r'^view/profile/', enrollment.disenroll_modal),
    re_path(r'^view/profile/', enrollment.disenroll),
    re_path(r'^enrollment$', enrollment.enrollment_page),
    re_path(r'^enrollment_table$', enrollment.enrollment_table),
    re_path(r'^disenroll_modal$', enrollment.disenroll_modal),
    re_path(r'^disenroll', enrollment.disenroll),
         
    # Teaching
    re_path(r'^teaching$', teaching.teaching_page),
    re_path(r'^refresh_teaching_table$', teaching.refresh_teaching_table),
                       
    re_path(r'^course_modal$', teaching.course_modal),
    re_path(r'^save_course$', teaching.save_course),
    re_path(r'^delete_course_modal$', teaching.delete_course_modal),
    re_path(r'^course_delete$', teaching.course_delete),
                    
    # Transcript
    re_path(r'^view/profile/$', transcript.transcript_page),
    re_path(r'^transcript$', transcript.transcript_page),
                       
    # Certificate(s)
    re_path(r'^certificates$', certificate.certificates_page),
    re_path(r'^certificates_table$', certificate.certificates_table),
    re_path(r'^change_certificate_accessiblity$', certificate.change_certificate_accessiblity),
    re_path(r'^certificate/(\d+)$', certificate.certificate_page),
    re_path(r'^certificate_permalink_modal$', certificate.certificate_permalink_modal),
    # re_path(r'^allcourse/', payment.index, name='index'),
    # re_path(r'^course/<int:course_id>/',payment.show_course, name='course_detail'),
    # re_path(r'^cart/', payment.show_cart, name='show_cart'),
    # re_path(r'^checkout/', payment.checkout, name='checkout'),
    # re_path(r'^process-payment/', payment.process_payment, name='process_payment'),
    # re_path(r'^payment-done/', payment.payment_done, name='payment_done'),
    # re_path(r'^payment-cancelled/', payment.payment_canceled, name='payment_cancelled'),
    # re_path(r'^paypal/', include('paypal.standard.ipn.urls')),
    


]



from django.urls import  path, re_path

from . import views

# Import custom views.
from student.views import announcement
from student.views import syllabus
from student.views import policy
from student.views import lecture
from student.views import lecture_note
from student.views import assignment
from student.views import quiz
from student.views import exam
from student.views import discussion
from student.views import peer_review
from student.views import credit
from student.views import quickoverview
from student.views import module
from student.views import module_unit
app_name="student"
urlpatterns = [
    # Announcement
    re_path(r'^course/(?P<id>\d+)/announcements$', announcement.announcements_page, name='announcements_page'),

    # Syllabus
    re_path(r'^course/(\d+)/syllabus$', syllabus.syllabus_page, name='syllabus_page'),
        
    #quickoverview
    re_path(r'^course/(\d+)/quickoverview$', quickoverview.quickoverviews_page, name='quickoverview_page'),

   #modules
    
    re_path(r'^course/(\d+)/modules$', module.modules_page),
    re_path(r'^course/(\d+)/module$', module.module),
    #units
    re_path(r'^course/(\d+)/module/(\d+)/units$', module_unit.module_units_page),
    re_path(r'^course/(\d+)/module/(\d+)/view_module_unit$', module_unit.view_module_unit),
    # Grades & Policy
    re_path(r'^course/(\d+)/policy$', policy.policy_page),

    # Lecture
    re_path(r'^course/(\d+)/lectures$', lecture.lectures_page),
    re_path(r'^course/(\d+)/lecture$', lecture.lecture),
    re_path(r'^shortcourse/(\d+)/lectures$', lecture.shortcourselectures_page),
    re_path(r'^shortcourse/(\d+)/shortcourselecture$', lecture.shortcourselecture),
                       
                       
    # Lecture Notes
    re_path(r'^course/(\d+)/lecture/(\d+)/notes$', lecture_note.lecture_notes_page),
    re_path(r'^course/(\d+)/lecture/(\d+)/view_lecture_note$', lecture_note.view_lecture_note),

    # Assignment(s)
    re_path(r'^course/(\d+)/assignments$', assignment.assignments_page),
    re_path(r'^course/(\d+)/assignments_table$', assignment.assignments_table),
    re_path(r'^course/(\d+)/delete_assignment$', assignment.delete_assignment),
                       
    # Assignment
    re_path(r'^course/(\d+)/assignment/(\d+)$', assignment.assignment_page),
    re_path(r'^course/(\d+)/assignment/(\d+)/submit_assignment$', assignment.submit_assignment),
    re_path(r'^course/(\d+)/assignment/(\d+)/submit_e_assignment_answer$', assignment.submit_e_assignment_answer),
    re_path(r'^course/(\d+)/assignment/(\d+)/submit_mc_assignment_answer$', assignment.submit_mc_assignment_answer),
    re_path(r'^course/(\d+)/assignment/(\d+)/submit_tf_assignment_answer$', assignment.submit_tf_assignment_answer),
    re_path(r'^course/(\d+)/assignment/(\d+)/submit_r_assignment_answer$', assignment.submit_r_assignment_answer),
                       
    # Quiz(zes)
    re_path(r'^course/(\d+)/quizzes$', quiz.quizzes_page),
    re_path(r'^course/(\d+)/quizzes_table$', quiz.quizzes_table),
    re_path(r'^course/(\d+)/quiz_delete$', quiz.delete_quiz),
                       
    # Quiz
    re_path(r'^course/(\d+)/quiz/(\d+)$', quiz.quiz_page),
    re_path(r'^course/(\d+)/quiz/(\d+)/submit_quiz$', quiz.submit_quiz),
    re_path(r'^course/(\d+)/quiz/(\d+)/submit_tf_quiz_answer$', quiz.submit_tf_assignment_answer),

    # Exam(s)
    re_path(r'^course/(\d+)/exams$', exam.exams_page),
    re_path(r'^course/(\d+)/exams_table$', exam.exams_table),
    re_path(r'^course/(\d+)/delete_exam$', exam.delete_exam),
                       
    # Exam
    re_path(r'^course/(\d+)/exam/(\d+)$', exam.exam_page),
    re_path(r'^course/(\d+)/exam/(\d+)/submit_exam$', exam.submit_exam),
    re_path(r'^course/(\d+)/exam/(\d+)/submit_mc_exam_answer$', exam.submit_mc_exam_answer),

    # Peer-Review
    re_path(r'^course/(\d+)/peer_reviews$', peer_review.peer_reviews_page),
    re_path(r'^course/(\d+)/peer_review/(\d+)$', peer_review.assignment_page),
    re_path(r'^course/(\d+)/peer_review/(\d+)/peer_review_modal$', peer_review.peer_review_modal),
    re_path(r'^course/(\d+)/peer_review/(\d+)/save_peer_review$', peer_review.save_peer_review),
    re_path(r'^course/(\d+)/peer_review/(\d+)/delete_peer_review$', peer_review.delete_peer_review),
    re_path(r'^course/(\d+)/peer_review/(\d+)/update_assignment_marks$', peer_review.update_assignment_marks),
                       
    # Discussion
    re_path(r'^course/(\d+)/discussion$', discussion.discussion_page),
    re_path(r'^course/(\d+)/threads_table$', discussion.threads_table),
    re_path(r'^course/(\d+)/new_thread$', discussion.new_thread_modal),
    re_path(r'^course/(\d+)/insert_thread$', discussion.insert_thread),
    re_path(r'^course/(\d+)/delete_thread$', discussion.delete_thread),                   
    re_path(r'^course/(\d+)/thread/(\d+)$', discussion.thread_page),
    re_path(r'^course/(\d+)/thread/(\d+)/posts_table$', discussion.posts_table),
    re_path(r'^course/(\d+)/thread/(\d+)/new_post$', discussion.new_post_modal),
    re_path(r'^course/(\d+)/thread/(\d+)/insert_post$', discussion.insert_post),
                       
    # Credit
    re_path(r'^course/(\d+)/credit$', credit.credit_page),
    re_path(r'^course/(\d+)/submit_credit_application$', credit.submit_credit_application),
]

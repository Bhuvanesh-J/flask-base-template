from flask import Blueprint
from flask import request
from student.models import Student
from .views import student_operations

students = Blueprint('student-api', __name__, url_prefix='/api/v1/student_controller/')
# from student.models import Student


@students.route('student', methods=['GET', 'POST'])
# @students.route('student/<id>', methods=['GET', 'PUT', 'DELETE'])
def student_operation(id=None):
    student = Student.query.all()
    return student_operations(request, id)

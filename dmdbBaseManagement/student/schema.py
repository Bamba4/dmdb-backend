from graphene import List, Field, Int, ObjectType, Argument
from graphql import GraphQLError

from .type import StudentType
from .mutation import CreateStudent, DeleteStudent, UpdateStudent
from dmdbBaseManagement.models import Student

# Query


class StudentQuery(ObjectType):
    students = List(StudentType)
    student = Field(StudentType, student_id = Argument(Int, required=True))

    def resolve_students(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to get all Student!")
        return Student.objects.all()

    def resolve_student(self, info, student_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to get a Student!")
        return Student.objects.get(id=student_id)


class StudentMutation(ObjectType):
    create_student = CreateStudent.Field()
    update_student = UpdateStudent.Field()
    delete_student = DeleteStudent.Field()

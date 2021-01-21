from graphene import Mutation, Field, Int

from dmdbBaseManagement.employe.helper import serializerEmployee
from dmdbBaseManagement.serializers.serializer import StudentSerializer
from .type import StudentType, StudentInput
from graphql import GraphQLError
from dmdbBaseManagement.models import Student, Tutor, GodParent


class CreateStudent(Mutation):
    student = Field(StudentType)

    class Arguments:
        student = StudentInput()
    
    def mutate(self, info, **args):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to add a Student!")
        #TODO manage error handling
        try:
            tutor = Tutor.objects.get(id=args.get('student').get('tutor_id'))
        except:
            raise GraphQLError("Tutor with id {} does not exist".format(args.get('student').get('tutor_id')))
        try:
            god_parent = GodParent.objects.get(id=args.get('student').get('god_parent_id'))
        except:
            raise GraphQLError("GodParent with id {} does not exist".format(args.get('student').get('god_parent_id')))
        student = Student(tutor=tutor, god_parent=god_parent, **args.get('student'))
        serializer = serializerEmployee(data=student, modelSerializer=StudentSerializer)
        if serializer.is_valid(raise_exception=True):
            student.save()
            return CreateStudent(student=student)


class UpdateStudent(Mutation):
    student = Field(StudentType)

    class Arguments:
        student = StudentInput()

    def mutate(self, info, **args):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to update a Student!")
        old_student = Student.objects.get(id=args.get('student').get("id"))
        try:
            tutor = Tutor.objects.get(id=args.get('student').get('tutor').get('id'))
        except:
            raise GraphQLError("Tutor with id {} does not exist".format(args.get('student').get('tutor_id')))
        try:
            god_parent = GodParent.objects.get(id=args.get('student').get('god_parent_id'))
        except:
            raise GraphQLError("GodParent with id {} does not exist".format(args.get('student').get('god_parent_id')))
        old_student.__dict__.update(args.get('student'))
        old_student.tutor = tutor
        old_student.god_parent = god_parent
        serializer = serializerEmployee(data=old_student, modelSerializer=StudentSerializer)
        if serializer.is_valid(raise_exception=True):
            old_student.save()
            return UpdateStudent(student=old_student)


class DeleteStudent(Mutation):
    student_id = Int()

    class Arguments:
        student_id = Int(required=True)

    def mutate(self, info, student_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to delete a Student!")
        student = Student.objects.get(id=student_id)
        student.delete()
        return DeleteStudent(student_id=student_id)

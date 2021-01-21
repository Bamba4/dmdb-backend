from graphene import  String, DateTime, InputObjectType, Int

from dmdbBaseManagement.godParent.type import GodParentInput
from dmdbBaseManagement.models import Student
from graphene_django import DjangoObjectType

from dmdbBaseManagement.tutor.type import TutorInput


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class StudentInput(InputObjectType):
    id = Int()
    first_name = String()
    last_name = String()
    address = String()
    date_of_birth = DateTime()
    surate = String()
    joined_at = DateTime()
    avatar = String()
    god_parent_id = Int()
    tutor_id = Int()
    tutor = TutorInput()
    god_parent = GodParentInput()

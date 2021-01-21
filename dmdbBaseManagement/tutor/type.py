from graphene import  String, InputObjectType, DateTime, Int
from graphene_django import DjangoObjectType
from dmdbBaseManagement.models import Tutor


class TutorType(DjangoObjectType):
    class Meta:
        model = Tutor


class TutorInput(InputObjectType):
    id = Int()
    first_name = String()
    last_name = String()
    address = String()
    date_of_birth = DateTime()

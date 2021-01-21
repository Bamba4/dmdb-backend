from graphene_django import DjangoObjectType
from dmdbBaseManagement.models import Employee
from graphene import ObjectType, List, Mutation, Field, String, InputObjectType, Int, Argument, DateTime


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee


class InputEmployee(InputObjectType):
    id = Int()
    first_name = String()
    last_name = String()
    address = String()
    date_of_birth = DateTime()
    role = String()
    phone_number = String()
    email = String()
    avatar = String()

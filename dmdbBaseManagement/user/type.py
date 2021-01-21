from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from graphene import String, InputObjectType


class UserType(DjangoObjectType):
    """
        User generate by django
    """
    class Meta:
        model = get_user_model()


class InputUser(InputObjectType):
    """
        Input for to create and update a user
    """
    username = String()
    password = String()
    email = String()
    first_name = String()
    last_name = String()

from graphene import ObjectType, List, Mutation, Field, String, InputObjectType, Int, Argument
from django.contrib.auth import get_user_model
from .type import UserType
from .type import InputUser


class CreateUser(Mutation):
    """
        Create a new user
        @method: Post in REST API
    """
    user = Field(UserType)

    class Arguments:
        username = String(required=True)
        password = String(required=True)
        email = String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(username=username, email=email)
        user.set_password(password)
        user.save()
        return CreateUser(user=user)


class UpdateUser(Mutation):
    """
        Update a user
        @method: Put in REST API
    """
    user = Field(UserType)
    
    class Arguments:
        user_id = Int()
        user = InputUser()
    
    def mutate(self, info, user_id, user=None):
        old_user = get_user_model().objects.get(id=user_id)
        old_user.username = user.username if user.username else old_user.username
        old_user.email = user.email if user.email else old_user.email
        old_user.set_password(user.password) if user.password else old_user.set_password(old_user.password)
        old_user.first_name = user.first_name if user.first_name else old_user.first_name
        old_user.last_name = user.last_name if user.last_name else old_user.last_name
        old_user.save()
        return UpdateUser(user=old_user)


class DeleteUser(Mutation):
    """
        Delete a user existing
        @DELETE in Rest API
    """
    user_id = Int()
    
    class Arguments:
        user_id = Int()
    
    def mutate(self, info, user_id):
        user = get_user_model().objects.get(id=user_id)
        user.delete()
        return DeleteUser(user_id=user_id)

from graphene import ObjectType, List, Mutation, Field, String, InputObjectType, Int, Argument
from django.contrib.auth import get_user_model
from .type import UserType
from .mutation import CreateUser, UpdateUser, DeleteUser
# Query for user


class UserQuery(ObjectType):
    """
        The query for the user
        @method: GET
    """
    users = List(UserType)
    user = Field(UserType, user_id=Argument(Int))
    me = Field(UserType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        return user

    def resolve_user(self, root, user_id):
        return get_user_model().objects.get(id=user_id)

    def resolve_users(self, root):
        return get_user_model().objects.all()

# Mutation for user


class UserMutation(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

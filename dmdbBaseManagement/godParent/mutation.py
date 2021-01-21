from graphene import Mutation, Field, Int
from graphql import GraphQLError

from dmdbBaseManagement.employe.helper import serializerEmployee
from dmdbBaseManagement.error.employeeException import EmailAlreadyExistException
from dmdbBaseManagement.serializers.serializer import GodParentSerializer
from .type import GodParentType, GodParentInput
from dmdbBaseManagement.models import GodParent


class CreateGodParent(Mutation):
    godparent = Field(GodParentType)

    class Arguments:
        godparent = GodParentInput()

    def mutate(self, info, **args):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to add a GodParent!")
        print(args.get('godparent'))
        godparent = GodParent(**args.get('godparent'))
        serializer = serializerEmployee(data=godparent, modelSerializer=GodParentSerializer)
        if serializer.is_valid(raise_exception=True):
            godparents = GodParent.objects.filter(email__icontains=godparent.email)
            if len(list(godparents)):
                raise EmailAlreadyExistException(godparent.email)
            godparent.save()
            return CreateGodParent(godparent=godparent)


class UpdateGodParent(Mutation):
    godparent = Field(GodParentType)

    class Arguments:
        godparent_id = Int(required=True)
        godparent = GodParentInput()

    def mutate(self, info, **args):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to update a GodParent!")
        print("-----------")
        print(args.get('godparent_id'))
        old_godparent = GodParent.objects.get(id=args.get('godparent_id'))
        print(old_godparent)
        print('------------')
        print(args.get('godparent'))
        old_godparent.__dict__.update(args.get('godparent'))
        email = old_godparent.email
        godparents = GodParent.objects.filter(email__icontains=old_godparent.email)
        serializer = serializerEmployee(data=old_godparent, modelSerializer=GodParentSerializer)
        if serializer.is_valid(raise_exception=True):
            if old_godparent.email != email and len(list(godparents)):
              raise EmailAlreadyExistException(old_godparent.email)
            old_godparent.save()
            return UpdateGodParent(godparent=old_godparent)


class DeleteGodParent(Mutation):
    godparent_id = Int()

    class Arguments:
        godparent_id = Int(required=True)

    def mutate(self, info, godparent_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to delete a GodParent!")
        godparent = GodParent.objects.get(id=godparent_id)
        godparent.delete()
        return DeleteGodParent(godparent_id=godparent_id)

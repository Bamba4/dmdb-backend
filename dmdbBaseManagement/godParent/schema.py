from graphene import ObjectType, List, Field, Int, Argument
from graphql import GraphQLError

from dmdbBaseManagement.models import GodParent
from .type import GodParentType
from .mutation import CreateGodParent, UpdateGodParent, DeleteGodParent
# Query


class GodParentQuery(ObjectType):
    godparents = List(GodParentType)
    godparent = Field(GodParentType, godparent_id = Argument(Int))

    def resolve_godparents(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to get all GodParent!")
        return GodParent.objects.all()

    def resolve_godparent(self, info, godparent_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to get a GodParent!")
        return GodParent.objects.get(id=godparent_id)


class GodParentMutation(ObjectType):
    create_godparent = CreateGodParent.Field()
    update_godparent = UpdateGodParent.Field()
    delete_godparent = DeleteGodParent.Field()

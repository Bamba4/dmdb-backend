from graphene import ObjectType, Field, Int, List, Argument
from graphql import GraphQLError

from .type import TutorType
from dmdbBaseManagement.models import Tutor
from .mutation import CreateTutor, UpdateTutor, DeleteTutor
# Query


class TutorQuery(ObjectType):
    tutors = List(TutorType)
    tutor = Field(TutorType, tutor_id=Argument(Int, required=True))

    def resolve_tutors(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to get all Tutor!")
        return Tutor.objects.all()

    def resolve_tutor(self, info, tutor_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to get a Tutor!")
        return Tutor.objects.get(id=tutor_id)

# Mutation


class TutorMutation(ObjectType):
    create_tutor = CreateTutor.Field()
    update_tutor = UpdateTutor.Field()
    delete_tutor = DeleteTutor.Field()

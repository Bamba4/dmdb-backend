from graphene import Mutation, Field, Int
from graphql import GraphQLError

from dmdbBaseManagement.employe.helper import serializerEmployee
from dmdbBaseManagement.serializers.serializer import TutorSerializer
from .type import TutorType, TutorInput
from dmdbBaseManagement.models import Tutor


class CreateTutor(Mutation):
    tutor = Field(TutorType)

    class Arguments:
        tutor = TutorInput()

    def mutate(self, info, **args):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to add a Tutor!")
        tutor = Tutor(**args.get('tutor'))
        serializer = serializerEmployee(data=tutor, modelSerializer=TutorSerializer)
        if serializer.is_valid(raise_exception=True):
            tutor.save()
            return CreateTutor(tutor=tutor)


class UpdateTutor(Mutation):
    tutor = Field(TutorType)

    class Arguments:
        tutor_id = Int(required=True)
        tutor = TutorInput()

    def mutate(self, info, **args):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to update a Tutor!")
        old_tutor = Tutor.objects.get(id=args.get('tutor_id'))
        old_tutor.__dict__.update(args.get('tutor'))
        serializer = serializerEmployee(data=old_tutor, modelSerializer=TutorSerializer)
        if serializer.is_valid(raise_exception=True):
            old_tutor.save()
            return UpdateTutor(tutor=old_tutor)


class DeleteTutor(Mutation):
    tutor_id = Int()

    class Arguments:
        tutor_id = Int(required=True)

    def mutate(self, info, tutor_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to delete a Tutor!")
        tutor = Tutor.objects.get(id=tutor_id)
        tutor.delete()
        return DeleteTutor(tutor_id=tutor_id)

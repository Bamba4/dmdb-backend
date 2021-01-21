import graphql_jwt

from graphene import ObjectType, Schema
from dmdbBaseManagement.user.schema import UserQuery, UserMutation
from dmdbBaseManagement.employe.schema import EmployeeQuery, EmployeeMutation
from dmdbBaseManagement.godParent.schema import GodParentQuery, GodParentMutation
from dmdbBaseManagement.tutor.schema import TutorQuery, TutorMutation
from dmdbBaseManagement.student.schema import StudentQuery, StudentMutation


class Query(UserQuery, EmployeeQuery, GodParentQuery, TutorQuery, StudentQuery, ObjectType):
    pass


class Mutation(UserMutation, EmployeeMutation, GodParentMutation, TutorMutation, StudentMutation, ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = Schema(query=Query, mutation=Mutation)

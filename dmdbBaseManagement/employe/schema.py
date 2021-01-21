from graphene import ObjectType, List, Mutation, Field, String, InputObjectType, Int, Argument
from graphql import GraphQLError

from dmdbBaseManagement.models import Employee
from .type import EmployeeType
from .mutation import CreateEmployee, UpdateEmployee, DeleteEmployee
# Query


class EmployeeQuery(ObjectType):
    """
        Get Employee
    """
    employees = List(EmployeeType)
    employee = Field(EmployeeType, employee_id=Argument(String, required=True))

    def resolve_employees(self, info):
        """
            Get list of employees
        :param info:
        :return: List employees
        """
        user = info.context.user
        print(user)
        print(user.is_anonymous)
        if user.is_anonymous:
            raise GraphQLError("Log in to get all Employee!")
        return Employee.objects.all()

    def resolve_employee(self, info, employee_id):
        """
         Get Employee by id
        :param info:
        :param employee_id: Id of employee
        :return:
        """
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to add a Employee!")
        return Employee.objects.get(id=employee_id)

# mutation


class EmployeeMutation(ObjectType):
    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()

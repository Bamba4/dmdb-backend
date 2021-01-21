import base64

from graphene import Mutation, Field, Int
from graphql import GraphQLError

from dmdbBaseManagement.employe.helper import serializerEmployee
from dmdbBaseManagement.error.employeeException import  EmailAlreadyExistException
from dmdbBaseManagement.serializers.serializer import EmployeeSerializer
from .type import EmployeeType, InputEmployee
from dmdbBaseManagement.models import Employee


class CreateEmployee(Mutation):
    employee = Field(EmployeeType)

    class Arguments:
        employee = InputEmployee()

    def mutate(self, info, **args):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to add a Employee!")
        new_employee = Employee(**args.get('employee'))
        serializer = serializerEmployee(data=new_employee, modelSerializer=EmployeeSerializer)
        if serializer.is_valid(raise_exception=True):
            employees = Employee.objects.filter(email__icontains=new_employee.email)
            if len(list(employees)):
                raise EmailAlreadyExistException(new_employee.email)
            new_employee.save()
            return CreateEmployee(employee=new_employee)


class UpdateEmployee(Mutation):
    employee = Field(EmployeeType)

    class Arguments:
        employee_id = Int()
        employee = InputEmployee()

    def mutate(self, info, **args):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to update an Employee!")
        old_employee = Employee.objects.get(id=args.get('employee_id'))
        email = old_employee.email
        old_employee.__dict__.update(args.get('employee'))
        serializer = serializerEmployee(data=old_employee, modelSerializer=EmployeeSerializer)
        if serializer.is_valid(raise_exception=True):
            employees = Employee.objects.filter(email__icontains=old_employee.email)
            if old_employee.email != email and len(list(employees)):
                raise EmailAlreadyExistException(old_employee.email)
            Employee.save(old_employee)
            return UpdateEmployee(employee=old_employee)


class DeleteEmployee(Mutation):
    employee_id = Int()

    class Arguments:
        employee_id = Int(required=True)

    def mutate(self, info, employee_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in to delete a Employee!")
        employee = Employee.objects.get(id=employee_id)
        employee.delete()
        return DeleteEmployee(employee_id=employee_id)

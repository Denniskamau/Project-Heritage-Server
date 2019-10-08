import graphene
from graphene_django import DjangoObjectType
from .models import Attendance


class AttendaceType(DjangoObjectType):
    class Meta:
        model = Attendance
class Query(graphene.ObjectType):
    attendance = graphene.List(AttendaceType)

    def resolve_classes(self,info,**kwargs):
        return Attendance.objects.all()

class Mutation():
    pass
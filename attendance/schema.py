import graphene
from graphene_django import DjangoObjectType
from .models import Attendance

from .mutations import CreateAttendace

class AttendaceType(DjangoObjectType):
    class Meta:
        model = Attendance
        
class Query(graphene.ObjectType):
    attendance = graphene.List(AttendaceType)

    def resolve_classes(self,info,**kwargs):
        return Attendance.objects.all()


class Mutation(graphene.ObjectType):
    create_attendance = CreateAttendace.Field()

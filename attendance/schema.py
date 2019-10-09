import graphene
from graphene_django import DjangoObjectType
from .models import Attendance
from classes.schema import PhClassType

class AttendaceType(DjangoObjectType):
    class Meta:
        model = Attendance
class Query(graphene.ObjectType):
    attendance = graphene.List(AttendaceType)

    @staticmethod
    def resolve_classes(self,info,**kwargs):
        return Attendance.objects.all()


class CreateAttendace(graphene.Mutation):
    id = graphene.Int()
    isPresent = graphene.Boolean()
    childName = graphene.String()
    # phClass= graphene.Field(PhClassType)

    class Arguments:
        isPresent = graphene.Boolean()
        childName = graphene.String()

    @staticmethod
    def mutate(self,info,isPresent,childName):
        # phclass = info.context.phClass or None
        # print('phclass',phClass)
        newAttendace = Attendance(isPresent=isPresent,childName=childName)
        newAttendace.save()

        return CreateAttendace(
            id=newAttendace.id,
            isPresent = newAttendace.isPresent,
            childName = newAttendace.childName,
            # phClass = newAttendace.phClass

        )

class Mutation(graphene.ObjectType):
    create_attendance = CreateAttendace.Field()
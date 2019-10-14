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



class CreateAttendace(graphene.Mutation):
    id = graphene.Int()
    isPresent = graphene.Boolean()
    childName = graphene.String()

    class Arguments:
        isPresent = graphene.Boolean()
        childName = graphene.String()

    def mutate(self,info,isPresent,childName):
        newAttendace = Attendance(isPresent=isPresent,childName=childName)
        newAttendace.save()

        return CreateAttendace(
            id=newAttendace.id,
            isPresent = newAttendace.isPresent,
            childName = newAttendace.childName
        )

class Mutation(graphene.ObjectType):
    create_attendance = CreateAttendace.Field()

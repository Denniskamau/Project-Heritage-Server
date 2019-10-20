import graphene
from graphene_django import DjangoObjectType
from .models import Attendance


class CreateAttendace(graphene.Mutation):
    id = graphene.Int()
    isPresent = graphene.Boolean()
    child = graphene.Int()

    class Arguments:
        isPresent = graphene.Boolean()
        child = graphene.Int()

    def mutate(self,info,**kwargs):
        newAttendace = Attendance(isPresent=kwargs['isPresent'],child=kwargs['child'])
        newAttendace.save()

        return CreateAttendace(
            id=newAttendace.id,
            isPresent = newAttendace.isPresent,
            child = newAttendace.child
        )

import graphene
from graphene_django import DjangoObjectType
from .models import PhClass

class PhClassType(DjangoObjectType):
    class Meta:
        model = PhClass

class CreateClass(graphene.Mutation):
    id = graphene.Int()
    ageGroup = graphene.String()
    facilitator = graphene.String()

    """Define the data to be sent ot the server"""
    class Arguments:
        ageGroup = graphene.String()
        facilitator = graphene.String()

    """Save the data sent by the user to the db"""
    def mutate(self,info,ageGroup,facilitator):
        newClass =  PhClass(ageGroup=ageGroup,facilitator=facilitator)
        newClass.save()
        """Return the newly created data"""
        return CreateClass(
            id = newClass.id,
            ageGroup = newClass.ageGroup,
            facilitator = newClass.facilitator
        )
class Query(graphene.ObjectType):
    classes = graphene.List(PhClassType)

    def resolve_classes(self,info,**kwargs):
        return PhClass.objects.all()


"""Create a mutation class for the fields to be resolved"""
class Mutation(graphene.ObjectType):
    create_class = CreateClass.Field()
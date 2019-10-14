import graphene
from graphene_django import DjangoObjectType
from .models import PhClass

class PhClassType(DjangoObjectType):
    class Meta:
        model = PhClass

class CreateClass(graphene.Mutation):
    id = graphene.Int()
    ageGroup = graphene.String()
    class_designation = graphene.String()
    name = graphene.String()
    min_age = graphene.Int()
    max_age = graphene.Int()

    """Define the data to be sent ot the server"""
    class Arguments:
        ageGroup = graphene.String()
        class_designation = graphene.String()
        name = graphene.String()
        min_age = graphene.Int()
        max_age = graphene.Int()


    """Save the data sent by the user to the db"""
    def mutate(self,info,**kwargs):
        newClass =  PhClass(ageGroup=kwargs['ageGroup'],
                    class_designation = kwargs['class_designation'],
                    name= kwargs['name'],
                    max_age=kwargs['max_age'],
                    min_age=kwargs['min_age'])
        newClass.save()
        """Return the newly created data"""
        return CreateClass(
            id = newClass.id,
            ageGroup = newClass.ageGroup,
            class_designation = newClass.class_designation,
            name = newClass.name,
            max_age = newClass.max_age,
            min_age = newClass.min_age
        )
class Query(graphene.ObjectType):
    classes = graphene.List(PhClassType)

    def resolve_classes(self,info,**kwargs):
        return PhClass.objects.all()



"""Create a mutation class for the fields to be resolved"""
class Mutation(graphene.ObjectType):
    create_class = CreateClass.Field()

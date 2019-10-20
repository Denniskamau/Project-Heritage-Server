import graphene
from graphene_django import DjangoObjectType
from .models import PhClass



class CreateClass(graphene.Mutation):
    """Create a new class"""
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


class UpdateClass(graphene.Mutation):
    """Update an existing"""
    id = graphene.Int()
    ageGroup = graphene.String()
    class_designation = graphene.String()
    name = graphene.String()
    min_age = graphene.Int()
    max_age = graphene.Int()

    class Arguments:
        id = graphene.Int()
        ageGroup = graphene.String()
        class_designation = graphene.String()
        name = graphene.String()
        min_age = graphene.Int()
        max_age = graphene.Int()

    def mutate(self,info,**kwargs):
        phclassInstance = PhClass.objects.get(pk=kwargs['id'])
        if phclassInstance:
            newClass =  PhClass(ageGroup=kwargs['ageGroup'],
                        class_designation = kwargs['class_designation'],
                        name= kwargs['name'],
                        max_age=kwargs['max_age'],
                        min_age=kwargs['min_age'])
            newClass.save()
            return UpdateClass(
                id = newClass.id,
                ageGroup = newClass.ageGroup,
                class_designation = newClass.class_designation,
                name = newClass.name,
                max_age = newClass.max_age,
                min_age = newClass.min_age
            )
        else:
            raise Exception('No class with that ID')

class DeleteClass(graphene.Mutation):
    """Delete Existing record"""
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self,info,**kwargs):
        phclassInstance = PhClass.objects.get(pk=kwargs['id'])
        if phclassInstance:
            phclassInstance.delete()
            message = 'Delete succesful'
            return DeleteClass(
                id = kwargs['id']
            )
        else:
            raise Exception('No class with that ID')
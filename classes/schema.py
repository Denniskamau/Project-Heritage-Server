import graphene
from graphene_django import DjangoObjectType
from .models import PhClass


from .mutations import CreateClass,UpdateClass,DeleteClass


class PhClassType(DjangoObjectType):
    class Meta:
        model = PhClass


class Query(graphene.ObjectType):
    classes = graphene.List(PhClassType)

    def resolve_classes(self,info,**kwargs):
        return PhClass.objects.all()




"""Create a mutation class for the fields to be resolved"""
class Mutation(graphene.ObjectType):
    create_class = CreateClass.Field()
    update_class = UpdateClass.Field()
    delete_class = DeleteClass.Field()

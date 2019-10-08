import graphene
from graphene_django import DjangoObjectType
from .models import PhClass

class PhClassType(DjangoObjectType):
    class Meta:
        model = PhClass

class Query(graphene.ObjectType):
    classes = graphene.List(PhClassType)

    def resolve_classes(self,info,**kwargs):
        return PhClass.objects.all()

class Mutation():
    pass
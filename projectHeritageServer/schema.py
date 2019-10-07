import graphene

import classes.schema
import attendance.schema

class Query(classes.schema.Query,attendance.schema.Query, graphene.ObjectType):
    pass

class Mutation(classes.schema.Mutation,attendance.schema.Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)
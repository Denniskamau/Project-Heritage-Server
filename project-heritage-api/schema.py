import graphene
import graphql_jwt

import classes.schema
import attendance.schema
from .users import schema

class Query(schema.Query,classes.schema.Query,attendance.schema.Query, graphene.ObjectType):
    pass

class Mutation(schema.Mutation,classes.schema.Mutation,attendance.schema.Mutation,graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)
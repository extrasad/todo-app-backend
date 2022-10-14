from graphene import Schema

from .mutations import Mutation

schema = Schema(mutation=Mutation)

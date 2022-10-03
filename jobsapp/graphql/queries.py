import graphene

from .types import JobGQLType
from jobsapp.models import BookableObject
from .exceptions import GraphQLError


class JobQuery(graphene.ObjectType):
    jobs = graphene.List(JobGQLType)
    job = graphene.Field(JobGQLType, pk=graphene.Int())

    def resolve_jobs(self, info):
        return BookableObject.objects.all()

    def resolve_job(self, info, pk, **kwargs):
        if pk:
            try:
                return BookableObject.objects.get(pk=pk)
            except BookableObject.DoesNotExist:
                return GraphQLError("Job doesn't exists")
        return None

import graphene

from .types import JobGQLType
from jobsapp.models import BookableEvent
from .exceptions import GraphQLError


class JobQuery(graphene.ObjectType):
    jobs = graphene.List(JobGQLType)
    job = graphene.Field(JobGQLType, pk=graphene.Int())

    def resolve_jobs(self, info):
        return BookableEvent.objects.all()

    def resolve_job(self, info, pk, **kwargs):
        if pk:
            try:
                return BookableEvent.objects.get(pk=pk)
            except BookableEvent.DoesNotExist:
                return GraphQLError("Job doesn't exists")
        return None

from django.db.models import Manager
from django.db.models.query import QuerySet


class StaffQuerySet(QuerySet):

    def published(self):
        return self.filter(published=True)


class StaffManager(Manager):

    def get_query_set(self):
        return StaffQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_query_set().published()
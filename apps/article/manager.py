from django.db.models import Manager
from apps.article.choise import Status


class PublishManager:
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(status=Status.PUBLISHED)
        return queryset

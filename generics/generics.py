from django.db.models import DateTimeField, Model
from django.utils import timezone


class CreatedUpdatedMixin(Model):
    """
    CreatedUpdatedMixin
        - set created_at time of creation
        - set updated_at time of updation
    """

    created_at = DateTimeField(default=timezone.now, editable=False)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

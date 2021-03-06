from django.db.models import signals
from django.dispatch import receiver

from validate.validator import validate
from metadata.models import File


@receiver(signals.post_save, sender=File)
def file_post_save(sender, instance, **kwargs):
    if kwargs.get('created'):
        validate(instance.id)

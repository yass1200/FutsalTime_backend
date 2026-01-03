from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(recipient, actor, verb: str, target=None):
    ct = ContentType.objects.get_for_model(target) if target else None
    obj_id = target.pk if target else None
    return Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target_content_type=ct,
        target_object_id=obj_id,
    )

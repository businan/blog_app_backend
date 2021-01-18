from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Post
from .utils import get_random_uid


@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwards):
    if not instance.slug:
        print("sqsqsqs")
        instance.slug = slugify(instance.post_title + " " + get_random_uid())
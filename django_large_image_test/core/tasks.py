from celery import shared_task

from django_large_image_test.core.models import Image


@shared_task
def image_compute_checksum(image_id: int):
    image = Image.objects.get(pk=image_id)
    image.compute_checksum()
    image.save()

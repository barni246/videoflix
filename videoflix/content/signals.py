from .models import Video
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from content.tasks import convert_480p
import os
import django_rq
from django_rq import enqueue

@receiver(post_save,sender=Video)
def video_post_save(sender,instance,created,**kwargs):
    print('Video wurde gespeichert!')
    
    if created:
        print('New Video created')
        queue = django_rq.get_queue('default', autocommit=True)
        print('New Video created --> queue')
        queue.enqueue(convert_480p,instance.video_file.path)
        print('New Video created --> queue.enqueue()')
        # convert_480p(instance.video_file.path)
        

@receiver(post_delete,sender=Video)
def auto_delete_file_on_delete(sender,instance,**kwargs):
    
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Compare
import logging
 
 
logger = logging.getLogger('django')

@receiver(post_save, sender=Compare)
def create_profile(sender, instance, created, **kwargs):
    if created:
        logger.info("--------------------------------------------------------------------")
        logger.info("------------------Loggers for file comparision----------------------")
        logger.info("--------------------------------------------------------------------")
        
        logger.info("New Entry for Comparision of two file is triggered")    
        
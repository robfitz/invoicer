from django.db import models

from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from djangotoolbox.fields import ListField 

from s_media.models import Image


class UserProfile(models.Model):

    user = models.OneToOneField(User)

    thumbnail = models.ForeignKey(Image, null=True)

    signup_date = models.DateTimeField(auto_now_add=True, null=True)


    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):

    if created:

        # extra info
        profile = UserProfile.objects.create(user=instance)

        # cards they start with
        profile.deck = Deck.create_starting_deck()
        profile.save()



post_save.connect(create_user_profile, sender=User)

admin.site.register(UserProfile)

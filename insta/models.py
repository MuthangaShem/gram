from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)


    @classmethod
    def get_all(cls):
        profiles = Profile.objects.all()
        return profiles 

    @classmethod
    def searched(cls, query):
        result = cls.objects.filter(user__username__icontains=query).first()   
        return result

    @classmethod
    def get_Image_by_profile(cls,search_term):
        profile = cls.objects.filter(location__icontains=search_term)
        return profile


    # @property
    # def avatar(self):
    #     if self.avatar and hasattr(self.avatar, 'url'):
    #         return self.avatar.url

class Image(models.Model):
    image = models.ImageField(upload_to='post/')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

    @classmethod
    def get_all(cls):
        imgs = Image.objects.all()
        return imgs

    @classmethod
    def search_by_title(cls, search_term):
        news = cls.objects.filter(image_name__icontains=search_term)
        return news

    class Meta:
        ordering = ['-post_date',]

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance,  **kwargs):
    instance.profile.save()


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Image,on_delete=models.CASCADE)
    comment_content = models.TextField(blank=True)

    def __str__(self):
        return self.user.user

    @classmethod
    def get_post_comments(cls,post_id):
        post_comments = Comment.objects.filter(post=post_id)
        return post_comments
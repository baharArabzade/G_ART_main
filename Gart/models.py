from django.db import models
class Studio_item(models.Model):
    title = models.CharField(max_length=250)
    short_info = models.CharField(max_length=150)
    running_time = models.CharField(max_length=30)
    genre = models.CharField(max_length=250,null=True)
    info = models.TextField(null=True)
    info_table = models.TextField(null=True,blank=True)
    crew = models.TextField(null=True)
    nomination = models.TextField(null=True, blank=True)
    award = models.TextField(null=True, blank=True)
    poster = models.ImageField(null=True, blank=True,upload_to='upload/')
    photo1 = models.ImageField(null=True, blank=True, upload_to='upload/')
    photo2 = models.ImageField(null=True, blank=True, upload_to='upload/')
    photo3 = models.ImageField(null=True, blank=True, upload_to='upload/')

    thrailer_src=models.URLField(blank=True)


    def __str__(self):
        return "{}".format(self.title)


class Tutorial_item(models.Model):
    title = models.CharField(max_length=250)
    info = models.TextField(null=True,blank=True)
    running_time = models.CharField(max_length=30)
    poster =models.ImageField(null=True,blank=True)
    video_src=models.URLField(null=True,blank=True)


    def __str__(self):
        return "{}".format(self.title)

class Collection_item(models.Model):
    title = models.CharField(max_length=250)
    info = models.TextField()
    poster = models.ImageField(null=True,upload_to='upload/')
    photo1 = models.ImageField(null=True, blank=True, upload_to='upload/')
    photo2 = models.ImageField(null=True, blank=True, upload_to='upload/')
    photo3 = models.ImageField(null=True,blank=True , upload_to='upload/')

class Event_item(models.Model):
    title = models.CharField(max_length=250)
    info = models.TextField()
    poster = models.ImageField(null=True,upload_to='upload/')
    photo1 = models.ImageField(null=True, blank=True, upload_to='upload/')
    photo2 = models.ImageField(null=True, blank=True, upload_to='upload/')
    photo3 = models.ImageField(null=True,blank=True , upload_to='upload/')
    video_src = models.URLField(null=True, blank=True)
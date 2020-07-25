from django.db import models


def studio_poster_file_name(instance, filename):
    return '/'.join(["studio",instance.title, filename])
def studio_photo_file_name(instance, filename):
    return '/'.join(["studio",instance.studio_item.title, filename])
def collection_file_name(instance, filename):
    return '/'.join(["collection",instance.title, filename])

def event_file_name(instance, filename):
    return '/'.join(["event",instance.title, filename])

def tutorial_file_name(instance, filename):
    return '/'.join(["tutorial",instance.title, filename])


class Studio_item(models.Model):
    title = models.CharField(max_length=250)
    short_info = models.CharField(max_length=120)
    running_time = models.CharField(max_length=30)
    genre = models.CharField(max_length=250,null=True)
    info = models.TextField(null=True)
    info_table = models.TextField(null=True,blank=True)
    crew = models.TextField(null=True)
    nomination = models.TextField(null=True, blank=True)
    award = models.TextField(null=True, blank=True)
    poster = models.ImageField(upload_to=studio_poster_file_name)
    thrailer_src=models.URLField(blank=True)
    thrailer_text = models.TextField(blank=True,null=True)
    TYPE_CHOICES = (
        ('movie', 'movie'),
        ('music video', 'music video'),
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)

    def __str__(self):
        return "{}".format(self.title)


class Studio_Photo(models.Model):
    studio_item = models.ForeignKey(Studio_item, on_delete=models.DO_NOTHING, null=True)
    photo = models.ImageField(upload_to=studio_photo_file_name)

class Tutorial_item(models.Model):

    title = models.CharField(max_length=250)
    info = models.TextField(null=True,blank=True)
    short_info = models.TextField(max_length=60,verbose_name="short info(on card)")
    main_info = models.TextField(verbose_name="Specifications \n (E.g:level=beginner)")

    running_time = models.CharField(max_length=30)
    poster =models.ImageField(null=True)
    video_src=models.URLField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    material_file=models.FileField(upload_to=tutorial_file_name , blank=True)



    def __str__(self):
        return "{}".format(self.title)

class Collection_item(models.Model):
    title = models.CharField(max_length=250)
    info = models.TextField()
    poster = models.ImageField(null=True,upload_to=collection_file_name)
    photo1 = models.ImageField(null=True, blank = True, upload_to=collection_file_name)
    photo2 = models.ImageField(null=True, blank = True, upload_to=collection_file_name)
    photo3 = models.ImageField(null=True,blank = True, upload_to=collection_file_name)
    photo4 = models.ImageField(null=True,blank=True, upload_to=collection_file_name)
    photo5 = models.ImageField(null=True, blank=True, upload_to=collection_file_name)

    def __str__(self):
        return "{}".format(self.title)
class Event_item(models.Model):
    title = models.CharField(max_length=250)
    info = models.TextField()
    poster = models.ImageField(null=True,upload_to=event_file_name)
    photo1 = models.ImageField(null=True, blank=True, upload_to=event_file_name)
    photo2 = models.ImageField(null=True, blank=True, upload_to=event_file_name)
    photo3 = models.ImageField(null=True,blank=True , upload_to=event_file_name)
    photo4 = models.ImageField(null=True, blank=True, upload_to=event_file_name)
    photo5 = models.ImageField(null=True,blank=True , upload_to=event_file_name)
    video_src = models.URLField(null=True, blank=True)
    def __str__(self):
        return "{}".format(self.title)
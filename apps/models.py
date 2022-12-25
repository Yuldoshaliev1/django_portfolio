import sys
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models import Model, CharField, TextField, ImageField, DateField, ForeignKey, IntegerField, CASCADE, \
    DO_NOTHING, PROTECT
from django.db.models.signals import post_delete
from django.utils.text import slugify
from tinymce.models import HTMLField
from .signals import file_cleanup


class AboutUser(Model):
    full_name = CharField(max_length=50)
    birthday = DateField()
    age = CharField(max_length=25)
    phone = CharField(max_length=255)
    city = CharField(max_length=255)

    degree = CharField(max_length=60)
    image = ImageField(upload_to='profile/')
    academy = CharField(max_length=255)
    experience = CharField(max_length=25)


    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About me'


class Education(Model):
    user = ForeignKey(AboutUser,PROTECT)
    school = CharField(max_length=255)
    college = CharField(max_length=50)
    field = CharField(max_length=255)
    description = TextField()
    from_date = DateField()
    to_date = DateField()
    current = CharField(max_length=60)

    def __str__(self):
        return self.school



class Service(Model):
    title = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to="services", default='default.png')

    def __str__(self):
        return self.title




class ProjectCategory(Model):
    title = CharField(max_length=100)

    def __str__(self):
        return self.title



class Project(Model):
    project_category = ForeignKey(ProjectCategory, on_delete=DO_NOTHING)
    title = CharField(max_length=255)
    slug = CharField(max_length=255, unique=True, null=True)
    image = ImageField(upload_to='project/', default="default.png")
    link = CharField(max_length=255, null=True)
    from_date = DateField()
    to_date = DateField()
    description = HTMLField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)


        im = Image.open(self.image)

        if im.mode in ("RGBA", "P"):
            im = im.convert("RGB")

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((550, 370))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        # change the image field value to be the newly modified image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)

        super(Project, self).save()


post_delete.connect(file_cleanup, sender=Project)


class Skill(Model):
    title = CharField(max_length=50)
    rate = IntegerField()

    def __str__(self):
        return self.title




#
# class BlogCategory(Model):
#     name = CharField(max_length=255)
#
#     class Meta:
#         verbose_name = "Blog Category"
#         verbose_name_plural = "Blog Categories"
#
#     def __str__(self):
#         return self.name
#
#
# def blog_directory_path(instance, filename):
#     return 'blog/{0}/{1}'.format(strftime('%Y/%m/%d'), generate_file_name(25) + '.' + filename.split('.')[-1])
#
#
# class Blog(Model):
#     title = CharField(max_length=255)
#     slug = CharField(max_length=255, unique=True)
#     category = ForeignKey(BlogCategory, on_delete=CASCADE)
#     description = HTMLField()
#     image = ImageField(upload_to=blog_directory_path, null=True, blank=True)
#     created_at = DateField(default=now)
#
#     def __str__(self):
#         return self.title
#
#     def save(self, *args, **kwargs):
#         if self.title:
#             self.slug = slugify(self.title)
#         super(Blog, self).save()
#
#     @property
#     def photo(self):
#         if self.image:
#             return self.image.url
#         else:
#             return static("images/blog_default.jpg")
#
#     def get_absolute_url(self):
#         return reverse_lazy('apps:blog-details', self.slug)
#

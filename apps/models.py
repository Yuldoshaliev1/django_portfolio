from django.db.models import Model, CharField, TextField, ImageField, DateField, ForeignKey, IntegerField, CASCADE, \
    DO_NOTHING, PROTECT

from django.utils.text import slugify




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


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Project.objects.filter(slug=self.slug).exists():
                slug = Project.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.title:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Skill(Model):
    title = CharField(max_length=50)
    rate = IntegerField()

    def __str__(self):
        return self.title




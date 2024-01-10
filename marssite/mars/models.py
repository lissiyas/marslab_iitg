from django.db import models



# Create your models here.

class ResearchType(models.TextChoices):
    ONGOING = 'og','ongoing'
    COMPLETED = 'comp', 'completed'

class Research(models.Model):
    title = models.CharField(max_length=500)
    details = models.TextField()
    summary = models.TextField()
    researchtype = models.CharField(
        max_length=5,
        choices=ResearchType.choices,
        default=ResearchType.ONGOING,

    )

    def __str__(self):
        return self.title


##news database
class News(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    display = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.display:  # Check if this post is meant to be displayed
            # Set 'display' to False for all other News objects
            News.objects.all().update(display=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title




class PublicationType(models.TextChoices):
    CONFERENCE = 'CONF', 'Conference'
    JOURNAL = 'JRNL', 'Journal'
    BOOK = 'BOOK', 'Book'

class Journal(models.Model):
    title = models.CharField(max_length=500)
    author = models.TextField()
    body = models.TextField()
    url = models.URLField()
    date_posted = models.DateTimeField(auto_now_add=True)
    publication_type = models.CharField(
        max_length=5,
        choices=PublicationType.choices,
        default=PublicationType.JOURNAL,
    )

    def __str__(self):
        return f'{self.title} - {self.get_publication_type_display()}'



class People(models.TextChoices):
    Postdoc = 'POST','Postdoc'
    Doc = 'DOC','Doc'
    Mtech = 'MTECH', 'Mtech'
    Btech = 'BTECH', 'Btech'
    ProjectStaff ='PS', 'ProjectStaff'


class Team(models.Model):
    status_choices = [
        ('CURRENT','current'),
        ('ALLUMNI', 'allumni'),
    ]
    name = models.CharField(max_length=100)
    project_topic = models.TextField()
    education = models.TextField()
    current_designation =models.TextField(max_length=500)
    url = models.URLField()
    image = models.ImageField(default='default.jpg' , upload_to='profile_pics')
    category = models.CharField(
        max_length=6,
        choices=People.choices,
        default=People.ProjectStaff,

    )
    status = models.CharField(
        max_length=8,
        choices=[('CURRENT', 'current'), ('ALLUMNI', 'allumni')],
        default='CURRENT',
    )
    def __str__(self):
        return f'{self.name} - {self.get_category_display()}'



    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class EventImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/')
    description = models.TextField()
    

    def __str__(self):
        return self.description
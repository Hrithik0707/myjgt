from django.db import models
from datetime import datetime
# Create your models here.
choices = (
    ('Daily','Daily'),
    ('Weekly','Weekly'),
    ('Monthly','Monthly'),
)
teamlead = (
    ('Raktima Mitra', 'Raktima Mitra'),
    ('Akansha', 'Akansha'),
    ('Amitesh Rajan', 'Amitesh Rajan'),
    ('Sheetal', 'Sheetal'),
    ('Kanika', 'Kanika'),
    ('Ajeet', 'Ajeet'),
    ('Shekhar', 'Shekhar'),

)
class Form(models.Model):
    Name = models.CharField(max_length = 50)
    Date = models.DateField(default = datetime.now)
    Reports = models.CharField(max_length = 10,choices = choices,default = 'Daily')
    Team_lead = models.CharField(max_length = 30,choices = teamlead,default = 'Raktima Mitra')
    No_of_hours = models.CharField(max_length = 2, default = '0')
    Todays_progress = models.TextField()
    Todays_documents = models.FileField(upload_to = 'media/')
    Concern = models.TextField()
    Next_document = models.FileField(upload_to = 'media/')
    Next_plan = models.TextField()
    def __str__(self):
        return self.name
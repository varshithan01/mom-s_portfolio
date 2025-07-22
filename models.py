from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=200)
    published_year = models.IntegerField()
    journal = models.CharField(max_length=200)
    file = models.FileField(upload_to='publications_files/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

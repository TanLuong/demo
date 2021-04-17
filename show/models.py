from django.db import models
from django.urls import reverse

# Create your models here.
class ieltsstories(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('ieltsstories-detail', args=[str(self.id)])
    def __str__(self):
        return self.title

class ieltstest(models.Model):
    sublevel = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    qnumber = models.IntegerField(blank=True, primary_key=True)  # Field name made lowercase.
    qcontent = models.TextField(blank=True, null=True)  # Field name made lowercase.
    answera = models.TextField(blank=True, null=True)  # Field name made lowercase.
    answerb = models.TextField(blank=True, null=True)  # Field name made lowercase.
    answerc = models.TextField(blank=True, null=True)  # Field name made lowercase.
    answerd = models.TextField(blank=True, null=True)  # Field name made lowercase.
    correctanswer = models.TextField(db_column='CorrectAnswer', blank=True, null=True)  # Field name made lowercase.
    passed = models.IntegerField(db_column='Passed', blank=True, null=True)  # Field name made lowercase.

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('test-detail', args=[str(self.id)])

    def __str__(self):
        return self.answera

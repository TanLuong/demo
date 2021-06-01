from django.db import models
from django.urls import reverse
from html.parser import HTMLParser

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

class lesson(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    type = models.IntegerField(blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=100)
    content = models.TextField(blank=True,null=True)
    question = models.TextField(blank=True, null=True)
    audio = models.TextField(blank=True,null=True)
    favorite = models.IntegerField(blank=True, null=True)
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail', args=[str(self.id)])

'''class question(models.Model):
    content = models.TextField(blank = True, primary_key = True)
    answera = models.TextField(blank = True, null = True)
    answerb = models.TextField(blank = True, null = True)
    answerc = models.TextField(blank = True, null = True)
    answerd = models.TextField(blank = True, null = True)
    correctanswer = models.TextField(blank =True, null = True)
    for i in lesson.objects.all():
        content = lesson.question.values()'''

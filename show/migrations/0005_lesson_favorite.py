# Generated by Django 3.2 on 2021-04-19 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0004_rename_lesson_lesson_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='favorite',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

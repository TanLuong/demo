# Generated by Django 3.2 on 2021-04-19 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0003_lesson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='lesson',
            new_name='title',
        ),
    ]
# Generated by Django 3.2 on 2021-04-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0002_auto_20210417_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='lesson',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('lesson', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('audio', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

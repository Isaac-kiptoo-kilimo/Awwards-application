# Generated by Django 4.0.5 on 2022-06-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

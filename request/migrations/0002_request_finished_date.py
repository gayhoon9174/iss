# Generated by Django 3.1.4 on 2020-12-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='finished_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.2.8 on 2023-06-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='details',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]

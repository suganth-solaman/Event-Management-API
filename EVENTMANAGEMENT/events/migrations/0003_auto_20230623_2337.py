# Generated by Django 3.2.8 on 2023-06-23 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_eventdetails_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='end_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='event',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='seat',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='start_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='seats',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]

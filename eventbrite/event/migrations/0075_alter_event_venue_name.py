# Generated by Django 4.2b1 on 2023-04-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0074_alter_event_venue_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='venue_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

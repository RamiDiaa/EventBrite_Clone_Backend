# Generated by Django 4.2b1 on 2023-04-25 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0061_delete_myimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
    ]

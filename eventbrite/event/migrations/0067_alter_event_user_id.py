# Generated by Django 4.2b1 on 2023-04-26 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0066_eventfollower_delete_eventfollowers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='User_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

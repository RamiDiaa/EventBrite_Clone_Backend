# Generated by Django 4.2b1 on 2023-04-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publish_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField()),
                ('Event_ID', models.IntegerField()),
                ('Event_Status', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=7)),
                ('Audience_Link', models.CharField(max_length=50)),
                ('Audience_Password', models.CharField(max_length=50)),
                ('Keep_Private', models.BooleanField()),
                ('Publication_Date', models.DateField(null=True)),
            ],
        ),
    ]

# Generated by Django 3.2.3 on 2021-08-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30)),
                ('event_description', models.TextField()),
                ('venue', models.CharField(max_length=30)),
                ('event_date', models.DateTimeField()),
                ('attendees', models.EmailField(max_length=254)),
            ],
        ),
    ]

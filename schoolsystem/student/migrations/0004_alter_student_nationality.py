# Generated by Django 3.2.3 on 2021-08-12 20:09

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]

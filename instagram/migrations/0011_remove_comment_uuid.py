# Generated by Django 3.2.7 on 2022-09-28 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0010_comment_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='uuid',
        ),
    ]
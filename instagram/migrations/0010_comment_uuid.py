# Generated by Django 3.2.7 on 2022-09-28 20:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0009_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]

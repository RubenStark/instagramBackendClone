# Generated by Django 3.2.7 on 2022-09-27 21:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0004_post_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='Comments', to=settings.AUTH_USER_MODEL),
        ),
    ]

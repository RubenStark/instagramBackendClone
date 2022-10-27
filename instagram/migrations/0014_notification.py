# Generated by Django 3.2.7 on 2022-10-04 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0013_alter_story_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='instagram.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notification', to='instagram.profile')),
                ('user_to_notify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_to_notify', to='instagram.profile')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]

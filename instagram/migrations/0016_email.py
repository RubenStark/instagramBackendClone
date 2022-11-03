# Generated by Django 3.2.7 on 2022-11-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0015_alter_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('body', models.TextField(blank=True, max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
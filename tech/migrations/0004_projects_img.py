# Generated by Django 4.2.9 on 2024-02-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0003_profile_bio_profile_qualifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='img',
            field=models.ImageField(default='\\img\\gallery\\project-2.jpg', upload_to='media'),
        ),
    ]

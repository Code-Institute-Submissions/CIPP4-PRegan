# Generated by Django 4.2.2 on 2023-06-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pianoblog', '0004_rename_profile_owner_profile_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='https://res.cloudinary.com/dayngkoud/image/upload/v1687988552/piano_icon_pijapc.png', upload_to=''),
        ),
    ]

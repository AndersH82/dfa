# Generated by Django 3.2.25 on 2024-03-13 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_qdjgyp', upload_to='images/'),
        ),
    ]

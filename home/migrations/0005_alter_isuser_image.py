# Generated by Django 4.0.6 on 2022-07-16 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_isuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='isuser',
            name='image',
            field=models.ImageField(default='unknown.jpg', upload_to='profile_image/'),
        ),
    ]

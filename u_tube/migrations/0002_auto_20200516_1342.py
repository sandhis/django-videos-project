# Generated by Django 3.0.6 on 2020-05-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('u_tube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos/'),
        ),
    ]

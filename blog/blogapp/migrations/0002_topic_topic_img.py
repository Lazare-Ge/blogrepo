# Generated by Django 2.2.5 on 2021-02-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic_img',
            field=models.ImageField(blank=True, upload_to='blogapp/blogimages'),
        ),
    ]

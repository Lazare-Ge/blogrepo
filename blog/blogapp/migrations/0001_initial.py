# Generated by Django 2.2.5 on 2021-02-13 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=164)),
                ('author_surname', models.CharField(max_length=164)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_title', models.CharField(max_length=200)),
                ('topic_text', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Author')),
            ],
        ),
    ]

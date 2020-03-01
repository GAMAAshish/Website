# Generated by Django 3.0.3 on 2020-02-23 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('published', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
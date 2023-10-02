# Generated by Django 4.2.5 on 2023-10-01 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='MusicWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iswc', models.CharField(default=None, max_length=30, null=True, verbose_name='ISWC')),
                ('title', models.CharField(default=None, max_length=128, null=True)),
                ('authors', models.ManyToManyField(to='sv.author')),
            ],
        ),
    ]

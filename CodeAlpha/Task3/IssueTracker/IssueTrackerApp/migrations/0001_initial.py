# Generated by Django 4.2.7 on 2024-02-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Issue_ID', models.IntegerField(default='')),
                ('Issue', models.CharField(default='', max_length=50)),
                ('Contact', models.IntegerField(default='')),
                ('Mail', models.CharField(default='', max_length=50)),
            ],
        ),
    ]

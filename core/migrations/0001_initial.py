# Generated by Django 4.2.4 on 2023-09-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EndpointData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_name', models.CharField(max_length=100)),
                ('current_day', models.CharField(max_length=50)),
                ('utc_time', models.DateTimeField()),
                ('track', models.CharField(max_length=50)),
                ('github_file_url', models.URLField()),
                ('github_repo_url', models.URLField()),
            ],
        ),
    ]

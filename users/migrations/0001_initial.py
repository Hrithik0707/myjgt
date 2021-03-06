# Generated by Django 2.2.6 on 2020-04-19 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Date', models.DateField(default=datetime.datetime.now)),
                ('Reports', models.CharField(max_length=10)),
                ('Team_lead', models.CharField(max_length=30)),
                ('No_of_hours', models.CharField(default='0', max_length=2)),
                ('Todays_progress', models.TextField()),
                ('Todays_documents', models.FileField(upload_to='media/')),
                ('Concern', models.TextField()),
                ('Next_document', models.FileField(upload_to='media/')),
                ('Next_plan', models.TextField()),
            ],
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-03 12:17

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('profile_unique_key', models.CharField(default=profiles.models.generate_id, max_length=8, unique=True)),
                ('email_id', models.EmailField(default=profiles.models.generate_email, max_length=254, unique=True)),
                ('roll_number', models.CharField(default='Not interested', max_length=255)),
                ('department', models.CharField(choices=[('IT', 'INFORMATION TECHNOLOGY'), ('EEE', 'ELECTRICAL AND ELECTRONICS ENGINEERING'), ('ECE', 'ELECTRONICS AND COMMUNICATION ENGINEERING'), ('CIVIL', 'CIVIL'), ('CSE', 'COMPUTER SCIENCE'), ('MECH', 'MECHANICAL'), ('CHEMICAL', 'CHEMICAL'), ('EIE', 'ELECTRONICS AND INSTRUMENTATION ENGINEERING'), ('TEXTILE', 'TEXTILE')], default='IT', max_length=100)),
                ('year', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')], default='I', max_length=3)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

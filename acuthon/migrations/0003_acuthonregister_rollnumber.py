# Generated by Django 3.0.3 on 2020-03-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acuthon', '0002_auto_20200307_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='acuthonregister',
            name='rollnumber',
            field=models.CharField(default='No rollnumber given', max_length=20),
        ),
    ]

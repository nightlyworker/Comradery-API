# Generated by Django 2.2.7 on 2020-01-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0032_auto_20200121_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='invite_code',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]

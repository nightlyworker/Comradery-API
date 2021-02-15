# Generated by Django 2.2.7 on 2020-03-21 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0066_userpostview'),
    ]

    operations = [
        migrations.AddField(
            model_name='customfield',
            name='sort',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='customfield',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_custom_fields', to='forum.Community'),
        ),
    ]
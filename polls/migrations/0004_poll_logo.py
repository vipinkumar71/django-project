# Generated by Django 4.0.3 on 2022-03-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_poll_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='uploads'),
        ),
    ]

# Generated by Django 2.2.2 on 2019-09-26 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_facebookfile_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebookfile',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

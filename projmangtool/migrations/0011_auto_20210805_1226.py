# Generated by Django 3.1 on 2021-08-05 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projmangtool', '0010_auto_20210805_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registereduser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.  Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]

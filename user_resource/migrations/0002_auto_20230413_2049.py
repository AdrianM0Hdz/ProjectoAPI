# Generated by Django 3.2.18 on 2023-04-14 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_resource', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manageruser',
            old_name='firsname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='playeruser',
            old_name='firsname',
            new_name='firstname',
        ),
    ]

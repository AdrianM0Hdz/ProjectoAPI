# Generated by Django 3.2.18 on 2023-04-14 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password_hash', models.CharField(max_length=512)),
                ('firsname', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password_hash', models.CharField(max_length=512)),
                ('firsname', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=32)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_resource.manageruser')),
            ],
        ),
    ]
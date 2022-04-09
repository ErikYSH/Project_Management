# Generated by Django 4.0.3 on 2022-04-07 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management_app', '0005_project_team_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Watch', 'Watch'), ('Complete', 'Complete'), ('Not Started', 'Not Started'), ('In Progress', 'In Progress')], max_length=20),
        ),
    ]
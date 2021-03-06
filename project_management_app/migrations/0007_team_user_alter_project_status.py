# Generated by Django 4.0.3 on 2022-04-07 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_management_app', '0006_alter_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('In Progress', 'In Progress'), ('Not Started', 'Not Started'), ('Watch', 'Watch'), ('Complete', 'Complete')], max_length=20),
        ),
    ]

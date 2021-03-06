# Generated by Django 4.0.3 on 2022-04-03 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management_app', '0003_alter_project_options_project_create_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='create_at',
            new_name='created_at',
        ),
    ]

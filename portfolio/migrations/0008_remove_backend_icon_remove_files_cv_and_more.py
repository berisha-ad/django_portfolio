# Generated by Django 5.1.3 on 2024-11-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_files_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backend',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='files',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='frontend',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.RemoveField(
            model_name='tools',
            name='icon',
        ),
        migrations.AddField(
            model_name='backend',
            name='iconlink',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='files',
            name='cvlink',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='frontend',
            name='iconlink',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='imagelink',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='tools',
            name='iconlink',
            field=models.CharField(max_length=250, null=True),
        ),
    ]

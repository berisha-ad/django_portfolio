# Generated by Django 5.1.3 on 2024-11-14 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_backendskills_frontendskills_tools'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BackendSkills',
        ),
        migrations.DeleteModel(
            name='FrontendSkills',
        ),
        migrations.DeleteModel(
            name='Tools',
        ),
    ]

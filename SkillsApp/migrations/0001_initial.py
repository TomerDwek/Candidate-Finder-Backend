# Generated by Django 4.0 on 2021-12-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('SkillName', models.CharField(max_length=24, primary_key=True, serialize=False)),
            ],
        ),
    ]
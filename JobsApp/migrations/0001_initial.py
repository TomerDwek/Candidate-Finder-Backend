# Generated by Django 4.0 on 2021-12-14 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SkillsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('JobId', models.AutoField(primary_key=True, serialize=False)),
                ('JobTitle', models.CharField(max_length=100)),
                ('JobSkills', models.ManyToManyField(to='SkillsApp.Skill')),
            ],
        ),
    ]

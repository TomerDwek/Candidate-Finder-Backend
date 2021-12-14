# Generated by Django 4.0 on 2021-12-14 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SkillsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('CandidateId', models.AutoField(primary_key=True, serialize=False)),
                ('CandidateTitle', models.CharField(max_length=100)),
                ('CandidateSkills', models.ManyToManyField(to='SkillsApp.Skill')),
            ],
        ),
    ]

# Generated by Django 2.2 on 2020-05-15 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('courseTitle', models.CharField(max_length=50, null=True)),
                ('numberOfParticipants', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stuID', models.IntegerField(primary_key=True, serialize=False)),
                ('stuName', models.CharField(max_length=30, null=True)),
                ('stuEmail', models.EmailField(max_length=60, null=True)),
                ('GPA', models.FloatField(null=True)),
            ],
            options={
                'ordering': ['stuID'],
            },
        ),
        migrations.CreateModel(
            name='StudentLogin',
            fields=[
                ('stuID', models.IntegerField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=10)),
                ('password', models.CharField(default='123456', max_length=20)),
            ],
            options={
                'ordering': ['stuID'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('staffID', models.IntegerField(primary_key=True, serialize=False)),
                ('staffName', models.CharField(max_length=30, null=True)),
                ('staffEmail', models.EmailField(max_length=60, null=True)),
                ('programme', models.CharField(max_length=100, null=True)),
                ('userName', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(default='123456', max_length=20)),
            ],
            options={
                'ordering': ['staffID'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamID', models.CharField(max_length=15, unique=True)),
                ('numberOfMembers', models.IntegerField(default=0)),
                ('courseID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Course')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuName', models.CharField(max_length=30, null=True)),
                ('leader', models.BooleanField(default=False)),
                ('stuID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Student')),
                ('teamID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(through='app01.TeamMembership', to='app01.Student'),
        ),
        migrations.CreateModel(
            name='SubmissionCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submissionID', models.IntegerField(unique=True)),
                ('submissionTitle', models.CharField(max_length=30, null=True)),
                ('percentage', models.CharField(default='0%', max_length=5)),
                ('courseID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='staffIDs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Teacher'),
        ),
        migrations.CreateModel(
            name='MemberContribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessFromLeader', models.FloatField(default=1.0)),
                ('stuID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Student')),
                ('submissionID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.SubmissionCourse')),
            ],
            options={
                'unique_together': {('submissionID', 'stuID')},
            },
        ),
        migrations.CreateModel(
            name='LeaderContribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessFromMember', models.IntegerField(default=0)),
                ('stuID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Student')),
                ('submissionID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.SubmissionCourse')),
            ],
            options={
                'unique_together': {('submissionID', 'stuID')},
            },
        ),
    ]
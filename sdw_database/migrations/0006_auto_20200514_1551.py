# Generated by Django 2.2 on 2020-05-14 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdw_database', '0005_auto_20200514_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='staffID',
        ),
        migrations.DeleteModel(
            name='StudentLogin',
        ),
        migrations.AlterUniqueTogether(
            name='submissioncontributionleader',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='submissioncontributionleader',
            name='stuID',
        ),
        migrations.RemoveField(
            model_name='submissioncontributionleader',
            name='submissionID',
        ),
        migrations.AlterUniqueTogether(
            name='submissioncontributionmember',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='submissioncontributionmember',
            name='stuID',
        ),
        migrations.RemoveField(
            model_name='submissioncontributionmember',
            name='submissionID',
        ),
        migrations.RemoveField(
            model_name='submissioncourse',
            name='courseID',
        ),
        migrations.RemoveField(
            model_name='team',
            name='courseID',
        ),
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
        migrations.RemoveField(
            model_name='teammembership',
            name='stuID',
        ),
        migrations.RemoveField(
            model_name='teammembership',
            name='teamID',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='SubmissionContributionLeader',
        ),
        migrations.DeleteModel(
            name='SubmissionContributionMember',
        ),
        migrations.DeleteModel(
            name='SubmissionCourse',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.DeleteModel(
            name='TeamMembership',
        ),
    ]

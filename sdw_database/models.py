from django.db import models


# Create your models here.
class Student(models.Model):
    stuID = models.IntegerField(primary_key=True)
    stuName = models.CharField(max_length=30, null=True)
    stuEmail = models.EmailField(max_length=60, null=True)
    GPA = models.FloatField(null=True)

    class Meta:
        ordering = ["stuID"]

    def __str__(self):
        return "%s" % self.stuName


class StudentLogin(models.Model):
    stuID = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=10)
    password = models.CharField(max_length=20, default='123456')

    class Meta:
        ordering = ["stuID"]


class Teacher(models.Model):
    staffID = models.IntegerField(primary_key=True)
    staffName = models.CharField(max_length=30, null=True)
    staffEmail = models.EmailField(max_length=60, null=True)
    programme = models.CharField(max_length=100, null=True)
    userName = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, default='123456')

    class Meta:
        ordering = ["staffID"]

    def __str__(self):
        return "%s" % self.staffName


class Course(models.Model):
    courseID = models.CharField(max_length=15, primary_key=True)
    staffIDs = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    courseTitle = models.CharField(max_length=50, null=True)
    numberOfParticipants = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s" % (self.courseID, self.courseTitle)


class Team(models.Model):
    teamID = models.CharField(max_length=15, unique=True)
    courseID = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    numberOfMembers = models.IntegerField(default=0)
    members = models.ManyToManyField(Student, through='TeamMembership')

    def __str__(self):
        return "%s" % self.teamID


class TeamMembership(models.Model):
    teamID = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    stuID = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    stuName = models.CharField(max_length=30, null=True)
    leader = models.BooleanField(default=False)


class SubmissionCourse(models.Model):
    submissionID = models.IntegerField(unique=True)
    courseID = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    submissionTitle = models.CharField(max_length=30, null=True)
    percentage = models.CharField(max_length=5, default='0%')


class MemberContribution(models.Model):
    submissionID = models.ForeignKey(SubmissionCourse, on_delete=models.SET_NULL, null=True)
    stuID = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    assessFromLeader = models.FloatField(default=1.0)

    class Meta:
        unique_together = ("submissionID", "stuID")


class LeaderContribution(models.Model):
    submissionID = models.ForeignKey(SubmissionCourse, on_delete=models.SET_NULL, null=True)
    stuID = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    assessFromMember = models.IntegerField(default=0)

    class Meta:
        unique_together = ("submissionID", "stuID")


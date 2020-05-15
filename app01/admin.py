from django.contrib import admin
from .models import Student, StudentLogin, Teacher, Course, Team, TeamMembership, SubmissionCourse, LeaderContribution, MemberContribution


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuID', 'stuName', 'stuEmail', 'GPA')


@admin.register(StudentLogin)
class StudentLoginAdmin(admin.ModelAdmin):
    list_display = ('stuID', 'userName', 'password')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('staffID', 'staffName', 'staffEmail', 'programme', 'userName', 'password')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseID', 'staffIDs', 'courseTitle', 'numberOfParticipants')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def ShowMembers(self, obj):
        return [i.stuID for i in obj.members.all()]
    list_display = ('teamID', 'courseID', 'numberOfMembers', 'ShowMembers')


@admin.register(TeamMembership)
class TeamMembershipAdmin(admin.ModelAdmin):
    list_display = ('teamID', 'stuID', 'stuName', 'leader')


@admin.register(SubmissionCourse)
class SubmissionCourseAdmin(admin.ModelAdmin):
    list_display = ('submissionID', 'courseID', 'submissionTitle', 'percentage')


@admin.register(MemberContribution)
class MemberContributionAdmin(admin.ModelAdmin):
    list_display = ('submissionID', 'stuID', 'assessFromLeader')


@admin.register(LeaderContribution)
class LeaderContributionAdmin(admin.ModelAdmin):
    list_display = ('submissionID', 'stuID', 'assessFromMember')

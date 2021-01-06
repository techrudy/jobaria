from django.db import models
from django.contrib.auth.models import User, UserManager
# Create your models here.


class Candidate(User):

    objects = UserManager()


class Companies(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()


class Professional(User):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)

    objects = UserManager()


class JobOffers(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    candidate = models.ManyToManyField(Candidate)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()


class JobApplications(models.Model):
    joboffer = models.OneToOneField(JobOffers, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

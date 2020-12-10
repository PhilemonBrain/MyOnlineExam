from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUserManager(BaseUserManager):

    def _create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kwargs):

        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **kwargs)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('Email'), unique=True)
    # exam = models.ForeignKey(Exam, )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email


class Exam(models.Model):
    user = models.ForeignKey(User, related_name='exams', on_delete=models.CASCADE)
    exam_id = models.AutoField(primary_key=True)
    instructions = models.CharField(max_length=255, default="This are instructions for a test exam") #We could consider increasing this value
    title = models.CharField(max_length=100)
    exam_time = models.TimeField(verbose_name="Exam Duration")
    # exam_date = models.DateField

    def __str__(self):
        return self.title


class Question(models.Model):
    # While creating a question user must enter at least two options as answer
    question_id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, related_name="questions", on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=100)
    # order = models.IntegerField()
    optionA = models.CharField(null=False,max_length=100)
    optionB = models.CharField(null=False,max_length=100)
    optionC = models.CharField(null=True,max_length=100)
    optionD = models.CharField(null=True,max_length=100)
    optionE = models.CharField(null=True,max_length=100)
    answer = models.CharField(null=False,max_length=100)

    def __str__(self):
        return self.title
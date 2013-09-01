#!/usr/bin/python
# -*- coding: utf-8

#Django settings
from django.core.management import setup_environ
from askPupkin import settings
setup_environ(settings)

#Connecting with models
from askPupkinApp.models import User,Question,Answer

tempUser = User.objects.get(id=111)
tempUser.delete()
tempQuestion = Question.objects.get(id=555)
tempQuestion.delete()
tempAnswer = Answer.objects.get(id=100505)
tempAnswer.delete()


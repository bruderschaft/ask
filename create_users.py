#!/usr/bin/python
# -*- coding: utf-8

#Django settings
from django.core.management import setup_environ
from ask_pupkin import settings
setup_environ(settings)

#Connecting with models
from askPupkinApp.models import Question,Answer
from django.contrib.auth.models import User

import string
import random

symbols = " ".join(string.letters);
emails = [ "@ya.ru", "@yandex.ru", "@gmail.com" , "@mail.ru" ]
tempUsername = ["",]
tempEmail = ["",]
tempPass = ["",]
tempHeader = ["",]
tempContent = ["",]

for i in range(1):
	tempUsername = "KonstAnTeen2"
	#for j in range(5):
	#	tempUsername.append(random.choice(string.lowercase))
	#tempUsername = "".join(tempUsername)
	
	tempEmail = ["",]
	for j in range(5):
		tempEmail.append(random.choice(string.lowercase))
	tempEmail.append(random.choice(emails))
	tempEmail = "".join(tempEmail)
	
	tempPass = "tempPass"
	#for j in range(5):
	#	tempPass.append(random.choice(string.lowercase))
	#tempPass = "".join(tempPass)
	
	tempUser = User.objects.create_user(tempUsername, tempEmail, tempPass)
	tempUser.save()
	print(tempUsername)
	print(tempPass)
	
	tempQuestion = Question(header='10tempHeader', content='5tempContent', author=tempUser)
	tempQuestion.save()
	tempAnswer = Answer(content='ответный ответ', question=tempQuestion, author=tempUser)
	tempAnswer.save()

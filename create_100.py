#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')


#Django settings
from django.core.management import setup_environ
from ask_pupkin import settings
setup_environ(settings)

import string
import random

#Connecting with models
from askPupkinApp.models import User,Question,Answer
symbols = " ".join(string.letters);
emails = [ "@ya.ru", "@yandex.ru", "@gmail.com" , "@mail.ru" ]
tempUsername = ["",]
tempEmail = ["",]
tempPass = ["",]
tempHeader = ["",]
tempContent = ["",]
for i in range(100):
	#new Users
#	tempLetter = random.choice(string.letters)	
	tempUsername = ["",]
	for j in range(5):
		tempUsername.append(random.choice(string.lowercase))
	tempUsername = "".join(tempUsername)
	
	tempEmail = ["",]
	for j in range(5):
		tempEmail.append(random.choice(string.lowercase))
	tempEmail.append(random.choice(emails))
	tempEmail = "".join(tempEmail)
	
	tempPass = ["",]
	for j in range(5):
		tempPass.append(random.choice(string.lowercase))
	tempPass = "".join(tempPass)

	tempUser = User (email=tempEmail,username=tempUsername,password=tempPass)
	tempUser.save()
	
	for j in range(10):
		tempHeader = []
		for k in range(10):
			tempHeader.append(random.choice(string.lowercase))
		tempHeader = "".join(tempHeader)
		tempContent = ["",]
		for k in range(15):
			tempContent.append(random.choice(string.lowercase))
		tempContent.append('?')
		tempContent = "".join(tempContent)
		tempQuestion = Question(header=tempHeader,content=tempContent,author_id=tempUser.id)
		tempQuestion.save()
	for j in range(100):
		tempContentAn = ["",]
		for k in range(15):
			tempContentAn.append(random.choice(string.lowercase))
		tempContentAn.append(u'. понятно?')#.encode('utf-8')
		tempContentAn = "".join(tempContentAn)
		tempQuestionID = random.randint(2,tempQuestion.id)
		tempAuthorID=tempUser.id
		tempAnswer = Answer (content=tempContentAn, question_id=tempQuestionID, author_id=tempAuthorID)
		tempAnswer.save()
#tempUsername = [a for x in range(6) a=random.choice(string.letters)]
#random.choice
#symbols[random.randrange(len(symbols)-10)]
#	tempEmail = "";
#	tempPassword = "";
#	

#[random.choice(string.letters) for x in range(6)]




#tempUser = User (email='5tempEmail',username='5tempNickname',password='5tempPassword')
#tempUser.save()
#tempQuestion = Question(header='5tempHeader',content='5tempContent',author=tempUser)
#tempQuestion.save()



from django import forms
from askPupkinApp.models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

def index(request):
    q = Question.objects.order_by('-create_date')[0:30]
    u = User.objects.order_by('-date_joined')[0:10]
    for qq in q:
        qq.count = Answer.objects.filter(question_id=qq.id).count()
    #r = Question.objects.get(id=52)
    #s = Question.objects.get(id=53)
    #h = q.header
    #con = q.content
    #q_count = Question.objects.filter(author_id=q.author_id).count()
    #a = Answer.objects.filter(question_id=question_id)

    #t = loader.get_template("index.html")
    return render(request, 'index.html', {'qq': q})

def questions (request, question_id):
    q = Question.objects.get(id=question_id)
    a = Answer.objects.filter(question_id=question_id)
    t = loader.get_template("question.html")
    q_count = Question.objects.filter(author_id=q.author_id).count()  

    #if request.method=='POST':
    #    form = AnswerForm(request.POST)
    #    if form.is_valid():
    #        user = User.objects.get(username='iuqda')
    #        userr = request.user
    #        print(userr)
    #        answer = Answer(content=form.cleaned_data['content'],author=userr, question=q)
    #        answer.save()
    #    return HttpResponseRedirect(request.path)
    #else:
    #    form = AnswerForm()  
    last_users = User.objects.order_by('-date_joined')[0:10]
    c = RequestContext(request,{'header': 'fjjj', 'qq':q, 'aa':a,'q_count':q_count, 'last_users': last_users})
    return HttpResponse(t.render(c))
#####################################################################################################################################
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    #    state_logon = forms.BooleanFiend(required=False)

    def clean_username(self):
        username1 = self.cleaned_data.get('username')
        exis = User.objects.filter(username=username1).exists()
        if  exis:
            #raise forms.ValidationError("Another username should you choose")
            msg = "Not correct your username is."
            self._errors["username"] = self.error_class([msg])
        return username1

#    def clean(self):
#        #cleaned_data = super(LoginForm, self).clean()
#        username1 = self.cleaned_data.get('username')
#        password1 = self.cleaned_data.get('password')
#        if not self.errors:
#           user = authenticate(username=username1, password=password1)
#        if user is None:
#           raise forms.ValidationError("not okk")
#            msg = "passwords!="
#           self._errors["password2"] = self.error_class([msg])
#           self.user = user
#        return cleaned_data

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            #passs = User.objects.get(username=cleaned_data['username']).password
            if user is None:
                ##exis = User.objects.get(username=cleaned_data['username']).exists() # in clean_username
                ##if not exis:
                ##    msg = "username not exists!!!11"
                ##    self._errors["username"] = self.error_class([msg])
                msg = "login or password not correct"
                self._errors["password"] = self.error_class([msg])
                #raise forms.ValidationError('not okk!!!!!'+' '+ cleaned_data['username']+ ' ')
            self.user = user
        return user

    def get_user(self):
        return self.user or None



#def log_in(request):
#    if request.method == 'POST': # If the form has been submitted...
#        form = LoginForm(request.POST) # A form bound to the POST data
#        if form.is_valid():
#        ##username = form.cleaned_data['username']
#            ##password = form.cleaned_data['password']
#            username = request.POST['username']
#            password = request.POST['password']
#            #state_logon = form.cleaned_data['state_logon']
#            login(request, form.get_user())
#            return HttpResponseRedirect(request.path) # Redirect after POST
#    else:
#        form = LoginForm() # An unbound form

#    return render(request, 'login.html', {
#        'form': form
#    })
def log_in(request):
    if ('username' in request.REQUEST) and ('password' in request.REQUEST):
        username = request.REQUEST['username']
        password = request.REQUEST['password']
        usser = authenticate(username=username, password=password)
        flag = False
        if usser is not None:
            flag = True
            login(request, usser)
            return HttpResponseRedirect('/')
    return render(request, 'base1.html', {'user': usser})
    #return HttpResponseRedirect('/')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


  
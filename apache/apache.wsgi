import os, sys
# место, где лежит джанго
sys.path.append('/home/maxim/Django-1.5.1/')
# место, где лежит проект
sys.path.append('/home/maxim/PycharmProjects/ask_pupkin/')
# файл конфигурации проекта
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

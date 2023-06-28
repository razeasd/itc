# ITC site v.1
Django, HTML5 + CSS
Trial site site will be disabled on Thursday 28 September 2023 http://raze33.pythonanywhere.com/ 

![image](https://github.com/razeasd/itc/assets/66547997/ad78442f-fe2a-4e3b-a580-64e71257c58b)

# Security
# X-XSS-Protection
Межсайтовый скриптинг (Cross-Site Scripting), или XSS, – это метод, который злоумышленники могут использовать для внедрения своего собственного кода на ваш сайт. С помощью этого вида атаки можно например, добавить ложный контент или шпионить за пользователями, чтобы украсть их пароли. Настройка заголовка X-XSS-Protection для использования «block mode» обеспечивает дополнительную безопасность. Это настройка указывает браузеру полностью блокировать страницы с обнаруженными атаками XSS, в случае, если они содержат другие проблемные элементы.

#Web-app deploy instruction 
Visit and register https://www.pythonanywhere.com/

Push your project to github

Start bash console at pythonanywhere

Git clone your project to pythonanywhere

Create virtual env

cd to clonned project dir
    python3 -m venv env
Activate venv and install all dependencies

Create new custom webapp at pythonanywhere

Fill in all the gaps

Source code: - the path to the folder with manage.py (/home/denniskot/django-dummy/src)
Virtualenv:
The path to the folder with virtual env (/home/denniskot/django-dummy/env)
Static files:
Create in bash conslole folders static and media on the same level as src folder. (/home/denniskot/django-dummy/static and /home/denniskot/django-dummy/media)
Add url /static/ and directory /home/denniskot/django-dummy/static
Add url /media/ and directory /home/denniskot/django-dummy/media
Edit WSGI configuration file (click the link)

Comment "hello world" section

Find "django" section

Comment out django section
Change path to the folder with your 'manage.py' file (/home/denniskot/django-dummy/src)
Change os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings' where mysite is the project/module/folder name with 'settings.py' file (os.environ['DJANGO_SETTINGS_MODULE'] = 'proj.settings')
My WSGI file
+++++++++++ DJANGO +++++++++++
To use your own django app use code like this:
import os
import sys

assuming your django settings file is at '/home/denniskot/mysite/mysite/settings.py'
and your manage.py is is at '/home/denniskot/mysite/manage.py'
path = '/home/denniskot/django-dummy/src'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'proj.settings'

then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
Edit settings.py

edit
ALLOWED_HOSTS = ['yourloginname.pythonanywhere.com',]
add lines below STATIC_URL
Change path in *_ROOT according to your static and media path
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/denniskot/django-dummy/static'
MEDIA_ROOT = '/home/denniskot/django-dummy/media'
reload webapp

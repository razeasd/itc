<h1 align="center">Site for ITC</h1> 

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)  

  ![image](https://img.shields.io/badge/onwork-text)   
  Site made by Fedorov A. for "ITC"  
  _Trial site will be disabled on Thursday 28 September 2023_  
  http://raze33.pythonanywhere.com/
  
# Web-app scheme
  ![image](https://github.com/razeasd/itc/assets/66547997/ad78442f-fe2a-4e3b-a580-64e71257c58b)

# Security
# X-XSS-Protection
Межсайтовый скриптинг (Cross-Site Scripting), или XSS, – это метод, который злоумышленники могут использовать для внедрения своего собственного кода на ваш сайт. С помощью этого вида атаки можно например, добавить ложный контент или шпионить за пользователями, чтобы украсть их пароли. Настройка заголовка X-XSS-Protection для использования «block mode» обеспечивает дополнительную безопасность. Это настройка указывает браузеру полностью блокировать страницы с обнаруженными атаками XSS, в случае, если они содержат другие проблемные элементы.

# Web-app deploy instruction 
Visit and register https://www.pythonanywhere.com/

Push your project to github

Start bash console at pythonanywhere

Git clone your project to pythonanywhere

Create virtual env

cd to clonned project dir
`python3 -m venv env`
Activate venv and install all dependencies

Create new custom webapp at pythonanywhere

Fill in all the gaps

Source code: - the path to the folder with manage.py (/home/src)
Virtualenv:
The path to the folder with virtual env (/home/env)
Static files:
Create in bash conslole folders static and media on the same level as src folder. 
Add url /static/ and directory /home/static
Add url /media/ and directory /home/media

Edit WSGI configuration file
Comment "hello world" section
Find "django" section

Comment out django section
Change path to the folder with your 'manage.py' file (/home/src)
Change os.environ
```
['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
```
where mysite is the project/module/folder name with 'settings.py' file 
```
(os.environ['DJANGO_SETTINGS_MODULE'] = 'proj.settings')
```

+++++++++++ DJANGO +++++++++++
To use your own django app use code like this:  
```
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
application = get_wsgi_application()`
```
Edit settings.py

```
ALLOWED_HOSTS = ['yourloginname.pythonanywhere.com',]
```
add lines below STATIC_URL

Change path in *_ROOT according to your static and media path
```
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/denniskot/django-dummy/static'
MEDIA_ROOT = '/home/denniskot/django-dummy/media' 
```
reload webapp


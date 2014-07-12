#Applications

The web application on Python2/Django/jQuery. The application management system. 
It’s used by one of the local ISP companies in Russia. The interface is in Russian.

#Описание

Система позволяет принимать заявки на подключение.

##Required packages

* [Python v2.6.5+](http://www.python.org)
* [Django v1.5](http://djangoproject.com)
* [django-annoying v0.7.7+](https://github.com/skorokithakis/django-annoying)
* pyExcelerator v0.6.4.1

##Used Javascript libraries
* [jQuery v1.9.1](http://jquery.com/)
* [jQuery UI v1.10.2](http://jqueryui.com/)
* [jQuery UI Bootstrap v0.5](http://addyosmani.github.com/jquery-ui-bootstrap/)
* [jQuery plugin: Validation v1.11.0](http://bassistance.de/jquery-plugins/jquery-plugin-validation/)
* [jGrowl v1.2.11]( https://github.com/stanlemon/jGrowl)

##Installation instructions

* Insert your database settings in settings.py

* Run
```
python manage.py syncdb
python manage.py collectstatic
```

* Import db.sql to your database. db.sql also includes some example data.

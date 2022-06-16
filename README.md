# fastestcrm
Программа, которая помогает бизнесу не терять заявки, хранить историю работы с клиентами и упрощает процесс продаж. 

##### Задача: спроектировать и разработать CRM для системы продаж

CRM — Customer Relationship Management(управление отношениями с клиентами) - программа, 
которая помогает бизнесу не терять заявки, хранить историю работы с клиентами и упрощает процесс продаж.

##### _разработка Sayfullin R.R. 

========================================================================================================================

### _Документация  (документирование c помощью плагина IDEA Mind Map для Intellij IDEA

========================================================================================================================

##### Описание ТЗ:

## Окружение проекта: requirements.txt

========================================================================================================================

Склонируйте репозиторий с помощью git:
https://github.com/RuslanSayfullin/fastestcrm.git

перейти в папку:
$ cd fastestcrm

Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```
========================================================================================================================

# Отладка Django — добавление Django Debug Toolbar в проект

1) Установка библиотеки: pip install django-debug-toolbar;
2) Добавление в INSTALLED_APPS: в settings.py добавьте debug_toolbar в раздел INSTALLED_APPS(после django.contrib.staticfiles).
Также убедитесь, что в файле settings.py присутствует следующая строка STATIC_URL = '/static/';
3) Импорт в urls.py: Чтобы использовать Debug Toolbar, мы должны импортировать его пути. Следовательно, в urls.py добавьте код:
# debug_tool/urls.py
...
from django.conf import settings
from django.urls import path, include

# urlpatterns = [....

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

4) Подключение MiddleWare:
Добавьте middleware панели инструментов debug_toolbar.middleware.DebugToolbarMiddleware, в список MIDDLEWARE в settings.py.

5) Упоминание INTERNAL_IPS:
Django Debug Toolbar отображается только в том случае, если в списке INTERNAL_IPS есть IP приложения. 
Для разработки на локальном компьютере добавьте в список IP 127.0.0.1.

========================================================================================================================
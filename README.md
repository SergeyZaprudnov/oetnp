# OETNP (Online electronics trading network platform)

In this task you are asked to develop an online platform for an electronics retail chain.

# Technical requirements:

     Python 3.8+
     Django 3+
     DRF 3.10+
     PostgreSQL 10+

# Exercise:

     - Create a web application with an API interface and admin panel.
     - Create a database using Django migrations.

# Implementation requirements:

     1. It is necessary to implement a network model for selling electronics.

     The network should be a hierarchical structure of 3 levels:
         Factory;
         Retail network;
         Individual entrepreneur.

     Each link in the network refers to only one equipment supplier (not necessarily the previous one 
     in the hierarchy). It is important to note that the hierarchy level is determined not by the name 
     of the link, but by its relationship to other elements of the network, i.e. The plant is always 
     at level 0, and if the retail network relates directly to the plant, bypassing other links, its 
     level is -1.

     2. Each link in the network must have the following elements:
         - Name;
         - Contacts:
             Email;
             A country;
             City;
             Street;
             House number;
         - Products:
             Name;
             Model;
             Date of product launch on the market;
         - Supplier (the previous network object in the hierarchy);
         - Debt to the supplier in monetary terms, accurate to the nearest kopeck;
         - Creation time (filled in automatically upon creation).

     3. Display created objects in the admin panel:
        On the network object page add:
         - link to the “Supplier”;
         - filter by city name;
         - “admin action”, clearing the debt to the supplier for the selected objects.

     4. Using DRF, create a set of views:
        CRUD for the supplier model (prohibit updating the “Debt to Supplier” field via the API);

     5. Add the ability to filter objects by a specific country.
        Configure API access rights so that only active employees have access to the API.

# To launch the application, follow these steps:
    1. Clone the project from the repository
    2. Install the dependencies of the requirements.txt file with the command: pip install -r requirements.txt
    3. Activate the virtual environment with the command: source venv/bin/activate (if it is not activated)
    4. Create a .env file and make settings using the .env.example file as an example (in this case, database settings)
    5. Apply database migrations with the command: python3 manage.py migrate
    6. Start the server (locally) with the command: python3 manage.py runserver

# URLs for launching documentation:
     - Swagger:        http://127.0.0.1:8000/api/schema/swagger-ui/
     - Redoc:          http://127.0.0.1:8000/api/redoc/
     - Admin pannel:   http://127.0.0.1:8000/admin/


# - - - RU - - -

В данном задании вам предлагается разработать онлайн платформу торговой сети электроники.

# Технические требования:

    Python 3.8+
    Django 3+
    DRF 3.10+
    PostgreSQL 10+

# Задание

    Создайте веб-приложение, с API интерфейсом и админ-панелью.
    Создайте базу данных используя миграции Django.

# Требования к реализации:

    1. Необходимо реализовать модель сети по продаже электроники.
       Сеть должна представлять собой иерархическую структуру из 3 уровней:
           Завод;
           Розничная сеть;
           Индивидуальный предприниматель.

    Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего 
    по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением 
    к остальным элементам сети, т.е. завод всегда находится на 0 уровне, а если розничная сеть 
    относится напрямую к заводу, минуя остальные звенья - её уровень - 1.

    2. Каждое звено сети должно обладать следующими элементами:
        - Название;
        - Контакты:
              Email;
              Страна;
              Город;
              Улица;
              Номер дома;
        - Продукты:
              Название;
              Модель;
              Дата выхода продукта на рынок;
        - Поставщик (предыдущий по иерархии объект сети);
        - Задолженность перед поставщиком в денежном выражении с точностью до копеек;
        - Время создания (заполняется автоматически при создании).

    3. Сделать вывод в админ-панели созданных объектов:
       На странице объекта сети добавить:
          - ссылку на «Поставщика»;
          - фильтр по названию города;
          - «admin action», очищающий задолженность перед поставщиком у выбранных объектов.

    4. Используя DRF, создать набор представлений:
       CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед 
       поставщиком»);

    5. Добавить возможность фильтрации объектов по определенной стране.
       Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.


# Для запуска приложения выполните следующие щаги:
   1. Клонировать проект с репозитория
   2. Установить зависимости файла requirements.txt командой: pip install -r requirements.txt
   3. Активировать виртуальное окружение командой: source venv/bin/activate (усли оно не активировано)
   4. Создать файл .env и внести настройки на примере файла .env.example ( в данном случае настройки БД)
   5. Выполнить применение миграций БД командой: python3 manage.py migrate
   6. Запустить сервер (локально) командой: python3 manage.py runserver


#  URL-адреса для запуска документации:
     - Swagger:        http://127.0.0.1:8000/api/schema/swagger-ui/
     - Redoc:          http://127.0.0.1:8000/api/redoc/
     - Admin pannel:   http://127.0.0.1:8000/admin/
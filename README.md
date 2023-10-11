OETNP (Online electronics trading network platform)

Exercise
In this task you are asked to develop an online platform for an electronics retail chain.

Technical requirements:

     Python 3.8+
     Django 3+
     DRF 3.10+
     PostgreSQL 10+

Exercise

     Create a web application with an API interface and admin panel.
     Create a database using Django migrations.

Implementation requirements:

     It is necessary to implement a network model for selling electronics.

     The network should be a hierarchical structure of 3 levels:
         Factory;
         Retail network;
         Individual entrepreneur.

     Each link in the network refers to only one equipment supplier (not necessarily the previous one in the hierarchy). It is important to note that the hierarchy level is determined not by the name of the link, but by its relationship to other elements of the network, i.e. The plant is always at level 0, and if the retail network relates directly to the plant, bypassing other links, its level is 1.
     Each link in the network must have the following elements:
         Name;
         Contacts:
             Email;
             A country;
             City;
             Street;
             House number;
         Products:
             Name;
             Model;
             Date of product launch on the market;
         Supplier (the previous network object in the hierarchy);
         Debt to the supplier in monetary terms, accurate to the nearest kopeck;
         Creation time (filled in automatically upon creation).
     Display created objects in the admin panel

     On the network object page add:
         link to the “Supplier”;
         filter by city name;
         “admin action”, clearing the debt to the supplier for the selected objects.
     Using DRF, create a set of views:

     CRUD for the supplier model (prohibit updating the “Debt to Supplier” field via the API);

     Add the ability to filter objects by a specific country.
     Configure API access rights so that only active employees have access to the API.


Задание
В данном задании вам предлагается разработать онлайн платформу торговой сети электроники.

Технические требования:

    Python 3.8+
    Django 3+
    DRF 3.10+
    PostgreSQL 10+

Задание

    Создайте веб-приложение, с API интерфейсом и админ-панелью.
    Создайте базу данных используя миграции Django.

Требования к реализации:

    Необходимо реализовать модель сети по продаже электроники.

    Сеть должна представлять собой иерархическую структуру из 3 уровней:
        Завод;
        Розничная сеть;
        Индивидуальный предприниматель.

    Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т.е. завод всегда находится на 0 уровне, а если розничная сеть относится напрямую к заводу, минуя остальные звенья - её уровень - 1.
    Каждое звено сети должно обладать следующими элементами:
        Название;
        Контакты:
            Email;
            Страна;
            Город;
            Улица;
            Номер дома;
        Продукты:
            Название;
            Модель;
            Дата выхода продукта на рынок;
        Поставщик (предыдущий по иерархии объект сети);
        Задолженность перед поставщиком в денежном выражении с точностью до копеек;
        Время создания (заполняется автоматически при создании).
    Сделать вывод в админ-панели созданных объектов

    На странице объекта сети добавить:
        ссылку на «Поставщика»;
        фильтр по названию города;
        «admin action», очищающий задолженность перед поставщиком у выбранных объектов.
    Используя DRF, создать набор представлений:

    CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»);

    Добавить возможность фильтрации объектов по определенной стране.
    Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.

# Django_shop_project
## Описание
В текущем проекте я буду создавать интернет магазин и шаг за шагом разбираться с фреймворком Django, языком разметки HTML, языком стилей CSS и возможностями оптимизации jinja. Каждый шаг будет описан ниже.  

Заполнение БД --> `python manage.py loaddata saved_data.json`  
Логин-пароль админки --> admin - admin  
## Шаги реализации
### Шаг первый
- Создан основной интерфейс страниц, описаны первые шаги, знакомство с jinja, html, css и django.  
- В приложении реализовано два контроллера:  
  - Контроллер, который отвечает за отображение домашней страницы.  
  -  Контроллер, который отвечает за отображение контактной информации.  
- Реализована обработка сбора обратной связи от пользователя, который зашел на страницу контактов и отправил свои данные для обратной связи.  
### Шаг второй
- Подключена СУБД PostgreSQL для работы в проекте  
- В приложении каталога созданы модели:  
  - Product  
  - Category  
- Использованы создание, применение и откат миграций.  
- Для моделей категории и продукта настроено отображение в административной панели.  
- Настроена возможность фильтровать результат отображения фильтровать по категории, а также осуществлять поиск по названию и полю описания.  
- Освоен инструмент shell для взаимодействия с БД.  
- Использованы фикстуры для заполнения базы данных.  
- Создана кастомная команда, которая умеет заполнять данные в базу данных, при этом предварительно зачищать ее от старых данных.  
- В контроллер отображения главной страницы добавлена выборка последних 5 товаров.  
- Создана модель для хранения контактных данных и их вывод на страницу с контактами.  
### Шаг третий
- Создан контроллер и шаблон, который отвечает за отображение отдельной страницы с товаром.  
- В созданный ранее шаблон для главной страницы выведен список товаров в цикле.  
- Для единообразия выводимых карточек отображаемое описание обрезано после первых выведенных 100 символов.  
- Разобрал с кастомные теги и фильтры (создан тег для получения пути файла media).  
- Добавлен функционал создания продукта через внешний интерфейс.  
- Реализован постраничный вывод списка продуктов.  
- Разобрал создание форм внутри Django и использовал для добавления товара через сайт.
- Разобрал загрузку файлов через форму.  
### Шаг четвертый
- Разобрана тема инлайн-формсетов.
- Переработана форма добавления товара (вместо  переписывания метода post теперь используются методы form_in/valid, get_context_data).
- При создании товара теперь автоматически создается версия продукта 1.0 с описанием "Название товара".  
- Добавлена обработка полей формы товара на проверку запрещенных слов.  
- Добавлена новая модель «Версия», которая отражает данные о текущей версии продукта.  
- При наличии активной версии выводятся данные о версии на странице товара.  
- При изменении версий добавлена проверка на только одну используемую версию. В случае нескольких активных версий возвращаем ошибку-уведомление пользователю об ограничении только одной активной версии на товар.  

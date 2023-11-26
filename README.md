# Django_shop_project  
## Описание  
В текущем проекте я буду создавать интернет магазин и шаг за шагом разбираться с фреймворком Django, языком разметки HTML, языком стилей CSS и возможностями оптимизации jinja. Каждый шаг будет описан ниже.  

Доступный функционал:
- Система аккаунтов, смена и сброс пароля.  
- Добавление, изменение продуктов зарегистрированным пользователям.  
- Блог, который могут редактировать только контент-менеджеры и супер-пользователи.
- Роль модератора, которая может редактировать описание, категорию и статус публикации продукта после модерации.

Заполнение БД --> `python manage.py loaddata saved_data.json`  

## Права доступа и аккаунты  
### Супер-пользователь  
Создание супер-пользователя --> `python manage.py csu`  
Логин пароль супер-пользователя --> admin@gmail.com - admin  
### Модератор  
Имеет доступ к изменению описания, категории и статуса публикации продукта.  
Создание модератора --> `python manage.py cmoder`  
Логин пароль модератора --> moder@gmail.com - moder  
### Контент-менеджер  
Имеет доступ к созданию и редактированию блога.  
Создание контент-менеджера --> `python manage.py ccontentmanager`  
Логин пароль контент-менеджера --> content@gmail.com - content  
## Первоначальная настройка  
- Создать виртуальное окружение и войти в него.  
- Установка зависимостей --> `pip install -r r.txt`  
- Переименовать файл .env.tpl --> .env и заполнить его.
- Заполнение БД --> `python manage.py loaddata saved_data.json`  
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
### Шаг пятый  
- Знакомство с системой аутентификации, кастомной моделью пользователя, стандартными вьюхами и формами для регистрации, авторизации, смены пароля и сброса пароля.  
- Создайно новое приложение для работы с пользователем. Переопределена стандартная форма авторизации, добавлены новые поля в профиль.  
- В сервисе реализован следующий функционал аутентификации:  
  - регистрацию пользователя по почте и паролю;  
  - верификацию почты пользователя через отправленное письмо;  
  - авторизацию пользователя;  
  - восстановление пользователя через почту.  
- Закрыты для анонимных пользователей все контроллеры, которые отвечают за работу с продуктами. При этом создаваемые продукты автоматически привязываются к авторизованному пользователю.
- Добавлен интерфейс редактирования профиля пользователя.
### Шаг шестой  
- Знакомство с правами доступа, миксинами и декораторами, кастомными правами, группами пользователей. Использование jinja для кастомизации отображения страницы в зависимости от прав.
- Доработка модели продуктов полем статуса публикации и изменение отображения продукта в списке и принадлежности товара пользователю.  
- Создание роли модератора со следующими правами:  
  - может отменять публикацию продукта,  
  - может менять описание любого продукта,  
  - может менять категорию любого продукта.  
- Реализовано решение, которое проверяет, что редактирование продукта доступно только его владельцу, модератору и суперпользователю.  
- Выделена отдельная роль для пользователя контент-менеджера, который может управлять публикациями в блоге.  
- Изучение модуля django-filters для возможности фильтрации продуктов по статусу опубликованности. Доступна только модераторам и супер-юзеру.
### Шаг седьмой  
- Знакомство с типами кеширования, уровнями кеширования, брокерами, использование python_dotenv для использования персональных настроек проекта и безопасности.  
- Добавление страницы категорий продуктов. Добавление фильтра категорий в каталоге для всех пользователей.  
- Настройка кеширования всего контроллера отображения данных относительно одного продукта.  
- Создание сервисной функции, которая отвечает за выборку категорий и которую можно переиспользовать в любом месте системы. Добавлено низкоуровневое кеширование для списка категорий.
- Вынесены необходимые настройки в переменные окружения и проект настроен для работы с ними.
- Оптимизоран процесс добавления пользователя в группу.  


# Вопросы с собеседований

## 1. Что такое инженерия и процесс разработки в целом?
   - процесс, посредством которого потребности пользователей преобразуются в программный продукт

## 2. Какие знаете принципы программирования?
   - DRY - Принцип „отсутствия повторов” (“don’t repeat yourself” ) имеет решающее значение при написании чистого и легко изменяемого кода. При написании кода следует избегать дублирования данных и логики. Если вы заметили, что один и тот же фрагмент кода написан снова и снова, принцип был нарушен
    
   - KISS (акроним для «Keep it simple, stupid» — «Делай проще, тупица») - Принцип KISS утверждает, что большинство систем работают лучше всего, если они остаются простыми, а не усложняются. Поэтому в области проектирования простота должна быть одной из ключевых целей, и следует избегать ненужной сложности.
    
   - FIFO (англ. first in, first out «первым пришёл — первым ушёл») — способ организации и манипулирования данными относительно времени и приоритетов. Это выражение описывает принцип технической обработки очереди или обслуживания конфликтных требований путём упорядочения процесса по принципу: «первым пришёл — первым обслужен» (ПППО). Тот, кто приходит первым, тот и обслуживается первым, пришедший следующим ждёт, пока обслуживание первого не будет закончено, и так далее. Этот принцип аналогичен поведению лиц, стоящих в очереди, когда люди получают обслуживание в том порядке, в котором они занимали очередь.
    
   - SOLID (single responsibility, open–closed, Liskov substitution, interface segregation и dependency inversion) — мнемонический акроним, означающий 5 основных принципов объектно-ориентированного программирования и проектирования:
   - Принцип единственной ответственности (англ. single-responsibility principle, SRP) — принцип ООП, обозначающий, что каждый объект должен иметь одну ответственность и эта ответственность должна быть полностью инкапсулирована в класс. Все его поведения должны быть направлены исключительно на обеспечение этой ответственности.
   - При́нцип откры́тости/закры́тости (англ. open–closed principle, OCP) - Принцип открытости/закрытости означает, что программные сущности должны быть:

        > открыты для расширения: означает, что поведение сущности может быть расширено путём создания новых типов сущностей.
          
        > закрыты для изменения: в результате расширения поведения сущности, не должны вноситься изменения в код, который эту сущность использует.
      
   - Принцип подстановки Барбары Лисков (англ. Liskov Substitution Principle, LSP) - более простыми словами можно сказать, что поведение наследующих классов не должно противоречить поведению, заданному базовым классом, то есть поведение наследующих классов должно быть ожидаемым для кода, использующего переменную базового типа.
   - Принцип разделения интерфейса (англ. interface segregation principle, ISP) — говорит о том, что слишком «толстые» интерфейсы необходимо разделять на более маленькие и специфические, чтобы программные сущности маленьких интерфейсов знали только о методах, которые необходимы им в работе.
   - Принцип инверсии зависимостей (англ. dependency inversion principle, DIP) — классы должны зависеть от абстракций, а не от конкретных деталей
      
## 3. Чем отличаются процедурная и объектов-ориентированная парадигмы программирования?
   - Процедурное программирование - это тип программирования, в котором инструкции для решения задачи выполняются одна за другой, сверху вниз, иногда возникают изменения в их последовательности. Когда программа становится более сложной на помощь приходят методы. 
   - Объектно-ориентированное программирование (ООП) - методика программирования, в которой основными концепциями являются понятия объектов и классов. 
        ###### Процедурное программирование можно сравнить с постройкой маленького домика - нет необходимости тратить время и ресурсы на продумывание архитектуры. ООП же похоже на постройку сложного архитектурного сооружения, где очень важно продумать все детали, и только потом приступать к программированию

## 4. Какие основные принципы ООП (наследование, инкапсуляция, полиморфизм)?
   - Инкапсуляция – сокрытие данных, т. е. классы не имеют прямого доступа к полям друг друга, а взаимодействие между ними осуществляется через публичные методы.
   - Наследование – процесс при котором дочерний класс приобретает все св-ва и методы родителя, при этом дочерний класс может быть дополнен своим функционалом. 
   - Полиморфизм – (в python исп. параметрический полиморфизм) -  это способность одного и того же объекта вести себя по-разному в зависимости от того, в контексте какого класса он используется.

## 5. Что такое множественное наследование?
   - это возможность класса иметь более одного родительского класса. При множественном наследовании дочерний класс наследует все свойства родительских классов. Синтаксис множественного наследования очень похож на синтаксис обычного наследования.

## 6. Какие есть шесть этапов разработки продукта в Software Development lifecycle и какая разница между Agile и Kanban?
   - Анализ, составление требований к продукту.
   - Планирование.
   - Проектирование и дизайн.
   - Разработка.
   - Тестирование.
   - Развертывание, эксплуатация.
      - [Agile](https://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%B1%D0%BA%D0%B0%D1%8F_%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F_%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8) – это набор принципов, помогающих делать новые продукты быстрее и приносить большую ценность пользователям. Многие гибкие методологии, например, Scrum, основаны на философии Agile.

      - [Scrum](https://ru.wikipedia.org/wiki/Scrum) – это метод разработки нового продукта. Подходит для ситуации, когда вы разрабатываете инновационный продукт и не можете запланировать заранее, какой результат получится.

      - [Kanban](https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BD%D0%B1%D0%B0%D0%BD) – это метод улучшения работы в компании.

## 7. Какие есть методы HTTP-запросов и какая между ними разница?

   - **GET** запрашивает представление ресурса. Запросы с использованием этого метода могут только извлекать данные.

   - **HEAD** запрашивает ресурс так же, как и метод GET, но без тела ответа.

   - **POST** используется для отправки сущностей к определённому ресурсу. Часто вызывает изменение состояния или какие-то побочные эффекты на сервере.

   - **PUT** заменяет все текущие представления ресурса данными запроса.

   - **DELETE** удаляет указанный ресурс.

   - **CONNECT** устанавливает "туннель" к серверу, определённому по ресурсу.

   - **OPTIONS** используется для описания параметров соединения с ресурсом.

   - **TRACE** выполняет вызов возвращаемого тестового сообщения с ресурса.

   - **PATCH** используется для частичного изменения ресурса.

## 8. Как выглядят HTTP-request / response?
   - Обычно HTTP request(запрос) содержит:
      * строку запроса, в которой указывается версия HTTP протокола и HTTP метод запроса;
      * ноль или несколько заголовков, разделенных между собой символом конца строки, в которых передаются другие HTTP праметры для успешного HTTP соединения;
      * пустую строку, чтобы отделить служебную информацию от тела сообщения;
      * необязательное тело сообщения.
   
   
   - Структура HTTP ответа сервера состоит из:
      * Строки состояния HTTP ответа, в которой сервер указывает версию HTTP протокола и код состояния.
      * Нуля или нескольких полей HTTP заголовка, разделенных между собой символом CRLF.
      * Пустой строки (в этой строке должен быть только символ CRLF), эта строка обозначает окончание полей заголовка.
      * Необязательное тело HTTP сообщения.

## 9. Что такое авторизация и как она работает?
   - Авторизация — процесс предоставления пользователю или группе пользователей определенных разрешений, прав доступа и привилегий в компьютерной системе.
   - Когда пользователь хочет войти в систему, приложение отправляет запрос авторизации на сервер авторизации. Учетные данные пользователя проверяются сервером авторизации, и если все хорошо, сервер авторизации выдает идентификационный токен приложению.

## 10. Что такое cookies?
   - Файлы cookie – это небольшие фрагменты данных, передаваемые в браузер с сайта, который вы открываете. С их помощью сайт запоминает информацию о ваших посещениях. Это упрощает взаимодействие с сайтом

## 11. Что такое веб уязвимость?
   - это возможности их взлома из-за наличия ошибок в программном коде, неправильных настроек системы управления контентом (CMS) и операционной системы веб-сервера
## 12. Классические базы данных.
   - Реляционная - это набор данных с предопределенными связями между ними. Эти данные организованны в виде набора таблиц, состоящих из столбцов и строк. В таблицах хранится информация об объектах, представленных в базе данных
      > Распространенные: MySQL, Oracle DB, PostgreSQL, SQLite, Microsoft SQL
   - Иерархическая - это модель данных, где используется представление базы данных в виде древовидной (иерархической) структуры, состоящей из объектов (данных) различных уровней
   - Сетевая - логическая модель данных, являющаяся расширением иерархического подхода, строгая математическая теория, описывающая структурный аспект, аспект целостности и аспект обработки данных в сетевых базах данных
   - Объектные или объектно-ориентированные
   - Объектно-реляционные
   - Функциональные

## 13. Как читать спецификацию в конкретном языке (например, PEP8 в Python)?
   - ?????

## 14. Как происходит взаимодействие клиента и сервера?
   - Веб-браузеры взаимодействуют с веб-серверами при помощи протокола передачи гипертекста (HTTP). Когда вы кликаете на ссылку на странице, заполняете форму или производите поиск, браузер отправляет на сервер HTTP-запрос

## 15. Какие есть подходы к проектированию API?

   ****REST****
 
   Эти принципы ввёл Рой Филдинг в 2000 году в своей диссертации «Архитектурные стили и дизайн сетевых программных структур».
   - Клиент-сервер. Разделение ответственности между клиентом и сервером
Клиент и сервер отвечают за разные вещи. Ответственность клиента — пользовательский интерфейс, ответственность сервера — данные. Если API возвращает HTML-страницу, его нельзя назвать REST API: ведь при этом сервер берёт на себя ответственность за интерфейс.
   - Отсутствие состояния. Сервер не хранит состояние
Каждый запрос должен быть независимым, как будто он сделан в первый раз. Сервер не должен хранить какой-либо информации о клиенте. Каждый запрос клиента к серверу должен содержать всю информацию, необходимую для обработки этого запроса: кто запрашивает данные, какие данные запрашиваются.
   - Единый интерфейс
Интерфейс обращения к серверу одинаков для всех и не зависит от клиента. Запрос к данным может быть сформирован из браузера, мобильного приложения и с «умного» чайника по одним и тем же правилам.
    - Многоуровневость
Первый принцип гласит, что в коммуникации участвуют двое: клиент и сервер. Но можно строить более сложные системы, не нарушая этого принципа.
API сервиса Яндекс.Такси может использовать API Яндекс.Навигатора. Вы как клиент взаимодействуете только с API Яндекс.Такси, а он, в свою очередь, является клиентом навигатора. Здесь есть одно условие — каждый компонент должен видеть только свой уровень. Например, Яндекс.Навигатор не должен видеть все данные, которые вы отправили в Яндекс.Такси.
   - Кешируемость
Данные ответа могут быть закешированы. Это значит, что можно сохранить полученные данные на клиенте, а при идентичном запросе взять их из памяти клиента — кеша, а не ждать их с сервера. Нет смысла запрашивать данные повторно, если они никак не изменились.
   - Код по запросу
Этот принцип необязательный. Он гласит, что функциональность клиента может быть расширена кодом, приходящим с сервера. Сейчас такое можно встретить повсеместно: JavaScript используется для «оживления» страниц и исполнения каких-то сценариев на стороне клиента. Но принципы формулировались в 2000 году — тогда исполняемый код с сервера возвращали не так часто. Потому и выделили это в отдельный принцип.


   ****SOAP***
   
   или Simple Object Access Protocol – это простой протокол доступа к объектам, в котором не только вызов процедур, но и передача БД происходит в формате XML.

   Базовые элементы (теги) SOAP:
   - Envelope. Обязательный корневой элемент. Непосредственно он определяет сообщения и пространство времен;
   - Header. Он же заголовок. Не является обязательным элементом, но содержит необходимые атрибуты для обработки сообщения (информация об идентификаторе, маршрутизации или безопасности);
   - Body. Обязательный элемент, в котором содержится основная информация из сообщения;
   - Fault. Необязательный, но полезный элемент. В нем содержится информация об ошибках, которые возникают в процессе обработки сообщений.

   ****GraphQL****
   
   GraphQL был создан для того, чтобы преодолеть ограничения REST-архитектуры. Он подходит для приложений, в которых очень много данных и они хранятся в разных базах.
   В основе подхода GraphQL лежит простая идея — вместо того, чтобы создавать конечные точки для каждого объекта, достаточно создать один «умный» эндпойнт, который будет работать со сложными запросами и возвращать клиентам кумулятивные данные в том объеме, в котором клиенты их запрашивают
   
   - Строгая типизация — оценить правильность запроса можно до его выполнения.
   - Универсальность — можно использовать с любым фреймворком, языком программирования. Источник данных также не имеет значения.
   - Простое масштабирование — позволяет добавлять новые типы и поля, не трогая существующие запросы и не создавая несколько версий одного и того же API.

## 16. Как использовать паттерны программирования?
   - На практике паттерны используются программистами для того, чтобы решить какую-нибудь проблему, устранить определенную «боль» разработчика.

## 17. Что такое Acceptance Testing и зачем его используют?
   - UAT нужен для того, чтобы: понять, как ведет себя продукт в реальных условиях, соответствует ли результат задумке; выявить, были ли добавлены все возможные функции; проверить, есть ли ошибки, которые будут мешать пользователю

## 18. Что такое модульные и интеграционные тесты, API-тесты?
   - Интеграционное тестирование - это тестирование взаимодействия нескольких классов, выполняющих вместе какую-то работу
   - Модульное тестирование (Unit Testing) – это тип тестирования программного обеспечения, при котором тестируются отдельные модули или компоненты программного обеспечения. Его цель заключается в том, чтобы проверить, что каждая единица программного кода работает должным образом
   - API-тесты - тесты мониторинга API: Проверяют реализацию на различные ошибки, сбои внутренних обработчиков и другие неотъемлемые проблемы в кодовой базе API. Эти тесты гарантируют отсутствие дыр, которые могут привести к проблемам с безопасностью приложения

## 19. Как писать unit-тесты?
   - ???
## 20. Какие есть best practices в написании автотестов?
   **Признаки хороших тестов**
   
   - Атомарность - Каждый тест проверяет только один логический фрагмент кода.Если не придерживаться этого правила, тесты будет сложно обновлять и дорабатывать.Тестирование сложного сценария (например, подписки на новости) должно быть разделено на несколько частей; каждая часть должна тестироваться отдельно.
   - Независимость - Работа теста не должна зависеть от результатов работы других тестов или ждать ввода данных от пользователя. Тест должен использовать специально для него подготовленные данные — и никакие другие.
   - Вариативность - Тестируйте все варианты состояний (statements) и немножко больше. Проверяйте, что сущность работает ожидаемо на корректных данных и адекватно — при некорректных.
   - Неизбыточность - Тесты не должны перекрывать друг друга: не пишите одинаковые тесты несколько раз.
   - Читабельные имена - Название теста, как и название переменной — очень важно. В короткое слово нужно уместить как можно больше смысла. Название теста вы увидите в отчёте, оно будет светиться в редакторе кода. По названию теста вы должны получить представление о том, что же он проверяет и что в нём происходит. 

## 21. Какие базовые команды системы контроля версий?
   ```
   git add .
   git commit -m 'my creative description'
   git push
   ```
   - Более подробный список команд для новичка [тут](https://habr.com/ru/company/ruvds/blog/599929/)

## 22. Как использовать Git?
   - установите Git на вашу ОС
   - настройте имя пользователя и пароль
   ```
   git config --global user.name "My Name"
   git config --global user.email myEmail@example.com
   ```

## 23. В чем разница между хешированием и шифрованием?
   - Хеширование — это преобразование входных данных в уникальную последовательность символов, из которой невозможно получить исходное сообщение. Самый яркий пример использования — для проверки целостности. Если изменить в исходном файле или тексте хоть один бит, в результате получим новую уникальную последовательность.
   - Шифрова́ние — обратимое преобразование информации в целях сокрытия от неавторизованных лиц с предоставлением в это же время авторизованным пользователям доступа к ней __Смысл шифрования — сделать исходное сообщение нечитаемым для любого, кто не владеет ключом.__

## 24. Python - интерпретируемый язык или компилируемый?
   - Интерпретируемый

## 25. Какие есть меняющиеся и постоянные типы данных?
   - Неизменяемые(immutable):
      * Numbers (числа)
      * Strings (строки)
      * Tuples (кортежи)
      * Boolean (логический тип данных)
   - Изменяемые(mutable):
      * Lists (списки)
      * Dictionaries (словари)
      * Sets (множества)

## 26. Что такое область видимости переменных?
   - концепция, определяющая доступность переменных

## 27. Что такое introspection?
   - способность объекта во время выполнения получить тип, доступные атрибуты и методы, а также другую информацию, необходимую для выполнения дополнительных операций с объектом.
      > Самые популярные: dir(), type(), isinstance(), id(), hasattr()

## 28. Разница между is и ==?
   - Разница заключается в том, что is проверяет идентичность (объектов), а == проверяет равенство (значения)

## 29. Разница между __init __ () и __new __ ()?
   - new вызывается перед созданием обьекта класса, init вызывется __сразу__ после создания обьекта класса

## 30. В чем разница между потоками и процессами?
   - потоки выполняются в одном и том же пространстве памяти, а у процессов отдельная память

## 31. Какие есть виды импорта?
   - есть 4 __вида__ импортов:
      ```
      import <пакет>
      import <модуль>
      from <пакет> import <модуль или подпакет или объект>
      from <модуль> import <объект>
      ```
   - так же импорты делятся на:
      * Абсолютные - включает полный путь к вашему скрипту, начиная с корневой папки программы. Вы должны разделять каждую папку точкой
         ```
         from package1.firstmodule import firstmodule import package1.secondmodule.myfunction
         ```
      * Относительные - вы только указываете, где находятся ваши ресурсы относительно текущего файла кода. Относительный импорт использует точечную нотацию. Одиночные точки представляют каталог текущего скрипта. Две точки представляют родительскую папку.

## 32. Что такое класс, итератор, генератор?
   - Класс - модель для создания обьектов
   - Итератор - объект, которые позволяет проходить через все элементы коллекции, независимо от ее конкретной реализации.
   - Генератор - это объект, который сразу при создании не вычисляет значения всех своих элементов. Он хранит в памяти только последний вычисленный элемент, правило перехода к следующему и условие, при котором выполнение прерывается. Вычисление следующего значения происходит лишь при выполнении метода **next()**
      ```
      >>> a = (i**2 for i in range(1,5))
      >>> a
      <generator object <genexpr> at 0x0000023A7524D6D0>
      >>> next(a)
      1
      >>> next(a)
      4
      >>> next(a)
      9
      >>> next(a)
      ```

## 33. Что такое метакласс, переменная цикла?
   - Метакласс - обьект особого рода, который нельзя динамически создать, является отправной точкой для создания обычных классов и их обьектов
      > Метаклассы — это более глубокая магия, о которой 99% пользователей не должны беспокоиться. Если вы задаетесь вопросом, нужны ли они вам – значит, нет, вы в них не нуждаетесь (люди, которые действительно нуждаются в метаклассах, точно знают, что они им нужны, и не нуждаются в объяснении зачем)
      > © Тим Питерс

   - Переменная, хранящая текущий номер итерации, она же - счётчик итераций цикла или просто счётчик цикла.

## 34. В чем разница между итераторами и генераторами?
   - итератор — это механизм поэлементного обхода данных, а генератор позволяет отложено создавать результат при итерации

## 35. В чем разница между staticmethod и classmethod?
   - @classmethod используется в суперклассе для определения того, как метод должен вести себя, когда он вызывается разными дочерними классами. В то время как @staticmethod используется, когда мы хотим вернуть одно и то же, независимо от вызываемого дочернего класса.

## 36. Как работают декораторы, контекстные менеджеры?
   - Декоратор — это функция, которая позволяет обернуть другую функцию для расширения её функциональности без непосредственного изменения её кода.
   - Контекстные менеджеры - позволяют задать поведение при работе с конструкцией with: при входе и выходе из блока. Контекстные менеджеры обычно используются для захвата и освобождения ресурсов

## 37. Как работают dict comprehension, list comprehension и set comprehension?
   
   **list comprehension**
   - В общем случае, list comprehension это выражение, которое преобразует итерируемый объект в список. То есть, последовательность элементов преобразуется и добавляется в новый список
      ```
      new_list = [int(x) for x in items]
      ```
   - В list comprehensions можно использовать выражение if
      ```
      only_digits = [int(item) for item in items if item.isdigit()]
      ```
   **Dict comprehensions**
   - Генераторы словарей аналогичны генераторам списков
      ```
      d = {num: num**2 for num in range(1, 11)}
      ```
   - Как и list comprehensions, dict comprehensions можно делать вложенными
   **Set comprehensions**
   - Генераторы множеств в целом аналогичны генераторам списков
      ```
      unique_vlans = {int(vlan) for vlan in vlans}
      ```

## 38. Можно ли использовать несколько декораторов для одной функции?
   - Можно

## 39. Можно ли создать декоратор из класса?
   - Можно. Так как в Python классы создаются динамически по время интерпретации исходного кода, то можно влиять на этот процесс, например, путем декорирования. Аналогично декораторам функций, декоратор класса призван модифицировать поведение и содержание класса, не изменяя его исходный код. Похоже на наследование, но есть отличия:
      * Декоратор класса имеет более глубокие возможности по влиянию на класс, он может удалять, добавлять, менять, переименовывать атрибуты и методы класса. Он может возвращать совершенно другой класс.
      * Старый класс «затирается» и не может быть использован, как базовый класс при полиморфизме
      * Декорировать можно любой класс одним и тем же универсальный декоратором, а при наследовании – мы ограничены иерархией классов и должны считаться с интерфейсами базовых классов.
      * Презираются все принципы и ограничения ООП (из-за пунктов 1-3).

## 40. Какие есть основные популярные пакеты (requests, pytest, etc)?
   - NumPy – одна из лучших библиотек машинного обучения в Python
   - Keras — упрощение экспериментирования с глубокими нейронными сетями за счет высокоуровневой абстракции
   - Pandas – библиотека машинного обучения на Python, предоставляющая структуры данных высокого уровня и большой набор инструментов для анализа данных.
   - Pillow — основная библиотека изображений для быстрого доступа к данным, хранящимся в разных пиксельных формах. Поддерживает большой список форматов файлов и дает широкие возможности для обработки изображений разного качества.
   - Requests — HTTP-библиотека Python, выпущенная под лицензией Apache License 2.0. Главная задача библиотеки «Запросов» — упрощение отправки запросов, по сравнению со встроенными библиотеками urllib/urllib2.
   - Numba - библиотека Python дает пользователю возможность компилировать код сразу после его выполнения (компилятор «точно-в-срок» / Just-in-Time). Таким образом достигается скорость кода C, не отказываясь от простоты Python. Предназначен для кода, использующего массивы NumPy, функции и циклы.
   - Pytest - подходит и для модульного (тестирование отдельных компонентов ПО), и для функционального тестирования (тестирование способности кода удовлетворять бизнес-требованиям).

## 41. Что такое lambda-функции?
   - В Python лямбда-выражение позволяет создавать анонимные функции - функции, которые не привязаны к имени.
      ```
      In [3]: sum_arg = lambda a, b: a + b
      In [4]: sum_arg(1, 2)
      Out[4]: 3
      ```
## 42. Что означает *args, **kwargs и как они используются?
   - \*args — это сокращение от arguments (аргументы), а \*\*kwargs — это сокращение от keyword arguments (именованные аргументы). Каждый из них используется для распаковки соответствующих им типов аргументов, определенных вызовами функции, согласно списку аргументов переменной длины

## 43. Что такое exceptions, <try-except>?
   - Исключения в программировании (exceptions) — это механизм, который позволяет программе обрабатывать нетипичную ситуацию и при этом не прекращать работу. Благодаря этому механизму разработчик может описать в коде реакцию программы на такие ситуации. Конструкция try-except выглядит как:
   ```
   try(попытаться):
      поделить число А на число В
   except(исключение):
      число В не может быть == 0, введите корректное число
   ```

## 44. Что такое PEP (Python Enhancement Proposal), какие из них знаете (PEP 8, PEP 484)?
   -  PEP 8 - руководство по написанию кода на Python, описывает соглашение о том, как писать код для языка python, включая стандартную библиотеку, входящую в состав python

## 45. Напишите hello-world сервис, используя один из фреймворков.
   - ???

## 46. Какие есть типы данных и какая разница между list и tuple, зачем они?
   - список — изменяемый тип данных, а кортеж нет. В этом различии кроется суть кортежей: они защищают данные от непреднамеренных изменений. Вторая причина, по которой используют кортежи, это экономия места. Они занимают меньше объема в памяти, чем списки

## 47. Как использовать встроенные коллекции (list, set, dictionary)?
   - Конвертация одного типа коллекции в другой
      ```
      my_tuple = ('a', 'b', 'a')
      my_list = list(my_tuple)
      my_set = set(my_tuple)		        # теряем индексы и дубликаты элементов!
      my_frozenset = frozenset(my_tuple)      # теряем индексы и дубликаты элементов!
      print(my_list, my_set, my_frozenset)    # ['a', 'b', 'a'] {'a', 'b'} frozenset({'a', 'b'})
      ```

## 48. В чем заключается сложность доступа к элементам dict?
   - В dict хранятся хэши от ключей. Каждый раз, когда мы ищем в dict значение по ключу, мы сначала вычисляем его хэш, а потом выполняем бинарный поиск. Таким образом, сложность составляет O(lg(N))

## 49. Что знаете из модуля collections, какими еще built-in модулями пользовались?
   - collections.defaultdict ничем не отличается от обычного словаря за исключением того, что по умолчанию всегда вызывается функция, возвращающая значение
   - collections.OrderedDict - ещё один похожий на словарь объект, но он помнит порядок, в котором ему были даны ключи. Методы:
      * popitem(last=True) - удаляет последний элемент если last=True, и первый, если last=False.
      * move_to_end(key, last=True) - добавляет ключ в конец если last=True, и в начало, если last=False.
   - collections.namedtuple позволяет создать тип данных, ведущий себя как кортеж, с тем дополнением, что каждому элементу присваивается имя, по которому можно в дальнейшем получать доступ
   - collections.Counter - вид словаря, который позволяет нам считать количество неизменяемых объектов (в большинстве случаев, строк)
   - collections.deque(iterable, \[maxlen\]) - создаёт очередь из итерируемого объекта с максимальной длиной maxlen. Очереди очень похожи на списки, за исключением того, что добавлять и удалять элементы можно либо справа, либо слева

## 50. Что такое шаблонизатор и как в нем выполнять базовые операции (объединять участки шаблона, выводить дату, выводить данные с серверной стороны)?
   - программное обеспечение, позволяющее использовать шаблоны для генерации конечных документов с помощью декларативного языка разметки. Основная цель использования шаблонизаторов — это отделение формы документа и данных от полученного в результате документа.

## 51. Как Python работает с HTTP-сервером?
   - через эндпоинты???

## 52. Что происходит, когда создается виртуальная среда?
   - создается каталог venv с указанной версией Python
   - устанавливаются зависимости

## 53. Какие есть базовые [методы работы](https://proglib.io/p/kak-podruzhit-python-i-bazy-dannyh-sql-podrobnoe-rukovodstvo-2020-02-27) с SQL базой данных в Python?
   - для востребованных баз типа [MySQL](database_mysql_example.py) и [PostgreSQL](database_postgresql_example.py) существуют специальные библиотеки. Более развернутые примеры по ссылкам в репозитории

## 54. Что такое SQL-транзакция?
   - это группа последовательных операций с базой данных, которая представляет собой логическую единицу работы с данными. Иными словами, транзакции позволяют нам контролировать процессы сохранения и изменения в базах данных.

## 55. Как сделать выборку из SQL-базы с простой агрегацией?
   - доработать, инфа [тут](https://www.politerm.com/zuludoc/sql_aggreg.html)

## 56. Как отправлять запросы в SQL-базу данных без ORM?
   - Чистый SQL запрос строится из:
      ```
      SELECT ('столбцы или * для выбора всех столбцов; обязательно')
      FROM ('таблица; обязательно')
      WHERE ('условие/фильтрация, например, city = 'Moscow'; необязательно')
      GROUP BY ('столбец, по которому хотим сгруппировать данные; необязательно')
      HAVING ('условие/фильтрация на уровне сгруппированных данных; необязательно')
      ORDER BY ('столбец, по которому хотим отсортировать вывод; необязательно')
      ```

## 57. Что такое Big-O notation?
   - Big O – это мера эффективности «в худшем случае», верхняя граница того, сколько времени потребуется для выполнения задачи, или сколько памяти для этого необходимо. В О-нотации не учитываются константы и коэффициенты.

## 58. Какие есть базовые алгоритмы сортировки?
   - [Bubble sort](bubble.py)(ниже)
   - Сортировка перемешиванием (шейкерная сортировка) - Шейкерная сортировка отличается от пузырьковой тем, что она двунаправленная: алгоритм перемещается не строго слева направо, а сначала слева направо, затем справа налево.
   - Быстрая сортировка - Этот алгоритм состоит из трёх шагов. Сначала из массива нужно выбрать один элемент — его обычно называют опорным. Затем другие элементы в массиве перераспределяют так, чтобы элементы меньше опорного оказались до него, а большие или равные — после. А дальше рекурсивно применяют первые два шага к подмассивам справа и слева от опорного значения.
   - Сортировка слиянием - пригодится для таких структур данных, в которых доступ к элементам осуществляется последовательно (например, для потоков). Здесь массив разбивается на две примерно равные части и каждая из них сортируется по отдельности. Затем два отсортированных подмассива сливаются в один.
   - [Бинарный поиск](binary.py) - классический алгоритм поиска элемента в отсортированном массиве (векторе), использующий дробление массива на половины

## 59. Что такое Bubble Sort и как это работает?
   - простой [алгоритм](bubble.py) сортировки, при каждом проходе алгоритма по внутреннему циклу, очередной наибольший элемент массива ставится на своё место в конце массива рядом с предыдущим «наибольшим элементом», а наименьший элемент перемещается на одну позицию к началу массива («всплывает» до нужной позиции как пузырёк в воде, отсюда и название алгоритма)

## 60. Что такое линейная сложность сортировки?
   - **O(log n)** - Линейная временная сложность алгоритма означает, что время его работы находится в прямой зависимости от размера входящих данных. Если количество элементов наборе данных растет, пропорционально растет и время работы

## 61. Что такое многопоточность?
   - Способность процесса выполнять несколько потоков параллельно называется многопоточностью

## 62. Что такое архитектура веб сервисов?
   - Архитектура веб-приложения описывает расположение всех компонентов веб-приложения, а также акцентирует взаимодействие между различными компонентами приложения, системами промежуточного программного обеспечения сторонних производителей, веб-службами и базами данных

## 63. Что такое абстрактная фабрика, как ее реализовать и зачем ее применяют?
   - [Абстрактная фабрика](https://refactoring.guru/ru/design-patterns/abstract-factory/python/example) — это порождающий паттерн проектирования, который решает проблему создания целых семейств связанных продуктов, без указания конкретных классов продуктов

## 64. Что такое цикломатическая сложность?
   - мера количества независимых путей кода в вашем приложении. Путь - это последовательность операторов, которой интерпретатор может следовать, чтобы добраться до конца приложения

## 65. Async Python: как работает, зачем, что под капотом?

## 66. Что такое модель памяти Python?
   - При запуске Python-программы создается новый процесс, в рамках которого операционная система выделяет пул ресурсов, включая виртуальное адресное пространство. В эту память загружается интерпретатор Python вместе со всеми необходимыми ему для работы данными, включая код вашей программы. Оставшаяся свободная виртуальная память может использоваться для хранения информации об объектах Python’а. Для управления этой памятью в CPython используется специальный механизм, который называется аллокатор. Он используется каждый раз, когда вам нужно создать новый объект.

## 67. Что такое SQLAlchemy и какие есть альтернативы?

## 68. Принципы работы и механизм Garbage collection, reference counting?
   - GC итерирует каждый объект из выбранных поколений и временно удаляет все ссылки от отдельно взятого объекта (все ссылки на которые этот объект ссылается). После полного прохода, все объекты, у которых счетчик ссылок меньше двух считаются недоступными из питона и могут быть удалены.

## 69. Что такое \__slots\__?
 - __slots__ - магический метод, который позволяет задать ограниченный набор атрибутов, которыми будет обладать экземпляр класса.
   
## 70. Что такое type annotation?
   - Type Hinting — это механизм, который позволяет явно указывать типы параметров. Интерпретатор использует их и применяет исключение в тех ситуациях, когда тип не соответствует ожидаемому

## 71. Для чего используют нижние подчеркивания в именах классов?
   - Двойное нижнее подчеркивание в начале используется для искажения имени. Такое подчеркивание указывает интерпретатору Python переписать имя атрибута подклассов, чтобы избежать конфликтов имен.

## 72. Разница между SQL и NoSQL?
   - В отличие от SQL, в NoSQL вся информация хранится без четко установленной структуры и явных связей между всеми данными. Здесь хранятся не какие-то структурированные и четкие таблицы, а любые сведения, которые могут быть представлены в виде текстового документа, аудиофайла или публикации в интернете

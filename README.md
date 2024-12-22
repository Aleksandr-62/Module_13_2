__Modul_13_2__
Цель: написать простейшего телеграм-бота, используя асинхронные функции.

Подготовка:

Выполните все действия представленные в предыдущих видео модуля, создав и подготовив Telegram-бот для дальнейших заданий.
Нужные версии для 13 и 14 модулей и вашего виртуального окружения находятся здесь. Если не помните, как установить необходимые библиотеки, 
обратитесь к материалам 11 модуля.

Актуальная версия Python для дальнейшей работы - 3.9.13.

Задача "Бот поддержки (Начало)":

К коду из подготовительного видео напишите две асинхронные функции:

start(message) - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.' . Запускается только когда написана команда '/start' 
в чате с ботом. (используйте соответствующий декоратор)

all_massages(message) - печатает строку в консоли 'Введите команду /start, чтобы начать общение.'. Запускается при любом обращении не 
описанном ранее. (используйте соответствующий декоратор)

Запустите ваш Telegram-бот и проверьте его на работоспособность.

Пример результата выполнения программы:

Ввод в чат Telegram:

Хэй!

/start

Вывод в консоль:

Updates were skipped successfully.

Введите команду /start, чтобы начать общение.

Привет! Я бот помогающий твоему здоровью.

Примечания:

Для ответа на сообщение используйте декоратор message_handler.

При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!



__Modul_13_3__

Задача "Он мне ответил!":

Измените функции start и all_messages так, чтобы вместо вывода в консоль строки отправлялись в чате телеграм.
Запустите ваш Telegram-бот и проверьте его на работоспособность.


__Module_13_4__
Необходимо сделать цепочку обработки состояний для нахождения нормы калорий для человека.
Группа состояний:
1. Импортируйте классы State и StatesGroup из aiogram.dispatcher.filters.state.
2. Создайте класс UserState наследованный от StatesGroup.
3. Внутри этого класса опишите 3 объекта класса State: age, growth, weight (возраст, рост, вес).
Эта группа(класс) будет использоваться в цепочке вызовов message_handler'ов. Напишите следующие функции для обработки состояний:
*Функцию set_age(message):*

| Оберните её в message_handler, который реагирует на текстовое сообщение 'Calories'.
| Эта функция должна выводить в Telegram-бот сообщение 'Введите свой возраст:'.
| После ожидать ввода возраста в атрибут UserState.age при помощи метода set.
*Функцию set_growth(message, state):*

|Оберните её в message_handler, который реагирует на переданное состояние UserState.age.
|Эта функция должна обновлять данные в состоянии age на message.text (написанное пользователем сообщение). Используйте метод update_data.
|Далее должна выводить в Telegram-бот сообщение 'Введите свой рост:'.
|После ожидать ввода роста в атрибут UserState.growth при помощи метода set.
*Функцию set_weight(message, state):*

|Оберните её в message_handler, который реагирует на переданное состояние UserState.growth.
|Эта функция должна обновлять данные в состоянии growth на message.text (написанное пользователем сообщение). Используйте метод update_data.
|Далее должна выводить в Telegram-бот сообщение 'Введите свой вес:'.
|После ожидать ввода роста в атрибут UserState.weight при помощи метода set.
*Функцию send_calories(message, state):*

|Оберните её в message_handler, который реагирует на переданное состояние UserState.weight.
|Эта функция должна обновлять данные в состоянии weight на message.text (написанное пользователем сообщение). Используйте метод update_data.
|Далее в функции запомните в переменную data все ранее введённые состояния при помощи state.get_data().
Используйте упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы калорий (для женщин или мужчин - на ваше усмотрение). Данные для 
формулы берите из ранее объявленной переменной data по ключам age, growth и weight соответственно.

Результат вычисления по формуле отправьте ответом пользователю в Telegram-бот.

Финишируйте машину состояний методом finish().

!В течение написания этих функций помните, что они асинхронны и все функции и методы должны запускаться с оператором await.


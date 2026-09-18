# 🚀 Cassandra Framework
## Техническое задание: Страница Access Restoration (Восстановление доступа)

### 📌 Обозначения

-   **`ElementName`** *(type)* — UI-элемент с указанием типа
-   *"Text content"* — отображаемый текст на интерфейсе
-   `code` — технические термины, классы, методы
`'/access-restoration.html'` *(url)* — адрес страницы (URL) для проверки навигации
-   ⚠️ *(decorative)* — декоративный элемент, не подлежит автоматизированному тестированию

## 1. 🎯 Назначение
Единая форма восстановления учётных данных для операторов, потерявших доступ к системе. Обеспечивает идентификацию пользователя по позывному и шифру восстановления, а также выдачу нового ключа доступа с сохранением в эмулируемую базу данных восстановленных пользователей.

## 2. 🖥️ Элементы интерфейса

### 2.1 Основные элементы формы

- **`Brand Title`** *(text)* — Заголовок "CASSANDRA". "CASSAN" белый, "DRA" с голубым свечением. Скрывается при успешном восстановлении.

- **`Page Subtitle`** *(text)* — Статичная подпись: "Access Restoration Protocol". Скрывается при успешном восстановлении.

- **`Restoration Error Block`** *(alert)* — Блок ошибки. Текст по умолчанию: "⚠️ Restoration data invalid". Динамически меняется. По умолчанию скрыт.

- **`Callsign`** *(input)* — Поле ввода позывного. Placeholder: `Enter callsign`. Мин. длина: 4, макс. длина: 100. Допустимые символы: латиница и цифры (фильтрация через JS).

- **`Recovery Cipher`** *(input)* — Поле ввода шифра восстановления. Placeholder: `Enter recovery cipher`. Мин. длина: 4, макс. длина: 100. Допустимые символы: только буквы латиницы (фильтрация через JS).

- **`New Access Code`** *(input)* — Поле нового ключа. Placeholder: `Enter new access code`. Тип: password. Длина: 4–30 символов. Допустимые символы: латиница, цифры, _.

- **`Confirm Access Code`** *(input)* — Поле подтверждения. Placeholder: `Confirm access code`. Тип: password. Те же ограничения.

- **`Toggle Password Buttons`** *(button)* — Две кнопки переключения видимости (иконка глаза) для полей нового ключа и подтверждения.

- **`Restore Button`** *(button)* — Главная кнопка. Label: `RESTORE ACCESS`. Состояние: неактивна (disabled), пока все 4 поля не заполнены валидными данными. При нажатии запускает анимацию пульсации (добавляется класс processing), текст меняется на `VERIFYING PROTOCOLS...`, а кнопка блокируется (disabled) на 2 секунды.

### 2.2 Экран успеха (Success Screen)

Отображается вместо формы при успешном восстановлении.

- **`Success Message`** *(text)* — Текст: `✅ Access Protocol Verified` (зелёный цвет).

- **`Success Logo`** *(text)* — Заголовок: `ACCESS RESTORED`.

- **`Restoration Summary`** *(container)* — Блок сводки с 5 строками:

    - **`Sum Callsign`** (text) — Позывной.

    - **`Sum Role`** (text) — Роль с иконкой.

    - **`Sum Function`** (text) — Функция.

    - **`Sum ID`** (text) — Идентификатор оператора.

    - **`Sum New Code`** (text) — Новый ключ доступа (голубой цвет, класс highlight).

### 2.3 Декоративные элементы ⚠️

> Примечание: Элементы данного раздела являются частью визуального оформления страницы и не подлежат автоматизированному тестированию. Они не имеют data-wm-id и не включаются в CAS-сценарии.

- **`Satellite`** *(decorative/svg)* — Летающий спутник. По умолчанию красный (состояние тревоги). При успешном восстановлении плавно меняет цвет на белый с синими радиоволнами (состояние signal-restored).

-   **`Stars Background`** *(decorative/css)* — Анимированный фон со звёздами и Млечным Путём.

### 2.4 Служебные элементы

-   **`Telemetry`** *(text)* — Строка состояния системы в футере. Отображается моноширинным шрифтом с мигающим курсором (█). Во время 2-секундной анимации обработки текст телеметрии не меняется, оставаясь в состоянии "по умолчанию" до получения финального результата. 

    - Состояние по умолчанию: "> SYSTEM READY. AWAITING RESTORATION PROTOCOL" (синий цвет, #4da6ff).

    - Состояние при ошибке: "> SECURITY PROTOCOL FAILED. RESTORATION ABORTED" (или специфичная ошибка, красный, #e74c3c).

    - Состояние при успешном восстановлении: "> RESTORATION COMPLETE. NEW CREDENTIALS ISSUED." (зелёный, #2ecc71).

-   **`Footer Brand`** *(text)* — Копирайт в футере. Текст: *"Evknopia © 2026"*.

### 2.5 Угловая навигация (Corner Navigation)

- **`Corner Nav Container`** *(layout)* — Контейнер вторичной навигации, зафиксированный в нижней части экрана по углам (`position: fixed`, `bottom: 3vmin`). Не перекрывает основную форму и не мешает взаимодействию с ней.

- **`Log In Corner Button`** *(button/link)* — Круглая навигационная кнопка в **левом нижнем углу**. 
  - Иконка: 🔭 
  - Label: `Log In`
  - Поведение: При клике происходит мгновенный переход на `login.html`. Активна на Шагах 1 и 2.

- **`Sign Up Corner Button`** *(button/link)* — Круглая навигационная кнопка в **правом нижнем углу**. 
  - Иконка: 📡 
  - Label: `Sign Up`
  - Поведение: При клике происходит мгновенный переход на `Signup.html`. Активна на Шагах 1 и 2.


## 3. ✅ Правила валидации

- **`Callsign:`** - Мин. 4 символа. Только латиница и цифры.

- **`Recovery Cipher:`** - Мин. 4 символа, макс. 100. Только буквы латиницы.

- **`New Access Code:`** - 4–30 символов. Латиница, цифры, _.

- **`Confirm Access Code:`** - Должен точно совпадать с New Access Code.

- **`Кнопка RESTORE ACCESS`** - неактивна, пока все 4 условия не выполнены.

## 4. ⚙️ Логика работы

> ⚠️ **Важно: Контекст проекта**
> Данный проект является учебным и **не имеет серверной части (бэкенда)**. 
> Все процессы аутентификации, хранения пользователей и передачи данных эмулируются исключительно на стороне клиента (Frontend) с использованием `sessionStorage` (для хранения активной сессии currentUser), `localStorage` (для эмуляции базы данных `restoredUsers`) и локальных конфигурационных файлов (data.js).
> В реальном продакшн-проекте эти функции выполнялись бы на сервере.

- Валидные данные для восстановления `KNOPA`:

    - `Recovery Cipher`: Должно быть строго `AERO`

    - `New Access Code`: Должен быть строго `AERO_99` 

    - `Confirm Access Code`: Должен быть строго `AERO_99` 

- Проверки при отправке формы (после 2 секунд имитации задержки):

    - Проверка позывного (`Fail-Fast`): Если введённый позывной не равен строго KNOPA, процесс немедленно прерывается.

    - Проверка совпадения кодов: `New Access Code` и `Confirm Access Code` должны быть идентичны.

    - Проверка нового кода: `New Access Code` должен быть строго равен `AERO_99`.

    - Проверка шифра: Введённый `Recovery Cipher` должен совпадать с `recoveryCipher` пользователя `KNOPA` из `MOCK_USERS` (значение AERO).

    - Проверка статуса восстановления: Пользователь `KNOPA` не должен уже присутствовать в `localStorage.restoredUsers`.

    - Защита от двойного клика: Повторное нажатие на кнопку игнорируется, пока идет процесс обработки.

- При успехе:

    - Данные пользователя из `MOCK_USERS` копируются в `localStorage` по ключу `restoredUsers`, при этом поле `accessCode` перезаписывается на новый `AERO_99`.

    - Форма скрывается, отображается Экран успеха.

    - Спутник меняет цвет на белый/синий (добавляется класс `signal-restored к body`).

    - Автоматического редиректа нет. Пользователь переходит на `login.html` через угловую кнопку.

    - При обновлении страницы (F5) или уходе: Форма всегда сбрасывается к начальному состоянию. `sessionStorage` не используется для сохранения состояния восстановления.

- Сообщения об ошибках 

    - Если позывной не `KNOPA`: `⚠️ Restoration unavailable. Only operator 'KNOPA' is eligible for access recovery`.

    - Если пользователь уже восстановлен: `⚠️ Operator 'KNOPA' has already been restored. Please use your new credentials to log in`. (Телеметрия: `> SECURITY PROTOCOL FAILED. OPERATOR ALREADY RESTORED.`)

    - При любой другой ошибке (неверный шифр, несовпадение кодов, неверный новый код): `⚠️ Security protocol failed. Invalid credentials provided.` (Единая фраза для предотвращения перебора данных. Телеметрия: `> SECURITY PROTOCOL FAILED. RESTORATION ABORTED`).

>Примечание: Оператор KNOPA является предсуществующим в системе (определён в глобальном объекте MOCK_USERS) и восстанавливается исключительно через процедуру Access Restoration. На текущем этапе разработки восстановление доступа разрешено только для этого оператора.

>New Access Code: AERO_99 (жестко заданное значение). Попытки восстановления других позывных (например, AURORA, ORION, NOVA) будут немедленно отклонены с ошибкой ⚠️ Restoration unavailable. Only operator KNOPA is eligible for access recovery., так как процедура восстановления на текущем этапе разрешена исключительно для этого оператора.

## 5. 🤖 Спецификация данных

- **Структура объекта в restoredUsers:**

  - {
    - "KNOPA": {
    -  "callsign": "KNOPA",
    -  "role": "PILOT",
    -  "roleIcon": "✈️",
    -  "function": "Flight Operations",
    -  "accessLevel": "1",
    -  "accessCode": "AERO_99",
    -  "id": "769-1A"
  - }

- **Хранение:**

- **`localStorage`** → ключ `restoredUsers` (JSON-объект). Сохраняется до ручной очистки.

- **`sessionStorage`** → не используется на этой странице.

## 6. 🧪 Сценарии автоматизированного тестирования (CAS)

> **CAS (Cassandra Automation Scenarios)** — внутренний стандарт именования сценариев автоматизированного тестирования в рамках Cassandra Framework. Формат: `CAS-{NN}: {Краткое описание}`.

- **Структура реализации**

    - Тесты разделены на логические файлы в директории tests/testaccess_restoration/. Ниже приведено описание каждого сценария с привязкой к файлу реализации.

### test_errors.py — Негативные сценарии и ошибки

- **CAS-01: Неверный новый ключ доступа.**

  - Переход: Открыть страницу Access Restoration.
Ввести валидные значения в поля Callsign (KNOPA) и Recovery Cipher (AERO). Ввести неверное значение WRONG_CODE в поле New Access Code. Ввести такое же неверное значение WRONG_CODE в поле Confirm Access Code. Нажать кнопку RESTORE ACCESS.

  - Ожидаемый результат: Через 2 секунды появляется блок ошибки с текстом ⚠️ Security protocol failed. Invalid credentials provided.. Телеметрия красная: > SECURITY PROTOCOL FAILED. RESTORATION ABORTED. Кнопка возвращается в активное состояние.

- **CAS-02: Несовпадение новых ключей доступа**.

  - Переход: Открыть страницу Access Restoration.

  - Действие: Ввести валидные значения в поля Callsign (KNOPA) и Recovery Cipher (AERO). Ввести валидное значение AERO_99 в поле New Access Code. Ввести неверное значение WRONG в поле Confirm Access Code. Нажать кнопку RESTORE ACCESS.

  - Ожидаемый результат: Через 2 секунды появляется блок ошибки с текстом ⚠️ Security protocol failed. Invalid credentials provided.. Телеметрия красная: > SECURITY PROTOCOL FAILED. RESTORATION ABORTED. Кнопка возвращается в активное состояние.
  
- **CAS-03: Неверный шифр восстановления.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Ввести валидное значение KNOPA в поле Callsign. Ввести неверное значение WRONG в поле Recovery Cipher. Ввести валидное значение AERO_99 в поле New Access Code. Ввести валидное значение AERO_99 в поле Confirm Access Code. Нажать кнопку RESTORE ACCESS.

  - Ожидаемый результат: Через 2 секунды появляется блок ошибки с текстом ⚠️ Security protocol failed. Invalid credentials provided.. Телеметрия красная: > SECURITY PROTOCOL FAILED. RESTORATION ABORTED. Кнопка возвращается в активное состояние.

- **CAS-04: Попытка повторного восстановления доступа.**

  - Предусловие: Успешно восстановить доступ пользователю KNOPA через страницу Access Restoration (ввести KNOPA, AERO, AERO_99, AERO_99 и нажать RESTORE ACCESS). Дождаться появления экрана успеха.

  - Переход: Обновить страницу (F5).

  - Действие: Ввести валидное значение KNOPA в поле Callsign. Ввести валидное значение AERO в поле Recovery Cipher. Ввести валидное значение AERO_99 в поле New Access Code. Ввести валидное значение AERO_99 в поле Confirm Access Code. Нажать кнопку RESTORE ACCESS.

  - Ожидаемый результат: Через 2 секунды появляется блок ошибки с текстом ⚠️ Operator 'KNOPA' has already been restored. Please use your new credentials to log in.. Телеметрия красная: > SECURITY PROTOCOL FAILED. OPERATOR ALREADY RESTORED.. Кнопка возвращается в активное состояние.

- **CAS-05: Попытка восстановления для неизвестного оператора.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Ввести неверное значение UNKNOWN в поле Callsign. Ввести валидное значение AERO в поле Recovery Cipher. Ввести валидное значение AERO_99 в поле New Access Code. Ввести валидное значение AERO_99 в поле Confirm Access Code. Нажать кнопку RESTORE ACCESS.

  - Ожидаемый результат: Через 2 секунды появляется блок ошибки с текстом ⚠️ Restoration unavailable. Only operator KNOPA is eligible for access recovery.. Телеметрия красная: > SECURITY PROTOCOL FAILED. RESTORATION ABORTED. Кнопка возвращается в активное состояние.

### test_success.py — Позитивные сценарии

- **CAS-01: Успешное восстановление доступа для KNOPA.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Ввести валидное значение KNOPA в поле Callsign. Ввести валидное значение AERO в поле Recovery Cipher. Ввести валидное значение AERO_99 в поле New Access Code. Ввести валидное значение AERO_99 в поле Confirm Access Code. Нажать кнопку RESTORE ACCESS.

  - Ожидаемый результат: Через 2 секунды форма скрывается, отображается экран успеха. Появляется сообщение ✅ Access Protocol Verified (зелёный цвет). Отображается заголовок ACCESS RESTORED. В блоке сводки отображаются данные: Callsign: KNOPA, Role: ✈️ Pilot, Function: Flight Operations, Operator ID: 769-1A, New Access Code: AERO_99. Телеметрия зелёная: > RESTORATION COMPLETE. NEW CREDENTIALS ISSUED. Спутник плавно меняет цвет на белый с синими радиоволнами (добавляется класс signal-restored к body).

- **CAS-02: Проверка данных в localStorage после успеха.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Ввести валидное значение KNOPA в поле Callsign. Ввести валидное значение AERO в поле Recovery Cipher. Ввести валидное значение AERO_99 в поле New Access Code. Ввести валидное значение AERO_99 в поле Confirm Access Code. Нажать кнопку RESTORE ACCESS.

  - Ожидаемый результат: Через 2 секунды отображается экран успеха. В localStorage по ключу restoredUsers сохраняется объект с ключом KNOPA, содержащий обновлённые данные пользователя с accessCode: "AERO_99".

### test_ui_navigation.py — UI-состояния, тултипы, hover-эффекты, навигация


- **CAS-01: Состояние страницы при загрузке.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Оценить начальное состояние элементов без ввода данных.

  - Ожидаемый результат: Видим подзаголовок Access Restoration Protocol. Поля Callsign, Recovery Cipher, New Access Code, Confirm Access Code пустые. Кнопка RESTORE ACCESS неактивна (disabled). Телеметрия синего цвета с текстом > SYSTEM READY. AWAITING RESTORATION PROTOCOL.


- **CAS-02: Реактивное состояние кнопки RESTORE ACCESS.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Ввести менее 4 символов в поле Callsign. Ввести менее 4 символов в поле Recovery Cipher. Ввести менее 4 символов в поля New Access Code и Confirm Access Code. Проверить состояние кнопки. Очистить все поля. Ввести 4 символа в поле Callsign. Ввести 4 символа в поле Recovery Cipher. Ввести 4 или более символов в поля New Access Code и Confirm Access Code.

  - Ожидаемый результат: Кнопка RESTORE ACCESS остаётся неактивной (disabled), пока длина хотя бы одного из полей менее 4 символов. После ввода 4 или более символов во все 4 поля кнопка RESTORE ACCESS становится активной (enabled).

- **CAS-03: Переключение видимости полей пароля.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Ввести текст AERO_99 в поле New Access Code. Ввести текст AERO_99 в поле Confirm Access Code. Нажать кнопки Toggle Password (иконка глаза) для обоих полей. Нажать кнопки ещё раз.

  - Ожидаемый результат: После первого нажатия тип обоих полей меняется с password на text, символы становятся видимыми. После повторного нажатия тип полей возвращается с text на password, символы скрываются.

- **CAS-04: Успешная навигация на страницу Log In.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Нажать на угловую кнопку Log In (иконка 🔭).

  - Ожидаемый результат: Происходит мгновенная навигация, URL страницы меняется на login.html.

- **CAS-05: Успешная навигация на страницу Sign Up.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Нажать на угловую кнопку Sign Up (иконка 📡).

  - Ожидаемый результат: Происходит мгновенная навигация, URL страницы меняется на signup.html.

### test_validation.py - Проверка состояний, валидация UI, анимации

- **CAS-01: Позывной короче минимальной длины.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Действие: Ввести 3 символа в поле Callsign. Ввести валидное значение AERO в поле Recovery Cipher. Ввести валидные значения AERO_99 в поля New Access Code и Confirm Access Code.

  - Ожидаемый результат: Кнопка RESTORE ACCESS остаётся неактивной (disabled), так как длина поля Callsign менее 4 символов.

- **CAS-02: Шифр восстановления короче минимальной длины.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Ввести валидное значение KNOPA в поле Callsign. Ввести 3 символа в поле Recovery Cipher. Ввести валидные значения AERO_99 в поля New Access Code и Confirm Access Code.

  - Ожидаемый результат: Кнопка RESTORE ACCESS остаётся неактивной (disabled), так как длина поля Recovery Cipher менее 4 символов.

- **CAS-03: Новый код доступа короче минимальной длины.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Действие: Ввести валидное значение KNOPA в поле Callsign. Ввести валидное значение AERO в поле Recovery Cipher. Ввести 3 символа в поле New Access Code. Ввести валидное значение AERO_99 в поле Confirm Access Code.

  - Ожидаемый результат: Кнопка RESTORE ACCESS остаётся неактивной (disabled), так как длина поля New Access Code менее 4 символов.

- **CAS-04: Код подтверждения короче минимальной длины.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Действие: Ввести валидное значение KNOPA в поле Callsign. Ввести валидное значение AERO в поле Recovery Cipher. Ввести валидное значение AERO_99 в поле New Access Code. Ввести 3 символа в поле Confirm Access Code.

  - Ожидаемый результат: Кнопка RESTORE ACCESS остаётся неактивной (disabled), так как длина поля Confirm Access Code менее 4 символов.

- **CAS-05: Превышение максимальной длины Callsign >100.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Попытаться ввести более 100 символов в поле Callsign.

  - Ожидаемый результат: Поле Callsign принимает не более 100 символов (избыточные символы игнорируются или обрезаются).

- **CAS-06: Превышение максимальной длины Recovery Cipher >100.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Попытаться ввести более 100 символов в поле Recovery Cipher.

  - Ожидаемый результат: Поле Recovery Cipher принимает не более 100 символов (избыточные символы игнорируются или обрезаются).

- **CAS-07: Превышение максимальной длины New Access Code >30.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Попытаться ввести более 30 символов в поле New Access Code.

  - Ожидаемый результат: Поле New Access Code принимает не более 30 символов (избыточные символы игнорируются или обрезаются).

- **CAS-08: Превышение максимальной длины Confirm Access Code >30.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Попытаться ввести более 30 символов в поле Confirm Access Code.

  - Ожидаемый результат: Поле Confirm Access Code принимает не более 30 символов (избыточные символы игнорируются или обрезаются).

- **CAS-09: SQL-инъекция в поле Callsign.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Ввести SQL-инъекцию ' OR '1'='1 в поле Callsign. Ввести валидное значение AERO в поле Recovery Cipher. Ввести валидное значение AERO_99 в поле New Access Code. Ввести валидное значение AERO_99 в поле Confirm Access Code. Нажать кнопку RESTORE ACCESS.

  - Ожидаемый результат: Фронтенд автоматически отсекает спецсимволы — в поле Callsign остаётся только OR11. Через 2 секунды появляется сообщение об ошибке: ⚠️ Restoration unavailable. Only operator KNOPA is eligible for access recovery. Отображается красная телеметрия: > SECURITY PROTOCOL FAILED. RESTORATION ABORTED. Данные не сохраняются в localStorage.

- **CAS-10: SQL-инъекция в поле Recovery Cipher.**

  - Переход: Открыть страницу Access Restoration.

  - Действие: Ввести валидное значение KNOPA в поле Callsign. Ввести SQL-инъекцию ' OR '1'='1 в поле Recovery Cipher. Ввести валидное значение AERO_99 в поле New Access Code. Ввести валидное значение AERO_99 в поле Confirm Access Code.

  - Ожидаемый результат: Фронтенд автоматически отсекает спецсимволы и цифры — в поле Recovery Cipher остаётся только OR (2 символа). Кнопка RESTORE ACCESS остаётся неактивной (disabled), так как длина поля Recovery Cipher менее 4 символов. Отправка формы не происходит. Данные не сохраняются в localStorage.
 
## 7. 🎨 Визуальные требования

  - **Цветовая схема:** Тёмно-синий космический фон #050816, голубые акценты #4da6ff, зелёные акценты успеха #2ecc71, красные акценты ошибки #e74c3c, белый текст #ffffff.

-   **Анимации:** 

  - Мигающий курсор в строке `Telemetry` (1s, step-end).

  - Пульсация радиоволн спутника (2s цикл, 3 волны с задержкой 0.6s). По умолчанию волны и тело спутника красные (состояние тревоги). При успешном восстановлении плавно меняют цвет на белый/синий (состояние signal-restored, transition 0.8s).

  - Пульсация кнопки `RESTORE ACCESS` при обработке (1.5s, pulse-btn). Эффект применяется только во время отправки формы. В состоянии disabled кнопка выглядит тусклой и не имеет эффектов при наведении.

  - Плавное появление блоков ошибок (fadeInUp, 0.3s).

- **Карточка формы:** Полупрозрачный фон с backdrop-filter: blur(12px), голубая рамка со свечением (box-shadow).

- **Угловые кнопки навигации:** Круглые кнопки с неоновым свечением. При наведении (:hover) увеличиваются (scale(1.15)), усиливается свечение. Всегда активны и кликабельны, включая экран успеха.

- **Адаптивность:** `Desktop-only` (1024px+). Мобильная версия не предусмотрена.

## 8. 🏷️ Спецификация data-wm-id (Ironclad Locators)

> Все интерактивные элементы должны иметь уникальный атрибут `data-wm-id` для надёжной автоматизации.

| Элемент | data-wm-id |
|---------|-----------|
| Подзаголовок страницы |`restoration-page-subtitle`|
| Блок ошибки восстановления |`restoration-error-message`|
| Поле Callsign |`restoration-callsign-input`|
| Поле Recovery Cipher |`restoration-recovery-cipher-input`|
| Поле New Access Code |`restoration-new-access-code-input`|
| Кнопка-глазик для New Access Code |`restoration-toggle-new-access-code`|
| Поле Confirm Access Code |`restoration-confirm-access-code-input`|
| Кнопка-глазик для Confirm Access Code |`restoration-toggle-confirm-access-code`|
| Кнопка RESTORE ACCESS|`restoration-restore-btn`|
| Сообщение об успехе |`restoration-success-message`|
| Логотип успеха |`restoration-success-logo`|
| Контейнер сводки |`restoration-summary`|
| Сводка: Callsign |`sum-callsign`|
| Сводка: Role |`sum-role`|
| Сводка: Function |`sum-function`|
| Сводка: Operator ID |`sum-id`|
| Сводка: New Access Code |`sum-new-code`|
| Строка телеметрии|`system-telemetry`|
| Угловая кнопка входа (Log In) |`btn-login`|
| Угловая кнопка регистрации (Sign Up) |`btn-signup`|


## 9. 🌐 URL и маршрутизация

Так как проект является учебным и статическим (без серверной части), для локальной разработки и деплоя на GitHub Pages используются следующие адреса:

- **Local Base URL (Локальная разработка и тесты):** 
  - Главная: `file:///.../cassandra/index.html`
  - Авторизация: `file:///.../cassandra/login.html`
  - Регистрация: `file:///.../cassandra/signup.html`
  - Восстановление: `file:///.../cassandra/access-restoration.html`

- **GitHub Pages URL (Публичный деплой):** 
  - Главная: `https://<username>.github.io/cassandra/index.html`
  - Авторизация: `https://<username>.github.io/cassandra/login.html`
  - Регистрация: `https://<username>.github.io/cassandra/signup.html`
  - Восстановление: `https://<username>.github.io/cassandra/access-restoration.html`


> **Примечание для автоматизации:** 
> В конфигурационных файлах фреймворка (например, `config.py`) определяется базовый URL (`BASE_URL`) в зависимости от окружения. 
> Переход на конкретную страницу осуществляется путем добавления имени файла (например, `login.html`) к `BASE_URL`. Это гарантирует корректную работу тестов как на локальной машине, так и в CI/CD.

*Версия ТЗ: 1.0 (Production Ready) | Обновлено: 11.09.2026 | Автор: Evknopia*

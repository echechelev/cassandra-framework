# 🚀 Cassandra Framework
## Техническое задание: Страница Sign Up (Регистрация)

### 📌 Обозначения

-   **`ElementName`** *(type)* — UI-элемент с указанием типа
-   *"Text content"* — отображаемый текст на интерфейсе
-   `code` — технические термины, классы, методы
-   `'/signup.html'` *(url)* — адрес страницы (URL) для проверки навигации
-   ⚠️ *(decorative)* — декоративный элемент, не подлежит автоматизированному тестированию

## 1. 🎯 Назначение
Многошаговая форма регистрации нового оператора в системе оценки колонизации. Обеспечивает сбор идентификационных данных (Шаг 1), настройку учётных данных безопасности (Шаг 2) и финальное подтверждение с сохранением оператора в эмулируемую базу данных (Шаг 3).

## 2. 🖥️ Элементы интерфейса

### 2.1 Основные элементы формы

-   **`Brand Title`** *(text)*  — Заголовок "CASSANDRA" со стилизованным суффиксом. *"CASSAN"* отображается белым шрифтом, *"DRA"* имеет голубое свечение. На Шаге 3 меняется на "ACTIVATION COMPLETE".

- **`Page Subtitle`** *(text)* — Динамическая подпись под заголовком. Меняется в зависимости от текущего шага:

    - Шаг 1: "Phase 1: Operator Identity"

    - Шаг 2: "Phase 2: Security Setup"

    - Шаг 3: "Welcome aboard, new Operator." (зелёный цвет)

### 2.2 Шаг 1: Operator Identity (step-1)

- **`Full Name`** *(input)* — Поле ввода полного имени оператора. Placeholder: `Enter full name`. Максимальная длина: 100 символов. Допустимые символы: латиница, цифры и пробелы (фильтрация через JS).

- **`Callsign`** *(input, readonly)* — Поле позывного. Placeholder: `AUTO-GENERATED`. Поле заблокировано для ручного ввода (readonly). Значение автоматически генерируется из `Full Name` приведением к верхнему регистру.

- **`Role`** *(select)* — Выпадающий список выбора роли. Варианты:

    - **`COMMANDER`** - Access Level 1

    - **`PILOT`** - Access Level 1

    - **`SPECIALIST`** - Access Level 2

    - **`ENGINEER`** - Access Level 3

    - *По умолчанию:* `Select role` (disabled).

- **`Function`** *(input, readonly)* — Поле функции. Placeholder: `Auto-assigned based on role`. Поле заблокировано (readonly). Значение автоматически подставляется при выборе роли:

    - **`COMMANDER`** → "Command & Strategy"

    - **`PILOT`** → "Flight Operations"

    - **`SPECIALIST`** → "Comms & Diagnostics"

    - **`ENGINEER`** → "Systems Engineering"

- **`Proceed Button`** *(button)* — Кнопка перехода к Шагу 2. Label: `PROCEED`. Состояние: неактивна (disabled), пока `Full Name` < 4 символов, `Role` не выбран или `Function` пуст. При нажатии меняет текст на `VERIFYING IDENTITY...` и запускает анимацию пульсации.

- **`Signup Error Block`** *(alert)* — Блок ошибки Шага 1. Отображается над формой при невалидных данных. Текст по умолчанию: *"⚠️ Registration data invalid"*. Динамически меняется в зависимости от типа ошибки. По умолчанию скрыт.

### 2.3 Шаг 2: Security Setup (step-2)

- **`Access Code`** *(input)* — Поле ввода ключа доступа. Placeholder: `Enter access code`. Тип: password. Минимальная длина: 4, максимальная: 30. Допустимые символы: латиница, цифры, _.

- **`Confirm Access Code`** *(input)* — Поле подтверждения ключа. Placeholder: `Confirm access code`. Тип: password. Те же ограничения, что у `Access Code`.

- **`Recovery Cipher`** *(input)* — Поле контрольного слова восстановления. Placeholder: `Enter recovery word`. Минимальная длина: 4, максимальная: 30. Допустимые символы: только буквы латиницы.

- **`Toggle Password Buttons`** *(button)* — Две кнопки переключения видимости (по одной на каждое поле пароля). Содержат SVG-иконку глаза. Переключают тип поля между `password` и `text`.

- **`Complete Button`** *(button)* — Главная кнопка завершения регистрации. Label: `COMPLETE REGISTRATION`. Расположена выше кнопки Back. Состояние: неактивна (disabled), пока все три поля не заполнены валидными данными. При нажатии меняет текст на `ACTIVATING ACCOUNT`... и запускает анимацию пульсации на 2 секунды (аналогично кнопке `PROCEED` на Шаге 1).

- **`Back Button`** *(button)* — Второстепенная кнопка возврата к Шагу 1. Label: `← BACK TO OPERATOR DATA`. Расположена **ниже** кнопки Complete. Очищает все поля Шага 2 при нажатии, но сохраняет данные Шага 1.

- **`Security Error Block`** *(alert)* — Блок ошибки Шага 2. Текст по умолчанию: `⚠️ Security protocol failed. Invalid credentials provided.`. По умолчанию скрыт.

### 2.4 Шаг 3: Confirmation Protocol (step-3)

- **`Operator Summary`** *(container)* — Блок сводки данных зарегистрированного оператора. Содержит 6 строк:

    - **`Sum Callsign`** (text) — Позывной.

    - **`Sum Name`** (text) — Полное имя.

    - **`Sum Role`** (text) — Роль с иконкой (например, "⚙️ Engineer").

    - **`Sum Function`** (text) — Функция.

    - **`Sum Level`** (text) — Уровень доступа (голубой цвет, класс highlight).

    - **`Sum ID`** (text) — Идентификатор оператора.

### 2.5 Декоративные элементы ⚠️

> Примечание: Элементы данного раздела являются частью визуального оформления страницы и не подлежат автоматизированному тестированию. Они не имеют data-wm-id и не включаются в CAS-сценарии.

-   **`Satellite`** *(decorative/svg)* — Летающий спутник с зелёными акцентами (в отличие от синего на логине).
Перемещается по экрану с отталкиванием от границ окна браузера (эффект "DVD-логотипа"). От спутника каждые ~2 секунды расходятся три радиоволны (анимированные SVG-круги), символизирующие поиск сигнала. Проходит за формой авторизации (z-index ниже карточки), создавая эффект "мёртвой зоны".

-   **`Stars Background`** *(decorative/css)* — Анимированный фон со звёздами и Млечным Путём.

### 2.6 Служебные элементы

-   **`Telemetry`** *(text)* — Строка состояния системы в футере. Отображается моноширинным шрифтом с мигающим курсором (█). Во время 2-секундной анимации обработки (мерцания кнопки) текст телеметрии не меняется, оставаясь в состоянии "по умолчанию" до получения финального результата.

    - Состояние по умолчанию (Шаг 1): `> SYSTEM READY. AWAITING OPERATOR REGISTRATION` (синий цвет, #4da6ff).

    - Состояние по умолчанию (Шаг 2): `> SYSTEM READY. AWAITING SECURITY REGISTRATION` (синий цвет, #4da6ff).

    - Состояние при ошибке для Шага 1: `> SYSTEM LOCKED. {SPECIFIC_REASON}`, например, `RESERVED CALLSIGN, INVALID ROLE` (красный, #e74c3c).

    - Состояние при ошибке для Шага 2: "> SYSTEM LOCKED. INVALID CREDENTIALS." (красный, #e74c3c).

    - Состояние после успешной регистрации: "> REGISTRATION COMPLETE. OPERATOR ACCOUNT ACTIVATED." (зелёный, #2ecc71).

-   **`Footer Brand`** *(text)* — Копирайт в футере. Текст: *"Evknopia © 2026"*.

### 2.7 Угловая навигация (Corner Navigation)

- **`Corner Nav Container`** *(layout)* — Контейнер вторичной навигации, зафиксированный в нижней части экрана по углам (`position: fixed`, `bottom: 3vmin`). Не перекрывает основную форму и не мешает взаимодействию с ней.

- **`Log In Corner Button`** *(button/link)* — Круглая навигационная кнопка в **левом нижнем углу**. 
  - Иконка: 🔭 
  - Label: `Log In`
  - Поведение: При клике происходит мгновенный переход на `login.html`. Активна на Шагах 1, 2 и 3.

- **`Restore Corner Button`** *(button/link)* — Круглая навигационная кнопка в **правом нижнем углу**. 
  - Иконка: 🔑 
  - Label: `Restore`
  - Поведение: При клике происходит мгновенный переход на `access-restoration.html`. Активна на Шагах 1, 2 и 3 .

## 3. ✅ Правила валидации

- **Шаг 1: Operator Identity:**

    - **`Full Name`**: - Минимальная длина — 4 символа, максимальная — 100. Допустимы только латиница,цифры и пробелы.

    - **`Callsign:`** - Генерируется автоматически из `Full Name` (верхний регистр). Ручной ввод невозможен (readonly).

    - **`Role:`** - Должна быть выбрана одна из четырех ролей. Пустое значение (placeholder) невалидно.
    `Function`: Заполняется автоматически при выборе роли. Пустое значение невалидно.

    - **`Кнопка PROCEED`** неактивна, пока все три условия не выполнены.

- **Шаг 2: Security Setup**

    - **`Access Code:`** - Минимальная длина — 4, максимальная — 30. Допустимы латиница, цифры, _.

    - **`Confirm Access Code:`** - Те же ограничения. Должен точно совпадать с `Access Code`.

    - **`Recovery Cipher:`** - Минимальная длина — 4, максимальная — 30. Допустимы только буквы латиницы (цифры и спецсимволы фильтруются).

    - **Кнопка COMPLETE REGISTRATION`** - неактивна, пока все три поля не заполнены валидными данными.

## 4. ⚙️ Логика работы

> ⚠️ **Важно: Контекст проекта**
> Данный проект является учебным и **не имеет серверной части (бэкенда)**. 
> Все процессы аутентификации, хранения пользователей и передачи данных эмулируются исключительно на стороне клиента (Frontend) с использованием `sessionStorage` (для хранения активной сессии currentUser), `localStorage` (для эмуляции базы данных `registeredUsers`) и локальных конфигурационных файлов (data.js).
> В реальном продакшн-проекте эти функции выполнялись бы на сервере.

- Многошаговый визард: Страница содержит 3 шага (step-1, step-2, step-3). Видимость управляется CSS-классом hidden. При обновлении страницы (F5) или уходе с неё форма сбрасывается к Шагу 1 для обеспечения чистоты тестового окружения.

- **Автогенерация данных (Шаг 1):**

    - Ввод в `Full Name` фильтруется (только латиница и цифры) и автоматически копируется в `Callsign` в верхнем регистре.

    - Выбор `Role` автоматически заполняет `Function`, `Access Level` и `Role Icon`.

- **Проверки при отправке Шага 1 (после 2 секунд имитации задержки):**

    - Зарезервированные позывные: `AURORA` и `ORION` заблокированы (системные аккаунты).

    - Дубликаты: Позывной проверяется на наличие в `localStorage` (registeredUsers).

- **Нарративное ограничение:** 

    - На текущем этапе разработки разрешена регистрация только оператора с позывным `NOVA` и ролью `ENGINEER`.

    - Любые другие комбинации отклоняются с соответствующим сообщением об ошибке.

- **Проверки при отправке Шага 2:**

    - Защита от двойного клика: Повторное нажатие на кнопку игнорируется, пока идет процесс активации.

    - `Access Code` и `Confirm Access Code` должны совпадать.

    - Нарративное ограничение: `Access Code` должен быть строго `QUASAR_5`.

    - Нарративное ограничение: `Recovery Cipher` должен быть строго `COMETA`.

- **Завершение регистрации (Шаг 3, кнопка Launch):**

    - При успешной валидации Шага 2 данные оператора мгновенно сохраняются в `localStorage` (ключ `registeredUsers`).

    - Интерфейс переключается на Шаг 3 (`Confirmation Protocol`), отображая сводку данных.

    - Автоматического редиректа нет. Пользователь может самостоятельно перейти на страницу входа (`login.html`) или восстановления (`access-restoration.html`) через угловую навигацию.

> Примечание: Оператор 'KNOPA' является предсуществующим и восстанавливается исключительно через процедуру Access Restoration. Попытки регистрации данного позывного должны обрабатываться как блокировка зарезервированного имени (аналогично AURORA/ORION).

## 5. 🤖 Спецификация данных

- **Структура объекта оператора (сохраняется в registeredUsers и currentUser):**

    - {
        - "fullName": "Nova",
        - "callsign": "NOVA",
        - "role": "ENGINEER",
        - "roleIcon": "⚙️",
        - "function": "Systems Engineering",
        - "accessLevel": "3",
        - "accessCode": "QUASAR_5",
        - "recoveryCipher": "COMETA",
        - "id": "512-3A"
    - }

- **⚠️ Важное примечание об операторе KNOPA:**

    - Оператор KNOPA является предсуществующим и восстанавливается исключительно через процедуру `Access Restoration`.

    - Любые попытки зарегистрировать данный позывной на этой странице должны обрабатываться как блокировка зарезервированного имени (аналогично `AURORA` и `ORION`). Он не может быть создан через форму `Sign Up`.

- **Хранение:**

    - **`localStorage`** → ключ `registeredUsers` (JSON-объект, где ключ — позывной, значение — данные оператора). Сохраняется навсегда до ручной очистки.

    - **`sessionStorage`** → ключ `currentUser` (JSON-строка с данными текущего оператора). Используется страницей логина и дашбордом.

    - Примечание: Страница регистрации (`signup.html`) не использует `sessionStorage` для хранения черновиков или шагов визарда. При любом обновлении страницы (F5) или уходе с неё форма гарантированно сбрасывается к Шагу 1, обеспечивая детерминированность для автотестов.

## 6. 🧪 Сценарии автоматизированного тестирования (CAS)

> **CAS (Cassandra Automation Scenarios)** — внутренний стандарт именования сценариев автоматизированного тестирования в рамках Cassandra Framework. Формат: `CAS-{NN}: {Краткое описание}`.

- **Структура реализации**

    - Тесты разделены на логические файлы в директории tests/test_signup/. Ниже приведено описание каждого сценария с привязкой к файлу реализации.

### test_errors.py — Негативные сценарии и ошибки

- **CAS-01: Блокировка зарезервированного позывного AURORA.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Aurora в Full Name, выбрать SPECIALIST в Role. Нажать PROCEED.

    - Ожидаемый результат: Через 2 секунды появляется блок ошибки Signup Error Block с текстом ⚠️ Callsign 'AURORA' is already in use. This identity is reserved.. Телеметрия красная с текстом > SYSTEM LOCKED. CALLSIGN 'AURORA' ALREADY EXISTS.

- **CAS-02: Блокировка зарезервированного позывного ORION.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Orion в Full Name, выбрать COMMANDER в Role. Нажать PROCEED.

    - Ожидаемый результат: Через 2 секунды появляется блок ошибки Signup Error Block с текстом ⚠️ Callsign 'ORION' is already in use. This identity is reserved.. Телеметрия красная с текстом > SYSTEM LOCKED. CALLSIGN 'ORION' ALREADY EXISTS.

- **CAS-03: Блокировка неверной роли для NOVA.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, выбрать COMMANDER в Role. Нажать PROCEED.
    
    - Ожидаемый результат: Через 2 секунды появляется блок ошибки Signup Error Block с текстом ⚠️ Registration suspended. Pre-allocated identity requires ENGINEER role.. Телеметрия красная с текстом > SYSTEM LOCKED. ROLE MISMATCH DETECTED.

- **CAS-04: Блокировка зарезервированного позывного KNOPA.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Knopa в Full Name, выбрать COMMANDER в Role. Нажать PROCEED.
    
    - Ожидаемый результат: Через 2 секунды появляется блок ошибки Signup Error Block с текстом ⚠️ Callsign 'KNOPA' is already in use. This identity is reserved.. Телеметрия красная с текстом > SYSTEM LOCKED. CALLSIGN 'KNOPA' ALREADY EXISTS.

- **CAS-05: Блокировка неизвестного позывного.**

    - Переход: Открыть страницу Sign Up.    

    - Действие: Ввести Ivan в Full Name, выбрать ENGINEER в Role. Нажать PROCEED.

    - Ожидаемый результат: Через 2 секунды появляется блок ошибки Signup Error Block с текстом ⚠️ Registration suspended. System capacity reached. Only pending activation: NOVA.. Телеметрия красная с текстом > SYSTEM LOCKED. PLEASE ENTER CORRECT FULL NAME AND CALLSIGN.

- **CAS-06: Невалидный Access Code (несовпадение).**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, выбрать ENGINEER в Role. Нажать PROCEED. Ввести QUASAR_5 в Access Code, WRONG_CODE в Confirm Access Code, COMETA в Recovery Cipher. Нажать COMPLETE REGISTRATION.

    - Ожидаемый результат: Через 2 секунды появляется блок ошибки Security Error Block с текстом ⚠️ Security protocol failed. Invalid credentials provided.. Телеметрия красная с текстом > SYSTEM LOCKED. INVALID CREDENTIALS.. Кнопка COMPLETE REGISTRATION возвращается в активное состояние.

- **CAS-07: Невалидный Access Code (неверное значение).**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, выбрать ENGINEER в Role. Нажать PROCEED. Ввести WRONG_CODE в Access Code, WRONG_CODE в Confirm Access Code, COMETA в Recovery Cipher. Нажать COMPLETE REGISTRATION.

    - Ожидаемый результат: Через 2 секунды появляется блок ошибки Security Error Block с текстом ⚠️ Security protocol failed. Invalid credentials provided.. Телеметрия красная с текстом > SYSTEM LOCKED. INVALID CREDENTIALS.. Кнопка COMPLETE REGISTRATION возвращается в активное состояние.

- **CAS-08: Невалидный Recovery Cipher.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, выбрать ENGINEER в Role. Нажать PROCEED. Ввести QUASAR_5 в Access Code, QUASAR_5 в Confirm Access Code, WRONG в Recovery Cipher. Нажать COMPLETE REGISTRATION.

    - Ожидаемый результат: Через 2 секунды появляется блок ошибки Security Error Block с текстом ⚠️ Security protocol failed. Invalid credentials provided.. Телеметрия красная с текстом > SYSTEM LOCKED. INVALID CREDENTIALS.. Кнопка COMPLETE REGISTRATION возвращается в активное состояние.

### test_success.py — Позитивные сценарии

- **CAS-01: Успешный переход на Шаг 2.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, выбрать ENGINEER в Role. Нажать PROCEED.

    - Ожидаемый результат: Через 2 секунды Шаг 1 скрывается, Шаг 2 становится видимым. Подзаголовок меняется на Phase 2: Security Setup. Телеметрия синяя с текстом > SYSTEM READY. AWAITING SECURITY REGISTRATION.

- **CAS-02: Успешная регистрация NOVA.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, выбрать ENGINEER в Role. Нажать PROCEED. Ввести QUASAR_5 в Access Code, QUASAR_5 в Confirm Access Code, COMETA в Recovery Cipher. Нажать COMPLETE REGISTRATION.

    - Ожидаемый результат: Шаг 3 становится видимым. Подзаголовок зелёного цвета: Welcome aboard, new Operator.. Телеметрия зелёная с текстом > REGISTRATION COMPLETE. OPERATOR ACCOUNT ACTIVATED.. Сводка отображает: Callsign: NOVA, Full Name: Nova, Role: ⚙️ Engineer, Function: Systems Engineering, Access Level: 3, Operator ID: 512-3A.

- **CAS-03: Проверка данных в localStorage после регистрации.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, выбрать ENGINEER в Role. Нажать PROCEED. Ввести QUASAR_5 в Access Code, QUASAR_5 в Confirm Access Code, COMETA в Recovery Cipher. Нажать COMPLETE REGISTRATION.

    - Ожидаемый результат: В localStorage по ключу registeredUsers сохранён объект оператора NOVA со всеми данными (fullName, callsign, role, roleIcon, function, accessLevel, accessCode, recoveryCipher, id).

### test_ui_navigation.py — UI-состояния, тултипы, hover-эффекты, навигация

- **CAS-01: Состояние страницы при загрузке (Шаг 1).**

    - Переход: Открыть страницу Sign Up.

    - Действие: Оценить начальное состояние элементов без ввода данных.

    - Ожидаемый результат: Видим Шаг 1. Подзаголовок: Phase 1: Operator Identity. Поле Callsign пустое и readonly. Поле Function пустое и readonly. Кнопка PROCEED неактивна (disabled). Телеметрия синяя с текстом > SYSTEM READY. AWAITING OPERATOR REGISTRATION.

- **CAS-02: Состояние формы на Шаге 2.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, выбрать ENGINEER в Role. Нажать PROCEED.

    - Ожидаемый результат: Через 2 секунды Шаг 2 становится видимым. Поля Access Code, Confirm Access Code и Recovery Cipher пустые. Кнопка COMPLETE REGISTRATION неактивна (disabled).

- **CAS-03: Реактивное состояние кнопки PROCEED.**

    -   Переход: Открыть страницу Sign Up.

    -   Действие: Ввести менее 4 символов в Full Name, выбрать ENGINEER в Role. Проверить состояние кнопки. Очистить поле Full Name, ввести 4 символа.

    -   Ожидаемый результат: Кнопка PROCEED остаётся неактивна (disabled), пока длина Full Name < 4 символов. После ввода 4 символов кнопка PROCEED становится активной (enabled).

- **CAS-04: Реактивное состояние кнопки COMPLETE REGISTRATION.**

    -   Переход: Открыть страницу Sign Up.

    -   Действие: Ввести Nova в Full Name, выбрать ENGINEER в Role. Нажать PROCEED. Ввести менее 4 символов в поля Access Code, Confirm Access Code и Recovery Cipher. Проверить состояние кнопки. Ввести 4 и более символов в те же поля.

    -   Ожидаемый результат: Кнопка COMPLETE REGISTRATION остаётся неактивна (disabled), пока длина всех трёх полей < 4 символов. После ввода 4 и более символов в каждое поле кнопка COMPLETE REGISTRATION становится активной (enabled).


- **CAS-05: Кнопка BACK возвращает на Шаг 1.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, выбрать ENGINEER в Role. Нажать PROCEED. Нажать кнопку ← BACK TO OPERATOR DATA.

    - Ожидаемый результат: Шаг 2 скрывается, Шаг 1 становится видимым. Подзаголовок меняется на Phase 1: Operator Identity.

- **CAS-06: Переключение видимости полей пароля.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, выбрать ENGINEER в Role. Нажать PROCEED. Ввести текст в Access Code и Confirm Access Code. Нажать кнопки Toggle Password (иконка глаза) для обоих полей. Нажать кнопки ещё раз.

    - Ожидаемый результат: После первого нажатия тип обоих полей меняется с password на text, символы становятся видимыми. После повторного нажатия тип полей возвращается с text на password, символы скрываются.

- **CAS-07: Успешная навигация на страницу Log In.**

    - Переход: Открыть страницу Sign Up (Шаг 1).

    - Действие: Нажать на угловую кнопку с data-wm-id='btn-login'.

    - Ожидаемый результат: URL браузера изменяется на login.html. Страница успешно загружается.


- **CAS-08: Успешная навигация на страницу Access Restoration.**

    - Переход: Открыть страницу Sign Up (Шаг 1).

    - Действие: Нажать на угловую кнопку с data-wm-id='btn-restore'.

    - Ожидаемый результат: URL браузера изменяется на access-restoration.html. Страница успешно загружается.

### test_validation.py - Проверка состояний, валидация UI, анимации

- **CAS-01: Позывной короче минимальной длины.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести 3 символа в Full Name, выбрать ENGINEER в Role.

    - Ожидаемый результат: Кнопка PROCEED остаётся неактивна (disabled), так как минимальная длина Full Name — 4 символа.

- **CAS-02: Код доступа короче минимальной длины.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Заполнить Шаг 1 валидными данными и перейти на Шаг 2. Ввести 3 символа в Access Code, валидные данные в Confirm Access Code и Recovery Cipher.

    - Ожидаемый результат: Кнопка COMPLETE REGISTRATION остаётся неактивна (disabled), так как минимальная длина Access Code — 4 символа.

- **CAS-03: Подтверждение кода доступа короче минимальной длины.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Заполнить Шаг 1 валидными данными и перейти на Шаг 2. Ввести валидные данные в Access Code, 3 символа в Confirm Access Code, валидные данные в Recovery Cipher.

    - Ожидаемый результат: Кнопка COMPLETE REGISTRATION остаётся неактивна (disabled), так как минимальная длина Confirm Access Code — 4 символа.

- **CAS-04: Шифр доступа короче минимальной длины.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Заполнить Шаг 1 валидными данными и перейти на Шаг 2. Ввести валидные данные в Access Code, валидные данные в Confirm Access Code, 3 символа в Recovery Cipher.

    - Ожидаемый результат: Кнопка COMPLETE REGISTRATION остаётся неактивна (disabled), так как минимальная длина Recovery Cipher — 4 символа.

- **CAS-05: Пустой позывной при выбранной роли.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Оставить поле Full Name пустым, выбрать ENGINEER в Role.

    - Ожидаемый результат: Кнопка PROCEED остаётся неактивна (disabled), так как поле Full Name пустое (минимальная длина — 4 символа).

- **CAS-06: Пустая роль при заполненном позывном.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, оставить поле Role пустым (не выбирать значение).

    - Ожидаемый результат: Кнопка PROCEED остаётся неактивна (disabled), так как роль не выбрана.

- **CAS-07: Пустой код доступа при заполненных остальных полях.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Заполнить Шаг 1 валидными данными и перейти на Шаг 2. Оставить поле Access Code пустым, Ввести валидные данные в поля Confirm Access Code ввести и Recovery Cipher.

    - Ожидаемый результат: Кнопка COMPLETE REGISTRATION остаётся неактивна (disabled), так как поле Access Code пустое.

- **CAS-08: Пустое подтверждение кода при заполненных остальных полях.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Заполнить Шаг 1 валидными данными и перейти на Шаг 2. Ввести валидные данные в поля Access Code и Recovery Cipher, оставить поле Confirm Access Code пустым.

    - Ожидаемый результат: Кнопка COMPLETE REGISTRATION остаётся неактивна (disabled), так как поле Confirm Access Code пустое.
    
- **CAS-09: Пустой шифр при заполненных остальных полях.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Заполнить Шаг 1 валидными данными и перейти на Шаг 2. Ввести валидные данные в поля Access Code и Confirm Access Code, оставить поле Recovery Cipher пустым.

    - Ожидаемый результат: Кнопка COMPLETE REGISTRATION остаётся неактивна (disabled), так как поле Recovery Cipher пустое.

- **CAS-10: Проверка максимальной длины поля Full Name.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Попытаться ввести более 100 символов в поле Full Name.

    - Ожидаемый результат: Ввод блокируется на уровне UI (HTML атрибут maxlength), в поле остаётся не более 100 символов.

- **CAS-11: Проверка максимальной длины поля Access Code.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, выбрать ENGINEER в Role. Нажать PROCEED. Попытаться ввести более 30 символов в поле Access Code.

    - Ожидаемый результат: Ввод блокируется на уровне UI (HTML атрибут maxlength), в поле остаётся не более 30 символов.

- **CAS-12: Проверка максимальной длины поля Confirm Access Code.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, выбрать ENGINEER в Role. Нажать PROCEED. Попытаться ввести более 30 символов в поле Confirm Access Code.

    - Ожидаемый результат: Ввод блокируется на уровне UI (HTML атрибут maxlength), в поле остаётся не более 30 символов.

- **CAS-13: Проверка максимальной длины поля Recovery Cipher.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в Full Name, выбрать ENGINEER в Role. Нажать PROCEED. Попытаться ввести более 30 символов в поле Recovery Cipher.

    - Ожидаемый результат: Ввод блокируется на уровне UI (HTML атрибут maxlength), в поле остаётся не более 30 символов.

- **CAS-14: Санитизация ввода — попытка ввести спецсимволы в поле Recovery Cipher.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Действие: Ввести валидное значение NOVA в поле Callsign. Ввести строку со спецсимволами ' OR '1'='1' в поле Recovery Cipher. Ввести валидные значения QUASAR_5 в поля New Access Code и Confirm Access Code.

    - Ожидаемый результат: Фронтенд автоматически отсекает спецсимволы и цифры — в поле Recovery Cipher остаётся только OR (2 символа). Кнопка COMPLETE REGISTRATION остаётся неактивной (disabled), так как длина поля менее 4 символов. Отправка формы не происходит. Данные не сохраняются в localStorage.

- **CAS-15: Автогенерация Callsign из Full Name.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Ввести Nova в поле Full Name.

    - Ожидаемый результат: Поле Callsign автоматически заполняется значением NOVA (верхний регистр, синхронно с вводом имени).

- **CAS-16: Автозаполнение Function при выборе Role.**

    - Переход: Открыть страницу Sign Up.

    - Действие: Выбрать ENGINEER в выпадающем списке поля Role.

    - Ожидаемый результат: Поле Function автоматически заполняется значением Systems Engineering (синхронно с выбором роли, поле readonly).

## 7. 🎨 Визуальные требования

- **Цветовая схема:** Тёмно-синий космический фон #050816, голубые акценты #4da6ff, зелёные акценты #2ecc71 (спутник, кнопка Launch, успешная телеметрия), белый текст #ffffff.

- **Анимации:**

    - Пульсация кнопок `PROCEED` и `COMPLETE REGISTRATION` при обработке (длительность цикла анимации 1.5s, общее время состояния обработки 2s).

    - Мигающий курсор в строке `Telemetry` (1s, step-end).

    - Плавное появление блоков ошибок (fadeInUp, 0.3s).

    - Адаптивность: `Desktop-only` (1024px+). Мобильная версия не предусмотрена.

## 8. 🏷️ Спецификация data-wm-id (Ironclad Locators)

> Все интерактивные элементы должны иметь уникальный атрибут data-wm-id для надёжной автоматизации.

| Элемент | data-wm-id |
|---------|-----------|
| Поле Full Name | `signup-full-name-input`|
| Поле Callsign | `signup-callsign-input`|
| Выпадающий список Role | `signup-role-select`|
| Поле Function | `signup-function-input`|
| Кнопка PROCEED | `signup-proceed-btn`|
| Блок ошибки Шага 1 | `signup-error-message`|
| Поле Access Code | `signup-access-code-input`|
| Поле Confirm Access Code | `signup-confirm-code-input`|
| Поле Recovery Cipher | `signup-recovery-cipher-input`|
| Кнопка BACK | `signup-back-btn`|
| Кнопка COMPLETE | `signup-complete-btn`|
| Блок ошибки Шага 2 | `signup-security-error`|
| Сводка Callsign | `sum-callsign`|
| Сводка Full Name | `sum-name`|
| Сводка Role | `sum-role`|
| Сводка Function | `sum-function`|
| Сводка Access Level | `sum-level`|
| Сводка Operator ID | `sum-id`|
| Подзаголовок страницы | `signup-page-subtitle`|
| Логотип Шага 3 | `signup-activation-logo`|
| Кнопка глазик для Access Code  | `signup-toggle-access-code`|
| Кнопка глазик для Confirm Access Code  | `signup-toggle-confirm-code`|
| Угловая кнопка входа (Log in)| `btn-login`|
| Угловая кнопка восстановления (Restore)| `btn-restore`|

## 9. 🌐 URL и маршрутизация

Так как проект является учебным и статическим (без серверной части), для локальной разработки и деплоя на GitHub Pages используются следующие адреса:

- **Local Base URL (Локальная разработка и тесты):** 
  - Главная: `file:///.../cassandra/index.html`
  - Регистрация: `file:///.../cassandra/signup.html`

- **GitHub Pages URL (Публичный деплой):** 
  - Главная: `https://<username>.github.io/cassandra/`
  - Регистрация: `https://<username>.github.io/cassandra/signup.html`
  *(Остальные страницы формируются аналогично, с обязательным суффиксом `.html`)*



> Примечание для автоматизации:
> Тесты для страницы регистрации должны запускаться с чистым профилем браузера (без данных в localStorage и sessionStorage), чтобы избежать ложных срабатываний на дубликаты позывных.

*Версия ТЗ: 1.3 (Production Ready) | Обновлено: 08.09.2026 | Автор: Evknopia*
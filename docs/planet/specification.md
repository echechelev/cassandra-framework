# 🚀 Cassandra Framework
## Техническое задание: Страница Planet (Информация о планете)

### 📌 Обозначения

-   **`ElementName`** *(type)* — UI-элемент с указанием типа
-   *"Text content"* — отображаемый текст на интерфейсе
-   `code` — технические термины, классы, методы
- `'/galaxy-map.html'` *(url)* — адрес страницы (URL) для проверки навигации
-   ⚠️ *(decorative)* — декоративный элемент, не подлежит автоматизированному тестированию

## 1. 🎯 Назначение
Страница Planet — детализированное досье выбранной планеты. Отображает центральный визуал планеты, физические характеристики в левой панели, описание и статус исследования в правой панели, а также предоставляет навигацию для возврата на страницу звездной системы. Страница является конечным узлом детального изучения в иерархии навигации: Galaxy Map → Star System → Planet.

## 2. 🖥️ Элементы интерфейса

### 2.1 Основные элементы формы

- **`Main Planet Container`** (container) — Центральный визуальный элемент планеты. Динамически применяет CSS-класс .main-planet.{planet_id}-planet для отображения уникальной текстуры, цвета и теней.

- **`Planet Name`** (text) — Название планеты, отображаемое по центру под визуалом (например, "EARTH").

- **`Tech Panel`** (container) — Левая информационная панель. Отображает 8 физических метрик планеты (Mass, Radius, Surface Gravity, Mean Temperature, Atmospheric Pressure, Orbital Period, Rotation Period, Distance).

- **`Info Panel`** (container) — Правая информационная панель. Разделена на два блока:
Planetary Profile: Научное описание планеты.

- **`Exploration Status:`** История миссий и статус доступности (например, "ACTIVE OPERATIONS" или "BEYOND REACH").

- **`Star System Button`** (button) — Кнопка навигации (нижний левый угол). Иконка: ☄️. Текст: Star System. Ведет на star-system.html?star={star_key}. data-wm-id="nav-star-system-btn".

- **`Info Panel Role`** (container) — Информационная панель роли пользователя (верхний левый угол). Содержит иконку, название роли и тултип.

- **`Info Panel User`** (container) — Информационная панель данных пользователя (верхний правый угол). Содержит иконку, имя и тултип.

- **`System Telemetry`** (text) — Строка телеметрии в футере, отображающая статус загрузки данных.

- **`Cassandra Logo`** (container) — Декоративный логотип ИИ в правом нижнем углу (CASSAN + DRA). Не интерактивен.

### 2.2 Декоративные элементы ⚠️

> Примечание: Элементы данного раздела являются частью визуального оформления страницы и не подлежат автоматизированному тестированию. Они не имеют `data-wm-id` и не включаются в CAS-сценарии.

- **`Stars Background`** *(decorative/css)* — Анимированный фон со звёздами и Млечным Путём .stars, .milkyway.

- **`Milky Way Band`** *(decorative/css)* — Светящаяся полоса Млечного Пути .milkyway .band.

- **`Planet Visuals`** *(decorative/css)* — Уникальные CSS-градиенты и тени для каждой планеты (например, .main-planet.earth-planet, .main-planet.trappist-1e-planet).

- **`Copyright`** *(decorative/text)* — Текст копирайта Evknopia © 2026 в футере. data-wm-id="footer-copyright".

### 2.3 Служебные элементы

- **`Telemetry`** *(text)* — Строка состояния системы в футере. Формат: > CASSANDRA: {CALLSIGN}, {PLANET_NAME}. DOWNLOADING PLANETARY METRICS...(`█`)

## 3. ✅ Правила состояний (State Rules)

- **`Состояние default`** — Все основные элементы видимы. Кнопка навигации имеет базовое неоновое свечение. Информационные панели и логотип CASSANDRA имеют cursor: default.

- **`Состояние hover`** (для кнопки Star System) — Усиленный box-shadow, плавное увеличение масштаба (transform: scale(1.15)).

- **`Состояние active`** - (при нажатии на кнопку) — Лёгкий эффект "проваливания" (transform: scale(1.1)).

- **`Состояние логотипа CASSANDRA`** — Всегда статичен. pointer-events: none полностью отключает взаимодействие.

- **`Состояние Exploration Status`** — Текст статуса меняет стиль в зависимости от типа планеты:

    - **`Для Земли:`** - зеленый цвет, жирный шрифт (класс .home-planet).

    - **`Для экзопланет:`** - серый цвет, курсив (класс .unreachable).

## 4. ⚙️ Логика работы

>Парсинг URL: Скрипт извлекает параметры star и planet из URL (?star={star_key}&planet={planet_id}). Если параметры star или planet отсутствуют, пусты или планета не найдена в базе данных PlanetMetrics{StarName}, происходит автоматический редирект на galaxy-map.html. Fallback-отображение не используется.

- **`Генерация UI`**:

    - Центральному контейнеру присваивается класс .main-planet.{planet_id}-planet.

    - Данные для левой и правой панелей извлекаются из соответствующего массива window.PlanetMetrics{StarName} (например, window.PlanetMetricsSun) по совпадению id.

    - Специальная логика: Если planet_id === 'earth', текст лейбла дистанции меняется с "Distance from Earth:" на "Distance to Sun:".

    - Панель пользователя и роли заполняется данными из currentUser.

    - Телеметрия обновляется именем выбранной планеты.

- **`Навигация`**:

    - `Клик по Star System Button` → переход на `star-system.html?star={star_key}`.

    - `Клик по логотипу CASSANDRA` → не обрабатывается.

## 5. 🤖 Спецификация данных

Данные пользователя: sessionStorage.getItem('currentUser'). Fallback: UNKNOWN, OPERATOR.

Данные планеты: Глобальные массивы в data.js: window.PlanetMetricsSun, window.
PlanetMetricsAlphaCentauriA, window.PlanetMetricsTauCeti, window.PlanetMetricsEpsilonEridani, window.PlanetMetricsTeegarden, window.PlanetMetricsTrappist1.

При отсутствии данных планеты или звезды в глобальных массивах window.* происходит редирект на galaxy-map.html вместо отображения пустых значений.

## 6. 🧪 Сценарии автоматизированного тестирования (CAS)

> **CAS (Cassandra Automation Scenarios)** — внутренний стандарт именования сценариев автоматизированного тестирования в рамках Cassandra Framework. Формат: `CAS-{NN}: {Краткое описание}`.

### test_errors.py — Негативные сценарии и ошибки

- **CAS-01: Редирект при отсутствии данных в sessionStorage**

    - Переход: Перейти на страницу planet.html?star=sun&planet=earth.

    - Действие: Очистить sessionStorage и оценить реакцию системы при загрузке без сессии.

    - Ожидаемый результат: Автоматический редирект на login.html.

- **CAS-02: Обработка отсутствующего параметра планеты**

    - Переход: Перейти на страницу planet.html?star=sun (без &planet=).

    - Действие: Проверить URL после загрузки страницы.

    - Ожидаемый результат: Через 1.5 сек происходит автоматический редирект на 'galaxy-map.html'

### test_interactions.py — Взаимодействие с элементами интерфейса

- **CAS-01: Успешная загрузка Меркурия**

    - Переход: Перейти на страницу planet.html?star=sun&planet=mercury.

    - Действие: Проверить URL, имя планеты, текст телеметрии, кнопку навигации 'Star System'.

    - Ожидаемый результат: Ожидаемый URL 'planet.html?star=sun&planet=mercury'. Имя планеты 'MERCURY'. Телеметрия имеет текст '> CASSANDRA: AURORA, MERCURY. DOWNLOADING PLANETARY METRICS...'. Кнопка Star System видна.

- **CAS-02: Успешная загрузка Проксима Б**

    - Переход: Перейти на страницу planet.html?star=alpha-centauri&planet=proxima-b.

    - Действие: Проверить URL, имя планеты, текст телеметрии, кнопку навигации 'Star System'.

    - Ожидаемый результат: Ожидаемый URL 'planet.html?star=alpha-centauri&planet=proxima-b'. Имя планеты 'PROXIMA B'. Телеметрия имеет текст '> CASSANDRA: AURORA, PROXIMA B. DOWNLOADING PLANETARY METRICS...'. Кнопка Star System видна.

- **CAS-03: Успешная загрузка Тау Кита Е**

    - Переход: Перейти на страницу planet.html?star=tau-ceti&planet=tau-ceti-e.

    - Действие: Проверить URL, имя планеты, текст телеметрии, кнопку навигации 'Star System'.

    - Ожидаемый результат: Ожидаемый URL 'planet.html?star=tau-ceti&planet=tau-ceti-e'. Имя планеты 'TAU CETI E'. Телеметрия имеет текст '> CASSANDRA: AURORA, TAU CETI E. DOWNLOADING PLANETARY METRICS...'. Кнопка Star System видна.

- **CAS-04: Успешная загрузка Эпсилон Эридани Ц**

    - Переход: Перейти на страницу planet.html?star=epsilon-eridani&planet=epsilon-eridani-c.

    - Действие: Проверить URL, имя планеты, текст телеметрии, кнопку навигации 'Star System'.

    - Ожидаемый результат: Ожидаемый URL 'planet.html?star=epsilon-eridani&planet=epsilon-eridani-c'. Имя планеты 'EPSILON ERIDANI C'. Телеметрия имеет текст '> CASSANDRA: AURORA, EPSILON ERIDANI C. DOWNLOADING PLANETARY METRICS...'. Кнопка Star System видна.

- **CAS-05: Успешная загрузка Тегарден Б**

    - Переход: Перейти на страницу planet.html?star=teegarden&planet=teegarden-b.

    - Действие: Проверить URL, имя планеты, текст телеметрии, кнопку навигации 'Star System'.

    - Ожидаемый результат: Ожидаемый URL 'planet.html?star=teegarden&planet=teegarden-b'. Имя планеты 'TEEGARDEN B'. Телеметрия имеет текст '> CASSANDRA: AURORA, TEEGARDEN B. DOWNLOADING PLANETARY METRICS...'. Кнопка Star System видна.

- **CAS-06: Успешная загрузка Траппист 1Б**

    - Переход: Перейти на страницу planet.html?star=trappist-1&planet=trappist-1b.

    - Действие: Проверить URL, имя планеты, текст телеметрии, кнопку навигации 'Star System'.

    - Ожидаемый результат: Ожидаемый URL 'planet.html?star=trappist-1&planet=trappist-1b'. Имя планеты 'TRAPPIST-1B'. Телеметрия имеет текст '> CASSANDRA: AURORA, TRAPPIST-1B. DOWNLOADING PLANETARY METRICS...'. Кнопка Star System видна.

- **CAS-07: Навигация на Звездную Систему Солнце с Меркурия**

    - Переход: Перейти на страницу planet.html?star=sun&planet=mercury

    - Действие: Кликнуть на элемент data-wm-id='nav-star-system-btn'.

    - Ожидаемый результат: URL изменяется на star-system.html?star=sun.

- **CAS-08: Навигация на Звездную Систему Альфа Центавра А с Проксимы Б**

    - Переход: Перейти на страницу planet.html?star=alpha-centauri&planet=proxima-b

    - Действие: Кликнуть на элемент data-wm-id='nav-star-system-btn'.

    - Ожидаемый результат: URL изменяется на star-system.html?star=alpha-centauri-a.

- **CAS-09: Навигация на Звездную Систему Тау Кита с Тау Кита Е**

    - Переход: Перейти на страницу planet.html?star=tau-ceti&planet=tau-ceti-e

    - Действие: Кликнуть на элемент data-wm-id='nav-star-system-btn'.

    - Ожидаемый результат: URL изменяется на star-system.html?star=tau-ceti.

- **CAS-10: Навигация на Звездную Систему Эпсилон Эридани с Эпсилон Эридани Ц**

    - Переход: Перейти на страницу planet.html?star=epsilon-eridani&planet=epsilon-eridani-c

    - Действие: Кликнуть на элемент data-wm-id='nav-star-system-btn'.

    - Ожидаемый результат: URL изменяется на star-system.html?star=epsilon-eridani.

- **CAS-11: Навигация на Звездную Систему Тегарднес с Эпсилон Тегарднес Б**

    - Переход: Перейти на страницу planet.html?star=teegarden&planet=teegarden-b

    - Действие: Кликнуть на элемент data-wm-id='nav-star-system-btn'.

    - Ожидаемый результат: URL изменяется на star-system.html?star=teegarden.

- **CAS-12: Навигация на Звездную Систему Траппист-1 с Траппист-1Б**

    - Переход: Перейти на страницу planet.html?star=trappist-1&planet=trappist-1b

    - Действие: Кликнуть на элемент data-wm-id='nav-star-system-btn'.

    - Ожидаемый результат: URL изменяется на star-system.html?star=trappist-1.

### test_states.py — Валидация состояний UI

- **CAS-01: Валидация метрик для Меркурия**

    - Переход: Перейти на страницу planet.html?star=sun&planet=mercury

    - Действие: Проверить текстовое содержимое информацыионных панелей.

    - Ожидаемый результат:

        - PLANETARY METRICS - Mass: "0.055 M⊕"

        - PLANETARY PROFILE - The smallest planet in the

        - EXPLORATION STATUS - NO LANDINGS — Multiple flybys

- **CAS-02: Валидация метрик для Проксима Б**

    - Переход: Перейти на страницу planet.html?star=alpha-centauri&planet=proxima-b

    - Действие: Проверить текстовое содержимое информацыионных панелей.

    - Ожидаемый результат:

        - PLANETARY METRICS - Mass: "~1.2 M⊕"

        - PLANETARY PROFILE - The closest known exoplanet

        - EXPLORATION STATUS - BEYOND REACH — Physical landing currently

- **CAS-03: Валидация метрик для Тау Кита Е**

    - Переход: Перейти на страницу planet.html?star=tau-ceti&planet=tau-ceti-e

    - Действие: Проверить текстовое содержимое информацыионных панелей.

    - Ожидаемый результат:

        - PLANETARY METRICS - Mass: "~4.29 M⊕"

        - PLANETARY PROFILE - A super-Earth located in the habitable zone

        - EXPLORATION STATUS - BEYOND REACH — Physical landing currently

- **CAS-04: Валидация метрик для Эпсилона Эридани Ц**

    - Переход: Перейти на страницу planet.html?star=epsilon-eridani&planet=epsilon-eridani-c

    - Действие: Проверить текстовое содержимое информацыионных панелей.

    - Ожидаемый результат:

        - PLANETARY METRICS - Mass: "~248 M⊕"

        - PLANETARY PROFILE - A massive gas giant orbiting Epsilon Eridani
        
        - EXPLORATION STATUS - BEYOND REACH — Physical landing currently

- **CAS-05: Валидация метрик для Эпсилона Тегарден Б**

    - Переход: planet.html?star=teegarden&planet=teegarden-b

    - Действие: Проверить текстовое содержимое информацыионных панелей.

    - Ожидаемый результат:

        - PLANETARY METRICS - Mass: "~1.05 M⊕"

        - PLANETARY PROFILE - One of the most Earth-like exoplanets
        
        - EXPLORATION STATUS - BEYOND REACH — Physical landing currently

- **CAS-06: Валидация метрик для Эпсилона Траппист-1Б**

    - Переход: planet.html?star=trappist-1&planet=trappist-1b

    - Действие: Проверить текстовое содержимое информацыионных панелей.

    - Ожидаемый результат:

        - PLANETARY METRICS - Mass: "~1.02 M⊕"

        - PLANETARY PROFILE - The innermost known planet
        
        - EXPLORATION STATUS - BEYOND REACH — Physical landing currently

### test_workflows.py — Сквозные бизнес-сценарии

- **CAS-01: Полный цикл исследования планеты с возвратом**

    - Переход: Перейти на страницу planet.html?star=sun&planet=mercury
    
    - Действие: Кликнуть на data-wm-id="nav-star-system-btn" → Дождаться star-system.html?star=sun. Нажать кнопку "Назад" в браузере.

    - - Ожидаемый результат, URL соотвествует 'planet.html?star=sun&planet=mercury', левая и права информационные панели, содержат:

        - PLANETARY METRICS - Mass: "0.055 M⊕"

        - PLANETARY PROFILE - The smallest planet in the

        - EXPLORATION STATUS - NO LANDINGS — Multiple flybys

## 7. 🎨 Визуальные требования

- **Цветовая схема:** Тёмно-синий космический фон #050816, голубые акценты #4da6ff, белый текст #ffffff.

- **Панели:** Полупрозрачный фон rgba(5, 10, 30, 0.85) с backdrop-filter: blur(2vmin). Угловые декоративные элементы на левой панели.

- **Планета:** Анимация плавного парения (planet-float), уникальные радиальные градиенты и тени для каждой планеты, имитирующие освещение и атмосферу.

- **Логотип CASSANDRA:** Состоит из двух частей — CASSAN (белый #ffffff с лёгким свечением) и DRA (синий #4da6ff с более ярким свечением). Размещён в правом нижнем углу, визуально симметричен кнопке навигации слева.

- **Адаптивность:** Desktop-only (1024px+). Использование относительных единиц (vmin, vh, vw) для масштабирования.

## 8. 🏷️ Спецификация data-wm-id (Ironclad Locators)

> Все интерактивные элементы должны иметь уникальный атрибут `data-wm-id` для надёжной автоматизации.

Основные элементы

🌐 Основные элементы (Навигация, Футер, Статус)

| Элемент | data-wm-id |
|---------|-----------|
| Имя планеты | `{planet_id}]`|
| Кнопка Звездной Системы | `nav-star-system-btn`|
| Панель роли | `info-panel-role`|
| Иконка роли | `role-icon`|
| Текст роли | `role-label`|
| Панель пользователя | `info-panel-user`|
| Иконка пользователя | `user-icon`|
| Текст пользователя | `user-label`|
| Телеметрия системы | `system-telemetry`|
| Сообщение телеметрии | `telemetry-message`|
| Копирайт | `footer-copyright`|

📡 Левая панель (Planetary Metrics)

| Элемент | data-wm-id |
|---------|-----------|
| Контейнер панели | `tech-panel`|
| Иконка панели | `tech-panel-icon`|
| Значение Mass | `tech-mass`|
| Значение Radius | `tech-radius`|
| Значение Surface Gravity | `tech-gravity`|
| Значение Mean Temperature | `tech-temperature`|
| Значение Atmospheric Pressure | `tech-pressure`|
| Значение Orbital Period | `tech-orbital-period`|
| Значение Rotation Period | `tech-rotation-period`|
| Лейбл Distance | `tech-label-distance`|
| Значение Distance | `tech-distance`|

🔭 Правая панель (Planetary Profile & Exploration Status)

| Контейнер панели | `info-panel`|
| Иконка панели | `info-panel-icon`|
| Описание планеты | `info-description`|
| Текст статуса миссии | `mission-status-text`|

## 9. 🌐 URL и маршрутизация

Так как проект является учебным и статическим (без серверной части), для локальной разработки и деплоя на GitHub Pages используются следующие адреса:

- **Local Base URL (Локальная разработка и тесты):** 

    - Информация об объекте: `file:///.../cassandra/planet.html?star={star_key}&planet={planet_id}`

- **GitHub Pages URL (Публичный деплой):** 

    - Информация об объекте: `https://<username>.github.io/cassandra/planet.html?star={star_key}&planet={planet_id}`

> **Примечание для автоматизации:** 
>Переход на страницу требует наличия обоих query-параметров ?star= и &planet=. В конфигурационных файлах фреймворка URL формируется динамически.

*Версия ТЗ: 1.1 | Создано: 17.10.2026 | Автор: Evknopia*
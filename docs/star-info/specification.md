# 🚀 Cassandra Framework
## Техническое задание: Страница Star Info (Информация об объекте)

### 📌 Обозначения

-   **`ElementName`** *(type)* — UI-элемент с указанием типа
-   *"Text content"* — отображаемый текст на интерфейсе
-   `code` — технические термины, классы, методы
- `'/galaxy-map.html'` *(url)* — адрес страницы (URL) для проверки навигации
-   ⚠️ *(decorative)* — декоративный элемент, не подлежит автоматизированному тестированию

## 1. 🎯 Назначение
Страница Star Info — детализированное досье выбранного астрофизического объекта (звезды, звездной системы или сверхмассивной черной дыры). Отображает центральный визуал объекта, технические характеристики в левой панели, описание и предупреждения в правой панели, статус пользователя, а также предоставляет умную навигацию: возврат на карту галактики (для черной дыры) или на страницу звездной системы (для звезд). Страница является конечным узлом детального изучения в иерархии навигации: Galaxy Map → Star System → Star Info → Planet.

## 2. 🖥️ Элементы интерфейса

### 2.1 Основные элементы формы

- **`Black Hole Container`** (container) — Центральный визуальный элемент для черной дыры Sagittarius A*. Состоит из event-horizon, accretion-disk, photon-rings и lensing-arcs. Скрыт по умолчанию (display: none), показывается только при objectData.type === 'black-hole'. Ссылка ведет на star-info.html?star=sagittarius-a.

- **`Star Container`** (container) — Центральный визуальный элемент для звезд. Содержит star-sphere и star-glow-ring. Скрыт по умолчанию, показывается для всех объектов кроме черной дыры. Динамически применяет CSS-класс цвета из objectData.visual.sphereClass.

- **`Tech Panel`** (container) — Левая информационная панель. Отображает технические характеристики объекта. Заголовок панели динамический: состоит из типа объекта (BLACK HOLE / STAR / STAR SYSTEM) и имени объекта.

- **`Info Panel`** (container) — Правая информационная панель. Отображает описание объекта (Observation Log) и блок предупреждения (warning-box) при наличии objectData.info.warning.

- **`Galaxy Map Button`** (button) — Кнопка навигации (нижний левый угол). Показывается только для черной дыры. Иконка: 🌌. Текст: Galaxy Map. Ведет на galaxy-map.html. data-wm-id="nav-galaxy-map-btn".

- **`Star System Button`** (button) — Кнопка навигации (нижний левый угол). Показывается для всех звезд и систем. Иконка: . Текст: Star System. Ведет на star-system.html?star={star_key}. data-wm-id="nav-star-system-btn".

- **`Info Panel Role`** (container) — Информационная панель роли пользователя (верхний левый угол). Содержит иконку, название роли и тултип с деталями.

- **`Info Panel User`** (container) — Информационная панель данных пользователя (верхний правый угол). Содержит иконку, имя и тултип с позывным и ID.

- **`System Telemetry`** (text) — Строка телеметрии в футере, отображающая статус анализа объекта.

- **`Cassandra Logo`** (container) — Декоративный логотип ИИ в правом нижнем углу. Состоит из двух частей: CASSAN (белый) и DRA (синий #4da6ff). Не интерактивен. data-wm-id="nav-cassandra-logo".

### 2.2 Декоративные элементы ⚠️

> Примечание: Элементы данного раздела являются частью визуального оформления страницы и не подлежат автоматизированному тестированию. Они не имеют `data-wm-id` и не включаются в CAS-сценарии.

- **`Stars Background`** *(decorative/css)* — Анимированный фон со звёздами и Млечным Путём .stars, .milkyway.

- **`Milky Way Band (decorative/css) — Светящаяся полоса Млечного Пути .milkyway .band.
- **`Milky Way Band`** *(decorative/css)* — Светящаяся полоса Млечного Пути .milkyway .band.

- **`Star Glow Ring`** *(decorative/css)* — Неоновое кольцо вокруг центральной звезды .star-glow-ring.

- **`Black Hole Visuals`** *(decorative/css)* — Визуальные элементы черной дыры: event-horizon, photon-ring-inner, photon-ring-main, gravity-glow-outer, accretion-disk, lensing-arc-top, lensing-arc-bottom.

- **`Star Sphere Colors`** *(decorative/css)* — Уникальные CSS-градиенты для каждой звезды: .star-sphere.sun, .star-sphere.alpha, .star-sphere.epsilon, .star-sphere.tau, .star-sphere.teegarden, .star-sphere.trappist.

- **`Copyright`** *(decorative/text)* — Текст копирайта Evknopia © 2026 в футере. data-wm-id="footer-copyright".

### 2.3 Служебные элементы

- **`Telemetry`** *(text)* — Строка состояния системы в футере. Отображается моноширинным шрифтом с мигающим курсором (`█`). Формат: > CASSANDRA: {CALLSIGN}, ANALYZING {OBJECT_NAME} DATA...

- **`Warning Box`** *(container)* — Блок предупреждения в правой панели. Показывается только если objectData.info.warning существует. Содержит иконку ️ и текст предупреждения. Анимация пульсации красного свечения.

## 3. ✅ Правила состояний (State Rules)

- **`Состояние default`** — Все основные элементы видимы. Кнопки навигации имеют базовое неоновое свечение и cursor: pointer. Информационные панели и логотип CASSANDRA имеют cursor: default. Центральные контейнеры (black-hole/star) переключаются через JS.

- **`Состояние hover`** *(для кнопок Galaxy Map и Star System)* — Усиленный box-shadow (внешний и внутренний), плавное увеличение масштаба (transform: scale(1.15)).

- **`Состояние active`** `(при нажатии на кнопки)` — Лёгкий эффект "проваливания" (transform: scale(1.1)).

- **`Состояние логотипа CASSANDRA`** — Всегда статичен. Не реагирует на :hover, :active, :focus. pointer-events: none полностью отключает взаимодействие.

- **`Состояние Warning Box`** — Анимированная пульсация красного свечения (warningPulse). Иконка ⚠️ пульсирует отдельно (warningIconPulse).

## 4. ⚙️ Логика работы

> ⚠️ **Важно: Контекст проекта**
>Данный проект является учебным и не имеет серверной части (бэкенда). Все процессы аутентификации, хранения пользователей и передачи данных эмулируются исключительно на стороне клиента (Frontend) с использованием sessionStorage (для хранения активной сессии currentUser), localStorage (для эмуляции базы данных registeredUsers) и локальных конфигурационных файлов (data.js). В реальном продакшн-проекте эти функции выполнялись бы на сервере.

- Парсинг URL: Скрипт извлекает параметр star из URL (?star={star_key}). Если параметр отсутствует или объект не найден в window.*, в консоль выводится предупреждение, инициализация прерывается.

- **`Генерация UI`**:

    - Заголовок левой панели обновляется данными из объекта: тип (BLACK HOLE / STAR / STAR SYSTEM) + имя объекта.

    - Иконка левой панели устанавливается в 📡 для всех объектов.

    - Центральные контейнеры переключаются: black-hole-container для type === 'black-hole', star-container для остальных.

    - Для звезды применяется CSS-класс из objectData.visual.sphereClass.

    - Кнопки навигации переключаются: btn-galaxy-map для дыры, btn-star-system для звезд.

    - Панель пользователя и роли заполняется данными из currentUser.

    - Описание и предупреждение заполняются из objectData.info.

- **`Навигация`**:

    - `Клик по Black Hole Container` → переход на `star-info.html?star=sagittarius-a`.

    - `Клик по Galaxy Map Button` → переход на `galaxy-map.html`.

    - `Клик по Star System Button` → переход на `star-system.html?star={star_key}`.

    - `Клик по логотипу CASSANDRA` — не обрабатывается (элемент декоративный).

## 5. 🤖 Спецификация данных

Данные пользователя берутся из sessionStorage (currentUser). Fallback: UNKNOWN, OPERATOR, 🛰️.
Данные объекта берутся из глобальных объектов window.* (файл data.js) по ключу из URL.

## 6. 🧪 Сценарии автоматизированного тестирования (CAS)

> **CAS (Cassandra Automation Scenarios)** — внутренний стандарт именования сценариев автоматизированного тестирования в рамках Cassandra Framework. Формат: `CAS-{NN}: {Краткое описание}`.

### test_errors.py — Негативные сценарии и ошибки

- **CAS-01: Редирект при отсутствии данных в sessionStorage**

    - Переход: Перейти на страницу star-info.html?star=sun.

    - Действие: Очистить sessionStorage и оценить реакцию системы при загрузке без сессии.

    - Ожидаемый результат: Автоматический редирект на login.html.

- **CAS-02: Обработка отсутствующего параметра звезды**

    - Переход: Перейти на страницу star-info.html без параметра ?star= (или с пустым параметром ?star=).

    - Действие: Проверить URL после загрузки страницы.

    - Ожидаемый результат: Через 1.5 сек происходит автоматический редирект на 'galaxy-map.html'

### test_interactions.py — Взаимодействие с элементами интерфейса

- **CAS-01: Успешная загрузка Sagittarius A (черная дыра)**

    - Переход: Открыть страницу star-info.html?star=sagittarius-a.

    - Действие: Проверить заголовок панели, отображение черной дыры, телеметрию, кнопки навигации.

    - Ожидаемый результат: Заголовок панели: BLACK HOLE SAGITTARIUS A*. Отображается контейнер черной дыры (#black-hole-container видим, #star-container скрыт). Телеметрия содержит SAGITTARIUS A*. Кнопка Galaxy Map видна, кнопка Star System скрыта.

- **CAS-02: Успешная загрузка Солнца (Sol)**

    - Переход: Открыть страницу star-info.html?star=sun.

    - Действие: Проверить URL, заголовок левой панели, отображение звезды, телеметрию.

    - Ожидаемый результат: URL строго равен star-info.html?star=sun. Заголовок панели: STAR SOL (THE SUN). Отображается желтая звезда (.star-sphere.sun). Телеметрия содержит SOL (THE SUN). Кнопка Star System видна.

- **CAS-03: Успешная загрузка Альфы Центавра А**

    - Переход: Открыть страницу star-info.html?star=alpha-centauri.

    - Действие: Проверить заголовок панели, отображение звезды, телеметрию.

    - Ожидаемый результат: Заголовок панели: STAR SYSTEM ALPHA CENTAURI A. Отображается бело-желтая звезда (.star-sphere.alpha). Телеметрия содержит ALPHA CENTAURI A.

- **CAS-04: Успешная загрузка Эпсилон Эридана**

    - Переход: Открыть страницу star-info.html?star=epsilon-eridani.

    - Действие: Проверить заголовок панели, отображение звезды.

    - Ожидаемый результат: Заголовок панели: STAR EPSILON ERIDANI. Отображается оранжевая звезда (.star-sphere.epsilon).

- **CAS-05: Успешная загрузка Тау Кита**

    - Переход: Открыть страницу star-info.html?star=tau-ceti.

    - Действие: Проверить заголовок панели, отображение звезды.

    - Ожидаемый результат: Заголовок панели: STAR TAU CETI. Отображается желтая звезда (.star-sphere.tau).

- **CAS-06: Успешная загрузка Тигардена**

    - Переход: Открыть страницу star-info.html?star=teegarden.

    - Действие: Проверить заголовок панели, отображение звезды, классификацию.

    - Ожидаемый результат: Заголовок панели: STAR TEEGARDEN'S. Отображается красная звезда (.star-sphere.teegarden). Classification: Ultra-Cool Red Dwarf.

- **CAS-07: Успешная загрузка TRAPPIST-1**

    - Переход: Открыть страницу star-info.html?star=trappist-1.

    - Действие: Проверить заголовок панели, отображение звезды.

    - Ожидаемый результат: Заголовок панели: STAR SYSTEM TRAPPIST-1. Отображается красная звезда (.star-sphere.trappist).

- **CAS-08: Навигация на Карту Галактики (для черной дыры)**

    - Переход: Перейти на страницу star-info.html?star=sagittarius-a.

    - Действие: Кликнуть на элемент data-wm-id='nav-galaxy-map-btn'.

    - Ожидаемый результат: URL браузера изменяется на galaxy-map.html.

- **CAS-09: Навигация на Звездную Систему (для звезды)**

    - Переход: Перейти на страницу star-info.html?star=sun.

    - Действие: Кликнуть на элемент data-wm-id='nav-star-system-btn'.

    - Ожидаемый результат: URL браузера изменяется на star-system.html?star=sun.

- **CAS-10: Валидация hover-эффекта кнопки Star System**

    - Переход: Перейти на страницу star-info.html?star=sun

    - Действие: С помощью ActionChains навести курсор на data-wm-id='nav-star-system-btn'.

    - Ожидаемый результат: CSS-свойство transform содержит scale(1.10).

### test_states.py — Валидация состояний UI

- **CAS-01: Валидация левой и правой панелей для Sagittarius A**

    - Переход: Открыть страницу star-info.html?star=sagittarius-a.

    - Действие: Проверить текстовое содержимое левой и правой панели.

    - Ожидаемый результат: Левая панель содержит Classification: 'Supermassive Black Hole (SMBH)'. Правая панель содержит Description: 'This supermassive object acts as the gravitational anchor ...'

- **CAS-02: Валидация левой и правой панелей для Солнца**

    - Переход: Открыть страницу star-info.html?star=sun.

    - Действие: Проверить текстовое содержимое левой и правой панели.

    - Ожидаемый результат: Левая панель содержит Classification: 'G-type Yellow Dwarf'. Правая панель содержит Description: 'The central star of our planetary system...'

- **CAS-03: Валидация левой и правой панелей для Альфы Центавра А**

    - Переход: Открыть страницу star-info.html?star=alpha-centauri.

    - Действие: Проверить текстовое содержимое левой и правой панели.

    - Ожидаемый результат: Левая панель содержит Classification: 'Triple Star System'. Правая панель содержит Description: 'The closest star system to our Solar System...'

- **CAS-04: Валидация левой и правой панелей для Эпсилон Эридана**

    - Переход: Открыть страницу star-info.html?star=epsilon-eridani.

    - Действие: Проверить текстовое содержимое левой и правой панели.

    - Ожидаемый результат: Левая панель содержит Classification: 'K-type Orange Dwarf'. Правая панель содержит Description: 'A young orange dwarf star located ...'

- **CAS-05: Валидация левой и правой панелей для Тау Кита**

    - Переход: Открыть страницу star-info.html?star=tau-ceti.

    - Действие: Проверить текстовое содержимое левой и правой панели.

    - Ожидаемый результат: Левая панель содержит Classification: 'G-type Yellow Dwarf'. Правая панель содержит Description: 'A stable, metal-poor yellow dwarf remarkably similar to our Sun ...'

- **CAS-06: Валидация левой и правой панелей для Звезды Тигардена**

    - Переход: Открыть страницу star-info.html?star=teegarden.

    - Действие: Проверить текстовое содержимое левой и правой панели.

    - Ожидаемый результат: Левая панель содержит Classification: 'M-type Ultra-Cool Dwarf'. Правая панель содержит Description: 'An extremely faint ultra-cool red dwarf, one of the ...'

- **CAS-07: Валидация левой и правой панелей для TRAPPIST-1**

    - Переход: Открыть страницу star-info.html?star=trappist-1.

    - Действие: Проверить текстовое содержимое левой и правой панели.

    - Ожидаемый результат: Левая панель содержит Classification: 'Ultra-Cool Planetary Dwarf'. Правая панель содержит Description: 'An extraordinary ultra-cool red dwarf hosting seven Earth-sized ...'
    
### test_workflows.py — Сквозные бизнес-сценарии

- **CAS-01: Полный цикл исследования звезды с возвратом**

    - Переход: Перейти на страницу star-info.html?star=sun.

    - Действие: Кликнуть на data-wm-id='nav-star-system-btn' → Дождаться star-system.html?star=sun. Нажать кнопку "Назад" в браузере.

    - Ожидаемый результат: Возврат на star-info.html?star=sun. Состояние сессии сохранено, заголовок панели и телеметрия отображаются корректно.

## 7. 🎨 Визуальные требования

- **Цветовая схема:** Тёмно-синий космический фон #050816, голубые акценты #4da6ff, белый текст #ffffff, красный для предупреждений #e74c3c.

- **Звезды:** Используют сложные CSS-радиальные градиенты для имитации фотосферы, хромосферы и свечения. Уникальные классы для каждой звезды: .star-sphere.sun (желтая), .star-sphere.alpha (бело-желтая), .star-sphere.epsilon (оранжевая), .star-sphere.tau (желтая), .star-sphere.teegarden и .star-sphere.trappist (красные карлики).

- **Черная дыра:** Многослойная композиция из event-horizon, photon-rings, accretion-disk и lensing-arcs с анимациями пульсации и вращения.

- **Панели:** Полупрозрачный фон rgba(5, 10, 30, 0.85) с backdrop-filter: blur(2vmin). Угловые декоративные элементы (.info-panel-left::before/::after).

- **Логотип CASSANDRA:** Состоит из двух частей — CASSAN (белый #ffffff с лёгким свечением) и DRA (синий #4da6ff с более ярким свечением). Размещён в правом нижнем углу, визуально симметричен кнопке навигации слева.

- **Анимации:** Плавное свечение (box-shadow transitions), мигающий курсор в телеметрии, пульсация предупреждения (warningPulse), пульсация иконки предупреждения (warningIconPulse), плавное появление панелей (panelAppear).

- **Адаптивность:** Desktop-only (1024px+). Использование относительных единиц (vmin, vh, vw) для масштабирования.

## 8. 🏷️ Спецификация data-wm-id (Ironclad Locators)

> Все интерактивные элементы должны иметь уникальный атрибут `data-wm-id` для надёжной автоматизации.

Основные элементы

🌐 Основные элементы (Навигация, Футер, Статус)

| Элемент | data-wm-id |
|---------|-----------|
| Контейнер черной дыры | `visual-black-hole`|
| Контейнер звезды | `visual-star`|
| Сфера звезды | `visual-star-sphere`|
| Кнопка Карты Галактики | `nav-galaxy-map-btn`|
| Кнопка Звездной Системы | `nav-star-system-btn`|
| Логотип CASSANDRA | `cassandra-logo`|
| Копирайт | `footer-copyright`|
| Панель роли | `info-panel-role`|
| Иконка роли | `role-icon`|
| Текст роли | `role-label`|
| Панель пользователя | `info-panel-user`|
| Иконка пользователя | `user-icon`|
| Текст пользователя | `user-label`|
| Телеметрия системы | `system-telemetry`|
| Сообщение телеметрии | `telemetry-message`|

📡 Левая панель (Технические данные / Tech Panel)

| Элемент | data-wm-id |
|---------|-----------|
| Контейнер панели | `tech-panel`|
| Иконка панели | `tech-panel-icon`|
| Тип объекта | `tech-panel-type`|
| Имя объекта | `tech-panel-name`|
| Classification | `tech-classification`|
| Location | `tech-location`|
| Age | `tech-age`|
| Radius | `tech-radius`|
| Mass | `tech-mass`|
| Temperature | `tech-temperature`|
| Luminosity | `tech-luminosity`|
| Spectral Type | `tech-spectral-type`|
| Distance from Earth | `tech-distance`|

🔭 Правая панель (Журнал наблюдений / Observation Log)

| Элемент | data-wm-id |
|---------|-----------|
| Контейнер панели | `info-panel`|
| Иконка панели | `info-panel-icon`|
| Описание объекта | `info-description`|
| Блок предупреждения | `info-warning-box`|
| Текст предупреждения | `info-warning-text`|

## 9. 🌐 URL и маршрутизация
Так как проект является учебным и статическим (без серверной части), для локальной разработки и деплоя на GitHub Pages используются следующие адреса:

- **Local Base URL (Локальная разработка и тесты):** 

    - Информация об объекте: `file:///.../cassandra/star-system.html?star={star_key}`

- **GitHub Pages URL (Публичный деплой):** 

    - Информация об объекте: `https://<username>.github.io/cassandra/star-info.html?star={star_key}`

> **Примечание для автоматизации:** 
>Переход на страницу требует наличия query-параметра ?star=. В конфигурационных файлах фреймворка URL формируется динамически: BASE_URL + f"star-info.html?star={star_key}". При отсутствии параметра загружается fallback-объект (Sagittarius A*).

*Версия ТЗ: 1.0 | Создано: 09.10.2026 | Автор: Evknopia*













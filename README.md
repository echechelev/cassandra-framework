<p align="center">
  <img src="https://raw.githubusercontent.com/echechelev/cassandra-framework/main/assets/evknopia-banner.png" alt="Cassandra Framework" width="300">
</p>

<h1 align="center">Cassandra Framework</h1>
<p align="center">
  <strong>Фреймворк автоматизированного тестирования для системы оценки жизнепригодности планет</strong><br>
  <em>160+ автотестов | 8 модулей | Full-cycle QA Engineering</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Tests-160+-orange.svg" alt="Tests">
  <img src="https://img.shields.io/badge/Framework-Selene-orange.svg" alt="Selene">
  <img src="https://img.shields.io/badge/Runner-pytest-purple.svg" alt="pytest">
  <img src="https://img.shields.io/badge/Reports-Allure-green.svg" alt="Allure">
</p>

---

## 🌌 О проекте

**Cassandra** — это масштабируемый фреймворк автоматизированного тестирования, разработанный с нуля для комплексной системы оценки индексов жизнепригодности планет. Проект демонстрирует полный цикл QA-инженерии: от системного анализа и проектирования архитектуры до реализации 160+ стабильных автотестов, покрывающих 9 функциональных модулей.

Проект создан как доказательство того, что надежная QA-инфраструктура может быть выстроена самостоятельно, без готовых шаблонов, с глубоким пониманием архитектуры, паттернов проектирования и принципов поддерживаемости кода.

## 📊 Масштаб проекта

- **160+ автотестов** с покрытием критических бизнес-сценариев
- **9 функциональных модулей**: авторизация, регистрация, восстановление доступа, карта галактики, информация о звездах и системах, дашборд, расчеты индексов
- **100% Page Object Model** с централизованным управлением локаторами
- **Pre-commit hooks** для обеспечения качества кода на этапе коммита
- **Allure Report** с детальной визуализацией каждого шага и шагов валидации

## 🚀 Архитектурные особенности

### 🏛️ Page Object Model (POM)
- Модульная структура с четким разделением ответственности
- Fluent interface (`return self`) для читаемых цепочек вызовов
- Централизованное хранение локаторов через кастомные атрибуты `data-wm-id`
- Встроенная обработка исключений и умные ожидания (waits)

### 🧪 Тестовая архитектура
- **Строгий паттерн AAA** (Arrange-Act-Assert)
- **Параметризация тестов** через мощные pytest fixtures
- **Изоляция тестов** через независимые фикстуры и моки
- **Data-driven подход** с вынесенными тестовыми данными (`users.json`, `data.py`)

### ⚙️ Инфраструктура и Code Quality
- **Pre-commit hooks** (`flake8`, `black`, `isort`) для автоматического контроля стиля
- **Конфигурация через `pyproject.toml`** и `pytest.ini`
- **Allure integration** для детальной и красивой отчетности
- **Гибкая конфигурация** через переменные окружения (`BASE_URL`)

### 🛡️ Quality Assurance акценты
- **Реактивная валидация** форм в реальном времени
- **Тестирование UX/UI состояний** (анимации, сетевые задержки, переходы)
- **Security testing** (валидация ввода, XSS payloads, защита от перебора)
- **Edge cases & boundary values** покрытие

---

## 📦 Покрытые модули

| Модуль | Статус | Описание |
|--------|--------|----------|
| **test_login** | ✅ Completed | Авторизация, валидация, реактивность, security |
| **test_signup** | ✅ Completed | Регистрация, валидация полей, обработка ошибок |
| **test_access_restoration** | ✅ Completed | Восстановление доступа, email-верификация |
| **test_dashboard** | ✅ Completed | Главный дашборд, виджеты, навигация |
| **test_index** | ✅ Completed | Лендинг, основная навигация |
| **galaxy_map** | ✅ Completed | Интерактивная карта галактики, выбор звезд |
| **star_info** | ✅ Completed | Детальная информация о звездах |
| **star_system** | ✅ Completed | Планетарные системы, орбиты |

---

## 🗂️ Структура проекта

```text
cassandra-framework/
├── app/                        # Исходный код фронтенд-приложения (HTML/CSS/JS)
├── assets/                     # Статические ресурсы (логотипы, баннеры, гифки)
├── docs/                       # Техническая документация и спецификации (ТЗ)
│   ├── design/                 # Макеты и референсы интерфейса
│   └── specifications/         # Описание бизнес-логики и тест-кейсов
├── evknopia/                   # Кастомные утилиты, хелперы и обертки фреймворка
├── pages/                      # Реализация паттерна Page Object Model (POM)
│   ├── auth/                   # Модули: login, signup, access_restoration
│   ├── galaxy/                 # Модули: galaxy_map, star_info, star_system
│   └── dashboard/              # Модули: dashboard, calculations
├── tests/                      # Автотесты (160+ сценариев)
│   ├── conftest.py             # Глобальные и модульные фикстуры pytest
│   ├── data.py                 # Тестовые данные, константы и конфигурации
│   ├── users.json              # Демо-учетные данные для авторизации
│   └── [module_name]/          # Тестовые модули, зеркально отражающие структуру pages/
├── .pre-commit-config.yaml     # Конфигурация pre-commit хуков (black, flake8, isort)
├── pyproject.toml              # Настройки проекта, линтеров и форматтеров
├── pytest.ini                  # Конфигурация запуска pytest и Allure
├── requirements.txt            # Зависимости Python-окружения
├── CAS_PHILOSOPHY.md           # Философия и идеология проекта Кассандра
└── README.md                   # Этот файл

🔧 Технологический стек

Automation & Backend
Python 3.11+
pytest — мощный и гибкий тестовый раннер
selene — modern, лаконичная обертка над Selenium
allure-pytest — профессиональная система отчетности
Code Quality
black — бескомпромиссное форматирование кода
isort — интеллектуальная сортировка импортов
flake8 — строгий линтинг
pre-commit — автоматизация проверок перед коммитом
Frontend (в тестируемом приложении)
HTML5, CSS3, JavaScript (ES6+)
Vanilla JS (без тяжелых фреймворков для максимальной производительности)
Infrastructure
GitHub Pages — хостинг приложения
Git — контроль версий
JSON — хранение тестовых данных

🎯 Roadmap

✅ Реализовано (Q3-Q4 2024)
Базовая масштабируемая архитектура фреймворка
9 функциональных модулей (160+ стабильных тестов)
Pre-commit hooks и строгий code quality контроль
Allure интеграция и кастомные шаги
Data-driven подход и моки

🚧 В работе (Q1 2025)
CI/CD пайплайн (GitHub Actions / GitLab CI)
Параллельный запуск тестов в Docker-контейнерах
Расширение покрытия API-тестами (REST endpoints)
Тоггл "Реализм / Фантастика" с физическими расчетами массы и времени полета

🔮 Планы (2025)
Интеграция с системами мониторинга качества (Prometheus/Grafana)
Расширение общего покрытия до 300+ тестов
Мультибраузерное тестирование (Chrome, Firefox, Safari)
Визуальное регрессионное тестирование (Visual Regression Testing)

👨‍💻 Автор
Evgenii Chechelev (Evknopia)
QA Automation Engineer | SDET | Space Enthusiast
"Качество — это не проверка галочек, а системная инженерная работа. Каждый тест — это инвестиция в надежность продукта."
GitHub: @echechelev
Project: Cassandra Framework

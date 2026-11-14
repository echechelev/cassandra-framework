# ️ Философия архитектуры CAS / CAS Architecture Philosophy

---

## [RU] Генезис: От боли к принципам
На старте автоматизации своего первого проекта, я столкнулся с классическими проблемами QA-инженера: нестабильные тесты из-за `sleep()`, ломкие локаторы, «мусор» в данных и нечитаемые ошибки. Вместо латания симптомов я провел анализ корневых причин и спроектировал **CAS (Custom Automation Strategy)** — системный подход, устраняющий эти проблемы на архитектурном уровне.

### 7 Столпов CAS
1.  **Beautiful Errors (Красивые Ошибки):** Ошибки говорят на человеческом языке с бизнес-контекстом, а не выдают сухие стектрейсы.
2.  **Toast as Sync Point (Тост как Точка Синхронизации):** Синхронизация по бизнес-событиям (уведомлениям), а не по таймерам. Гарантия обработки бэкендом.
3.  **Ironclad Locators (Непробиваемые Локаторы):** Поиск через `ancestor::` по контексту родителя. Иммунитет к изменению верстки.
4.  **Idempotent & Honest Teardown (Честная Уборка):** Безопасное удаление без скрытых ошибок. Молчание при отсутствии элемента, крик при реальной проблеме.
5.  **Explicit Clear Before Type (Явная Очистка):** Обязательный `.clear()` перед вводом. Защита от автодополнения и остатков данных.
6.  **Atomic Methods (Атомарные Методы):** Один метод = одно бизнес-действие. Никакой «лапши», полная переиспользуемость.
7.  **DRY by Design (DRY по Проектированию):** Не копирование кода, а создание надежных абстракций, которые *хочется* использовать повторно.

> *CAS синтезирует проверенные принципы (SOLID, DRY) с уроками реальных проектов. Это не изобретение новых правил, а системное применение правильных.*

---

## [EN] Genesis: From Pain to Principles
At the start of automating my first project, I encountered classic QA pitfalls: flaky tests due to `sleep()`, brittle locators, data pollution, and unreadable errors. Instead of patching symptoms, I conducted root cause analysis and designed **CAS (Custom Automation Strategy)** — a systematic approach eliminating these issues at the architectural level.

### The 7 Pillars of CAS
1.  **Beautiful Errors:** Errors speak human language with business context, not dry stack traces.
2.  **Toast as Sync Point:** Synchronization via business events (toasts), not timers. Guaranteed backend processing.
3.  **Ironclad Locators:** Context-based search via `ancestor::`. Immune to UI refactoring.
4.  **Idempotent & Honest Teardown:** Safe cleanup without silent failures. Silence if missing, loud error if broken.
5.  **Explicit Clear Before Type:** Mandatory `.clear()` before input. Protection against autocomplete artifacts.
6.  **Atomic Methods:** One method = one business action. No spaghetti code, full reusability.
7.  **DRY by Design:** Not code copying, but creating reliable abstractions you *want* to reuse.

> *CAS synthesizes proven principles (SOLID, DRY) with hard-won lessons from real projects. It’s not about inventing new rules — it’s about systematically applying the right ones.*

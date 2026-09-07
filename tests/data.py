import json
from pathlib import Path

# ==========================================
# 📂 Настройка путей и загрузка данных
# ==========================================

USERS_FILE = Path(__file__).parent / "users.json"

with open(USERS_FILE, "r", encoding="utf-8") as f:
    USERS = json.load(f)

# ==========================================
# 🌐 URL-АДРЕСА (URLs)
# ==========================================
INDEX_URL = '/index.html'
SIGNUP_URL = '/signup.html'
LOGIN_URL = '/login.html'
DASHBOARD_URL = '/dashboard.html'
GALAXY_MAP_URL = '/galaxy-map.html'

# ==========================================
# 👨‍🚀 ДАННЫЕ ПОЛЬЗОВАТЕЛЕЙ (User Data)
# ==========================================

# Загруженные из JSON
USER_AURORA = USERS["users"]["AURORA"]
USER_ORION = USERS["users"]["ORION"]

# Nova — захардкожена в системе
USER_NOVA = {
    "callsign": "NOVA",
    "full_name": "Nova",
    "role": "ENGINEER",
    "function": "Systems Engineering",
    "access_level": "3",
    "id": "512-3A",
    "access_code": "QUASAR_5",
    "recovery_cipher": "COMETA",
}

# ==========================================
# 📡 ПОЗЫВНЫЕ (Callsigns)
# ==========================================
CALLSIGN_NOVA = 'NOVA'
CALLSIGN_AURORA = USERS["users"]["AURORA"]["callsign"]
CALLSIGN_ORION = USERS["users"]["ORION"]["callsign"]

# Тестовые данные (невалидные)
CALLSIGN_WRONG = 'IVAN'  # несуществующий пользователь
CALLSIGN_TOO_SHORT_2_CHARS = "AB"
CALLSIGN_MIN_VALID_3_CHARS = "ABC"

# ==========================================
# 👤 ОТОБРАЖАЕМЫЕ ИМЕНА В ТЕЛЕМЕТРИИ (Telemetry Names)
# ==========================================
TELEMETRY_NAME_AURORA = 'AURORA'
TELEMETRY_NAME_NOVA = 'NOVA'
TELEMETRY_NAME_ORION = 'ORION'

# ==========================================
# 👤 ИМЕНА ОПЕРАТОРОВ (Names)
# ==========================================
NAME_NOVA = 'Nova'
NAME_AURORA = 'Aurora'
NAME_ORION = 'Orion'
NAME_IVAN = 'Ivan'  # тестовое имя для негативных сценариев

# ==========================================
# 🔐 ДАННЫЕ АУТЕНТИФИКАЦИИ (Authentication)
# ==========================================

# Access Codes
ACCESS_CODE_NOVA = 'QUASAR_5'
ACCESS_CODE_AURORA = USERS["users"]["AURORA"]["access_code"]
ACCESS_CODE_ORION = USERS["users"]["ORION"]["access_code"]

# Recovery Ciphers
RECOVERY_CIPHER_NOVA = 'COMETA'

# Невалидные данные для тестов
ACCESS_CODE_WRONG = 'WRONG_CODE'
RECOVERY_CIPHER_WRONG = 'WRONG'
ACCESS_CODE_TOO_SHORT_3_CHARS = "abc"
ACCESS_CODE_MIN_VALID_4_CHARS = "abcd"
SQL_INJECTION_PAYLOAD = "' OR '1'='1'"

# ==========================================
# 🎖️ РОЛИ И ФУНКЦИИ (Roles & Functions)
# ==========================================

# Роли (значения для select на форме регистрации)
ROLE_COMMANDER = 'COMMANDER'
ROLE_SPECIALIST = 'SPECIALIST'
ROLE_ENGINEER = 'ENGINEER'

# Отображаемые роли (текст в сводке на Шаге 3)
ROLE_DISPLAY_COMMANDER = '🏅 Commander'
ROLE_DISPLAY_SPECIALIST = '🛰️ Specialist'
ROLE_DISPLAY_ENGINEER = '⚙️ Engineer'

# Функции операторов
FUNCTION_ENGINEER = 'Systems Engineering'

# Уровни доступа (автоматически присваиваются по роли)
ACCESS_LEVEL_COMMANDER = '1'
ACCESS_LEVEL_SPECIALIST = '2'
ACCESS_LEVEL_ENGINEER = '3'

# ID оператора NOVA (захардкожен в системе)
OPERATOR_ID_NOVA = '512-3A'

# ==========================================
# 🎖️ ОТОБРАЖАЕМЫЕ РОЛИ В ИНФО-ПАНЕЛЯХ (Info Panel Roles)
# ==========================================
INFO_PANEL_ROLE_COMMANDER = 'COMMANDER'
INFO_PANEL_ROLE_SPECIALIST = 'SPECIALIST'
INFO_PANEL_ROLE_ENGINEER = 'ENGINEER'

# ==========================================
# 💬 ТЕКСТЫ UI (UI Texts)
# ==========================================

# Подзаголовки шагов
SUBTITLE_PHASE_1 = 'Phase 1: Operator Identity'
SUBTITLE_PHASE_2 = 'Phase 2: Security Setup'
SUBTITLE_WELCOME_OPERATOR = 'Welcome aboard, new Operator.'

# Телеметрия (синий цвет — информационные сообщения)
TELEMETRY_AWAITING_OPERATOR = '> SYSTEM READY. AWAITING OPERATOR REGISTRATION'
TELEMETRY_AWAITING_SECURITY = '> SYSTEM READY. AWAITING SECURITY REGISTRATION'
DEFAULT_TEXT_TELEMETRY = "> SYSTEM READY. AWAITING CONNECTION"

# Телеметрия (зелёный цвет — успешные операции)
TELEMETRY_REGISTRATION_COMPLETE = '> REGISTRATION COMPLETE. OPERATOR ACCOUNT ACTIVATED.'
TELEMETRY_SYSTEM_READY_AURORA = '> CASSANDRA: AURORA, SYSTEM READY FOR WORK. AWAITING COMMANDS.'
SUCCESS_TELEMETRY_TEXT_AURORA = '> CONNECTION ESTABLISHED. WELCOME, SPECIALIST AURORA'
SUCCESS_TELEMETRY_TEXT_NOVA = '> CONNECTION ESTABLISHED. WELCOME, ENGINEER NOVA'
SUCCESS_TELEMETRY_TEXT_ORION = '> CONNECTION ESTABLISHED. WELCOME, COMMANDER ORION'

# Заголовки и футеры
LOGO_CASSAN = 'CASSAN'
LOGO_DRA = 'DRA'
PROJECT_TITLE = 'PLANETARY HABITABILITY ASSESSMENT PROJECT'
PROJECT_SLOGAN = 'We Find a New Home Among the Stars'
COPYRIGHT_TEXT = 'Evknopia © 2026'

# ==========================================
# ⚠️ СООБЩЕНИЯ ОБ ОШИБКАХ (Error Messages)
# ==========================================

# Ошибки валидации полей (красный текст в error block)
AUTH_ERROR_BLOCK_TEXT = "⚠️ Invalid callsign or access code"
ERROR_CALLSIGN_AURORA_RESERVED = "⚠️ Callsign 'AURORA' is already in use. This identity is reserved."
ERROR_CALLSIGN_ORION_RESERVED = "⚠️ Callsign 'ORION' is already in use. This identity is reserved."
ERROR_ROLE_MISMATCH = '⚠️ Registration suspended. Pre-allocated identity requires ENGINEER role.'
ERROR_CAPACITY_REACHED = '⚠️ Registration suspended. System capacity reached. Only pending activation: NOVA.'
ERROR_ACCESS_CODES_MISMATCH = "⚠️ Access codes do not match. Please verify and try again."
ERROR_ACCESS_CODE_INVALID = "⚠️ Access Code invalid. Pre-configured credentials required."
ERROR_RECOVERY_CIPHER_INVALID = "⚠️ Recovery Cipher invalid. Pre-configured credentials required."

# Телеметрия ошибок (красный текст)
ERROR_TEXT_TELEMETRY_RED = "> SYSTEM FAILURE. INVALID CREDENTIALS"
TELEMETRY_ACCESS_DENIED_REDIRECT = "> CASSANDRA: ACCESS DENIED. REDIRECTING..."
TELEMETRY_DATA_CORRUPTED_REDIRECT = "> CASSANDRA: DATA CORRUPTED. REDIRECTING..."
TELEMETRY_ERROR_AURORA = "> SYSTEM LOCKED. CALLSIGN 'AURORA' ALREADY EXISTS"
TELEMETRY_ERROR_ORION = "> SYSTEM LOCKED. CALLSIGN 'ORION' ALREADY EXISTS"
TELEMETRY_ERROR_ROLE_MISMATCH = '> SYSTEM LOCKED. ROLE MISMATCH DETECTED'
TELEMETRY_ERROR_UNKNOWN_USER = '> SYSTEM LOCKED. PLEASE ENTER CORRECT FULL NAME AND CALLSIGN'
TELEMETRY_ERROR_CODES_MISMATCH = '> SECURITY PROTOCOL FAILED. CODES MISMATCH DETECTED'
TELEMETRY_ERROR_INVALID_ACCESS_CODE = '> SECURITY PROTOCOL FAILED. INVALID ACCESS CODE'
TELEMETRY_ERROR_INVALID_RECOVERY_CIPHER = '> SECURITY PROTOCOL FAILED. INVALID RECOVERY CIPHER'
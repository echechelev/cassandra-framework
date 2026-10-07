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

# Аутентификация и вход
INDEX_URL = "index.html"
SIGNUP_URL = "signup.html"
LOGIN_URL = "login.html"
ACCESS_RESTORATION_URL = "access-restoration.html"

# Основные страницы навигации
DASHBOARD_URL = "dashboard.html"
GALAXY_MAP_URL = "galaxy-map.html"
CIS_INDEX_TABLE_URL = "cis-index-table.html"

# Звёздные системы и Чёрная дыра
STAR_SYSTEM_URL = {
    "no-star": "star-system.html",
    "black-hole": "black-hole.html", 
    "sun": "star-system.html?star=sun",
    "alpha-centauri": "star-system.html?star=alpha-centauri",
    "epsilon-eridani": "star-system.html?star=epsilon-eridani",
    "tau-ceti": "star-system.html?star=tau-ceti",
    "teegarden": "star-system.html?star=teegarden",
    "trappist-1": "star-system.html?star=trappist-1",
}

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
    "role_icon": "⚙️",
    "function": "Systems Engineering",
    "access_level": "3",
    "id": "512-3A",
    "access_code": "QUASAR_5",
    "recovery_cipher": "COMETA",
}

# Knopa — предсуществующий системный пользователь (Восстановление)
USER_KNOPA = {
    "callsign": "KNOPA",
    "full_name": "Knopa",
    "role": "PILOT",
    "role_icon": "✈️",
    "function": "Flight Operations",
    "access_level": "1",
    "id": "769-1A",
    "access_code": "AERO_99", 
    "recovery_cipher": "AERO", 
}

# ==========================================
# 📡 ПОЗЫВНЫЕ (Callsigns)
# ==========================================
CALLSIGN_KNOPA = 'KNOPA'
CALLSIGN_NOVA = 'NOVA'
CALLSIGN_AURORA = USERS["users"]["AURORA"]["callsign"]
CALLSIGN_ORION = USERS["users"]["ORION"]["callsign"]
CALLSIGN_MIN_VALID_4_CHARS = "ABCD"

# ==========================================
# 👤 ОТОБРАЖАЕМЫЕ ИМЕНА В ТЕЛЕМЕТРИИ (Telemetry Names)
# ==========================================
TELEMETRY_NAME_KNOPA = 'KNOPA'
TELEMETRY_NAME_AURORA = 'AURORA'
TELEMETRY_NAME_NOVA = 'NOVA'
TELEMETRY_NAME_ORION = 'ORION'

# ==========================================
# 👤 ИМЕНА ОПЕРАТОРОВ (Names)
# ==========================================
NAME_KNOPA = 'Knopa'
NAME_NOVA = 'Nova'
NAME_AURORA = 'Aurora'
NAME_ORION = 'Orion'
NAME_IVAN = 'Ivan'  
FULL_BNAME_MIN_VALID_4_CHARS = "ABCD"

# ==========================================
# 🔐 ДАННЫЕ АУТЕНТИФИКАЦИИ (Authentication)
# ==========================================

# Access Codes
ACCESS_CODE_KNOPA = 'AERO_99'
ACCESS_CODE_NOVA = 'QUASAR_5'
ACCESS_CODE_AURORA = USERS["users"]["AURORA"]["access_code"]
ACCESS_CODE_ORION = USERS["users"]["ORION"]["access_code"]
ACCESS_CODE_MIN_VALID_4_CHARS = "ABCD"

# Recovery Ciphers
RECOVERY_CIPHER_NOVA = 'COMETA'
RECOVERY_CIPHER_KNOPA = 'AERO'
RECOVERY_CIPHER_MIN_VALID_4_CHARS = "ABCD"

# Тестовые данные (невалидные)
ACCESS_CODE_TOO_SHORT_3_CHARS = "ABC"
ACCESS_CODE_WRONG = 'WRONG_CODE'
CALLSIGN_WRONG = 'IVAN'  
CALLSIGN_TOO_SHORT_3_CHARS = "ABC"
FULL_NAME_TOO_SHORT_3_CHARS = "ABC"
RECOVERY_CIPHER_TOO_SHORT_3_CHARS = "ABC"
RECOVERY_CIPHER_WRONG = 'WRONG'
SQL_INJECTION_PAYLOAD = "' OR '1'='1'"

# ==========================================
# 🎖️ РОЛИ И ФУНКЦИИ (Roles & Functions)
# ==========================================

# Роли (значения для select на форме регистрации)
ROLE_COMMANDER = 'COMMANDER'
ROLE_SPECIALIST = 'SPECIALIST'
ROLE_ENGINEER = 'ENGINEER'
ROLE_PILOT = 'PILOT'

# Отображаемые роли (текст в сводке на Шаге 3)
ROLE_DISPLAY_COMMANDER = '🏅 Commander'
ROLE_DISPLAY_SPECIALIST = '🛰️ Specialist'
ROLE_DISPLAY_ENGINEER = '⚙️ Engineer'
ROLE_DISPLAY_PILOT = '✈️ Pilot'

# Функции операторов
FUNCTION_COMMANDER = 'Command & Strategy'
FUNCTION_PILOT = 'Flight Operations'
FUNCTION_SPECIALIST = 'Comms & Diagnostics'
FUNCTION_ENGINEER = 'Systems Engineering'

# Уровни доступа (автоматически присваиваются по роли)
ACCESS_LEVEL_COMMANDER = '1'
ACCESS_LEVEL_SPECIALIST = '2'
ACCESS_LEVEL_ENGINEER = '3'

# ID оператора NOVA (захардкожен в системе)
OPERATOR_ID_NOVA = '512-3A'
OPERATOR_ID_KNOPA = '769-1A'

# ==========================================
# 🎖️ ОТОБРАЖАЕМЫЕ РОЛИ В ИНФО-ПАНЕЛЯХ (Info Panel Roles)
# ==========================================
INFO_PANEL_ROLE_COMMANDER = 'COMMANDER'
INFO_PANEL_ROLE_SPECIALIST = 'SPECIALIST'
INFO_PANEL_ROLE_ENGINEER = 'ENGINEER'
INFO_PANEL_ROLE_PILOT = 'PILOT'

# ==========================================
# 🌌 ПЛАНЕТЫ СОЛНЕЧНОЙ СИСТЕМЫ (Solar System Planets)
# ==========================================

# 🌑 Меркурий
MERCURY_ID = 'planet-mercury-btn'
MERCURY_NAME = 'MERCURY'

# 🌟 Венера
VENUS_ID = 'planet-venus-btn'
VENUS_NAME = 'VENUS'

# 🌍 Земля
EARTH_ID = 'planet-earth-btn'
EARTH_NAME = 'EARTH'
EARTH_CSS_CLASS = 'planet-icon.planet-earth'
EARTH_COLOR = '#4da6ff'

# 🔴 Марс
MARS_ID = 'planet-mars-btn'
MARS_NAME = 'MARS'

# 🧊 Уран
URANUS_ID = 'planet-uranus-btn'
URANUS_NAME = 'URANUS'

# 🌊 Нептун
NEPTUNE_ID = 'planet-neptune-btn'
NEPTUNE_NAME = 'NEPTUNE'

# ==========================================
# 🌠 ПЛАНЕТЫ АЛЬФЫ ЦЕНТАВРА (Alpha Centauri Planets)
# ==========================================

# 🪐 Проксима B
PROXIMA_B_ID = 'planet-proxima-b-btn'
PROXIMA_B_NAME = 'PROXIMA B'

# 🔵 Проксима C
PROXIMA_C_ID = 'planet-proxima-c-btn'
PROXIMA_C_NAME = 'PROXIMA C'

# 🌑 Проксима D
PROXIMA_D_ID = 'planet-proxima-d-btn'
PROXIMA_D_NAME = 'PROXIMA D'

# ==========================================
# 🟠 ПЛАНЕТЫ ЭПСИЛОН ЭРИДАНА (Epsilon Eridani Planets)
# ==========================================

# 🪐 Эпсилон Эридана C
EPSILON_ERIDANI_C_ID = 'planet-epsilon-eridani-c-btn'
EPSILON_ERIDANI_C_NAME = 'EPSILON ERIDANI C'

# ==========================================
# 🌟 ПЛАНЕТЫ ТАУ КИТА (Tau Ceti Planets)
# ==========================================

#  Тау Кита e
TAU_CETI_E_ID = 'planet-tau-ceti-e-btn'
TAU_CETI_E_NAME = 'TAU CETI E'

# 🌊 Тау Кита f
TAU_CETI_F_ID = 'planet-tau-ceti-f-btn'
TAU_CETI_F_NAME = 'TAU CETI F'

# 🧊 Тау Кита g
TAU_CETI_G_ID = 'planet-tau-ceti-g-btn'
TAU_CETI_G_NAME = 'TAU CETI G'

# ❄️ Тау Кита h
TAU_CETI_H_ID = 'planet-tau-ceti-h-btn'
TAU_CETI_H_NAME = 'TAU CETI H'

# ==========================================
# 🔴 ПЛАНЕТЫ ТИГАРДЕН (Teegarden Planets)
# ==========================================

# 🌑 Тигарден b
TEEGARDEN_B_ID = 'planet-teegarden-b-btn'
TEEGARDEN_B_NAME = 'TEEGARDEN B'

#  Тигарден c
TEEGARDEN_C_ID = 'planet-teegarden-c-btn'
TEEGARDEN_C_NAME = 'TEEGARDEN C'

# ==========================================
#  ПЛАНЕТЫ TRAPPIST-1 (TRAPPIST-1 Planets)
# ==========================================

# 🔴 TRAPPIST-1 b
TRAPPIST_1B_ID = 'planet-trappist-1b-btn'
TRAPPIST_1B_NAME = 'TRAPPIST-1B'

# 🟠 TRAPPIST-1 c
TRAPPIST_1C_ID = 'planet-trappist-1c-btn'
TRAPPIST_1C_NAME = 'TRAPPIST-1C'

#  TRAPPIST-1 d
TRAPPIST_1D_ID = 'planet-trappist-1d-btn'
TRAPPIST_1D_NAME = 'TRAPPIST-1D'

# 🌍 TRAPPIST-1 e
TRAPPIST_1E_ID = 'planet-trappist-1e-btn'
TRAPPIST_1E_NAME = 'TRAPPIST-1E'

# 🔵 TRAPPIST-1 f
TRAPPIST_1F_ID = 'planet-trappist-1f-btn'
TRAPPIST_1F_NAME = 'TRAPPIST-1F'

# 🧊 TRAPPIST-1 g
TRAPPIST_1G_ID = 'planet-trappist-1g-btn'
TRAPPIST_1G_NAME = 'TRAPPIST-1G'

# ⚪ TRAPPIST-1 h
TRAPPIST_1H_ID = 'planet-trappist-1h-btn'
TRAPPIST_1H_NAME = 'TRAPPIST-1H'

# ==========================================
# 💬 ТЕКСТЫ UI (UI Texts)
# ==========================================

# Фазы онбординга
PHASE_1_IDENTITY = 'Phase 1: Operator Identity'
PHASE_2_SECURITY = 'Phase 2: Security Setup'

# Приветствия и статусы
WELCOME_OPERATOR = 'Welcome aboard, new Operator.'
PROTOCOL_VERIFIED = '✅ Access Protocol Verified'

# Основные экраны
RESTORATION_PROTOCOL = 'Access Restoration Protocol'
COLONIZATION_ACCESS = 'Access to Colonization Assessment System'

# ==========================================
#  Телеметрия: Синий блок (Ожидание / Статусы)
# ==========================================
            
_BLUE_PREFIX = '> SYSTEM READY. AWAITING '

BLUE_TELEMETRY_AWAITING_OPERATOR = f"{_BLUE_PREFIX}OPERATOR REGISTRATION"
BLUE_TELEMETRY_AWAITING_SECURITY = f"{_BLUE_PREFIX}SECURITY REGISTRATION"
BLUE_TELEMETRY_AWAITING_CONNECTION = f"{_BLUE_PREFIX}CONNECTION" 
BLUE_TELEMETRY_AWAITING_RESTORATION = f"{_BLUE_PREFIX}RESTORATION PROTOCOL"

# ==========================================
# 🟢 Телеметрия: Зелёный блок (Успех / Завершение)
# ==========================================

_GREEN_BASE_PREFIX = '> '
_GREEN_WELCOME_PREFIX = f"{_GREEN_BASE_PREFIX}CONNECTION ESTABLISHED. WELCOME, "

GREEN_TELEMETRY_REGISTRATION_COMPLETE = f"{_GREEN_BASE_PREFIX}REGISTRATION COMPLETE. OPERATOR ACCOUNT ACTIVATED."
GREEN_TELEMETRY_SYSTEM_READY_AURORA = f"{_GREEN_BASE_PREFIX}CASSANDRA: AURORA, SYSTEM READY FOR WORK. AWAITING COMMANDS."
GREEN_TELEMETRY_SELECT_STAR_SYSTEM_AURORA = f"{_GREEN_BASE_PREFIX}CASSANDRA: AURORA, SELECT A STAR SYSTEM FOR INVESTIGATION."
GREEN_TELEMETRY_SELECT_STAR_SYSTEM_SOL_AURORA = f"{_GREEN_BASE_PREFIX}CASSANDRA: AURORA, SCANNING SOL (SUN) SYSTEM... 6 PLANETS DETECTED. AWAITING SELECTION."

GREEN_TELEMETRY_WELCOME_AURORA = f"{_GREEN_WELCOME_PREFIX}SPECIALIST AURORA"
GREEN_TELEMETRY_WELCOME_NOVA = f"{_GREEN_WELCOME_PREFIX}ENGINEER NOVA"
GREEN_TELEMETRY_WELCOME_ORION = f"{_GREEN_WELCOME_PREFIX}COMMANDER ORION"
GREEN_TELEMETRY_WELCOME_KNOPA = f"{_GREEN_WELCOME_PREFIX}PILOT KNOPA" 

GREEN_TELEMETRY_RESTORATION_COMPLETE = f"{_GREEN_BASE_PREFIX}RESTORATION COMPLETE. NEW CREDENTIALS ISSUED." 

# ==========================================
# 🏷️ Заголовки и футеры
# ==========================================
LOGO_CASSAN = 'CASSAN'
LOGO_DRA = 'DRA'
GALAXY_TITLE = 'GALAXY MILKY WAY'
STAR_SYSTEM_SUN = 'STAR SYSTEM SOL'
STAR_SYSTEM_TRAPPIST_TITLE = 'STAR SYSTEM TRAPPIST-1'
PROJECT_TITLE = 'PLANETARY HABITABILITY ASSESSMENT PROJECT'
PROJECT_SLOGAN = 'We Find a New Home Among the Stars'
COPYRIGHT_TEXT = 'Evknopia © 2026'

# ==========================================
# ⚠️ ОШИБКИ ВАЛИДАЦИИ ПОЛЕЙ (Красный текст в error block)
# ==========================================

RED_ERROR_AUTH_INVALID = '⚠️ Invalid callsign or access code'

RED_ERROR_CALLSIGN_AURORA_RESERVED = "⚠️ Callsign 'AURORA' is already in use. This identity is reserved."
RED_ERROR_CALLSIGN_KNOPA_RESERVED = "⚠️ Callsign 'KNOPA' is already in use. This identity is reserved."
RED_ERROR_CALLSIGN_ORION_RESERVED = "⚠️ Callsign 'ORION' is already in use. This identity is reserved."

RED_ERROR_ROLE_MISMATCH = '⚠️ Registration suspended. Pre-allocated identity requires ENGINEER role.'
RED_ERROR_CAPACITY_REACHED = '⚠️ Registration suspended. System capacity reached. Only pending activation: NOVA.'
RED_ERROR_ALREADY_RESTORED = "⚠️ Operator 'KNOPA' has already been restored. Please use your new credentials to log in." 

RED_ERROR_SECURITY_FAILED = "️ Security protocol failed. Invalid credentials provided."
RED_ERROR_ACCESS_RECOVERY = 'Restoration unavailable. Only operator KNOPA is eligible for access recovery.'


# ==========================================
# 🚨 ТЕЛЕМЕТРИЯ ОШИБОК (Красный текст системных сообщений)
# ==========================================
_RED_TELEMETRY_PREFIX = '> '
_RED_SYSTEM_LOCKED_PREFIX = f"{_RED_TELEMETRY_PREFIX}SYSTEM LOCKED. "
_RED_SECURITY_FAILED_PREFIX = f"{_RED_TELEMETRY_PREFIX}SECURITY PROTOCOL FAILED. "

RED_TELEMETRY_ACCESS_DENIED = f"{_RED_TELEMETRY_PREFIX}CASSANDRA: ACCESS DENIED. REDIRECTING..."
RED_TELEMETRY_DATA_CORRUPTED = f"{_RED_TELEMETRY_PREFIX}CASSANDRA: DATA CORRUPTED. REDIRECTING..."
RED_TELEMETRY_SYSTEM_FAILURE = f"{_RED_TELEMETRY_PREFIX}SYSTEM FAILURE. INVALID CREDENTIALS"

RED_TELEMETRY_CALLSIGN_AURORA_EXISTS = f"{_RED_SYSTEM_LOCKED_PREFIX}CALLSIGN 'AURORA' ALREADY EXISTS"
RED_TELEMETRY_CALLSIGN_KNOPA_EXISTS = f"{_RED_SYSTEM_LOCKED_PREFIX}CALLSIGN 'KNOPA' ALREADY EXISTS"
RED_TELEMETRY_CALLSIGN_ORION_EXISTS = f"{_RED_SYSTEM_LOCKED_PREFIX}CALLSIGN 'ORION' ALREADY EXISTS"

RED_TELEMETRY_ROLE_MISMATCH = f"{_RED_SYSTEM_LOCKED_PREFIX}ROLE MISMATCH DETECTED"
RED_TELEMETRY_UNKNOWN_USER = f"{_RED_SYSTEM_LOCKED_PREFIX}PLEASE ENTER CORRECT FULL NAME AND CALLSIGN"

RED_TELEMETRY_RESTORATION_ABORTED = f"{_RED_SECURITY_FAILED_PREFIX}RESTORATION ABORTED"
RED_TELEMETRY_SECURITY_INVALID = f"{_RED_SYSTEM_LOCKED_PREFIX}INVALID CREDENTIALS."
RED_TELEMETRY_OPERATOR_RESTORED = f"{_RED_SECURITY_FAILED_PREFIX}OPERATOR ALREADY RESTORED."




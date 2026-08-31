import json
from pathlib import Path

# ==========================================
# 📂 НАСТРОЙКА ПУТЕЙ И ЗАГРУЗКА ДАННЫХ
# ==========================================

PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
USERS_FILE = DATA_DIR / "users.json"

with open(USERS_FILE, "r", encoding="utf-8") as f:
    USERS = json.load(f)

# ==========================================
# 🌐 URL АДРЕСА (URL Addresses)
# ==========================================
LOGIN = "/login.html"
DASHBOARD_URL = "/dashboard.html"

# ==========================================
# 👤 ДАНННЫЕ ПОЛЬЗОВАТЕЛЕЙ (из JSON)
# ==========================================
AURORA_CALLSIGN = USERS["users"]["AURORA"]["callsign"]
AURORA_ACCESS_CODE = USERS["users"]["AURORA"]["access_code"]
ORION_CALLSIGN = USERS["users"]["ORION"]["callsign"]
ORION_ACCESS_CODE = USERS["users"]["ORION"]["access_code"]

# ==========================================
# 🎖️ РОЛИ И ИМЕНА (Как лежат в localStorage / users.json)
# ==========================================
ROLE_COMMANDER = "Commander"
ROLE_SPECIALIST = "Specialist"
NAME_AURORA = "Aurora"
NAME_ORION = "Orion"

# ==========================================
# 📏 ГРАНИЧНЫЕ ЗНАЧЕНИЯ (Boundary Values)
# ==========================================
CALLSIGN_TOO_SHORT_2_CHARS = "AB"
CALLSIGN_MIN_VALID_3_CHARS = "ABC"
ACCESS_CODE_TOO_SHORT_3_CHARS = "abc"
ACCESS_CODE_MIN_VALID_4_CHARS = "abcd"

# ==========================================
# 🚫 НЕВАЛИДНЫЕ И ВРЕДОНОСНЫЕ ДАННЫЕ (Invalid & Malicious Data)
# ==========================================
SQL_INJECTION_PAYLOAD = "' OR '1'='1"
WRONG_CALLSIGN = "WRONG"
WRONG_ACCESS_CODE = "WRONG_CODE"

# ==========================================
# 💬 ОЖИДАЕМЫЕ ТЕКСТЫ (Как отображаются в UI / Телеметрии)
# ==========================================
SUCCESS_TELEMETRY_TEXT_AURORA = "> CONNECTION ESTABLISHED. WELCOME, SPECIALIST AURORA"
SUCCESS_TELEMETRY_TEXT_ORION = "> CONNECTION ESTABLISHED. WELCOME, COMMANDER ORION"
DEFAULT_TEXT_TELEMETRY_BLUE = "> SYSTEM READY. AWAITING CONNECTION"

# ==========================================
# ⚠️  Тексты ошибок (Negative Scenarios)
# ==========================================
AUTH_ERROR_BLOCK_TEXT = "⚠️ Invalid callsign or access code"
ERROR_TEXT_TELEMETRY_RED = "> SYSTEM FAILURE. INVALID CREDENTIALS"



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
USER_ORION = USERS["users"]["ORION"]
USER_AURORA = USERS["users"]["AURORA"]

# ==========================================
# 🎖️ РОЛИ И ИМЕНА (Как лежат в localStorage / users.json)
# ==========================================
ROLE_COMMANDER = "COMMANDER"
ROLE_SPECIALIST = "SPECIALIST"
NAME_AURORA = "AURORA"
NAME_ORION = "ORION"

# ==========================================
# 💬 ОЖИДАЕМЫЕ ТЕКСТЫ (Как отображаются в UI / Телеметрии)
# ==========================================
# В tests/test_dashboard/data.py
TELEMETRY_ACCESS_DENIED_REDIRECT = "> CASSANDRA: ACCESS DENIED. REDIRECTING..."
TELEMETRY_DATA_CORRUPTED_REDIRECT = "> CASSANDRA: DATA CORRUPTED. REDIRECTING..."
TELEMETRY_SYSTEM_READY_AURORA = (
    "> CASSANDRA: AURORA, SYSTEM READY FOR WORK. AWAITING COMMANDS."
)
TELEMETRY_SYSTEM_READY_ORION = (
    "> CASSANDRA: ORION, SYSTEM READY FOR WORK. AWAITING COMMANDS."
)

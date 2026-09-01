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
LOGIN = '/login.html'
SIGNUP = '/signup.html'

# ==========================================
# 💬 ОЖИДАЕМЫЕ ТЕКСТЫ (Как отображаются в UI / Телеметрии)
# ==========================================
LOGO_CASSAN = 'CASSAN'
LOGO_DRA = 'DRA'
PROJECT_TITLE = 'PLANETARY HABITABILITY ASSESSMENT PROJECT'
PROJECT_SLOGAN = 'We Find a New Home Among the Stars'
COPYRIGHT_TEXT = 'Evknopia © 2026'







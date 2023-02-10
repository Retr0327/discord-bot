import os
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path("__file__").resolve().parent / ".env"
load_dotenv(ENV_PATH)

is_production = os.environ.get("PY_ENV") == "production"

TOKEN = os.environ.get("TOKEN")
GUILD = os.environ.get("GUILD")

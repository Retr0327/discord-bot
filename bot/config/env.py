import os
from pathlib import Path
from typing import Optional, Dict, Union
from dotenv import load_dotenv

ENV_PATH = Path("__file__").resolve().parent / ".env"
load_dotenv(ENV_PATH)

is_production = os.environ.get("PY_ENV") == 'production'

def get_env(field: Optional[str] = None) -> Union[Dict[str, str], str]:
    """The get_env function gets the environment variables."""
    env_dict = {
        "token": os.environ.get("TOKEN"),
        "guild": int(os.environ.get("GUILD")),
    }
    if field is None:
        return env_dict

    return env_dict[field]

from pathlib import Path

pkg_path = Path("__file__").resolve().parent
DB_DIR = pkg_path / "bot" / ".db"
DB_PATH = DB_DIR / "discord.db"


def make_db_dir() -> None:
    has_path = Path(DB_DIR).exists()
    if not has_path:
        return Path(DB_DIR).mkdir(parents=True, exist_ok=True)

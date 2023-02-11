import logging
from logging.handlers import RotatingFileHandler
from config import LOG_PATH, is_production
from .formatter import CustomFormatter

# --------------------------------------------------------------------
# handlers


def handle_console() -> logging.StreamHandler:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(CustomFormatter())
    return console_handler


def create_file_handler(log_path: str) -> RotatingFileHandler:
    config = {
        "filename": log_path,
        "encoding": "utf-8",
        "maxBytes": 32 * 1024 * 1024,
        "backupCount": 2,
    }
    log_handler = RotatingFileHandler(**config)
    log_handler.setFormatter(CustomFormatter())
    return log_handler


# --------------------------------------------------------------------
# public interface


def setup_logger(module_name: str) -> logging.Logger:
    library, _, _ = module_name.partition(".py")
    logger = logging.getLogger(library)
    logger.setLevel(logging.INFO)
    logger.addHandler(handle_console())
    if not is_production:
        logger.addHandler(create_file_handler(LOG_PATH))

    return logger

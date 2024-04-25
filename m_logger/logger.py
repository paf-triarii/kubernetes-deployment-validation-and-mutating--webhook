import logging
import os

# Global variable for log level
_global_log_level = os.environ.get("LOG_LEVEL", "INFO")


def get_custom_logger():
    """Gets a custom logger.

    Returns:
        Logger: The custom logger.
    """
    logger = logging.getLogger("PrettyLogger")
    logger.setLevel(_global_log_level)
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(_global_log_level)
        formatter = logging.Formatter(
            "%(levelname)s - %(asctime)s - %(message)s", "%Y-%m-%d %H:%M:%S"
        )
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger
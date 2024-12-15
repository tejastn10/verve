import os
import sys

from loguru import logger


class Logger:
    def __init__(
        self,
        log_file="logs/production.log",
        rotation="1 MB",
        retention="7 days",
        level="DEBUG",
    ) -> None:
        # Create the log directory if it doesn't exists
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Remove the default logger to avoid duplicate logs
        logger.remove()

        # Add the log file with rotation and retention
        logger.add(
            log_file,
            rotation=rotation,
            retention=retention,
            level=level,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {message}",
        )

        # Add console output for the logs
        logger.add(
            sys.stdout,
            level=level,
            format=(
                "<green>{time:YYYY-MM-DD HH:mm:ss}</green> "
                "| <level>{level:<8}</level> | {message}"
            ),
            colorize=True,
        )

    @staticmethod
    def info(message: str) -> None:
        logger.info(message)

    @staticmethod
    def debug(message: str) -> None:
        logger.debug(message)

    @staticmethod
    def warning(message: str) -> None:
        logger.warning(message)

    @staticmethod
    def error(message: str) -> None:
        logger.error(message)

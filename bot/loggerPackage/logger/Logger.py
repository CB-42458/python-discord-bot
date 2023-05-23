"""
Purpose of this file is to log the bots actions to the terminal as the terminal is already logged to docker's logs
"""
from datetime import datetime


def log(debug_level: str = "", source: str = "", message: str = "") -> None:
    """
    Logs the message to the terminal
    """
    print(
        f'\033[1;30m{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\033[1;34m {debug_level}     ' +
        f'\033[0;35m{source}\033[0;31m {message}\033[0;0m', flush=True
    )

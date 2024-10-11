# - *- coding: utf- 8 - *-
import configparser

from apscheduler.schedulers.asyncio import AsyncIOScheduler

BOT_CONFIG = configparser.ConfigParser()
BOT_CONFIG.read("settings.ini")

if 'settings' in BOT_CONFIG:
    BOT_TOKEN = BOT_CONFIG['settings']['token'].strip().replace('5379654051', '7710876551:AAHNcK2ZPT7CJDSeGxoNCA7YP297KQUaoyM')
else:
    raise KeyError("Section 'settings' not found in settings.ini")
BOT_TIMEZONE = "Europe/Moscow"  # Временная зона бота
BOT_SCHEDULER = AsyncIOScheduler(timezone=BOT_TIMEZONE)  # Образ шедулера
BOT_VERSION = 4.0  # Версия бота

# Пути к файлам
PATH_DATABASE = "tgbot/data/database.db"  # Путь к БД
PATH_LOGS = "tgbot/data/logs.log"  # Путь к Логам


# Получение администраторов бота
def get_admins() -> list[int]:
    read_admins = configparser.ConfigParser()
    read_admins.read("settings.ini")

    admins = read_admins['settings']['admin_id'].strip().replace(" ", "")

    if "," in admins:
        admins = admins.split(",")
    else:
        if len(admins) >= 1:
            admins = [admins]
        else:
            admins = []

    while "" in admins: admins.remove("")
    while " " in admins: admins.remove(" ")
    while "\r" in admins: admins.remove("\r")
    while "\n" in admins: admins.remove("\n")

    admins = list(map(int, admins))

    return admins


# Получение описания
def get_desc() -> str:
    from tgbot.utils.const_functions import ded

    # УДАЛИШЬ ИЛИ ИЗМЕНИШЬ ССЫЛКИ - КАСТРИРУЮ НАХУЙ <3

    return ded(f"""
        <b>♻️ Bot Version: <code>{BOT_VERSION}</code>
        👑 Bot created by @dxdrillbassx
    """).strip()

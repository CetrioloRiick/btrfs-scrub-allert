#!/usr/bin/python
import subprocess
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

config_path = Path("/etc/btrfs-telegram-notifier/config.env")

if config_path.exists():
    load_dotenv(dotenv_path=config_path)
else:
    print(f"Config file not found at {config_path}")
    exit(1)

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
MOUNT_POINT = os.getenv("DISK")


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Errore nell'invio del messaggio Telegram: {e}")


def check_scrub():
    try:
        result = subprocess.run(
            ["btrfs", "scrub", "status", MOUNT_POINT],
            capture_output=True,
            text=True,
            check=True,
        )

        output = result.stdout

        if "no errors found" not in output.lower():
            msg = (
                f"⚠️ <b>BTRFS ALERT</b> ⚠️\n\n"
                f"<b>Mount Point:</b> <code>{MOUNT_POINT}</code>\n"
                f"<b>Status:</b> Integrity issues detected during scrub.\n\n"
                f"<b>Technical Details:</b>\n"
                f"<pre>{output.strip()}</pre>"
            )
            send_telegram_message(msg)

    except subprocess.CalledProcessError as e:
        error_msg = (
            f"❌ <b>BTRFS MONITORING ERROR</b> ❌\n\n"
            f"<b>Mount Point:</b> <code>{MOUNT_POINT}</code>\n"
            f"<b>Error:</b> Failed to execute scrub command.\n"
            f"<b>Details:</b> <pre>{e.stderr.strip()}</pre>"
        )
        send_telegram_message(error_msg)


if __name__ == "__main__":
    if not all([os.getenv("TELEGRAM_TOKEN"), CHAT_ID, MOUNT_POINT]):
        print("Error: Missing required environment variables.")
    else:
        check_scrub()

import enum
from typing import List
import subprocess


class AdbAction(enum.Enum):
    # list devices
    LIST_DEVICES = "devices"
    LIST_DEVICES_LONG = "devices -l"

    # airplane mode
    AIRPLANE_STATUS = "shell cmd connectivity airplane-mode"
    AIRPLANE_ENABLE = "shell cmd connectivity airplane-mode enable"
    AIRPLANE_DISABLE = "shell cmd connectivity airplane-mode disable"

    # screen
    SCREEN_WAKE = "shell input keyevent KEYCODE_WAKEUP"
    SCREEN_POWER = "shell input keyevent KEYCODE_POWER"
    SCREEN_HOME = "shell input keyevent KEYCODE_HOME"

    # wifi
    WIFI_ENABLE = "shell svc wifi enable"
    WIFI_DISABLE = "shell svc wifi disable"

    # notifications
    NOTIFICATION_LIST = "shell cmd notification list"

    # send message
    # TODO


def run_adb(
    action: AdbAction, extra_args: List[str] | None = None
) -> subprocess.CompletedProcess:
    cmd = ["adb"] + action.value.split()
    if extra_args:
        cmd.extend(extra_args)

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True,
    )
    return result

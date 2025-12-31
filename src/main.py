import subprocess
from available_commands import run_adb, AdbAction

if __name__ == "__main__":
    try:
        # basic list devices
        print(run_adb(AdbAction.LIST_DEVICES).stdout)

        # detailed list devices
        print(run_adb(AdbAction.LIST_DEVICES_LONG).stdout)

        # check airplane mode status
        res = run_adb(AdbAction.AIRPLANE_STATUS)
        print("Airplane status:\n", res.stdout)

        # enable airplane mode
        run_adb(AdbAction.AIRPLANE_ENABLE)

        # wake screen
        run_adb(AdbAction.SCREEN_WAKE)

        # turn Wi‑Fi off
        run_adb(AdbAction.WIFI_DISABLE)

        # list notifications
        res = run_adb(AdbAction.NOTIFICATION_LIST)
        print("Notifications:\n", res.stdout)

    except subprocess.CalledProcessError as e:
        print("ADB command failed with code", e.returncode)
        print("Stdout:", e.stdout)
        print("Stderr:", e.stderr)

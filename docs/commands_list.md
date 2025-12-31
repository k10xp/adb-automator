# Adb commands list

Assume latest AOSP android version (16 as of writing).

## Airplane mode

```bash
# check status
adb shell cmd connectivity airplane-mode

# enable
adb shell cmd connectivity airplane-mode enable

# disable
adb shell cmd connectivity airplane-mode disable
```

## Screen on / off

```bash
# wake screen if off
adb shell input keyevent KEYCODE_WAKEUP

# turn screen off (same as pressing power)
adb shell input keyevent KEYCODE_POWER

# go to home (unlock if no secure lock)
adb shell input keyevent KEYCODE_HOME
```

## Toggle Wi‑Fi

```bash
# enable Wi‑Fi
adb shell svc wifi enable

# disable Wi‑Fi
adb shell svc wifi disable
```

## Post a notification

```bash
# list notifications
adb shell cmd notification list
```

## Send SMS via ADB

## Sources

- https://developer.android.com/tools/adb
- https://mattintech.github.io/tools/adb-cmd/

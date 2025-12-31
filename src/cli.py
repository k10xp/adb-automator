import argparse
from available_commands import AdbAction


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Thin CLI wrapper around adb using predefined actions."
    )

    # required positional = which predefined action
    parser.add_argument(
        "action",
        choices=[a.name.lower() for a in AdbAction],
        help="Action to execute (one of: %(choices)s)",
    )

    # everything after action
    parser.add_argument(
        "extra",
        nargs="*",
        help="Extra arguments passed after the action (e.g. serial with -s, etc.)",
    )

    # explicit optional for device serial
    parser.add_argument(
        "-s",
        "--serial",
        help="Target device serial (equivalent to `adb -s SERIAL ...`).",
    )

    return parser.parse_args()

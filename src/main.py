import subprocess
from typing import List

from cli import parse_args
from available_commands import run_adb, AdbAction


def main() -> None:
    args = parse_args()

    action = AdbAction[args.action.upper()]
    extra: List[str] = []

    if args.serial:
        extra.extend(["-s", args.serial])

    if args.extra:
        extra.extend(args.extra)

    try:
        result = run_adb(action, extra_args=extra if extra else None)
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="")
    except subprocess.CalledProcessError as e:
        print(f"ADB command failed with code {e.returncode}")
        if e.stdout:
            print("Stdout:\n", e.stdout)
        if e.stderr:
            print("Stderr:\n", e.stderr)


if __name__ == "__main__":
    main()

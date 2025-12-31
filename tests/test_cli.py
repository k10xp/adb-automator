import argparse
import sys
import pytest

from cli import parse_args


def test_parse_valid_action(monkeypatch):
    monkeypatch.setenv("PYTHONWARNINGS", "ignore")
    test_argv = ["prog", "list_devices"]
    monkeypatch.setattr(sys, "argv", test_argv)

    args = parse_args()
    assert isinstance(args, argparse.Namespace)
    assert args.action == "list_devices"
    assert args.extra == []
    assert args.serial is None


def test_parse_with_serial(monkeypatch):
    test_argv = ["prog", "screen_wake", "-s", "emulator-5554"]
    monkeypatch.setattr(sys, "argv", test_argv)

    args = parse_args()
    assert args.action == "screen_wake"
    assert args.extra == []
    assert args.serial == "emulator-5554"


def test_invalid_action_exits(monkeypatch):
    test_argv = ["prog", "non_existing_action"]
    monkeypatch.setattr(sys, "argv", test_argv)

    with pytest.raises(SystemExit) as excinfo:
        parse_args()

    assert excinfo.value.code == 2  # argparse parse error

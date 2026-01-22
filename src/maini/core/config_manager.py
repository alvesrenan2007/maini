import sys
import os
import tomllib
from pathlib import Path


def get_config_path():
    """Gets the path for the configuration file, according to XDG Standards
    Following the XDG Base Directory Specification (https://specifications.freedesktop.org/basedir/latest/), this function creates the configuration file for 'maini' at $XDG_CONFIG_HOME if it does not already exists.
    Returns:
        pathlib.Path object
    """

    xdg_config_home = os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
    config_dir = Path(xdg_config_home) / "maini"
    config_file = config_dir / "config.toml"

    if not config_dir.exists():
        config_dir.mkdir(parents=True, exist_ok=True)
        print(f"Config directory created at {config_dir}")

    if not config_file.exists():
        with open(config_file, "w") as file:
            data_to_write = '[general]\nbase_currency = "BRL"\n'
            file.write(data_to_write)
            print(f"Config file created at {config_file}")

    return config_file


def load():
    """Reads the TOML config file and returns it as a dictionary"""
    config = get_config_path()
    with open(config, "rb") as file:
        return tomllib.load(file)


def get_target_currency():
    """Gets the target currency defined by the user
    The target currency is the currency used to evaluate all transactions, so that they are all in the same currency
    Returns:
        string target_currency - 3-characters currency codes defined on ISO 4217
    """
    config_data = load()

    fix_command = "maini set target_currency <currency code>"
    if "general" not in config_data:
        print_config_error("Missing [general] section", fix_command)
        sys.exit(1)

    target_currency = config_data["general"].get("target_currency")

    if not target_currency:
        print_config_error("target_currency is not defined", fix_command)
        sys.exit(1)

    return target_currency


def print_config_error(reason, fix_command):
    """Helper to print errors related to the config file"""
    print(f"\n[ERROR] {reason} in configuration")
    print(f"Please run: {fix_command}")

import argparse

from repohelper import __version__
from repohelper.constants import APP_NAME
from repohelper.generator import create_project_placeholder
from repohelper.profiles import get_profiles
from repohelper.utils import print_header, print_kv
from repohelper.validators import (
    validate_profile_name,
    validate_project_name,
    validate_project_target,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=APP_NAME,
        description="Create clean small repos with a few practical defaults.",
    )

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("profiles", help="List available project profiles.")
    subparsers.add_parser("about", help="Show tool information.")

    check_name_parser = subparsers.add_parser(
        "check-name",
        help="Check whether a project name looks valid.",
    )
    check_name_parser.add_argument("project_name", help="Project name to validate.")

    create_parser = subparsers.add_parser(
        "create",
        help="Create a new project from a profile.",
    )
    create_parser.add_argument("project_name", help="Name of the new project.")
    create_parser.add_argument(
        "--profile",
        required=True,
        help="Profile to use for project setup.",
    )
    create_parser.add_argument(
        "--path",
        default=".",
        help="Target parent directory. Defaults to current directory.",
    )
    create_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without writing files.",
    )
    create_parser.add_argument(
        "--force",
        action="store_true",
        help="Allow overwrite if target folder already exists.",
    )

    return parser


def handle_profiles() -> None:
    print_header("Available profiles")
    for name, description in get_profiles().items():
        print(f"- {name}: {description}")


def handle_about() -> None:
    print_header("About repohelper")
    print_kv("Version", __version__)
    print_kv("Purpose", "Set up clean small repos with a few useful defaults.")


def handle_check_name(project_name: str) -> None:
    is_valid, message = validate_project_name(project_name)

    print_header("Project name check")
    print_kv("Name", project_name)
    print_kv("Valid", "yes" if is_valid else "no")
    print_kv("Message", message)


def handle_create(args: argparse.Namespace) -> None:
    print_header("Create project")
    print_kv("Project", args.project_name)
    print_kv("Profile", args.profile)
    print_kv("Path", args.path)
    print_kv("Dry run", "yes" if args.dry_run else "no")
    print_kv("Force", "yes" if args.force else "no")

    name_ok, name_message = validate_project_name(args.project_name)
    if not name_ok:
        print_kv("Status", "failed")
        print_kv("Reason", name_message)
        return

    profile_ok, profile_message = validate_profile_name(args.profile)
    if not profile_ok:
        print_kv("Status", "failed")
        print_kv("Reason", profile_message)
        return

    target_ok, target_message, project_path = validate_project_target(
        project_name=args.project_name,
        path_value=args.path,
        force=args.force,
    )
    if not target_ok or project_path is None:
        print_kv("Status", "failed")
        print_kv("Reason", target_message)
        return

    print_kv("Status", "ready")
    print_kv("Target", str(project_path))

    create_project_placeholder(
        project_name=args.project_name,
        profile_name=args.profile,
        project_path=project_path,
        dry_run=args.dry_run,
    )


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "profiles":
        handle_profiles()
    elif args.command == "about":
        handle_about()
    elif args.command == "check-name":
        handle_check_name(args.project_name)
    elif args.command == "create":
        handle_create(args)
    else:
        parser.print_help()
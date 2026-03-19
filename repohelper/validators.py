from pathlib import Path
import re

from repohelper.constants import AVAILABLE_PROFILES


def validate_project_name(name: str) -> tuple[bool, str]:
    cleaned_name = name.strip()

    if not cleaned_name:
        return False, "Project name cannot be empty."

    if len(cleaned_name) < 2:
        return False, "Project name is too short."

    if len(cleaned_name) > 50:
        return False, "Project name is too long."

    if cleaned_name.startswith("-") or cleaned_name.endswith("-"):
        return False, "Project name cannot start or end with a dash."

    if cleaned_name.startswith("_") or cleaned_name.endswith("_"):
        return False, "Project name cannot start or end with an underscore."

    if not re.fullmatch(r"[a-zA-Z0-9_-]+", cleaned_name):
        return False, "Use only letters, numbers, dashes, and underscores."

    return True, "Name format looks valid."


def validate_profile_name(profile_name: str) -> tuple[bool, str]:
    if profile_name not in AVAILABLE_PROFILES:
        return False, f"Unknown profile: {profile_name}"

    return True, "Profile looks valid."


def validate_target_parent(path_value: str) -> tuple[bool, str, Path | None]:
    target_parent = Path(path_value).expanduser().resolve()

    if not target_parent.exists():
        return False, "Target path does not exist.", None

    if not target_parent.is_dir():
        return False, "Target path is not a directory.", None

    return True, "Target path looks valid.", target_parent


def validate_project_target(
    project_name: str,
    path_value: str,
    force: bool,
) -> tuple[bool, str, Path | None]:
    path_ok, path_message, target_parent = validate_target_parent(path_value)

    if not path_ok or target_parent is None:
        return False, path_message, None

    project_path = target_parent / project_name

    if project_path.exists() and not force:
        return (
            False,
            f"Target folder already exists: {project_path}",
            project_path,
        )

    return True, "Target location looks valid.", project_path
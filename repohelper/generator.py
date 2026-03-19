from pathlib import Path

from repohelper.profiles import build_profile_structure


def create_project_placeholder(
    project_name: str,
    profile_name: str,
    project_path: Path,
    dry_run: bool,
) -> None:
    structure = build_profile_structure(profile_name, project_name)

    action_label = "Dry run preview" if dry_run else "Planned output"

    print(f"\n{action_label}")
    print("-" * len(action_label))
    print(f"Project folder: {project_path}")

    print("\nDirectories:")
    for directory in structure["directories"]:
        print(f"- {project_path / directory}")

    print("\nFiles:")
    for file_entry in structure["files"]:
        print(f"- {project_path / file_entry['path']}")
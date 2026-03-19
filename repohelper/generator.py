from pathlib import Path


def create_project_placeholder(
    project_name: str,
    profile_name: str,
    project_path: Path,
    dry_run: bool,
) -> None:
    action_label = "Would create" if dry_run else "Would generate"

    print(
        f"[placeholder] {action_label} project '{project_name}' "
        f"with profile '{profile_name}' at '{project_path}'."
    )
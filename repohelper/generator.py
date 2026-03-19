from pathlib import Path

from repohelper.profiles import build_profile_structure


def create_project(
    project_name: str,
    profile_name: str,
    project_path: Path,
    dry_run: bool,
    force: bool,
) -> None:
    structure = build_profile_structure(profile_name, project_name)

    if dry_run:
        print("\nDry run preview")
        print("---------------")
        print(f"Project folder: {project_path}")

        print("\nDirectories:")
        for directory in structure["directories"]:
            print(f"- {project_path / directory}")

        print("\nFiles:")
        for file_entry in structure["files"]:
            print(f"- {project_path / file_entry['path']}")
        return

    created_directories: list[Path] = []
    created_files: list[Path] = []
    overwritten_files: list[Path] = []

    project_path.mkdir(parents=True, exist_ok=True)

    for directory in structure["directories"]:
        full_directory_path = project_path / directory
        if not full_directory_path.exists():
            full_directory_path.mkdir(parents=True, exist_ok=True)
            created_directories.append(full_directory_path)

    for file_entry in structure["files"]:
        full_file_path = project_path / file_entry["path"]
        file_content = file_entry["content"]

        full_file_path.parent.mkdir(parents=True, exist_ok=True)

        if full_file_path.exists():
            if force:
                full_file_path.write_text(file_content, encoding="utf-8")
                overwritten_files.append(full_file_path)
            else:
                continue
        else:
            full_file_path.write_text(file_content, encoding="utf-8")
            created_files.append(full_file_path)

    print("\nProject created")
    print("---------------")
    print(f"Location: {project_path}")

    print("\nCreated directories:")
    if created_directories:
        for directory in created_directories:
            print(f"- {directory}")
    else:
        print("- none")

    print("\nCreated files:")
    if created_files:
        for file_path in created_files:
            print(f"- {file_path}")
    else:
        print("- none")

    print("\nOverwritten files:")
    if overwritten_files:
        for file_path in overwritten_files:
            print(f"- {file_path}")
    else:
        print("- none")
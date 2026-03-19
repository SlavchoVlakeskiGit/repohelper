from pathlib import Path

from repohelper.profiles import build_profile_structure, get_profiles


def test_profiles_list_contains_expected_profiles() -> None:
    profiles = get_profiles()

    assert "python-tool" in profiles
    assert "python-app" in profiles
    assert "java-console" in profiles


def test_python_tool_profile_contains_expected_entries() -> None:
    structure = build_profile_structure("python-tool", "sample-tool")

    directories = structure["directories"]
    files = structure["files"]

    assert len(directories) == 3
    assert any(directory == Path("src") for directory in directories)
    assert any(file_entry["path"] == Path("README.md") for file_entry in files)
    assert any(file_entry["path"] == Path(".env.example") for file_entry in files)
    assert any(file_entry["path"] == Path("pyproject.toml") for file_entry in files)


def test_java_console_profile_contains_main_java() -> None:
    structure = build_profile_structure("java-console", "java-practice")
    files = structure["files"]

    assert any(file_entry["path"] == Path("src") / "Main.java" for file_entry in files)
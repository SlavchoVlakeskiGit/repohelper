from pathlib import Path
import tempfile

from repohelper.validators import (
    validate_profile_name,
    validate_project_name,
    validate_project_target,
)


def test_valid_project_name() -> None:
    is_valid, message = validate_project_name("sample-tool")
    assert is_valid is True
    assert message == "Name format looks valid."


def test_empty_project_name_is_rejected() -> None:
    is_valid, message = validate_project_name("")
    assert is_valid is False
    assert message == "Project name cannot be empty."


def test_invalid_project_name_characters_are_rejected() -> None:
    is_valid, message = validate_project_name("bad/project")
    assert is_valid is False
    assert message == "Use only letters, numbers, dashes, and underscores."


def test_valid_profile_name() -> None:
    is_valid, message = validate_profile_name("python-tool")
    assert is_valid is True
    assert message == "Profile looks valid."


def test_unknown_profile_name_is_rejected() -> None:
    is_valid, message = validate_profile_name("wrong-profile")
    assert is_valid is False
    assert message == "Unknown profile: wrong-profile"


def test_project_target_is_valid_when_folder_does_not_exist() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        is_valid, message, project_path = validate_project_target(
            project_name="sample-tool",
            path_value=temp_dir,
            force=False,
        )

        assert is_valid is True
        assert message == "Target location looks valid."
        assert project_path == Path(temp_dir).resolve() / "sample-tool"
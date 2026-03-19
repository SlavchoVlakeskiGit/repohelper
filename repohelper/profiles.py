from pathlib import Path


def _module_name(project_name: str) -> str:
    return project_name.replace("-", "_")


def get_profiles() -> dict[str, str]:
    return {
        "python-tool": "Small Python utility or CLI repo",
        "python-app": "Small Python app repo with src and tests",
        "java-console": "Small Java console project",
    }


def build_profile_structure(profile_name: str, project_name: str) -> dict[str, list]:
    module_name = _module_name(project_name)

    if profile_name == "python-tool":
        return {
            "directories": [
                Path("src"),
                Path("src") / module_name,
                Path("tests"),
            ],
            "files": [
                {
                    "path": Path("README.md"),
                    "content": build_generated_readme(project_name, profile_name),
                },
                {
                    "path": Path(".gitignore"),
                    "content": build_python_gitignore(),
                },
                {
                    "path": Path(".env.example"),
                    "content": "EXAMPLE_VALUE=\n",
                },
                {
                    "path": Path("pyproject.toml"),
                    "content": build_python_tool_pyproject(project_name, module_name),
                },
                {
                    "path": Path("src") / module_name / "__init__.py",
                    "content": "",
                },
                {
                    "path": Path("src") / module_name / "main.py",
                    "content": build_python_tool_main(project_name),
                },
                {
                    "path": Path("tests") / "test_main.py",
                    "content": build_python_test_file(),
                },
            ],
        }

    if profile_name == "python-app":
        return {
            "directories": [
                Path("src"),
                Path("src") / module_name,
                Path("tests"),
            ],
            "files": [
                {
                    "path": Path("README.md"),
                    "content": build_generated_readme(project_name, profile_name),
                },
                {
                    "path": Path(".gitignore"),
                    "content": build_python_gitignore(),
                },
                {
                    "path": Path("pyproject.toml"),
                    "content": build_python_app_pyproject(project_name, module_name),
                },
                {
                    "path": Path("src") / module_name / "__init__.py",
                    "content": "",
                },
                {
                    "path": Path("src") / module_name / "app.py",
                    "content": build_python_app_file(project_name),
                },
                {
                    "path": Path("tests") / "test_app.py",
                    "content": build_python_test_file(),
                },
            ],
        }

    if profile_name == "java-console":
        return {
            "directories": [
                Path("src"),
                Path("docs"),
            ],
            "files": [
                {
                    "path": Path("README.md"),
                    "content": build_generated_readme(project_name, profile_name),
                },
                {
                    "path": Path(".gitignore"),
                    "content": build_java_gitignore(),
                },
                {
                    "path": Path("src") / "Main.java",
                    "content": build_java_main_file(project_name),
                },
                {
                    "path": Path("docs") / "notes.md",
                    "content": build_java_notes_file(),
                },
            ],
        }

    raise ValueError(f"Unknown profile: {profile_name}")


def build_generated_readme(project_name: str, profile_name: str) -> str:
    return f"""# {project_name}

Small starter repo created with repohelper.

## Profile

`{profile_name}`

## Notes

This is just a clean starting point.
Update this README once the real project takes shape.
"""


def build_python_gitignore() -> str:
    return """__pycache__/
*.pyc
.venv/
venv/
env/
dist/
build/
*.egg-info/
.pytest_cache/
"""


def build_java_gitignore() -> str:
    return """out/
*.class
.idea/
.vscode/
"""


def build_python_tool_pyproject(project_name: str, module_name: str) -> str:
    return f"""[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name}"
version = "0.1.0"
description = "Small Python tool project"
readme = "README.md"
requires-python = ">=3.10"

[project.scripts]
{module_name} = "{module_name}.main:main"
"""


def build_python_app_pyproject(project_name: str, module_name: str) -> str:
    return f"""[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name}"
version = "0.1.0"
description = "Small Python app project"
readme = "README.md"
requires-python = ">=3.10"
"""


def build_python_tool_main(project_name: str) -> str:
    return f'''def main() -> None:
    print("Starting {project_name}...")


if __name__ == "__main__":
    main()
'''


def build_python_app_file(project_name: str) -> str:
    return f'''def run() -> None:
    print("{project_name} is ready to build on.")
'''


def build_python_test_file() -> str:
    return '''def test_placeholder() -> None:
    assert True
'''


def build_java_main_file(project_name: str) -> str:
    return f'''public class Main {{
    public static void main(String[] args) {{
        System.out.println("Starting {project_name}...");
    }}
}}
'''


def build_java_notes_file() -> str:
    return """# Notes

Use this file for setup notes, ideas, or small reminders while building.
"""
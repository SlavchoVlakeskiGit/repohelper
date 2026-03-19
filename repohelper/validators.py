def validate_project_name(name: str) -> tuple[bool, str]:
    cleaned_name = name.strip()

    if not cleaned_name:
        return False, "Project name cannot be empty."

    return True, "Name format looks valid."
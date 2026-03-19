def print_header(title: str) -> None:
    print(f"\n{title}")
    print("-" * len(title))


def print_kv(label: str, value: str) -> None:
    print(f"{label}: {value}")
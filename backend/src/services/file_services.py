from pathlib import Path


def get_static_file_routes() -> list[str]:
    """Get all file names in the static directory recursively."""
    static_dir = Path("static")

    if not static_dir.exists():
        return []

    return [
        f"/{file_path.relative_to(static_dir)}" for file_path in static_dir.iterdir()
    ]

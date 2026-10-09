"""JSON persistence for ticket collections."""

import json
from pathlib import Path

DEFAULT_STORAGE_PATH = Path("data/tickets.json")


def save_tickets(tickets, filepath=DEFAULT_STORAGE_PATH):
    """Write tickets as JSON, using a temporary file to avoid partial writes."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_suffix(path.suffix + ".tmp")
    try:
        temporary_path.write_text(json.dumps(tickets, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        temporary_path.replace(path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()
    return path


def load_tickets(filepath=DEFAULT_STORAGE_PATH):
    """Load tickets from JSON. A missing file is treated as an empty collection."""
    path = Path(filepath)
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Ticket file contains invalid JSON: {path}") from exc
    except OSError as exc:
        raise ValueError(f"Could not read ticket file: {path}") from exc
    if not isinstance(data, list):
        raise ValueError("Ticket file must contain a JSON list.")
    for index, ticket in enumerate(data):
        if not isinstance(ticket, dict) or not isinstance(ticket.get("id"), str):
            raise ValueError(f"Ticket at position {index} must be an object with a string ID.")
    return data

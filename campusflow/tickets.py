ALLOWED_CATEGORIES = {"Network", "Hardware", "Software", "Other"}
ALLOWED_URGENCIES = {"low", "medium", "high"}


def validate_ticket_details(title, category, urgency, affected_users):
    """Validate ticket details and return normalized values."""

    if not isinstance(title, str) or not title.strip():
        raise ValueError("Ticket title cannot be blank.")

    if not isinstance(category, str):
        raise ValueError("Category must be Network, Hardware, Software, or Other.")

    category = category.strip().capitalize()

    if category not in ALLOWED_CATEGORIES:
        raise ValueError(
            "Invalid category. Choose Network, Hardware, Software, or Other."
        )

    if not isinstance(urgency, str):
        raise ValueError("Urgency must be low, medium, or high.")

    urgency = urgency.strip().lower()

    if urgency not in ALLOWED_URGENCIES:
        raise ValueError("Invalid urgency. Choose low, medium, or high.")

    if type(affected_users) is not int or affected_users <= 0:
        raise ValueError("Affected users must be a positive integer.")

    return title.strip(), category, urgency, affected_users


def calculate_priority(urgency, affected_users):
    """Calculate priority using the required rule order."""

    if urgency not in ALLOWED_URGENCIES:
        raise ValueError("Urgency must be low, medium, or high.")

    if type(affected_users) is not int or affected_users <= 0:
        raise ValueError("Affected users must be a positive integer.")

    if urgency == "high" and affected_users >= 10:
        return "critical"

    if urgency == "high" or affected_users >= 10:
        return "high"

    if urgency == "medium" or affected_users >= 3:
        return "medium"

    return "low"


def generate_ticket_id(tickets):
    """Generate a unique ID based on existing ticket IDs."""

    highest_id = 0

    for ticket in tickets:
        ticket_id = ticket.get("id", "")

        if (
            isinstance(ticket_id, str)
            and ticket_id.startswith("T")
            and ticket_id[1:].isdigit()
        ):
            number = int(ticket_id[1:])
            highest_id = max(highest_id, number)

    return f"T{highest_id + 1:03d}"


def create_ticket(tickets, title, category, urgency, affected_users):
    """Validate details, create a ticket, and add it to the collection."""

    title, category, urgency, affected_users = validate_ticket_details(
        title, category, urgency, affected_users
    )

    ticket = {
        "id": generate_ticket_id(tickets),
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": calculate_priority(urgency, affected_users),
        "status": "open",
        "assigned_to": None,
    }

    tickets.append(ticket)

    return ticket
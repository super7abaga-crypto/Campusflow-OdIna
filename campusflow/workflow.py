"""Operations for finding, assigning, and updating tickets."""

ALLOWED_STATUSES = {"open", "in_progress", "resolved", "closed"}


def find_ticket(tickets, ticket_id):
    """Return a ticket by ID, ignoring ID letter case."""
    if not isinstance(ticket_id, str) or not ticket_id.strip():
        raise ValueError("Please provide a ticket ID.")
    wanted = ticket_id.strip().upper()
    for ticket in tickets:
        if isinstance(ticket, dict) and str(ticket.get("id", "")).upper() == wanted:
            return ticket
    raise ValueError(f"Ticket {wanted} was not found.")


def assign_ticket(tickets, ticket_id, assignee):
    """Assign an open or in-progress ticket to a named person."""
    if not isinstance(assignee, str) or not assignee.strip():
        raise ValueError("Assignee name cannot be blank.")
    ticket = find_ticket(tickets, ticket_id)
    if ticket.get("status") in {"resolved", "closed"}:
        raise ValueError("A resolved or closed ticket cannot be assigned.")
    ticket["assigned_to"] = assignee.strip()
    return ticket


def update_ticket_status(tickets, ticket_id, status):
    """Update a ticket to one of the supported statuses."""
    if not isinstance(status, str):
        raise ValueError("Invalid status. Choose open, in_progress, resolved, or closed.")
    status = status.strip().lower()
    if status not in ALLOWED_STATUSES:
        raise ValueError("Invalid status. Choose open, in_progress, resolved, or closed.")
    ticket = find_ticket(tickets, ticket_id)
    ticket["status"] = status
    return ticket

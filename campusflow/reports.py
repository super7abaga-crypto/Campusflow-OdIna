"""Summary and display helpers for ticket collections."""


def summarize_tickets(tickets):
    """Return totals grouped by status, priority, and category."""
    report = {
        "total": len(tickets),
        "by_status": {},
        "by_priority": {},
        "by_category": {},
        "unassigned": 0,
    }
    for ticket in tickets:
        for key, field in (("by_status", "status"), ("by_priority", "priority"), ("by_category", "category")):
            value = ticket.get(field, "unknown")
            report[key][value] = report[key].get(value, 0) + 1
        if not ticket.get("assigned_to"):
            report["unassigned"] += 1
    return report


def format_ticket(ticket):
    """Format a ticket as a readable single-line summary."""
    assignee = ticket.get("assigned_to") or "Unassigned"
    return (
        f"{ticket.get('id', '?')} | {ticket.get('title', '(no title)')} | "
        f"{ticket.get('category', '?')} | urgency: {ticket.get('urgency', '?')} | "
        f"priority: {ticket.get('priority', '?')} | status: {ticket.get('status', '?')} | "
        f"affected users: {ticket.get('affected_users', '?')} | assigned to: {assignee}"
    )


def format_report(tickets):
    """Return a human-readable summary report."""
    report = summarize_tickets(tickets)
    lines = [f"Ticket report — {report['total']} total ticket(s)"]
    for title, key in (("By status", "by_status"), ("By priority", "by_priority"), ("By category", "by_category")):
        lines.append(f"{title}:")
        if report[key]:
            lines.extend(f"  - {name}: {count}" for name, count in sorted(report[key].items()))
        else:
            lines.append("  - None")
    lines.append(f"Unassigned tickets: {report['unassigned']}")
    return "\n".join(lines)

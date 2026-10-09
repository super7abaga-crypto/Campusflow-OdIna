"""Interactive command-line interface for Campusflow-OdIna."""

from campusflow.reports import format_report, format_ticket
from campusflow.storage import DEFAULT_STORAGE_PATH, load_tickets, save_tickets
from campusflow.tickets import create_ticket
from campusflow.workflow import assign_ticket, update_ticket_status


def ask_positive_integer(prompt):
    """Prompt until the user enters a positive whole number."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a whole number, such as 1 or 12.")
            continue
        if value <= 0:
            print("The number must be greater than zero.")
            continue
        return value


def show_tickets(tickets):
    if not tickets:
        print("No tickets have been created yet.")
        return
    for ticket in tickets:
        print(format_ticket(ticket))


def create_ticket_from_prompt(tickets):
    title = input("Ticket title: ")
    category = input("Category (Network/Hardware/Software/Other): ")
    urgency = input("Urgency (low/medium/high): ")
    affected_users = ask_positive_integer("Number of affected users: ")
    try:
        ticket = create_ticket(tickets, title, category, urgency, affected_users)
    except ValueError as exc:
        print(f"Could not create ticket: {exc}")
        return
    print("Ticket created:")
    print(format_ticket(ticket))


def print_menu():
    print("\n=== OdIna-Campusflow Ticket Manager ===")
    print("1. Create a ticket")
    print("2. List tickets")
    print("3. Assign a ticket")
    print("4. Update ticket status")
    print("5. Show report")
    print("6. Save tickets")
    print("7. Reload tickets from disk")
    print("0. Save and exit")


def main():
    try:
        tickets = load_tickets()
    except ValueError as exc:
        print(f"Could not load saved tickets: {exc}")
        print("Fix the data file before starting so saved data is not overwritten.")
        return
    print(f"Loaded {len(tickets)} ticket(s) from {DEFAULT_STORAGE_PATH} (if the file existed).")
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            create_ticket_from_prompt(tickets)
        elif choice == "2":
            show_tickets(tickets)
        elif choice == "3":
            ticket_id = input("Ticket ID: ")
            assignee = input("Assign to (name): ")
            try:
                ticket = assign_ticket(tickets, ticket_id, assignee)
                print(f"Assigned {ticket['id']} to {ticket['assigned_to']}.")
            except ValueError as exc:
                print(exc)
        elif choice == "4":
            ticket_id = input("Ticket ID: ")
            status = input("New status (open/in_progress/resolved/closed): ")
            try:
                ticket = update_ticket_status(tickets, ticket_id, status)
                print(f"{ticket['id']} status is now {ticket['status']}.")
            except ValueError as exc:
                print(exc)
        elif choice == "5":
            print(format_report(tickets))
        elif choice == "6":
            try:
                save_tickets(tickets)
                print(f"Saved {len(tickets)} ticket(s) to {DEFAULT_STORAGE_PATH}.")
            except OSError as exc:
                print(f"Could not save tickets: {exc}")
        elif choice == "7":
            try:
                reloaded = load_tickets()
            except ValueError as exc:
                print(f"Could not reload tickets: {exc}")
            else:
                tickets = reloaded
                print(f"Reloaded {len(tickets)} ticket(s). Unsaved changes, if any, were discarded.")
        elif choice == "0":
            try:
                save_tickets(tickets)
            except OSError as exc:
                print(f"Could not save tickets: {exc}")
                answer = input("Exit anyway without saving? (y/N): ").strip().lower()
                if answer != "y":
                    continue
            else:
                print(f"Saved {len(tickets)} ticket(s). Thank You and Goodbye!")
            break
        else:
            print("Unknown option. Choose one of the menu numbers.")


if __name__ == "__main__":
    main()

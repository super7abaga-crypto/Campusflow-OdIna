PR TITLE: feat: Implement ticket workflow and reports 

Related Issue: Closes #<0> 

WHAT CHANGED? 

    Added ticket assignment functionality in campusflow/workflow.py. 

    Added ticket status update functionality. 

    Added validation for ticket IDs when assigning or updating tickets. 

    Added validation for assignee names. 

    Added allowed ticket statuses: open, in_progress, resolved, and closed. 

    Prevented invalid status values from being applied to tickets. 

    Added unit tests in tests/test_workflow.py covering ticket assignment and status updates. 

HOW DOES IT WORK? 

    The workflow functions search the existing ticket list using the ticket ID. 

    When a valid ticket is found, an engineer can be assigned to it using assign_ticket(). 

    The assigned engineer's name is stored in the ticket's assigned_to field. 

    Ticket status can be changed using update_ticket_status(). 

    Only the allowed workflow statuses are accepted. 

    If the ticket ID does not exist or the input is invalid, a ValueError is raised instead of changing the ticket. 

    The workflow logic is kept separate from main.py so the command-line interface only collects user input and calls the appropriate functions. 

HOW DID I TEST IT? 

    Command: python -m unittest discover -s tests -v 

    Actual result: All relevant workflow tests passed. 

    Edge cases verified: 

    Assigning an existing ticket to an engineer. 

    Updating an existing ticket to a valid status. 

    Using an invalid ticket ID. 

    Using an invalid or empty assignee name. 

    Using an unsupported ticket status. 

    Confirming that the ticket's assigned_to value changes correctly. 

    Confirming that the ticket's status changes only when a valid status is provided. 

    Confirming that invalid operations raise ValueError instead of silently changing the ticket. 

WHAT DID I LEARN WITH AI? 

    Concept: Python workflow logic, searching lists of dictionaries, validation, exception handling, and separating business logic from the command-line interface. 

    My verification: I tested assigning engineers to existing tickets and changing ticket statuses. I also tested invalid ticket IDs and unsupported statuses to make sure the functions rejected bad input. 

    Changed/rejected advice: I used AI explanations to understand how the workflow functions should behave, but verified the behaviour through the project's unit tests and adjusted the implementation to match the project's actual requirements. 

REVIEWER NOTES 

    Please check that ticket assignment only changes the intended ticket. 

    Please review the validation of ticket IDs and assignee names. 

    Please check that only the four supported statuses can be applied: open, in_progress, resolved, and closed. 

    Please verify that invalid workflow operations raise an error without modifying the ticket. 

    Please review whether the workflow tests cover the important invalid-input cases. 

KNOWN LIMITATIONS 

    The current workflow does not include authentication or permission checks for who is allowed to assign or update tickets. 

    Ticket assignment currently stores the engineer's name rather than linking to a separate engineer/user record. 

    The workflow operates on the in-memory ticket list; persistent saving is handled separately by the storage module. 

    More advanced workflow rules, such as preventing certain status transitions, can be added later. 

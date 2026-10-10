PR TITLE: feat: Complete ticket management system 

Related Issue: Closes #<0> 

WHAT CHANGED? 

    Added ticket creation functionality in campusflow/tickets.py. 

    Added validation for ticket titles, categories, urgency levels, and affected-user counts. 

    Added automatic ticket ID generation such as T001, T002, and so on. 

    Added automatic priority calculation based on urgency and number of affected users. 

    Added default ticket status of open. 

    Added assigned_to field with an initial value of None. 

    Added unit tests in tests/test_tickets.py covering ticket creation, validation, ticket IDs, and priority calculation. 

HOW DOES IT WORK? 

    Ticket information is validated before the ticket is added to the ticket list. 

    Categories are restricted to Network, Hardware, Software, and Other. 

    Urgency is restricted to low, medium, and high. 

    The number of affected users must be a positive integer. 

    Ticket IDs are generated automatically by checking the highest existing ticket number and creating the next ID. 

    Priority is calculated from urgency and affected users. 

    The most specific critical rule is checked before the broader high, medium, and low rules because Python evaluates if/elif conditions from top to bottom. 

    A successfully created ticket starts with status open and no assigned engineer. 

HOW DID I TEST IT? 

    Command: python -m unittest discover -s tests -v 

    Actual result: "15 tests ran — all passed." 

    Edge cases verified: 

    Blank ticket titles are rejected. 

    Invalid categories are rejected. 

    Invalid urgency values are rejected. 

    Zero affected users are rejected. 

    Negative affected users are rejected. 

    Non-integer affected-user values are rejected. 

    A high-urgency ticket affecting 10 or more users receives critical priority. 

    High urgency with fewer than 10 affected users receives high priority. 

    Medium urgency and different affected-user counts produce the expected priority. 

    Low urgency with a small number of affected users produces low priority. 

    Ticket IDs increase correctly, for example T001 followed by T002. 

WHAT DID I LEARN WITH AI? 

    Concept: Input validation, Python conditional logic, ticket-priority rules, exception handling, and unit testing. 

    My verification: I used unit tests to check both valid and invalid ticket inputs and tested different combinations of urgency and affected users. I specifically verified that a high-urgency ticket affecting 10 or more users is classified as critical rather than high. 

    Changed/rejected advice: I did not rely on AI suggestions without testing them. I checked the proposed validation and priority rules against the project's requirements and verified the behaviour through the unit tests. Where necessary, the implementation was adjusted to match the actual project rules. 

REVIEWER NOTES 

    Please check that ticket validation happens before invalid data can be added to the ticket list. 

    Please review the priority calculation, especially the critical condition for high urgency with 10 or more affected users. 

    Please check that ticket IDs remain unique and increase correctly when multiple tickets are created. 

    Please review whether the tests cover enough invalid input and priority combinations. 

KNOWN LIMITATIONS 

    Ticket creation and validation are currently focused on the core ticket data; authentication and user permissions are not part of this feature. 

    Ticket data is handled in memory by the ticket functions; persistent storage is handled separately by the storage module. 

    The current interface is command-line based. 

    More edge-case tests can be added as the rest of the ticket workflow is developed. 

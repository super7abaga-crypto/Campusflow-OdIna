# CampusFlow Design Decisions

## 1. Ticket Collection
Tickets will be stored in a Python list of dictionaries while
the application is running. The collection will be passed to
functions that need to access or modify tickets. Every ticket
will have a unique ID.

## 2. Error Handling
Functions will raise appropriate exceptions, such as ValueError,
when input is invalid. The CLI will catch these exceptions and
display clear, user-friendly error messages. Invalid input must
not corrupt or partially create a ticket.

## 3. Function Return Values
Ticket creation will return the newly created ticket dictionary.
Successful assignment and status-update operations will modify
the existing ticket and return the updated dictionary. Functions
that return collections will return lists. Invalid operations
will raise appropriate exceptions.

## 4. JSON Persistence
The storage.py module will own all JSON loading and saving.
Tickets will be stored in data/tickets.json. The application
will load tickets at startup and save changes through the storage
module. A missing file will allow a fresh start. Malformed JSON
will produce a clear error without silently discarding existing
data. Runtime ticket data will be excluded from Git.

## 5. Automated Testing
CampusFlow will use Python's built-in unittest framework.
Business-logic functions will accept arguments and return results
or raise exceptions without requesting interactive input. Tests
will cover valid inputs, invalid inputs, priority rules, edge cases,
and relevant workflow and persistence behaviour. 
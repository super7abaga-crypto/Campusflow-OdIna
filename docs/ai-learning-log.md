# AI and team learning log

Use this file to record how the team understood, checked, and adapted ideas while building Campusflow-OdIna. Keep entries honest: record what you actually asked, tested, changed, and learned.

## Entry template

- **Date:*October 9, 2026*
- **Engineer(s):*Campusflow-OdIna*
- **Problem or question:*How to handle invalid user inputs (e.g., empty ticket titles or invalid priority levels) before modifying state or saving to storage.*
- **Explanation or resource used:*Python control flow documentation on if / elif / else evaluation order.*
- **What we understood in our own words:*We can explain that json.dump() saves data to a JSON file and json.load() reads data from a JSON file.*
- **What we changed:*Reordered priority check logic so Critical is checked first, followed by High, Medium, and default Low.*
- **How we tested it:*Created sample tickets across all priority levels and logged output routing to verify critical tickets were processed by critical handlers.*
- **What we would do differently next time:*Use explicit enumerations or strict string equality checks rather than relying on loose comparison chaining.*

## Suggested topics to discuss together

1. Why should input validation happen before a ticket is appended to the list? Appending bad or incomplete data corrupts the in-memory ticket list and can lead to runtime exceptions in subsequent functions (e.g., missing keys during rendering or filtering). Validating first guarantees that every item inside the data store meets structural expectations.
2. Why must the critical-priority rule be checked before the high-priority rule? In if/elif chains, execution stops at the first True condition. Because critical tickets often meet or exceed the criteria assigned to high-priority tickets, evaluating high-priority first causes critical tickets to be mishandled before reaching their specific logic block.
3. What is the difference between a function returning a value and printing it? print() displays text to the standard output console for human observation, but yields None to the program context. return passes data back to the calling function, allowing other parts of the application to store, transform, test, or reuse the value.
4. Why are workflow functions tested separately from the CLI prompts? Decoupling workflow logic from CLI input/output allows business rules to be tested programmatically using unit tests without requiring interactive user input. It also makes the backend portable should the app switch from CLI to a web interface.
5. What happens if a JSON file is missing or malformed? A missing file triggers a FileNotFoundError, while malformed JSON triggers a json.decoder.JSONDecodeError. Without try/except handling, the program crashes on startup. Safe implementations catch these exceptions and initialize a fresh, empty data state.
6. What limitations might appear if two users save tickets at the same time? Without file locking or a database handling concurrency, simultaneous writes cause race conditions. One user's save will overwrite the other's changes, leading to lost ticket updates or truncated JSON files due to simultaneous file handles writing to disk.


## Team reflection

Complete this section together after reviewing the code.

- **Most useful concept learned:*Separating pure business logic (ticket operations) from user interface logic (CLI input() and print()) to make code testable and maintainable.*
- **Hardest bug and how we diagnosed it:*A JSONDecodeError on startup caused by an empty .json file. We diagnosed it by inspecting the call stack, isolating the load function, and wrapping json.load() with proper exception handling to fall back to an empty ticket list ([]).*
- **A test we added ourselves:*A unit test checking that critical-priority tickets trigger the immediate notification flag while lower priorities do not.*
- **A design choice we agreed to change:*Moving away from inline file saving on every variable change to explicit save calls managed by a controller module.*
- **Next improvement:*Implement file locking or migrate persistence to SQLite to handle potential concurrent reads and writes safely.*

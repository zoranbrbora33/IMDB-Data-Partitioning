This script, `logger.py`, configures a logger to handle logging functionality for the project. It sets up a logger named 'Logger' with two handlers: one for streaming logs to stdout and another for writing logs to a file. The log file is stored in a 'logs' directory with the filename format as the current date.

#### Logging Configuration:

1. **Logger Configuration**:
   - A logger named 'Logger' is created.
   - Two handlers are added:
     - `StreamHandler`: Sends log messages to the standard output (stdout).
     - `FileHandler`: Writes log messages to a file in the 'logs' directory, with the filename formatted as the current date in 'YYYY-MM-DD.log' format.
   - The logger is set to log messages with the DEBUG level.

#### External Dependencies:

- `logging`: Python's built-in logging module for configuring and utilizing loggers.
- `sys`: Provides access to some variables used or maintained by the Python interpreter and to functions that interact with the interpreter.
- `os`: Allows interaction with the operating system, used here for file handling.
- `datetime`: Provides classes for manipulating dates and times, used to generate the current date for the log file name.

#### Additional Notes:

- The logger is set to log messages at the DEBUG level, meaning it will capture all log messages (DEBUG, INFO, WARNING, ERROR, CRITICAL).
- Log messages are simultaneously output to the console and written to a log file in the 'logs' directory.
- The log file is named according to the current date to facilitate organization and reference.

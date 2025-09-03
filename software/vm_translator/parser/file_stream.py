#!/usr/bin/env python3
"""
Class for reading a file line by line.
"""


class FileStream:
    """Wrapper around Python file I/O that reads line by line"""
    def __init__(self, filename: str) -> None:
        self.file = open(filename, "r")
        self.next_line = None

    def has_more_commands(self) -> bool:
        """Return if there are more lines to read from the file"""
        if self.next_line is not None:
            return True
        self.next_line = self.file.readline()
        if self.next_line == "":
            return False
        return True

    def advance(self) -> str:
        """Return the next line and advance the stream"""
        if self.next_line is not None:
            line, self.next_line = self.next_line, None
            return line
        return self.file.readline()

    def close(self) -> None:
        self.file.close()

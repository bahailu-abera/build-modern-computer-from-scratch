#!/usr/bin/env python3
"""
Parser module for reading current_command line by line
and giving corresponding current_command type and current_command arguments
"""
from .file_stream import FileStream
from constants.command_types import (
    ALL_COMMANDS,
    COMPUTE_COMMANDS
)


class Parser:
    C_ARITHMETIC = 'C_ARITHMETIC'
    C_PUSH = 'C_PUSH'
    C_POP = 'C_POP'
    C_LABEL = 'C_LABEL'
    C_GOTO = 'C_GOTO'
    C_IF = 'C_IF'
    C_FUNCTION = 'C_FUNCTION'
    C_RETURN = 'C_RETURN'
    C_CALL = 'C_CALL'

    def __init__(self, filename: str) -> None:
        self.line_number = -1
        self.in_stream = FileStream(filename)
        self.current_command = None

    def eat_space(self) -> None:
        """ Reads spaces and consume. """
        command = self.current_command.split(" ")

        self.current_command = []

        for cmd in command:
            cmd = cmd.strip()

            if cmd:
                self.current_command.append(cmd)

        return len(self.current_command) > 0

    def eat_comments(self):
        """Reads comments and consume"""
        while self.in_stream.has_more_commands():
            self.current_command = self.in_stream.advance()
            if self.current_command.count("//"):
                self.current_command = self.current_command.split("//")[0]

            if self.eat_space():
                break

    def has_more_commands(self) -> bool:
        """Checks if there is more work to do (boolean)"""
        return self.in_stream.has_more_commands()

    def advance(self) -> str:
        """Gets the next command and makes it
        the current command (string)"""
        self.eat_comments()
        self.line_number += 1

        return self.current_command

    def command_type(self) -> str:
        """
        Get the VM command type for the current command.

        Returns:
            str: One of the C_* constants.

        Raises:
            ValueError: If the command is invalid or unsupported.
        """
        cmd = self.current_command[0]

        if cmd not in ALL_COMMANDS:
            raise ValueError(
                f"Unknown command '{cmd}' "
                f"at line {self.line_number} in {self.in_stream.filename}"
            )

        if cmd in COMPUTE_COMMANDS:
            return self.C_ARITHMETIC

        mapping = {
            "push": self.C_PUSH,
            "pop": self.C_POP,
            "label": self.C_LABEL,
            "goto": self.C_GOTO,
            "if-goto": self.C_IF,
            "function": self.C_FUNCTION,
            "call": self.C_CALL,
            "return": self.C_RETURN,
        }

        return mapping.get(cmd)

    def arg1(self) -> str:
        """
        Returns the first argument of the current command.
        In the case of C_ARITHMETIC, the command itself(add, sub, etc.)
        is returned.
        """
        ctype = self.command_type()

        if ctype == self.C_RETURN:
            raise ValueError(
                f"arg1() should not be called on 'return' "
                f"at line {self.line_number} in {self.in_stream.filename}"
            )

        if ctype == self.C_ARITHMETIC:
            return self.current_command[0]

        return self.current_command[1]

    def arg2(self) -> int:
        """
        Returns the second argument of the current command.
        """
        ctype = self.command_type()

        if ctype not in (self.C_PUSH, self.C_POP, self.C_FUNCTION, self.C_CALL):
            raise ValueError(
                f"arg2() is not applicable for command '{self.current_command[0]}' "
                f"at line {self.line_number} in {self.in_stream.filename}"
            )

        return int(self.current_command[2])

    def clear(self) -> None:
        """ Clear allocated resources. """
        self.in_stream.close()

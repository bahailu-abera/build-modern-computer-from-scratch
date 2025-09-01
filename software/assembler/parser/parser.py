#!/usr/bin/env python3
"""
Parser module for reading instruction line by line
and giving instruction type and instruction symbol
"""
from .file_stream import FileStream


class Parser:
    A_INSTRUCTION = 'A_INSTRUCTION'
    C_INSTRUCTION = 'C_INSTRUCTION'
    L_INSTRUCTION = 'L_INSTRUCTION'

    def __init__(self, filename: str) -> None:
        self.line_number = -1
        self.in_stream = FileStream(filename)
        self.current_instruction = None

    def eat_space(self) -> None:
        """ Reads spaces and consume. """
        line = ""

        for ch in self.current_instruction:
            if not ch.isspace():
                line += ch

        self.current_instruction = line

        return len(self.current_instruction) > 0

    def eat_comments(self):
        """Reads comments and consume"""
        while self.in_stream.has_more_lines():
            self.current_instruction = self.in_stream.advance()
            if self.current_instruction.count("//"):
                self.current_instruction = self.current_instruction.split("//")[0]

            if self.eat_space():
                break

    def has_more_lines(self) -> bool:
        """Checks if there is more work to do (boolean)"""
        return self.in_stream.has_more_lines()

    def advance(self) -> str:
        """Gets the next instruction and makes it
        the current instruction (string)"""
        self.eat_comments()
        
        if self.instruction_type() != self.L_INSTRUCTION:
            self.line_number += 1

        return self.current_instruction

    def instruction_type(self) -> str:
        """Returns the instruction type"""
        if self.current_instruction.startswith("@"):
            return self.A_INSTRUCTION
        elif self.current_instruction.startswith("(") and \
                self.current_instruction.endswith(")"):
            return self.L_INSTRUCTION
        else:
            return self.C_INSTRUCTION

    def symbol(self) -> str:
        """Returns the instruction's symbol (string)"""
        if self.instruction_type() == self.A_INSTRUCTION:
            return self.current_instruction[1:]
        elif self.instruction_type() == self.L_INSTRUCTION:
            return self.current_instruction[1:-1]
        return ""

    def dest(self) -> str:
        """Returns the instruction's dest field (string)"""
        if "=" in self.current_instruction:
            return self.current_instruction.split("=")[0]
        return "null"

    def comp(self) -> str:
        """Returns the instruction's comp field (string)"""
        instr = self.current_instruction
        if "=" in instr:
            instr = instr.split("=")[1]
        if ";" in instr:
            instr = instr.split(";")[0]
        return instr

    def jump(self) -> str:
        """Returns the instruction's jump field (string)"""
        if ";" in self.current_instruction:
            return self.current_instruction.split(";")[1]
        return "null"
    
    def clear(self) -> None:
        """ Clear allocated resources. """
        self.in_stream.close()

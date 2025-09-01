#!/usr/bin/env python3
"""
Hack Assembler

This module translates Hack assembly (.asm) programs into machine code (.hack).

Usage:
    ./assembler.py <filename>.asm
"""

import sys
from parser.parser import Parser
from code.code import Code
from symbol_table.symbol_table import SymbolTable


FILE_EXTENSION = '.hack'
INITIAL_VARIABLE_ADDRESS = 16


class Assembler:
    """Assembler class to handle symbol resolution and code generation."""

    def __init__(self, filename: str):
        """
        Initialize assembler with filename, parser, and symbol table.
        """
        self.filename = filename
        self.symbol_table = SymbolTable()
        self.memory_location = INITIAL_VARIABLE_ADDRESS

    def resolve_symbols(self) -> None:
        """
        First pass: resolve labels (L-instructions) and
        add them to the symbol table with their corresponding line numbers.
        """
        parser = Parser(self.filename)

        while parser.has_more_lines():
            parser.advance()
            if parser.instruction_type() == parser.L_INSTRUCTION:
                label = parser.symbol()
                self.symbol_table.add_entry(label, parser.line_number + 1)

        parser.clear()

    def decode_instruction_a(self, value: str) -> str:
        """
        Decode an A-instruction into a 16-bit binary string.
        - If the symbol is numeric, convert directly.
        - If it's a label or variable, resolve via symbol table.
        """
        if value.isdigit():
            return f"{int(value):016b}"

        if self.symbol_table.contains(value):
            return f"{self.symbol_table.get_address(value):016b}"

        # Assign new variable memory location
        self.symbol_table.add_entry(value, self.memory_location)
        self.memory_location += 1
        return f"{self.symbol_table.get_address(value):016b}"

    def decode_instruction_c(self, parser: Parser) -> str:
        """
        Decode a C-instruction into a 16-bit binary string.
        C-instructions have the format:
            dest=comp;jump
        """
        dest, comp, jump = parser.dest(), parser.comp(), parser.jump()
        return "111" + Code.comp(comp) + Code.dest(dest) + Code.jump(jump)

    def generate_code(self) -> None:
        """
        Second pass: translate instructions
        into binary and write to .hack file.
        """
        output_filename = self.filename.replace('.asm', FILE_EXTENSION)

        parser = Parser(self.filename)
        with open(output_filename, "w") as file:
            while parser.has_more_lines():
                parser.advance()

                if parser.instruction_type() == parser.A_INSTRUCTION:
                    code = self.decode_instruction_a(parser.symbol())
                elif parser.instruction_type() == parser.C_INSTRUCTION:
                    code = self.decode_instruction_c(parser)
                else:  # L-instructions are labels, skip in code generation
                    continue

                file.write(code + "\n")

        parser.clear()


def main():
    """Main driver function for Hack assembler."""
    if len(sys.argv) != 2:
        print("Error: Please provide the input .asm filename")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith('.asm'):
        print("Error: Input file must have a .asm extension")
        sys.exit(1)

    assembler = Assembler(filename)
    assembler.resolve_symbols()
    assembler.generate_code()


if __name__ == "__main__":
    main()

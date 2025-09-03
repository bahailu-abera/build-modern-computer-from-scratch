#!/usr/bin/env python3
"""
translator.py

Main driver for the Nand2Tetris VM Translator.
This program parses one or more `.vm` files and generates a single
`.asm` file containing equivalent Hack assembly instructions.

Usage:
    $ python3 translator.py <input.vm | input_directory>
"""

import sys
import os
from code_writer.code_writer import CodeWriter
from parser.parser import Parser
from constants.command_types import (
    POP,
    PUSH
)


FILE_EXTENSION = ".asm"


class VMTranslator:
    """
    Orchestrates the translation process between Parser and CodeWriter.
    """

    def __init__(self, parser: Parser, code_writer: CodeWriter) -> None:
        self.parser = parser
        self.code_writer = code_writer

    def generate_code(self) -> None:
        """
        Iterates through all VM commands, parses them,
        and dispatches to CodeWriter for translation.
        """
        while self.parser.has_more_commands():
            self.parser.advance()
            cmd_type = self.parser.command_type()

            if cmd_type == self.parser.C_ARITHMETIC:
                self.code_writer.write_compute(self.parser.arg1())
            elif cmd_type == self.parser.C_POP:
                self.code_writer.write_push_pop(
                    POP, self.parser.arg1(), self.parser.arg2()
                )
            elif cmd_type == self.parser.C_PUSH:
                self.code_writer.write_push_pop(
                    PUSH, self.parser.arg1(), self.parser.arg2()
                )
            else:
               raise NotImplementedError("No implementation avaible")


def main():
    """
    Entry point: determines if input is a single .vm file or a directory,
    initializes Parser and CodeWriter, and triggers translation.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 vm_translator.py <input.vm | input_directory>")
        sys.exit(1)

    input_path = sys.argv[1]

    # Single `.vm` file
    if input_path.endswith(".vm") and os.path.isfile(input_path):
        output_filename = input_path.replace(".vm", FILE_EXTENSION)
        vm_files = [input_path]

    # Directory containing `.vm` files
    elif os.path.isdir(input_path):
        dirname = os.path.basename(os.path.normpath(input_path))
        output_filename = os.path.join(input_path, dirname + FILE_EXTENSION)
        vm_files = [
            os.path.join(input_path, f)
            for f in os.listdir(input_path)
            if f.endswith(".vm")
        ]
        if not vm_files:
            print(f"Error: No .vm files found in directory {input_path}")
            sys.exit(1)

    else:
        print("Error: Please provide a valid .vm file or directory")
        sys.exit(1)

    code_writer = CodeWriter(output_filename)

    # Process each VM file
    for vm_file in vm_files:
        parser = Parser(vm_file)

        vm_file_name = os.path.splitext(os.path.basename(vm_file))[0]
        code_writer.set_file_name(vm_file_name)

        translator = VMTranslator(parser, code_writer)
        translator.generate_code()

        parser.clear()

    code_writer.close()


if __name__ == "__main__":
    main()

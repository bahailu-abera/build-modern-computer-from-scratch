#!/usr/bin/env python3
"""
builtin_symbols.py

This module defines the built-in symbols of the Hack assembly language
and their corresponding memory addresses. These symbols are part of the
Hack specification and must be initialized in every assembler's symbol table.

Symbols include:
- Predefined registers: R0 - R15
- Pointers: SP, LCL, ARG, THIS, THAT
- Memory-mapped I/O: SCREEN, KBD
"""

builtin_symbols = {
    # Predefined registers
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,

    # Pointers
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,

    # Memory-mapped I/O
    "SCREEN": 16384,
    "KBD": 24576,
}

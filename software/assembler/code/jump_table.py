#!/usr/bin/env python3
"""
jump_table.py

This module defines the lookup table for Hack assembly jump
mnemonics. Each mnemonic (e.g., "JGT", "JEQ", "JMP") maps to its
corresponding 3-bit binary code used in the C-instruction format.
"""

JUMP_TABLE = {
    None:   "000",
    "null": "000",
    "JGT":  "001",
    "JEQ":  "010",
    "JGE":  "011",
    "JLT":  "100",
    "JNE":  "101",
    "JLE":  "110",
    "JMP":  "111",
}

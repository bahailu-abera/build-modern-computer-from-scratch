#!/usr/bin/env python3
"""
Code module for the Hack assembler.

This module provides the Code class, which translates Hack assembly
mnemonics into their corresponding binary codes for the C-instruction
format (dest=comp;jump).

- dest(mnemonic): returns a 3-bit binary code for the destination field.
- comp(mnemonic): returns a 7-bit binary code for the computation field.
- jump(mnemonic): returns a 3-bit binary code for the jump field.

The actual lookup tables for dest, comp, and jump are defined in
separate modules (dest_table.py, comp_table.py, jump_table.py) to
keep the code organized and modular.

Note:
According to the Hack specification, mnemonics like DM and ADM are
valid aliases for MD and AMD respectively. This assembler handles
both forms correctly, mapping them to the same binary codes.
"""

from .comp_table import COMP_TABLE
from .dest_table import DEST_TABLE
from .jump_table import JUMP_TABLE


class Code:
    """Translates Hack assembly mnemonics into binary codes."""

    @staticmethod
    def dest(mnemonic: str) -> str:
        """Return the 3-bit binary code of the dest mnemonic."""
        return DEST_TABLE.get(mnemonic, "000")

    @staticmethod
    def comp(mnemonic: str) -> str:
        """Return the 7-bit binary code of the comp mnemonic."""
        if mnemonic in COMP_TABLE:
            return COMP_TABLE.get(mnemonic)
        raise ValueError(f"Unkown comp command: {mnemonic}")

    @staticmethod
    def jump(mnemonic: str) -> str:
        """Return the 3-bit binary code of the jump mnemonic."""
        return JUMP_TABLE.get(mnemonic, "000")

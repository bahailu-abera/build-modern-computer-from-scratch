#!/usr/bin/env python3
"""
symbol_table.py

This module implements the SymbolTable class for the Hack assembler.
The symbol table keeps a correspondence between symbolic labels/variables
and their numeric memory addresses.

Responsibilities:
- Initialize with built-in symbols (see builtin_symbols.py).
- Add new symbols (labels or variables) during assembly.
- Check if a symbol exists in the table.
- Retrieve the address associated with a given symbol.
"""
from .builtin_symbols import builtin_symbols


class SymbolTable:
    def __init__(self) -> None:
        """Initializes the symbol table with the built-in symbols."""
        # Use a copy to avoid accidental modification of the shared dictionary
        self.symbol_table = dict(builtin_symbols)

    def add_entry(self, symbol: str, address: int) -> None:
        """Adds a (symbol, address) entry to the table."""
        self.symbol_table[symbol] = address

    def contains(self, symbol: str) -> bool:
        """Checks if the symbol table contains the given symbol."""
        return symbol in self.symbol_table

    def get_address(self, symbol: str) -> int:
        """Returns the address associated with the symbol."""
        return self.symbol_table[symbol]

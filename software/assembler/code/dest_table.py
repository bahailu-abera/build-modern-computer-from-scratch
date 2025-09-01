#!/usr/bin/env python3
"""
dest_table.py

This module defines the lookup table for Hack assembly destination
mnemonics. Each mnemonic (e.g., "M", "D", "MD", "AMD") maps to its
corresponding 3-bit binary code used in the C-instruction format.

Note:
- The Hack specification allows storing results in multiple
  destinations simultaneously.
- To handle assembler variations, this table accepts both "MD" and
  "DM" (same code), and both "AMD" and "ADM" (same code), along with
  other valid permutations such as "AD", "DA", "AM", "MA", etc.
"""

DEST_TABLE = {
    None:   "000",
    "null": "000",
    "M":    "001",
    "D":    "010",
    "MD":   "011", "DM": "011",
    "A":    "100",
    "AM":   "101", "MA": "101",
    "AD":   "110", "DA": "110",
    "AMD":  "111", "ADM": "111",
    "MAD":  "111", "MDA": "111",
    "DAM":  "111", "DMA": "111",
}

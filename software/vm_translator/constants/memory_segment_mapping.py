"""
memory_segment_mapping.py

Defines memory segments and their physical base addresses
in the Hack platform. These mappings are used by the
VM translator when translating push/pop commands.

Reference: Nand2Tetris Project 7
"""

# -----------------------------
# Segment identifiers
# -----------------------------
LOCAL = "local"
ARGUMENT = "argument"
THIS = "this"
THAT = "that"
POINTER = "pointer"
TEMP = "temp"
STATIC = "static"
CONSTANT = "constant"

# -----------------------------
# Base symbols and addresses
# -----------------------------
SEGMENT_BASE = {
    LOCAL: "LCL",         # base of local segment
    ARGUMENT: "ARG",      # base of argument segment
    THIS: "THIS",         # base of this segment
    THAT: "THAT",         # base of that segment
    POINTER: "3",         # pointer starts at R3 (THIS=R3, THAT=R4)
    TEMP: "5",            # temp segment is R5–R12
    STATIC: "16",         # static variables start at R16
    CONSTANT: None,       # constant is a pseudo-segment
}

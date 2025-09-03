"""
command_types.py

This module defines all command types used in
the Nand2Tetris Virtual Machine (VM).
The VM language supports four broad categories of commands:

1. Arithmetic/Logical Commands
2. Memory Access Commands
3. Program Flow Commands
4. Function Calling Commands

These constants are used throughout
the VM translator (e.g., in the parser and code writer)
to identify and classify VM instructions.

Reference: Nand2Tetris Project 7 & Project 8 (VM I & II)
"""

# -----------------------------
# Command name constants
# -----------------------------

# Arithmetic
ADD = "add"
SUB = "sub"
NEG = "neg"

# Comparison
EQ = "eq"
LT = "lt"
GT = "gt"

# Logical
AND = "and"
OR = "or"
NOT = "not"

# Memory access
PUSH = "push"
POP = "pop"

# Program flow
LABEL = "label"
GOTO = "goto"
IF_GOTO = "if-goto"

# Function calling
FUNCTION = "function"
CALL = "call"
RETURN = "return"

# -----------------------------
# Command groups
# -----------------------------

# Arithmetic commands
ARITHMETIC_COMMANDS = {ADD, SUB, NEG}

# Comparison commands
COMPARE_COMMANDS = {EQ, LT, GT}

# Logical operation commands
LOGICAL_OP_COMMANDS = {AND, OR, NOT}

# Compute commands (all arithmetic/logical/compare)
COMPUTE_COMMANDS = (
    ARITHMETIC_COMMANDS
    | COMPARE_COMMANDS
    | LOGICAL_OP_COMMANDS
)

# Unary operations (operate on one operand)
UNARY_COMMANDS = {NEG, NOT}

# Memory access commands
MEMORY_ACCESS_COMMANDS = {PUSH, POP}

# Program flow commands
PROGRAM_FLOW_COMMANDS = {LABEL, GOTO, IF_GOTO}

# Function calling commands
FUNCTION_CALLING_COMMANDS = {FUNCTION, CALL, RETURN}

# All supported commands (for quick validation)
ALL_COMMANDS = (
    COMPUTE_COMMANDS
    | MEMORY_ACCESS_COMMANDS
    | PROGRAM_FLOW_COMMANDS
    | FUNCTION_CALLING_COMMANDS
)

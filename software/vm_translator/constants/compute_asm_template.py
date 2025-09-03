"""
compute_asm_template.py

Hack assembly templates for VM compute commands.
"""

# -----------------------------
# Stack pointer helpers
# -----------------------------

INCREMENT_SP = "// SP++ (move to next free stack slot)\n@SP\nM=M+1\n"
DECREMENT_SP = "// SP-- (move to topmost value)\n@SP\nM=M-1\n"

LOAD_SP_TO_A = "// A = SP (point to top of stack)\n@SP\nA=M\n"
LOAD_SP_TO_D = "// D = *SP (load top of stack value)\n@SP\nA=M\nD=M\n"


# -----------------------------
# Binary arithmetic
# -----------------------------

BINARY_ADD = """// add
{DECREMENT_SP}
{LOAD_SP_TO_D}  // D = y
{DECREMENT_SP}
{LOAD_SP_TO_A}
M=D+M              // x + y → top of stack
{INCREMENT_SP}
"""

BINARY_SUB = """// sub
{DECREMENT_SP}
{LOAD_SP_TO_D}  // D = y
{DECREMENT_SP}
{LOAD_SP_TO_A}
M=M-D               // x - y → top of stack
{INCREMENT_SP}
"""

# -----------------------------
# Binary logical
# -----------------------------

BINARY_AND = """// and
{DECREMENT_SP}
{LOAD_SP_TO_D}  // D = y
{DECREMENT_SP}
{LOAD_SP_TO_A}
M=D&M             // x & y → top of stack
{INCREMENT_SP}
"""

BINARY_OR = """// or
{DECREMENT_SP}
{LOAD_SP_TO_D}  // D = y
{DECREMENT_SP}
{LOAD_SP_TO_A}
M=D|M             // x | y → top of stack
{INCREMENT_SP}
"""

# -----------------------------
# Unary operations
# -----------------------------

UNARY_NEG = """// neg
{DECREMENT_SP}
{LOAD_SP_TO_A}
M=-M                // -y
{INCREMENT_SP}
"""

UNARY_NOT = """// not
{DECREMENT_SP}
{LOAD_SP_TO_A}
M=!M                // !y
{INCREMENT_SP}
"""

# -----------------------------
# Comparisons
# -----------------------------

COMPARE_EQ = """// eq
{DECREMENT_SP}
{LOAD_SP_TO_D}  // D = y
{DECREMENT_SP}
{LOAD_SP_TO_A}
D=M-D               // x - y
@EQ_TRUE_{label}
D;JEQ               // if x == y → jump
{LOAD_SP_TO_A}
M=0                 // false (0)
@EQ_END_{label}
0;JMP
(EQ_TRUE_{label})
{LOAD_SP_TO_A}
M=-1                // true (-1)
(EQ_END_{label})
{INCREMENT_SP}
"""

COMPARE_LT = """// lt
{DECREMENT_SP}
{LOAD_SP_TO_D}  // D = y
{DECREMENT_SP}
{LOAD_SP_TO_A}
D=M-D               // x - y
@LT_TRUE_{label}
D;JLT               // if x < y → jump
{LOAD_SP_TO_A}
M=0                 // false (0)
@LT_END_{label}
0;JMP
(LT_TRUE_{label})
{LOAD_SP_TO_A}
M=-1                // true (-1)
(LT_END_{label})
{INCREMENT_SP}
"""

COMPARE_GT = """// gt
{DECREMENT_SP}
{LOAD_SP_TO_D}  // D = y
{DECREMENT_SP}
{LOAD_SP_TO_A}
D=M-D               // x - y
@GT_TRUE_{label}
D;JGT               // if x > y → jump
{LOAD_SP_TO_A}
M=0                 // false (0)
@GT_END_{label}
0;JMP
(GT_TRUE_{label})
{LOAD_SP_TO_A}
M=-1                // true (-1)
(GT_END_{label})
{INCREMENT_SP}
"""

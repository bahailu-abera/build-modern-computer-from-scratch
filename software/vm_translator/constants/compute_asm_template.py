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

BINARY_ADD = """// add\n
{DECREMENT_SP}
// D = y\n{LOAD_SP_TO_D}
{DECREMENT_SP}
{LOAD_SP_TO_A}
M=M+D               // x + y → top of stack\n
{INCREMENT_SP}
"""

BINARY_SUB = """// sub\n
{DECREMENT_SP}
// D = y\n{LOAD_SP_TO_D}
{DECREMENT_SP}
{LOAD_SP_TO_A}
M=M-D               // x - y → top of stack\n
{INCREMENT_SP}
"""

# -----------------------------
# Binary logical
# -----------------------------

BINARY_AND = """// and\n
{DECREMENT_SP}
// D = y\n{LOAD_SP_TO_D}
{DECREMENT_SP}
{LOAD_SP_TO_A}
M=M&D               // x & y → top of stack\n
{INCREMENT_SP}
"""

BINARY_OR = """// or\n
{DECREMENT_SP}
// D = y\n{LOAD_SP_TO_D}
{DECREMENT_SP}
{LOAD_SP_TO_A}
M=M|D               // x | y → top of stack\n
{INCREMENT_SP}
"""

# -----------------------------
# Unary operations
# -----------------------------

UNARY_NEG = """// neg\n
{DECREMENT_SP}
{LOAD_SP_TO_A}
M=-M                // -y\n
{INCREMENT_SP}
"""

UNARY_NOT = """// not\n
{DECREMENT_SP}
{LOAD_SP_TO_A}
M=!M                // !y\n
{INCREMENT_SP}
"""

# -----------------------------
# Comparisons
# -----------------------------

COMPARE_EQ = """// eq
{DECREMENT_SP}
// D = y\n{LOAD_SP_TO_D}
{DECREMENT_SP}
{LOAD_SP_TO_A}
D=M-D               // x - y\n
@EQ_TRUE_{label}\n
D;JEQ               // if x == y → jump\n
{LOAD_SP_TO_A}
M=0                 // false (0)\n
@EQ_END_{label}\n
0;JMP\n
(EQ_TRUE_{label})\n
{LOAD_SP_TO_A}
M=-1                // true (-1)\n
(EQ_END_{label})\n
{INCREMENT_SP}\n
"""

COMPARE_LT = """// lt\n
{DECREMENT_SP}
// D = y\n{LOAD_SP_TO_D}
{DECREMENT_SP}
{LOAD_SP_TO_A}
D=M-D               // x - y
@LT_TRUE_{label}\n
D;JLT               // if x < y → jump
{LOAD_SP_TO_A}
M=0                 // false (0)
@LT_END_{label}\n
0;JMP\n
(LT_TRUE_{label})\n
{LOAD_SP_TO_A}
M=-1                // true (-1)\n
(LT_END_{label})\n
{INCREMENT_SP}\n
"""

COMPARE_GT = """// gt\n
{DECREMENT_SP}
// D = y\n{LOAD_SP_TO_D}
{DECREMENT_SP}
{LOAD_SP_TO_A}
D=M-D               // x - y\n
@GT_TRUE_{label}
D;JGT               // if x > y → jump\n
{LOAD_SP_TO_A}
M=0                 // false (0)\n
@GT_END_{label}\n
0;JMP\n
(GT_TRUE_{label})\n
{LOAD_SP_TO_A}\n
M=-1                // true (-1)\n
(GT_END_{label})\n
{INCREMENT_SP}
"""

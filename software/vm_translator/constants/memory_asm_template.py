"""
memory_asm_template.py

Hack assembly templates for VM memory access (push/pop) commands.
"""

# -----------------------------
# Stack pointer helpers
# -----------------------------

INCREMENT_SP = "// SP++ (move to next free stack slot)\n@SP\nM=M+1\n"
DECREMENT_SP = "// SP-- (move to topmost value)\n@SP\nM=M-1\n"

LOAD_SP_TO_A = "// A = SP (point to top of stack)\n@SP\nA=M\n"
LOAD_SP_TO_D = "// D = *SP (load top of stack value)\n@SP\nA=M\nD=M\n"


# -----------------------------
# Push commands
# -----------------------------
PUSH_M_TO_STACK = """ // push M to the stack
D=M
{LOAD_SP_TO_A}
M=D
{INCREMENT_SP}
"""

PUSH_CONSTANT = """// push constant {index}
@{index}
D=A // D = index
{LOAD_SP_TO_A}
M=D  // push index
{INCREMENT_SP}
"""

PUSH_SEGMENT = """// push {segment} {index}
@{index}
D=A
@{base}
A=D+M
{PUSH_M_TO_STACK}
"""

PUSH_TEMP = """// push temp {index}
@{addr}
{PUSH_M_TO_STACK}
"""

PUSH_POINTER = """// push pointer {index}
@{addr}
{PUSH_M_TO_STACK}
"""

PUSH_STATIC = """// push static {index}
@{filename}.{index}
{PUSH_M_TO_STACK}
"""


# -----------------------------
# Pop commands
# -----------------------------

POP_SEGMENT = """// pop {segment} {index}
@{index}
D=A
@{base}
D=D+M
@R13
M=D               // store target address in R13
{DECREMENT_SP}
{LOAD_SP_TO_D}
@R13
A=M
M=D               // *segment[index] = y
"""

POP_TEMP = """// pop temp {index}
{DECREMENT_SP}
{LOAD_SP_TO_D}
@{addr}
M=D               // temp[index] = y
"""

POP_POINTER = """// pop pointer {index}
{DECREMENT_SP}
{LOAD_SP_TO_D}
@{addr}
M=D               // pointer[index] = y
"""

POP_STATIC = """// pop static {index}
{DECREMENT_SP}
{LOAD_SP_TO_D}
@{filename}.{index}
M=D               // static[index] = y
"""

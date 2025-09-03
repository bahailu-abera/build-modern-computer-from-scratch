// Bootstrap
@256
D=A
@SP
M=D
// Translating tests/StackArithmetic/SimpleAdd/SimpleAdd.vm
// push constant 7
@7
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 8
@8
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// add
// SP-- (move to topmost value)
@SP
M=M-1

// D = *SP (load top of stack value)
@SP
A=M
D=M
  // D = y
// SP-- (move to topmost value)
@SP
M=M-1

// A = SP (point to top of stack)
@SP
A=M

M=D+M              // x + y → top of stack
// SP++ (move to next free stack slot)
@SP
M=M+1


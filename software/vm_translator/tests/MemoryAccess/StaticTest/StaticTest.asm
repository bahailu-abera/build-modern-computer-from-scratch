// Bootstrap
@256
D=A
@SP
M=D
// Translating StaticTest
// push constant 111
@111
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 333
@333
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 888
@888
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// pop static 8
// SP-- (move to topmost value)
@SP
M=M-1

// D = *SP (load top of stack value)
@SP
A=M
D=M

@StaticTest.8
M=D               // static[index] = y
// pop static 3
// SP-- (move to topmost value)
@SP
M=M-1

// D = *SP (load top of stack value)
@SP
A=M
D=M

@StaticTest.3
M=D               // static[index] = y
// pop static 1
// SP-- (move to topmost value)
@SP
M=M-1

// D = *SP (load top of stack value)
@SP
A=M
D=M

@StaticTest.1
M=D               // static[index] = y
// push static 3
@StaticTest.3
 // push M to the stack
D=M
// A = SP (point to top of stack)
@SP
A=M

M=D
// SP++ (move to next free stack slot)
@SP
M=M+1


// push static 1
@StaticTest.1
 // push M to the stack
D=M
// A = SP (point to top of stack)
@SP
A=M

M=D
// SP++ (move to next free stack slot)
@SP
M=M+1


// sub
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

M=M-D               // x - y → top of stack
// SP++ (move to next free stack slot)
@SP
M=M+1

// push static 8
@StaticTest.8
 // push M to the stack
D=M
// A = SP (point to top of stack)
@SP
A=M

M=D
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


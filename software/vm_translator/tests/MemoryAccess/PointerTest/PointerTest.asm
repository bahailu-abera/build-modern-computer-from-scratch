// Bootstrap
@256
D=A
@SP
M=D
// Translating PointerTest
// push constant 3030
@3030
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// pop pointer 0
// SP-- (move to topmost value)
@SP
M=M-1

// D = *SP (load top of stack value)
@SP
A=M
D=M

@3
M=D               // pointer[index] = y
// push constant 3040
@3040
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// pop pointer 1
// SP-- (move to topmost value)
@SP
M=M-1

// D = *SP (load top of stack value)
@SP
A=M
D=M

@4
M=D               // pointer[index] = y
// push constant 32
@32
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// pop this 2
@2
D=A
@THIS
D=D+M
@R13
M=D               // store target address in R13
// SP-- (move to topmost value)
@SP
M=M-1

// D = *SP (load top of stack value)
@SP
A=M
D=M

@R13
A=M
M=D               // *segment[index] = y
// push constant 46
@46
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// pop that 6
@6
D=A
@THAT
D=D+M
@R13
M=D               // store target address in R13
// SP-- (move to topmost value)
@SP
M=M-1

// D = *SP (load top of stack value)
@SP
A=M
D=M

@R13
A=M
M=D               // *segment[index] = y
// push pointer 0
@3
 // push M to the stack
D=M
// A = SP (point to top of stack)
@SP
A=M

M=D
// SP++ (move to next free stack slot)
@SP
M=M+1


// push pointer 1
@4
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

// push this 2
@2
D=A
@THIS
A=D+M
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

// push that 6
@6
D=A
@THAT
A=D+M
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


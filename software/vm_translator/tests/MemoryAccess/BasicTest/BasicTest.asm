// Bootstrap
@256
D=A
@SP
M=D
// Translating tests/MemoryAccess/BasicTest/BasicTest.vm
// push constant 10
@10
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// pop local 0
@0
D=A
@LCL
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
// push constant 21
@21
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 22
@22
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// pop argument 2
@2
D=A
@ARG
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
// pop argument 1
@1
D=A
@ARG
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
// push constant 36
@36
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// pop this 6
@6
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
// push constant 42
@42
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 45
@45
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// pop that 5
@5
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
// pop that 2
@2
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
// push constant 510
@510
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// pop temp 6
// SP-- (move to topmost value)
@SP
M=M-1

// D = *SP (load top of stack value)
@SP
A=M
D=M

@11
M=D               // temp[index] = y
// push local 0
@0
D=A
@LCL
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


// push that 5
@5
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

// push argument 1
@1
D=A
@ARG
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

// push this 6
@6
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


// push this 6
@6
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

// push temp 6
@11
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


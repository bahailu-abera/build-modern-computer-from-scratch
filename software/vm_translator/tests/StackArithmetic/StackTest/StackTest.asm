// Bootstrap
@256
D=A
@SP
M=D
// Translating tests/StackArithmetic/StackTest/StackTest.vm
// push constant 17
@17
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 17
@17
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// eq
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

D=M-D               // x - y
@EQ_TRUE_1
D;JEQ               // if x == y → jump
// A = SP (point to top of stack)
@SP
A=M

M=0                 // false (0)
@EQ_END_1
0;JMP
(EQ_TRUE_1)
// A = SP (point to top of stack)
@SP
A=M

M=-1                // true (-1)
(EQ_END_1)
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 17
@17
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 16
@16
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// eq
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

D=M-D               // x - y
@EQ_TRUE_2
D;JEQ               // if x == y → jump
// A = SP (point to top of stack)
@SP
A=M

M=0                 // false (0)
@EQ_END_2
0;JMP
(EQ_TRUE_2)
// A = SP (point to top of stack)
@SP
A=M

M=-1                // true (-1)
(EQ_END_2)
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 16
@16
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 17
@17
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// eq
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

D=M-D               // x - y
@EQ_TRUE_3
D;JEQ               // if x == y → jump
// A = SP (point to top of stack)
@SP
A=M

M=0                 // false (0)
@EQ_END_3
0;JMP
(EQ_TRUE_3)
// A = SP (point to top of stack)
@SP
A=M

M=-1                // true (-1)
(EQ_END_3)
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 892
@892
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 891
@891
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// lt
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

D=M-D               // x - y
@LT_TRUE_4
D;JLT               // if x < y → jump
// A = SP (point to top of stack)
@SP
A=M

M=0                 // false (0)
@LT_END_4
0;JMP
(LT_TRUE_4)
// A = SP (point to top of stack)
@SP
A=M

M=-1                // true (-1)
(LT_END_4)
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 891
@891
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 892
@892
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// lt
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

D=M-D               // x - y
@LT_TRUE_5
D;JLT               // if x < y → jump
// A = SP (point to top of stack)
@SP
A=M

M=0                 // false (0)
@LT_END_5
0;JMP
(LT_TRUE_5)
// A = SP (point to top of stack)
@SP
A=M

M=-1                // true (-1)
(LT_END_5)
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 891
@891
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 891
@891
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// lt
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

D=M-D               // x - y
@LT_TRUE_6
D;JLT               // if x < y → jump
// A = SP (point to top of stack)
@SP
A=M

M=0                 // false (0)
@LT_END_6
0;JMP
(LT_TRUE_6)
// A = SP (point to top of stack)
@SP
A=M

M=-1                // true (-1)
(LT_END_6)
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 32767
@32767
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 32766
@32766
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// gt
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

D=M-D               // x - y
@GT_TRUE_7
D;JGT               // if x > y → jump
// A = SP (point to top of stack)
@SP
A=M

M=0                 // false (0)
@GT_END_7
0;JMP
(GT_TRUE_7)
// A = SP (point to top of stack)
@SP
A=M

M=-1                // true (-1)
(GT_END_7)
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 32766
@32766
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 32767
@32767
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// gt
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

D=M-D               // x - y
@GT_TRUE_8
D;JGT               // if x > y → jump
// A = SP (point to top of stack)
@SP
A=M

M=0                 // false (0)
@GT_END_8
0;JMP
(GT_TRUE_8)
// A = SP (point to top of stack)
@SP
A=M

M=-1                // true (-1)
(GT_END_8)
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 32766
@32766
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 32766
@32766
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// gt
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

D=M-D               // x - y
@GT_TRUE_9
D;JGT               // if x > y → jump
// A = SP (point to top of stack)
@SP
A=M

M=0                 // false (0)
@GT_END_9
0;JMP
(GT_TRUE_9)
// A = SP (point to top of stack)
@SP
A=M

M=-1                // true (-1)
(GT_END_9)
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 57
@57
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 31
@31
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 53
@53
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

// push constant 112
@112
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
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

// neg
// SP-- (move to topmost value)
@SP
M=M-1

// A = SP (point to top of stack)
@SP
A=M

M=-M                // -y
// SP++ (move to next free stack slot)
@SP
M=M+1

// and
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

M=D&M             // x & y → top of stack
// SP++ (move to next free stack slot)
@SP
M=M+1

// push constant 82
@82
D=A // D = index
// A = SP (point to top of stack)
@SP
A=M

M=D  // push index
// SP++ (move to next free stack slot)
@SP
M=M+1

// or
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

M=D|M             // x | y → top of stack
// SP++ (move to next free stack slot)
@SP
M=M+1

// not
// SP-- (move to topmost value)
@SP
M=M-1

// A = SP (point to top of stack)
@SP
A=M

M=!M                // !y
// SP++ (move to next free stack slot)
@SP
M=M+1


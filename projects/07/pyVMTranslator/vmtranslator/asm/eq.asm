    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    D=M-D
    @JMPNUM
    D;JEQ
    @SP
    A=M-1
    M=0
    @JMPNUM_END
    0;JMP
(JMPNUM)
    @SP
    A=M-1
    M=-1
(JMPNUM_END)

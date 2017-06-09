#!/usr/local/bin/python3

# *** DESCRIPTION *** #
# contains all the types and names used by the VM-Translator
# ******************* #

# Commands
C_ARITHMETIC = 0
C_PUSH = 1
C_POP = 2
C_LABEL = 3
C_GOTO = 4
C_IF = 5
C_FUNCTION = 6
C_RETURN = 7
C_CALL = 8
C_ERROR = 9

# Segment names
SEG_LCL = 'local'
SEG_ARG = 'argument'
SEG_THIS = 'this'
SEG_THAT = 'that'
SEG_PTR = 'pointer'
SEG_TEMP = 'temp'
SEG_CONST = 'constant'
SEG_STATIC = 'static'

# Registers
REG_R0 = REG_SP = "R0"
REG_R1 = REG_LCL = "R1"
REG_R2 = REG_ARG = "R2"
REG_R3 = REG_THIS = REG_PTR = "R3"
REG_R4 = REG_THAT = "R4"
REG_R5 = REG_TEMP = "R5"
REG_R6 = "R6"
REG_R7 = "R7"
REG_R8 = "R8"
REG_R9 = "R9"
REG_R10 = "R10"
REG_R11 = "R11"
REG_R12 = "R12"
REG_R13 = REG_FRAME = "R13"
REG_R14 = REG_RET = "R14"
REG_R15 = REG_COPY = "R15"

# assembly code
ASM_ADD = "@SP\n" \
          "AM=M-1\n" \
          "D=M\n" \
          "A=A-1\n" \
          "M=D+M\n"

ASM_SUB = "@SP\n" \
          "AM=M-1\n" \
          "D=M\n" \
          "A=A-1\n" \
          "M=M-D\n"

ASM_NEG = "@SP\n" \
          "A=M-1\n" \
          "M=-M\n"

ASM_EQ = "@SP\n" \
         "AM=M-1\n" \
         "D=M\n" \
         "A=A-1\n" \
         "D=M-D\n" \
         "@EQTRUE{0}\n" \
         "D;JEQ\n" \
         "@SP\n" \
         "A=M-1\n" \
         "M=0\n" \
         "@EQEND{0}\n" \
         "0;JMP\n" \
         "(EQTRUE{0})\n" \
         "@SP\n" \
         "A=M-1\n" \
         "M=-1\n" \
         "(EQEND{0})\n"

ASM_GT = "@SP\n" \
         "AM=M-1\n" \
         "D=M\n" \
         "A=A-1\n" \
         "D=M-D\n" \
         "@GTTRUE{0}\n" \
         "D;JGT\n" \
         "@SP\n" \
         "A=M-1\n" \
         "M=0\n" \
         "@GTEND{0}\n" \
         "0;JMP\n" \
         "(GTTRUE{0})\n" \
         "@SP\n" \
         "A=M-1\n" \
         "M=-1\n" \
         "(GTEND{0})\n"

ASM_LT = "@SP\n" \
         "AM=M-1\n" \
         "D=M\n" \
         "A=A-1\n" \
         "D=M-D\n" \
         "@LTTRUE{0}\n" \
         "D;JLT\n" \
         "@SP\n" \
         "A=M-1\n" \
         "M=0\n" \
         "@LTEND{0}\n" \
         "0;JMP\n" \
         "(LTTRUE{0})\n" \
         "@SP\n" \
         "A=M-1\n" \
         "M=-1\n" \
         "(LTEND{0})\n"

ASM_AND = "@SP\n" \
          "AM=M-1\n" \
          "D=M\n" \
          "A=A-1\n" \
          "M=D&M\n"

ASM_OR = "@SP\n" \
          "AM=M-1\n" \
          "D=M\n" \
          "A=A-1\n" \
          "M=D|M\n"

ASM_NOT = "@SP\n" \
          "A=M-1\n" \
          "M=!M\n"

ASM_PUSH = "@SP\n" \
           "A=M\n" \
           "M=D\n" \
           "@SP\n" \
           "M=M+1\n"

ASM_PUSH_CONSTANT = "@{0}\n" \
                    "D=A\n" + \
                    ASM_PUSH

ASM_PUSH_LOCAL = "@LCL\n" \
                 "D=M\n" \
                 "@{0}\n" \
                 "A=D+A\n" \
                 "D=M\n" + \
                 ASM_PUSH

ASM_PUSH_ARGUMENT = "@ARG\n" \
                 "D=M\n" \
                 "@{0}\n" \
                 "A=D+A\n" \
                 "D=M\n" + \
                 ASM_PUSH

ASM_PUSH_THIS = "@THIS\n" \
                 "D=M\n" \
                 "@{0}\n" \
                 "A=D+A\n" \
                 "D=M\n" + \
                 ASM_PUSH

ASM_PUSH_THAT = "@THAT\n" \
                 "D=M\n" \
                 "@{0}\n" \
                 "A=D+A\n" \
                 "D=M\n" + \
                 ASM_PUSH

ASM_PUSH_POINTER = "@{0}\n" \
                 "D=M\n" + \
                 ASM_PUSH

ASM_PUSH_TEMP = "@R5\n" \
                 "D=A\n" \
                 "@{0}\n" \
                 "A=D+A\n" \
                 "D=M\n" + \
                 ASM_PUSH

ASM_PUSH_STATIC = "@{0}.{1}\n" \
                  "D=M\n" + \
                  ASM_PUSH

ASM_POP = "@R13\n" \
          "M=D\n" \
          "@SP\n" \
          "AM=M-1\n" \
          "D=M\n" \
          "@R13\n" \
          "A=M\n" \
          "M=D\n"

ASM_POP_CONSTANT = "@SP\n" \
                   "M=M-1\n" + \
                    ASM_POP

ASM_POP_LOCAL = "@LCL\n" \
                "D=M\n" \
                "@{0}\n" \
                "D=D+A\n" + \
                ASM_POP

ASM_POP_ARGUMENT = "@ARG\n" \
                "D=M\n" \
                "@{0}\n" \
                "D=D+A\n" + \
                ASM_POP

ASM_POP_THIS = "@THIS\n" \
                "D=M\n" \
                "@{0}\n" \
                "D=D+A\n" + \
                ASM_POP

ASM_POP_THAT = "@THAT\n" \
                "D=M\n" \
                "@{0}\n" \
                "D=D+A\n" + \
                ASM_POP

ASM_POP_POINTER = "@{0}\n" \
                "D=A\n" + \
                ASM_POP

ASM_POP_TEMP = "@R5\n" \
                "D=A\n" \
                "@{0}\n" \
                "D=D+A\n" + \
                ASM_POP

ASM_POP_STATIC = "@{0}.{1}\n" \
                 "D=A\n" + \
                ASM_POP

ASM_END_LOOP = "(END)\n" \
               "@END\n" \
               "0;JMP\n"

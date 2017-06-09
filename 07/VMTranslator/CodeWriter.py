#!/usr/local/bin/python3

# local imports
from LangSpecs import *

# system imports
import os

class CodeWriter:
    def __init__(self, outputfile):
        # opens output file => ready to write
        self._outputfile = open(outputfile, "w")
        self.labelcounter = [0, 0, 0]   # counter for labels used in eq, gt and lt
        self._vmfile = ""

    def set_file_name(self, filename):
        # informs codewriter that translation of new VM file started
        self._vmfile, ext = os.path.splitext(filename)
        pass

    def write_arithmetic(self, command):
        # writes assembly code that is the translation of given arithmetic command
        if command == "add":
            self._outputfile.write(ASM_ADD)
        elif command == "sub":
            self._outputfile.write(ASM_SUB)
        elif command == "neg":
            self._outputfile.write(ASM_NEG)
        elif command == "eq":
            self._outputfile.write(ASM_EQ.format(self.labelcounter[0]))
            self.labelcounter[0] += 1
        elif command == "gt":
            self._outputfile.write(ASM_GT.format(self.labelcounter[1]))
            self.labelcounter[1] += 1
        elif command == "lt":
            self._outputfile.write(ASM_LT.format(self.labelcounter[2]))
            self.labelcounter[2] += 1
        elif command == "and":
            self._outputfile.write(ASM_AND)
        elif command == "or":
            self._outputfile.write(ASM_OR)
        elif command == "not":
            self._outputfile.write(ASM_NOT)

    def write_push_pop(self, command, segment, index):
        # write assembly translation of given command (C_PUSH or C_POP)
        if command == "push":
            if segment == "constant":
                self._outputfile.write(ASM_PUSH_CONSTANT.format(index))
            elif segment == "local":
                self._outputfile.write(ASM_PUSH_LOCAL.format(index))
            elif segment == "argument":
                self._outputfile.write(ASM_PUSH_ARGUMENT.format(index))
            elif segment == "this":
                self._outputfile.write(ASM_PUSH_THIS.format(index))
            elif segment == "that":
                self._outputfile.write(ASM_PUSH_THAT.format(index))
            elif segment == "pointer":
                this_or_that = "THAT"
                if index == "0":
                    this_or_that = "THIS"
                self._outputfile.write(ASM_PUSH_POINTER.format(this_or_that))
            elif segment == "temp":
                self._outputfile.write(ASM_PUSH_TEMP.format(index))
            elif segment == "static":
                self._outputfile.write(ASM_PUSH_STATIC.format(self._vmfile, index))
        elif command == "pop":
            if segment == "constant":
                print("DEBUG: pop constant")
                self._outputfile.write(ASM_POP_CONSTANT.format(index))
            elif segment == "local":
                self._outputfile.write(ASM_POP_LOCAL.format(index))
            elif segment == "argument":
                self._outputfile.write(ASM_POP_ARGUMENT.format(index))
            elif segment == "this":
                self._outputfile.write(ASM_POP_THIS.format(index))
            elif segment == "that":
                self._outputfile.write(ASM_POP_THAT.format(index))
            elif segment == "pointer":
                this_or_that = "THAT"
                if index == "0":
                    this_or_that = "THIS"
                self._outputfile.write(ASM_POP_POINTER.format(this_or_that))
            elif segment == "temp":
                self._outputfile.write(ASM_POP_TEMP.format(index))
            elif segment == "static":
                self._outputfile.write(ASM_POP_STATIC.format(self._vmfile, index))

    def write_endloop(self):
        self._outputfile.write(ASM_END_LOOP)

    def close(self):
        # closes output file
        self._outputfile.close()



#!/usr/local/bin/python3

# system imports
import os
import sys

# local imports
import Parser
import CodeWriter
from LangSpecs import *


class VMTranslator:
    def __init__(self):
        pass

    def check_and_get_files(self, inputfile):
        if not os.path.exists(inputfile):
            # given path or file does not exist
            return -1
        elif os.path.isfile(inputfile):
            # given argument is a file
            if inputfile.endswith(".vm"):
                outputfile = inputfile.replace(".vm", ".asm")
                return [inputfile], outputfile
            else:
                return -1
        elif os.path.isdir(inputfile):
            # given argument is a directory
            file_list = []
            for file in os.listdir(inputfile):
                if file.endswith(".vm"):
                    file_list.append(os.path.join((inputfile + "/"), file))
            return file_list, inputfile + "/" + inputfile.split("/")[-1] + ".asm"
        else:
            # given argument exists but is neither a file nor a directory
            # don't know what should happen here, but better try to catch every possibility
            return -1

    def translate(self, inputfile, code_writer):
        parser = Parser.Parser(inputfile)
        while parser.has_more_commands():
            parser.advance()
            self._write_code(parser, code_writer)
        code_writer.write_endloop()

    def _write_code(self, parser, code_writer):
        command = parser.command_type()
        if command == C_ARITHMETIC:
            code_writer.write_arithmetic(parser.arg1())
        elif command in [C_PUSH, C_POP]:
            code_writer.write_push_pop(parser.current_command(), parser.arg1(), parser.arg2())

    def translate_files(self, inputfiles, outputfile):
        code_writer = CodeWriter.CodeWriter(outputfile)
        # TODO: initialize code writer in chapter 8
        if inputfiles:  # list of inputfiles is not empty
            for file in inputfiles:
                self.translate(file, code_writer)
        code_writer.close()

    def main(self):
        if len(sys.argv) != 2:
            print("ERROR: not enough arguments!\nUsage: python VMTranslator /path/to/file/or/directory\n"
                  "NOTE: If Python 3 is installed alongside Python 2 you may need to use python3 VMTranslator ...")
            exit(0)
        else:
            inputfiles, outputfile = self.check_and_get_files(sys.argv[1])
            self.translate_files(inputfiles, outputfile)


if __name__ == '__main__':
    vmtranslator = VMTranslator()
    vmtranslator.main()

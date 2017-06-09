#!/usr/local/bin/python3

# ** DESCRIPTION ** #
# ** -> reads VM commands
# ** -> parses them and provides access to their components
# ** -> removes white space and comments
# ***************** #

# system imports
import re
# local imports
from LangSpecs import *


class Parser:
    # mapping of commands to their number of arguments
    _cmd_no_args = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not',
                    'return']  # TODO: return needed in chapter 8
    _cmd_one_arg = ['label', 'goto', 'if-goto']  # TODO: all three needed in chapter 8
    _cmd_two_args = ['push', 'pop', 'function', 'call']  # TODO: function and call needed in chapter 8

    # command types
    _command_types = {  # arithmetic/boolean commands
        'add': C_ARITHMETIC, 'sub': C_ARITHMETIC, 'neg': C_ARITHMETIC,
        'eq': C_ARITHMETIC, 'gt': C_ARITHMETIC, 'lt': C_ARITHMETIC,
        'and': C_ARITHMETIC, 'or': C_ARITHMETIC, 'not': C_ARITHMETIC,
        # memory access commands
        'pop': C_POP, 'push': C_PUSH,
        # program flow commands TODO: needed in chapter 8
        'label': C_LABEL, 'goto': C_GOTO, 'if-goto': C_IF,
        # function calling commands
        'function': C_FUNCTION, 'call': C_CALL, 'return': C_RETURN}

    # regular expressions to match specified parts of the input file
    _regex_comment = re.compile('//.*$')
    _regex_number = r'\d+'
    _regex_label = r'[\w\-.]+'
    _regex_word = re.compile(_regex_number + '|' + _regex_label)

    def __init__(self, inputfile):
        with open(inputfile, "r") as infile:  # read whole file into memory (linewise)
            self._lines = infile.readlines()
        self._lines = self._read_and_clear_input(self._lines)
        self._current_line = None
        self._current_command = None

    def _read_and_clear_input(self, lines):
        cleared_input = []
        for line in lines:
            line = str(line)
            if not line.strip() == "":  # remove leading and trailing whitespaces => string is empty = empty line
                if not re.match(self._regex_comment, line):     # ignore comments
                    cleared_input.append(line)  # should be only lines with commands now
        return cleared_input

    def _split_line(self, line):
        return str(line).split()   # split line into its pieces (removes whitespaces)

    def has_more_commands(self):
        # returns boolean
        # true if there are more commands in input
        # false if not
        return self._lines != []    # there are lines left

    def current_command(self):
        return self._current_command

    def advance(self):
        # reads next command from input and makes it current command => only if has_more_commands is true
        if self.has_more_commands():
            self._current_line = self._lines.pop(0)  # pop first element/line of list
            self._current_line = self._split_line(self._current_line)
            self._current_command = self._current_line[0]

    def command_type(self):
        # returns type of current VM command
        # C_ARITHMETIC for all arithmetic commands
        # C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, C_FUNCTION, C_RETURN, C_CALL
        return self._command_types[self._current_command]

    def arg1(self):
        # Returns first argument of current command as string
        # in case of C_ARITHMETIC: command itself (add, sub, etc.)
        # => should not be called if current command is C_RETURN
        if not self.command_type() == C_RETURN:
            if self.command_type() == C_ARITHMETIC:
                return self._current_command
            elif self._current_command in self._cmd_one_arg or self._current_command in self._cmd_two_args:
                return self._current_line[1]
            else:
                return None

    def arg2(self):
        # Returns second argument of current command as int
        # should be called only if current command is C_PUSH, C_POP, C_FUNCTION, C_CALL
        if self._current_command not in self._cmd_two_args:
            return None
        else:
            return self._current_line[2]

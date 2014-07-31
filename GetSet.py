#!usr/bin/python

import sys

args = list(sys.argv)

types = ['int', 'std::string', 'double', 'float']

def parse_classname(f):
    File = open(f,'r')
    lines = File.readlines();
    for line in lines:
        currline = line.split()
        if len(currline) > 0:
            if currline[0] == 'class':
                classname = currline[1]
                File.close()
                return classname


def parse_variables(f):
    File = open(f,'r')
    lines = File.readlines();
    variables = []
    for line in lines:
        currline = line.split()
        if len(currline) > 0:
            if currline[0] in types:
                if '(' not in currline[1]:
                    variables.append(currline)
    File.close()
    return variables

def prep_vars(classname, variables):
    classname = classname + '::'
    functions = []
    functions.append('#include "' + classname[:-2] + '.h"\n\n')
    for variable in variables:
        declarations.append(variable[0] + " " + variable[1][:-1] + '() const;')
        functions.append(variable[0] + " " + classname + variable[1][:-1] + '() const {\n\treturn ' + variable[1] + '\n}\n\n')
    return functions

def write_to_file(filename):
    filename = filename[:-1] + 'cpp'
    try:
        with open(filename, 'r') as f:
            f = open(filename, 'a')
            for function in functions[1:]:
                f.write(function)
            f.close()
    except IOError as e:
            with open(filename, 'w') as f:
                for function in functions:
                    f.write(function)
                f.close()


if len(args) > 1:
    for filenm in args[1:]:
        filename = filenm
        classname = parse_classname(filename)
        variables = parse_variables(filename)

        declarations = [] #filled within prep_vars function
        functions = prep_vars(classname, variables)
        write_to_file(filename)
else:
    print "Enter each filename.h seperated by a space as arguments\nE.g Python GetSet.py file.h file2.h file3.h"

from sys import argv
from os import walk
from os.path import isdir, isfile, join


patterns = {"\\lambda" : u"\u03bb", "\\theta" : u"\u03f4"}
class ArgumentError(Exception):
    pass


def refactor_file(filename):
    print(f'Refactoring {filename}')
    with open(filename, 'r') as curfile:
        data = curfile.read()
    for pattern in patterns:
        data.replace(pattern, patterns[pattern])
    with open(filename, "w") as curfile:
        curfile.write(data)

if len(argv) is not 3:
    raise ArgumentError("Please use command: python Script.py [file or directory]")

if isfile(argv[2]):
    refactor_file(argv[2])
elif isdir(argv[2]):
    for root, dirs, files in walk(argv[2]):
        for filename in files:
            curfile = join(root, filename)
            refactor_file(curfile)

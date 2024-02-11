import argparse
import glob
import textwrap

# Continuation of **CommandLineArgumentsUsingSysArgv.py*

parser = argparse.ArgumentParser(description=textwrap.dedent('''Program to Learn Argument Parser'''),
                                 prog='CommandLIneArgumentsUsingArgParse.py',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog='Please consider this as an example')


parser.add_argument('-o', '--option1', required=False)
parser.add_argument('-p', '--option2', required=False)
parser.add_argument('-q', '--option3', required=False)
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-f', '--flag1', help='set flag1', required=True)
parser.add_argument('files', nargs='*')  # Postional argumet

args = parser.parse_args()


files = list[args.files]

print(files)

# print(args.files, args.option1, args.option2, args.option3, args.verbose)


print(args)


files = list[args.files]

print('-----------')

print(files)

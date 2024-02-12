import argparse
import textwrap

parser = argparse.ArgumentParser(description=textwrap.dedent("""DESCRIPTION
                                                             
     The cat utility reads files sequentially, writing them to the standard output.  The file operands are processed in command-line order.  If
     file is a single dash (‘-’) or absent, cat reads from the standard input.  If file is a UNIX domain socket, cat connects to it and then reads
     it until EOF.  This complements the UNIX domain binding capability available in inetd(8)"""))


parser.add_argument('files', metavar='F', type=str, nargs='+', help='File or file names')
parser.add_argument('-n', '--numbers', action='store_true', help='Print the line numbers')


args = parser.parse_args()


line_nubmer = 1

print(args.files)

for file in args.files:
    file_temp = open(file)
    print('---------------------------------------------------------')
    print("\tPrinting File", file)
    if args.numbers:
        for line in file_temp.readlines():
            print(f"\t{line_nubmer} \t {line}")
            line_nubmer += 1
    else:
        print(file_temp.read())
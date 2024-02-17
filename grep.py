import argparse
import re
import sys
from pathlib import Path
import rglob





def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('pattern', type=str, nargs=1, help="pattern to search for")
    parser.add_argument('path', metavar='FILE PATH OR DIRECTORY', type=str, nargs=1)
    parser.add_argument('-r', action='store_true', help="recursively search subdirectories")


    return parser.parse_args()



args = parse_args()

def search_in_file(f, pattern):
    try:
         with open(f, 'r') as file:
                    for line_number, line in enumerate(file, 1):
                        if re.search(pattern, line):
                            print(f"{f}:{line_number}: {line.strip()}")
    except UnicodeDecodeError:
         pass
       

def grep(pattern, start_path, recursive):
    print(f"Searching for pattern {pattern} in destination {start_path}")
    start_path = Path(start_path)

    if recursive and start_path.is_dir():

        for f in start_path.rglob("*"):
            if f.is_file():
                 search_in_file(f=f,pattern=pattern)
                
    else:
        if start_path.is_file():
            search_in_file(f=start_path,pattern=pattern)
        if start_path.is_dir():
             for f in start_path.glob("*"):
                  if f.is_file():
                    search_in_file(f=f, pattern=pattern)




if __name__ == "__main__":
    args = parse_args()
    grep(args.pattern[0], args.path[0], args.r)
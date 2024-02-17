#find . –name "*.rb" –exec rm {} \;

import os
import subprocess
import glob 
import argparse
from pathlib import Path
import sys 



parser = argparse.ArgumentParser(prog="find", 
                                 description="Implementaion of find command in python",
                                 epilog="Found it Good to do this")



parser.add_argument('directory', metavar='DIR', type=str, nargs=1)
parser.add_argument('-name', required=True, help="Pattern or name of files ")
parser.add_argument('-type', metavar='TYPE', type=str, choices=['f', 'd'], required=False)
parser.add_argument('-print', required=False, help="Prints the name of file", action='store_true')
parser.add_argument('-exec', required=False, help="Execute Some Comamnd")



args = parser.parse_args()


#print(args.directory)



def find(directory=args.directory[0], pattern=args.name, type=args.type, temp_print=args.print, command=args.exec):
    #print(directory,name, type, temp_print, exec)
    start_directory = directory
    #print(start_directory)
     
    if start_directory == ".":
        start_directory = os.getcwd()
        #print(start_directory)
        #print(os.getcwd())
    else:
        start_directory = os.path.join(start_directory)

        #print(start_directory)
    
   
    if os.path.exists(start_directory) and args.type == 'f':
        #print(pattern)
        search_path = os.path.join(start_directory, pattern)
        #print(search_path)
        files = glob.glob(search_path, recursive=True)
        if temp_print:
            for file in files:
                print(file)
    else:
        print("This Directory does not exist, please enter a valid path")
    if command:
        for file in files:
            
            subprocess.run([command, file])

        



if __name__ == "__main__":
     find()




    # geeksGFG@123






# Exercise Goals
# 1. implement -h
# 2. atleast 3 arguments which are flags
# 3. atlease 3 arguments which are options , they do take an argument and set a variable in script
# 4. Additional postional arguments , which are list of files at the end of all the - style arugments and can hangle terminal widlcards liek */.txt


# Tip : Sys.argv is mutable , since it is a list , so we can use pop


# args = sys.argv

# print(type(args))
# length = len(args)
# print("The length is {}".format(length))
# print(args)

# for arg in args:
#     print(arg)

# print("The number of arguments entered is {}".format(len(args)))
import sys
import glob


def print_help():
    print("Usage: python3 script.py [OPTIONS]... [FILES]...")
    print("Options:")
    print("     -h, --help      Show this help message and Exit")
    print("     -f, --flag1     Description of flag 1")
    print("     -g, --flag2     Description of flag2")
    print("     -t, --flag3     Description of flag3")
    print("Arguments:")
    print("     -o, --option1 <value>       Description of option 1")
    print("     -p, --option2 <value>       Description of option 2")
    print("     -1, --option3 <value>       Description of option 3")
    print("     -p, --option2 <value>       Description of option 2")


def parse_arguments():
    flags = {"-h", "--help", "-f", "--flag1", "-g", "--flag2", "-t", "--flag3"}
    options = {"-o", "--option1", "-p", "--option2", "-q", "--option3"}

    # Removing the Script name 
    sys.argv.pop(0)
    while sys.argv and sys.argv[0] in flags:
        flag = sys.argv.pop(0)
        if flag in {"-h", "--help"}:
            print_help()
            sys.exit(0)
        elif flag in {"-f", "--flag1"}:
            pass 
        elif flag in {"-g", "--flag2"}:
            pass 
        elif flag in {"-t", "--flag3"}:
            pass 
    
    options_dict = {}
    while sys.argv and sys.argv[0] in options:
        option = sys.argv.pop(0)
        value = sys.argv.pop[0]
        # Option handlind 
        if option in {"-o", "--option1"}:
            options_dict["option1"] = value 
        elif option in {"-p", "--option2"}:
            options_dict["optino2"] = value
        elif option in {"-q", "--option3"}:
            options_dict["option3"] = value 

    
    # Positional arguments (files)
    files = []
    while sys.argv:
        files.extend(glob.glob(sys.argv.pop(0)))

    return options_dict, files 


if __name__ == "__main__":
    options, files = parse_arguments()
    print("Options:", options)
    print("Files:", files)












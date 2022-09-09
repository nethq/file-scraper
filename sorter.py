from codecs import utf_8_decode
import codecs
from encodings import utf_8
from operator import contains, indexOf
import os
import sys
#for mus
def args():
    # -m (sf-single file / dir-directory) 
    # -i input file
    # -o output file
    # -p pattern
    # -id directory
    # -od output directory
    for arg in sys.argv:
        if arg == "-h":
            print("-m (sf-single file / dir-directory) -i input file -o output file -p pattern -id directory -od output directory")
            sys.exit()
        if arg == "-m":
            if sys.argv[indexOf(sys.argv,arg)+1] == "sf":
                single_file()
            elif sys.argv[indexOf(sys.argv,arg)+1] == "dir":
                directory()
            else:
                print("Invalid choice")

def main():
    args()
    print("1. Single file")
    print("2. Directory")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        single_file()
    elif choice == "2":
        directory()
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid choice")
        main()

def directory():
    print("Directory")
    directory_name = input("Enter path: ")
    visited_files = [] # list of files already visited
    if os.path.isdir(directory_name):
        print("Directory found")
        patt = pattern()
        if patt is not None:
            for root, dirs, files in os.walk(directory_name):
                for file in files:
                    if file not in visited_files:
                        visited_files.append(file)
                        task_start(patt,os.path.join(root,file))
    
    else:
        print("Directory not found")
        directory()

def single_file():
    print("Single file")
    file_name = input("Enter file name: ")
    if os.path.isfile(file_name):
        print("File found")
        patt = pattern()
        if patt is not None:
            task_start(patt,file_name)
    else:
        print("File not found")
        single_file()

def pattern():
    print("Default pattern is extraction by email domain provider. Would you like another pattern?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Enter pattern: #@*.ru# - will yield all different ru email providers")
        pattern = input()
        return pattern
    elif choice == "2":
        print("Default pattern will be used")
        return "@*:"
    else:
        print("Invalid choice")
        pattern()

def task_start(pattern,file_name):
    print("Starting task on {" + file_name + "} and pattern {" + pattern + "}")
    result_lines = []

    pattern_start = str(pattern).split("*")[0]
    pattern_end = str(pattern).split("*")[1]
    with codecs.open(file_name, 'r', encoding='utf-8',errors='ignore') as f:
        try:
            for line in f:
                if ":" in line and len(line)>1:
                    if pattern_start in line and pattern_end in line[indexOf(line,pattern_start)+2:]:
                        pattern_lookup_result = line.split(pattern_start)[1].split(pattern_end)[0]
                        f = open(pattern_lookup_result.lower().replace("\n","").replace(".","") + ".txt","a")
                        f.write(line)
                        f.close()
                        
        except Exception as e:
            print(e)
            print("Error in line: " + line)

main()
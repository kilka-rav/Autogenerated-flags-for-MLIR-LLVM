import os

def generate_git_diff():
    command = "git diff origin/main > git_info.diff"
    os.system(command)

def find_name(line):
    start = line.index('/')
    end = line.rindex(' ')
    return line[start:end]

def parser():
    file = open("git_info.diff", 'r')
    name = ""
    read_file = 0
    for line in file:
        if line.find("diff --git") != -1 and read_file == 0:
            name = find_name(line)
            read_file = 1
            print(name)
        elif line.find("diff --git") != -1 and read_file == 1:
            name = ""
            read_file = 0
        elif line[0] == "+" and read_file == 1:
            print(line, end= ' ')
    file.close()
if __name__ == "__main__":
    #generate_git_diff()
    parser()

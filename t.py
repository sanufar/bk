import sys

def tagsearch(stdout):
    for i in stdout[1:-2].split(","):
        print(i)

data = sys.stdin.read()
tagsearch(data)

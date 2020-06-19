import sys
import os

def readfilecontent():
    filename_logs = "logs\\test.log"
    with open(filename_logs) as f:
        content = f.readlines()

    for line in content:
        print(line)

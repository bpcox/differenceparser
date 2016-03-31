#!/usr/bin/env python

import os


#loop through
for i in os.listdir(os.getcwd()):
    if i.endswith(".log"):
        try:
            file = open(i)
            lines = file.readlines()
            total = int(lines[0].split(" ",1)[0])
            duplicate = int(lines[3].split(" ",1)[0])
            result = total-duplicate
            print "Result for {}: {}\n".format(i, result)
        except:
            print "Invalid File {}\n".format(i)


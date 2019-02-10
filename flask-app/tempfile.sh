#!/usr/bin/env python
import os
import subprocess
subprocess.call("rm -f ./a.out", shell=True)
retcode = subprocess.call("/usr/bin/g++ walk.cc", shell=True)
if retcode:
 print("failed to compile walk.cc")
 exit
subprocess.call("rm -f ./output", shell=True)
retcode = subprocess.call("./test.sh", shell=True)
print ("Score: " + str(retcode) + " out of 2 correct.")
print("*************Original submission*************")
with open('uploads/walk.cc','r') as fs:
 print(fs.read())
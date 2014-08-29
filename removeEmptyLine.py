import os
import argparse
import sys

originalFile = "C:\\Users\\david\\git\\AppContextCode\\MyFlowdroid\\packageName"
targetFile = "C:\\Users\\david\\git\\AppContextCode\\MyFlowdroid\\packageName_withoutSpace"
with open(targetFile, "a") as myfile:
    a=open(originalFile,'rb')
    lines = a.readlines()
    for line in lines:
        if line.strip():
    	    myfile.write(line[:-1])

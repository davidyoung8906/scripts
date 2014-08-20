import os
import argparse
import sys
import datetime
import time
import subprocess, threading
import shlex
import traceback


currentdir = os.getcwd()
num = 0
rootdir = "D:\\Programming\\Workspace\\CommandLine\\AppContextICSE\\InstrumentedApp"
for path, subdirs, files in os.walk(rootdir):
    for name in files:
        if name.endswith(".apk"):
            num = num +1
            filepath = os.path.join(path, name)
            #print filepath
            saveout = sys.stdout
            p, filename = os.path.split(filepath)
            #print filename
            a, dir = os.path.split(p)

            platformPath = "D:\\Programming\\Corpus\\android-platforms-soot"
            dirPath= os.path.join(currentdir,"FactorResult",dir);
            print dirPath
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)

            cmd = 'java -jar FactorExtract.jar '+filepath+' '+platformPath
            outputfile = os.path.join(dirPath,filename+"_out.log")
            errfile = os.path.join(dirPath,filename+"_err.log")
            open(outputfile, 'w').close()
            open(errfile, 'w').close()
            process = subprocess.Popen(cmd, shell=True, stdout = file(outputfile, 'w+'), stderr = file(errfile, 'w+')) #
            (output, error) = process.communicate() 
            print output #"Out:'%s'" % 
            print error #"Err:'%s'" % 

print "number of APK: ", str(num);
            
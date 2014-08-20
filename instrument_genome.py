import os
import argparse
import sys
import datetime
import time
import subprocess, threading
import shlex
import traceback


currentdir = os.getcwd()
rootdir = "D:\\Programming\\Corpus\\MalGenomeSamples\\samples"
for path, subdirs, files in os.walk(rootdir):
    for name in files:
        if name.endswith(".apk"):
            
            filepath = os.path.join(path, name)
            #print filepath
            saveout = sys.stdout
            p, filename = os.path.split(filepath)
            #print filename
            a, dir = os.path.split(p)
            #print dir
            

            platformPath = "D:\\Programming\\Corpus\\android-platforms-soot"
            dirPath= os.path.join(currentdir,dir);
            print dirPath
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)
            # print "decompiling"	
            # cmd1 = './apktool d ' + filepath + ' '+filepath1;
            # fp1 = os.popen(cmd1)
            # res1 = fp1.read()
            # print res1
            
            cmd = 'java -jar IfStmtInstrument.jar '+filepath+' '+platformPath+' '+dirPath
            outputfile = os.path.join(dirPath,filename+"_out.log")
            errfile = os.path.join(dirPath,filename+"_err.log")
            open(outputfile, 'w').close()
            open(errfile, 'w').close()
            process = subprocess.Popen(cmd, shell=True, stdout = file(outputfile, 'w+'), stderr = file(errfile, 'w+')) #
            (output, error) = process.communicate() 
            print output #"Out:'%s'" % 
            print error #"Err:'%s'" % 
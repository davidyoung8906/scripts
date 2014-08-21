import os
import argparse
import sys
import datetime
import time
import subprocess, threading
import shlex
import traceback

class Command(object):

    cmd = None
    process = None
    status = None
    output, error = '', ''

    def __init__(self, cmd):
        # if isinstance(cmd, basestring):
        #     cmd = shlex.split(cmd)
        self.cmd = cmd
        #self.process = None

    def run(self, timeout, outputfile, errfile):
        def target():
            print 'Thread started'
            try:
                print self.cmd
                open(outputfile, 'w').close()
                open(errfile, 'w').close()
                self.process = subprocess.Popen(self.cmd, shell=True, stdout = file(outputfile, 'w+'), stderr = file(errfile, 'w+')) #
                (self.output, self.error) = self.process.communicate() #
                self.status = self.process.returncode
                print self.output #"Out:'%s'" % 
                print self.error #"Err:'%s'" % 
                print 'Thread finished'
            except:
                self.error = traceback.format_exc()
                self.status = -1      
                print self.error  

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print 'Terminating process'
            self.process.kill() #terminate
            thread.join()
        print self.status


currentdir = os.getcwd()
num = 0
rootdir = "D:\\Programming\\Workspace\\CommandLine\\AppContextICSE\\InstrumentedApp\\VirusShare2"
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
            dirPath= os.path.join(currentdir,"FactorResult_VirusShare2",dir);
            print dirPath
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)

            outputfile = os.path.join(dirPath,filename+"_out.log")
            errfile = os.path.join(dirPath,filename+"_err.log")
            cmd = 'java -jar Main.jar factor '+filepath+' '+platformPath
            command = Command(cmd)
            command.run(timeout=1800,outputfile = outputfile, errfile = errfile)
            

print "number of APK: ", str(num);
            
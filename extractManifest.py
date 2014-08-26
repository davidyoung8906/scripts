import os
import argparse
import sys

currentdir = os.getcwd()
rootdir = os.path.join(currentdir, "Random_Sample")
for path, subdirs, files in os.walk(rootdir):
    for name in files:
        if name.endswith(".apk"):
            filepath = os.path.join(path, name)        	
            p, filename = os.path.split(filepath)
            manifest_dir = os.path.join(currentdir, "Decomplied", dir)
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)
            filepath1 = os.path.join(manifest_dir, filename)
            cmd1 = 'apktool d   ' + filepath + ' '+filepath1;
            fp1 = os.popen(cmd1)
            res1 = fp1.read()
            print res1
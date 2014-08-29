import os
import argparse
import sys
import shutil

currentdir = os.getcwd()
rootdir = "D:\\Programming\\Workspace\\CommandLine\\AppContextICSE\\InstrumentedAppAPKOnly\\InstrumentedApp1" 
for path, subdirs, files in os.walk(rootdir):
    for name in files:
        if name.endswith(".apk"):
            filepath = os.path.join(path, name)        	
            p, filename = os.path.split(filepath)
            a, dir = os.path.split(p)
            manifest_dir = os.path.join(currentdir, "Decomplied", dir)
            filepath1 = os.path.join(manifest_dir, filename)
            manifest_file = os.path.join(filepath1, "AndroidManifest.xml")
            destPath = os.path.join("D:\\Programming\\Workspace\\CommandLine\\AppContextICSE", "GenomeManifest",dir,filename)
            if not os.path.exists(destPath):
                os.makedirs(destPath)
            destManifest = os.path.join(destPath, "AndroidManifest.xml")
            destapk = os.path.join(destPath, name)
            shutil.copyfile(filepath, destapk);
            shutil.copyfile(manifest_file, destManifest);
            
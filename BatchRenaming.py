import os
import argparse
import sys
import datetime
import time
import subprocess, threading
import shlex
import traceback


currentdir = os.getcwd()
rootdir = "D:\\Programming\\Corpus\\VirusShare_Android_20130506"
for path, subdirs, files in os.walk(rootdir):
    for name in files:
    	filepath = os.path.join(path, name)
    	os.rename(filepath, filepath+".apk")
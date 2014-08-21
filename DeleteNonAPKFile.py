import os
import argparse
import sys
import datetime
import time
import subprocess, threading
import shlex
import traceback


currentdir = os.getcwd()
rootdir = "F:\\Workspace\\CommandLine\\AppContextICSE\\InstrumentedApp1"
for path, subdirs, files in os.walk(rootdir):
    for name in files:
        if not name.endswith(".apk"):
            filepath = os.path.join(path, name)
            os.remove(filepath)
    	
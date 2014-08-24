import os
import argparse
import sys

#parser = argparse.ArgumentParser(description='Generate SVG of callgraph and sub-callgraph for given APK')
#saveout = sys.stdout
currentdir = os.getcwd()
rootdir = os.path.join(currentdir, "Random_Sample")
for path, subdirs, files in os.walk(rootdir):
    for name in files:
        if name.endswith(".apk"):
            filepath = os.path.join(path, name)
            print filepath
            saveout = sys.stdout
            p, filename = os.path.split(filepath)
            print filename
            a, dir = os.path.split(p)
            print dir
            filepath1 = os.path.join(currentdir, "CG", dir, filename)
            if os.path.exists(filepath1):
                continue
            print filepath1
            platformPath = os.path.join(currentdir, "platforms")

            cmd1 = 'apktool d   ' + filepath + ' '+filepath1;
            fp1 = os.popen(cmd1)
            res1 = fp1.read()
            print res1

# Build call graph for whole app
# D:\Programming\Workspace\CommandLine\ContextStudy>java -jar constructCG.jar D:\P
# rogramming\Malwares\samples\Pjapps\a7f33bd0441b5151f73fc7f1b30fbf35a9be76e0.apk
# D:\Programming\Tools\ADT_bundle\sdk\platforms D:\Programming\Malwares\decompile\
# a7f33bd0441b5151f73fc7f1b30fbf35a9be76e0.apk\wholeCG.dot

            fsock = open(os.path.join(filepath1,"output.log"), 'w')
            sys.stdout = fsock    
            cmd = 'java -jar constructCG.jar ' + filepath + ' '+platformPath+' '+filepath1+'/wholeCG.dot'
            fp = os.popen(cmd)
            res = fp.read()
            print res
            fsock.close()
            sys.stdout = saveout
            print 'finish callgraph of '+ filename



            cmd2 = 'java -jar findmethod.jar ' +  filepath1
            fp2 = os.popen(cmd2)
            res2 = fp2.read()
            print res2

#build callgraph for methods
            ins = open( os.path.join(filepath1,"relatedMethod.txt"), "r" )
            for line in ins:
                fsock3 = open(os.path.join(filepath1,"subCalloutput.log"), 'w')
                sys.stdout = fsock3    
                cmd3 = 'java -jar constructCG.jar ' + os.path.join(path, filename) + ' '+platformPath+' '+ filepath1 + ' '+line
                fp3 = os.popen(cmd3)
                res3 = fp3.read()
                print res3
                fsock3.close()
                sys.stdout = saveout
                print 'finish callgraph of '+ filename + ' ' +line
            ins.close()

#delete duplicate edges
            for path1, subdirs1, files1 in os.walk(filepath1):
                for filename4 in files1:
                    if filename4.endswith(".dot"):
                        os.chdir(path1)
                        lines_seen = set() # holds lines already seen
                        outfile = open('nonduplicate_'+filename4, "w")
                        for line in open(filename4, "r"):
                            if line not in lines_seen:
                                outfile.write(line)
                                lines_seen.add(line)
                        outfile.close()
                        print('remove_duplicate '+filename4)
                        if os.path.getsize('nonduplicate_'+filename4) < 102400:
                            cmd = 'dot -Tsvg '+ 'nonduplicate_'+filename4 + ' -o ' + filename4+'.svg'
                            fp = os.popen(cmd)
                            res = fp.read()
                            print res
                        os.chdir(currentdir)
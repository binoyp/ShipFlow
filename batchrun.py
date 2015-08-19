# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 12:26:52 2015

@author: Binoy
"""
import subprocess
def runShipflow(configpath):
    SFLOW = r"C:\FLOWTECH\SHIPFLOW6.0.01-x86_64\bin\shipflow.bat"
    
    cmd = SFLOW + ' -c '+configpath
    pr = subprocess.Popen(cmd,shell= 1, stdout = subprocess.PIPE)
    for l in iter(pr.stdout.readline,''):
        print l
    pr.wait()
    
    print pr.returncode
    
#pr = subprocess.Popen(r"C:\FLOWTECH\SHIPFLOW6.0.01-x86_64\bin\shipflow.bat -c D:\Internship-Shipflow\fullhull\configfullhull", shell =1, stdout= subprocess.PIPE)
if __name__ == "__main__":
    
    path = r"D:\Internship-Shipflow\fullhull\configfullhull"
    runShipflow(path)
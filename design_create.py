# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 11:22:41 2015

@author: Binoy
"""

import re, os, shutil

config_file = open('configfullhull')

c_dat = config_file.read()

dvars = ['titl=......','stat=\d\d', 'poin=\d\d']
patterns = [re.compile(pat) for pat in dvars]
off_file = r"D:\Internship-Shipflow\fullhull\hullfull.shf"


for s in ['40','50','60']:


    for p in ['15','10','25']:
        _dir = os.path.join(os.getcwd(),'s'+s+'p'+p)
        if not os.path.exists(_dir):
            os.makedirs(_dir)
        shutil.copy2(off_file,_dir)
        fpath = os.path.join(_dir,'config-s'+s+'-p'+p)
        outfile = open(fpath,'w')

        for line in c_dat.split('\n'):
            match1 = re.search(patterns[1], line)
            match0 = re.search(patterns[0], line)
            match2 = re.search(patterns[2], line)            
            if match1:
                #print line.replace(match.group(),'____')
                print patterns[1].sub('stat='+s ,line)
                outfile.write(patterns[1].sub('stat='+s ,line))
                outfile.write('\n')
            elif match0:
                #print line.replace(match.group(),'____')
                print patterns[0].sub('titl="stations'+s+'points='+p+'"' ,line)
                outfile.write(patterns[0].sub('"stations'+s+'points='+p+'"' ,line))
                outfile.write('\n')
            elif match2:
                #print line.replace(match.group(),'____')
                print patterns[2].sub('poin='+p ,line)
                outfile.write(patterns[0].sub('"stations'+s+'points='+p+'"' ,line))
                outfile.write('\n')
            else:
                print line
                outfile.write(line)
                outfile.write('\n')
                
    #            print line
        outfile.close()
        

#print c_dat

config_file.close()
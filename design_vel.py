# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 11:22:41 2015

@author: Binoy
"""

import re, os, shutil

config_file = open('config_')

c_dat = config_file.read()
gpat = re.compile('vship')
dvars = ['titl=......','\[x\]']
patterns = [re.compile(pat) for pat in dvars]
off_file = r"C:\Users\admin\Desktop\BinoySFLOW\fullhull\hullfull.shf"
fname = open('filenames.txt','w')

for vel in [str(v) for v in range(2,12)]:
    _dir = os.path.join(os.getcwd(),'velocity='+vel+'knots')
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    shutil.copy2(off_file,_dir)
    fpath = os.path.join(_dir,'config-vel-'+vel+'kn')
    fname.write(fpath+'\n')
    outfile = open(fpath,'w')

    for line in c_dat.split('\n'):
        gmatch = re.search(gpat, line)
        match0 = re.search(patterns[0], line)
        matchvel = re.search(patterns[1], line)


        if match0:
            #print line.replace(match.group(),'____')
#                print(patterns[0].sub('titl="stations'+s+'points='+p+'"' ,line))
            line = patterns[0].sub('titl="Velocity='+vel+'"' ,line)
        if gmatch:   
#                if match1:
#                    #print line.replace(match.group(),'____')
#    #                print(patterns[1].sub('stat='+s ,line))
#                    line = patterns[1].sub('stat='+s ,line)
#                elif match2:
#                    #print line.replace(match.group(),'____')
#    #                print(patterns[2].sub('poin='+p ,line))
#                    line = patterns[2].sub('poin='+p ,line)
            if matchvel:
                
                #print line.replace(match.group(),'____')
#                print(patterns[1].sub('stat='+s ,line))
                line = patterns[1].sub('['+vel+']' ,line)
             
            print(line)
        outfile.write(line)
        outfile.write('\n')
            
    #            print line
    outfile.close()
        

#print c_dat
fname.close()
config_file.close()
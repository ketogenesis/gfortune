#!/usr/bin/env python
import codecs
import os

gsource = open("gsource", 'r').read()

g = open("build/g", 'w')
g.write(codecs.encode(gsource, "rot_13"))
g.close()

os.system("strfile -r -x build/g build/g.dat") 

#!/usr/bin/env python
import codecs
import os

gsource = open("gsource", 'r').read()

g = open("g", 'w')
g.write(codecs.encode(gsource, "rot_13"))
g.close()

os.system("strfile -r -x g g.dat") 

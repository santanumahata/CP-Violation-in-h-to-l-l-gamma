import numpy as np
from lhereader import LHEReader

reader = LHEReader("Events.lhe")

ofile = open("Check.dat", "w")


aa=[]
bb=[]
cc=[]
dd=[]

for iev, event in enumerate(reader):
    aa = event.particles[2].px
    bb = event.particles[2].py
    cc = event.particles[2].pz
    dd = event.particles[2].energy
    ofile.write(str(aa)+"\t"+str(bb)+"\t"+str(cc)+"\t"+str(dd)+"\n")
#    print(dd)
# 4 = -13 = mu+, 5 = 14 = nu-mu, 6 = 13 = mu-, 7 = -14 = nu-mu-bar  
ofile.close()  
  #  print ("\n",dd,"\t",bb, "\t")
   # with open(ofile, "a") as ff:
       # ff.write('\n{aa}\t{bb}\t{cc}\t{dd}')
    #   ff.write('{dd}')

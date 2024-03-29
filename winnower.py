#!/usr/bin/python
import sys,os
from optparse import OptionParser
import copy

l=6
d=1

class lmerNode:
    '''Graph node Represented as an adjacency list'''
    def __init__(self,_lmer,_readnum):
        self.lmer=_lmer
        self.readnum=_readnum
        self.edges=[]
        self.color="w"
        self.l=[]

    def __repr__(self):
        return(self.lmer+" "+str(self.readnum) )

                   

def getReads(inp):
    '''Reads in a fasta file and stores reads in a list'''
    fh = open(inp,"r")
    reads = []
    for line in fh:
       
        if ">" in line:
             reads.append("")
        else:
             reads[len(reads)-1]+= (line.rstrip()) 
    return reads         
    
    
    
def lmerfy(reads,l):
    '''Converts reads into lmers'''
    lmers = []
    i=0
    for read in reads:
        beg = 0
        end=l
        while not(end==len(read)+1):
            lmers.append(lmerNode(read[beg:end],i))
            beg+=1
            end+=1
        i+=1    
    return lmers       
    
def constructGraph(lmers,d):
    '''Construct lmer graph O(n^2)'''
    
    for lmer_lhs in lmers:
         
        for lmer_rhs in lmers:
            # condition lmer is hamming distance 2d away
            if not (lmer_rhs.readnum==lmer_lhs.readnum):
                diffs = 0
                for ch1, ch2 in zip(lmer_lhs.lmer, lmer_rhs.lmer):
                    if ch1 != ch2:
                        diffs += 1
                if diffs <= 2*d:        
                    lmer_rhs.edges.append(lmer_lhs)

        

def findCliques(lmers,r,d,l):
    '''Get starting vertices and feed to DP algorithm'''
    i=0
    print len(lmers)
    for item in lmers:
		if not item.readnum == 0:
			break
# startHere		newAlgo(item,r,d,l)
		i+=1
		sum=0
		
		print "Explored "+str(i)+" Nodes", sum
        
        #print motifList


if __name__ == "__main__":
   

    
    inp = None
    for i in range(0,len(sys.argv)):
        if sys.argv[i]=="-input":
            inp= sys.argv[i+1]
        if sys.argv[i]=="-l":
            l= int(sys.argv[i+1])
        if sys.argv[i]=="-d":
            d= int(sys.argv[i+1])
    
    ################## build graph
    
	print inp
    reads = getReads(inp)
    # l-merfy
    lmers=lmerfy(reads,l)
    print ("Connecting "+str(len(lmers))+" Nodes")
    constructGraph(lmers,d)
    print "Look for Cliques"
    findCliques(lmers,len(reads),d,l)

   
  

   
    
        
    


        
        










    
    
    
    
    


#get sequence
#import sys
#import string
seq1 = GGAATTCCTTA


G_count = seq1.count("G")
C_count = seq1.count("C")
A_count = seq1.count("A")
T_count = seq1.count("T")

my_dictionary = {"G":'G_count',"C":'C_count',"A":'A_count',"T":'T_count'}

print my_dictionary

#float (G_count + C_count)/seq1.len



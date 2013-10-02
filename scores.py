reader = open('uniprot_sprot.fasta', 'r')
line = reader .readline()
noOfHumanProtiens = 0
for line in reader:
    if(line[0] == '>'):
    print line
    if "Homo sapiens" in line:
    noOfHumanProtiens+=1
    print "No =",noOfHumanProtiens
    reader.close

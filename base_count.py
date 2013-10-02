def base_count(sequence, base):
    return sequence.count(base)
    
def gc_cont(sequence):
    return (base_count(sequence, 'G') + 
            base_count(sequence, 'C')) / float(len(sequence))
    
        
#test = 'GACTTGA'
#print base_count(test, 'C')
#print gc_cont(test)


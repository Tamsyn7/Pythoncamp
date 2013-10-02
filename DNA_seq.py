import string
class NucleotideSequence:
    '''An abstract class which is inherited by
    DNA and RNA sequences. Do not use! '''
    #assert sequence.isupper #make sure all are uppercase otherwise fail
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'T',
                   'T': 'A'}
    
    def __init__(self, sequence):
        '''Imput sequence should be a 
        sting in all upper case letters'''
        assert isinstance(sequence, str)
        assert len(sequence) > 0
        assert sequence.isupper
        sequence = sequence.upper()
        self.sequence = sequence
        self.base_counts = {}
    
    def base_count(self, base):
        '''Given a base, returns the number of
        times the base occurs in this sequence'''
        if base in self.base_counts:
            return self.base_counts[base]
        else:
            count = self.sequence.count(base)
            self.base_counts[base] = count
            return count
    
    def gc_content(self):
        '''This calculates the amount of GC in the
        sequence'''
        assert gc_content
        g = self.base_count('G')
        c = self.base_count('C')
        return float(g+c)/len(self.sequence)
        
    def reverse_complement(self):
        '''This gives the reverse complement of the DNA
        sequence'''
        rev_c = ""
        for base in self.sequence:
            rev_c = self.complements[base] + rev_c
            
        return rev_c
        
        
class DNASequence(NucleotideSequence):
        '''Uses the bases GATC'''
        #assert not 'U' in sequence
        #pass
    
    
class RNASequence(NucleotideSequence):
        '''Uses the bases GAUC'''
        #assert not 'T' in sequence
        complements = {'G': 'C',
                   'C': 'G',
                   'A': 'U',
                   'U': 'A'}
                   
x = raw_input("Enter your input here: ")

except:
    print "Ivalid base input, must contain bases G C T/U A"
    raise

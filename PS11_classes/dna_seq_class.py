#!/usr/bin/env python3

##START of CLASS DNASequence##
class DNASequence(object):
    #define class attributes
    def __init__(self, sequence, sequence_name, organism):
        self.sequence = sequence
        self.sequence_name = sequence_name
        self.organism = organism
    
    #define class methods
    def length(self):
        dnalength = len(self.sequence)
        return dnalength
    
    def nuc_comp(self):
        length = len(self.sequence)
        a_count = self.sequence.count("A")
        g_count = self.sequence.count("G")
        c_count = self.sequence.count("C")
        t_count = self.sequence.count("T")
        a_comp = a_count/length
        g_comp = g_count/length
        c_comp = c_count/length
        t_comp = t_count/length
        return a_comp, g_comp, c_comp, t_comp

    def GC_content(self):
        length = len(self.sequence)
        g_count = self.sequence.count("G")
        c_count = self.sequence.count("C")
        gc_content = (g_count+c_count)/length
        return gc_content
    
    def FASTA_formatter(self):
        fasta_dict = {}
        header = ">" + self.sequence_name
        fasta_dict[header]=''
        seq_list = [self.sequence[i:i+50] for i in range(0, len(self.sequence), 50)]
        seq_output = ("\n".join(seq_list))
        fasta_dict[header]=seq_output
        return fasta_dict
    
    def DNA_Compare(self,seq2):
        if self.sequence == seq2.sequence and self.sequence_name == seq2.sequence_name and self.organism == seq2.organism:
          return "True"
        else:
          return "False"


#input output
dna_rec_object = DNASequence('GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGT', 'c0_g1_i1', 'frog')
dna_rec_object2 = DNASequence('GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGT', 'c0_g1_i1', 'frog')
#print(f'sequence: {dna_rec_object.sequence}')
#print(f'sequence name {dna_rec_object.sequence_name}')
#print(f'organism: {dna_rec_object.organism}')
#print(f'length: {dna_rec_object.length()}')
#countlist = dna_rec_object.nuc_comp()
#As = countlist[0]
#Gs = countlist[1]
#Cs = countlist[2]
#Ts = countlist[3]
#print (f'nt composition: As:{As:.2%}, Gs:{Gs:.2%}, Cs:{Cs:.2%}, Ts:{Ts:.2%}')
#print(f'GC_content is {dna_rec_object.GC_content():.2%}')

#with open ("fasta_format.txt","w") as wfh:
#  fasta_seq = dna_rec_object.FASTA_formatter()
#  for key in fasta_seq:
#    wfh.write(f'{key}\n{fasta_seq[key]}')
#    print(f'{key}\n{fasta_seq[key]}')

print(f'The two sequences are the same: {dna_rec_object.DNA_Compare(dna_rec_object2)}')

from Bio import Entrez
handle=Entrez.efetch(db='nucleotide',id='34577062',rettype='fasta',retmode='text')
seq_obj=SeqIO.read(handle,'fasta')
sequence=seq_obj.seq
print(sequence)

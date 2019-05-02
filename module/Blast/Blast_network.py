import os
import json
from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import re
def mRNA_protein(RNA_string):
    start_code = 'ATG'
    end_code = ['TAA', 'TAG', 'TGA']
    protein_table = {'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V', \
                     'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V', \
                     'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V', \
                     'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V', \
                     'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A', \
                     'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', \
                     'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', \
                     'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', \
                     'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D', \
                     'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', \
                     'TAA': '*', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', \
                     'TAG': '*', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', \
                     'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G', \
                     'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G', \
                     'TGA': '*', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', \
                     'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
                     }


    protein = ''
    t=len(RNA_string)-len(RNA_string)%3
    for sit in range(0, t, 3):
        if "n" in RNA_string[sit:sit + 3].lower():
            protein = protein + "X"
        else:
            code=RNA_string[sit:sit + 3]
            if "A" in code:
                code=code.replace("A","")
            if "T" in code:
                code=code.replace("T","")
            if "C" in code:
                code=code.replace("C","")
            if "G" in code:
                code=code.replace("G","")
            if code!="":
                protein = protein + "X"
            else:
                protein = protein + protein_table[RNA_string[sit:sit + 3]]
    return protein

def translate(input,output):
    with open(output,"w") as wr:
        for seq_record in SeqIO.parse(input, "fasta"):
            dna = str(seq_record.seq)
    
            protein = mRNA_protein(dna)
            protein=str(protein).replace("*","")
            wr.write(">%s\t%s\n%s\n"%(seq_record.id,seq_record.description,protein))
if __name__ == '__main__':
    myfile = open("correlation_config.json", 'r')
    result = json.load(myfile)
    group = result["Basis_Information"]["Comparison_Group"]
    language = result["Basis_Information"]["Language"]
    
    SGEQueue = result["Basis_Information"]["SGEQueue"]
    memory = result["Filter Parameters"]["Blast_Memory"]
    R_HOME_PATH = result["Basis_Information"]["R_HOME_PATH"]
    string_root = result["Network"]["root_database"]
    database_type = result["Network"]["String_Species_type"]
    fasta_database="%s/%s.fa"%(string_root,database_type)

    evalue = result["Filter Parameters"]["BlastEvalue"]
    array_group = group.split(",")
    with open("transcription_all_diff.fasta","w") as wr:
        for seq_record in SeqIO.parse("transcription_all.fasta", "fasta"):
                if "None" not in seq_record.description:
                    wr.write(">%s\t%s\n%s\n"%(seq_record.id,seq_record.description,seq_record.seq))
    translate("transcription_all_diff.fasta","transcription_all_diff_translate.fasta")
    with open("protein_all_diff.fasta","w") as wr:
        for seq_record in SeqIO.parse("protein_all.fasta", "fasta"):
                if "None" not in seq_record.description:
                    wr.write(">%s\t%s\n%s\n"%(seq_record.id,seq_record.description,seq_record.seq))
    while True:
        if os.path.exists("protein_all_diff.fasta") and os.path.exists("transcription_all_diff_translate.fasta"):
            print("PPI network blast in progress.....")
            os.popen("cat protein_all_diff.fasta transcription_all_diff_translate.fasta>>all_diff.fasta")
            while True:
                if os.path.exists("all_diff.fasta"):
                    with open("./blast_ppi.sh", "w") as wr:
                        wr.write(
                            "/opt/bio/ncbi/bin/blastall -F F -p blastp -d %s -i ./all_diff.fasta -e %s -a 3 -b 1 -v 1 -m 8 -o all_diff_ppi.blast.out" % (fasta_database,evalue))
                    break
            break
    



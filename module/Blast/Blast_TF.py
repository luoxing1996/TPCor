from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from matplotlib import pyplot as plt
from matplotlib_venn import venn2
import os
import json





if __name__ == '__main__':
    myfile = open("correlation_config.json", 'r')
    result = json.load(myfile)
    home = result["Basis_Information"]["Correlation analysis process server path"]
    group = result["Basis_Information"]["Comparison_Group"]
    TF = result["Transcription factor"]["TF_Species_Name"]
    TF_Memory = result["Transcription factor"]["TF_Memory"]
    Species = result["Transcription factor"]["TF_Species_type"]
    SGEQueue = result["Basis_Information"]["SGEQueue"]
    array_group = group.split(",")
    wr1 = open("./TF_transcription_blast.sh" , "w")
    wr2 = open("./TF_protein_blast.sh" , "w")
    if "animal" in Species.lower():

        wr1.write("/ifs4/BC_PUB/biosoft/pipeline/RNA/RNA_RNAseq/RNA_RNAseq_2017a/TF/../software/diamond blastx --evalue 1e-8 --threads 3 --outfmt 6 -d /ifs4/BC_PUB/biosoft/db/Pub/AnimalTFDB/pep/%s.fasta -q ./transcription_all.fasta -o TF_transcription_all_blast.out --seg no --max-target-seqs 1 --more-sensitive -b 0.5 --salltitles  "%TF)

        wr2.write(
            "/ifs4/BC_PUB/biosoft/pipeline/RNA/RNA_RNAseq/RNA_RNAseq_2017a/TF/../software/diamond blastp --evalue 1e-8 --threads 3 --outfmt 6 -d /ifs4/BC_PUB/biosoft/db/Pub/AnimalTFDB/pep/%s.fasta -q ./protein_all.fasta -o TF_protein_all_blast.out --seg no --max-target-seqs 1 --more-sensitive -b 0.5 --salltitles  " % TF)

    elif  "plant" in Species.lower():
        wr1.write("/ifs4/BC_PUB/biosoft/pipeline/RNA/RNA_RNAseq/RNA_RNAseq_2017a/TF/../software/diamond blastx --evalue 1e-8 --threads 3 --outfmt 6 -d %s/lib/database/Plant-all_TF_pep.fasta -q ./transcription_all.fasta -o TF_transcription_all_blast.out --seg no --max-target-seqs 1 --more-sensitive -b 0.5 --salltitles  "%home)
        wr2.write(
            "/ifs4/BC_PUB/biosoft/pipeline/RNA/RNA_RNAseq/RNA_RNAseq_2017a/TF/../software/diamond blastp --evalue 1e-8 --threads 3 --outfmt 6 -d %s/lib/database/Plant-all_TF_pep.fasta -q ./protein_all.fasta -o TF_protein_all_blast.out --seg no --max-target-seqs 1 --more-sensitive -b 0.5 --salltitles  " % home)
    wr1.close()
    wr1.close()
    





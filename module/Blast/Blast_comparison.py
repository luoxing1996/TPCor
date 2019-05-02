import os
import json
from Bio import SeqIO
####################################################################
##########The purpose of this function is to Blast comparison#######
####################################################################
if __name__ == '__main__':
    pwd=os.getcwd()
    myfile = open("correlation_config.json", 'r')
    result = json.load(myfile)
    home = result["Basis_Information"]["Correlation analysis process server path"]
    group = result["Basis_Information"]["Comparison_Group"]
    perl_HOME_PATH = result["Basis_Information"]["perl_HOME_PATH"]
    SGEQueue= result["Basis_Information"]["SGEQueue"]
    memory = result["Filter Parameters"]["Blast_Memory"]
    evalue=result["Filter Parameters"]["BlastEvalue"]
    NR = result["Annotation"]["NR_Species_type"]
    KEGG = result["Annotation"]["root_KEGG"]
    KO = result["Annotation"]["Whether the transcriptome ko file exist"]

    array_group = group.split(",")
    protein={}
    transcription={}
    while True:
        if os.path.exists("./Data_Analysis"):
            for index in array_group:
                root="./Data_Analysis/%s/Quantitative/"%index
                for seq_record in SeqIO.parse("%sprotein.fasta"%root, "fasta"):
                    protein[seq_record.id]=str(seq_record.seq)
                for seq_record in SeqIO.parse("%stranscription.fasta" % root, "fasta"):
                    transcription[seq_record.id]=str(seq_record.seq)

            break
        else:
            print("Please build an input file")

    with open("./protein_all.fasta","w") as wr:
        for index in protein.keys():
            wr.write(">%s\n%s\n"%(index,protein[index]))
    with open("./transcription_all.fasta","w") as wr:
        for index in transcription.keys():
            wr.write(">%s\n%s\n"%(index,transcription[index]))
    with open("./blast.sh", "w") as wr:
        wr.write(
            "/opt/bio/ncbi/bin/formatdb -i ./transcription_all.fasta -p F\n/opt/bio/ncbi/bin/blastall -i ./protein_all.fasta  -d  ./transcription_all.fasta -o blast_all.out -m 8 -a 3 -F F -e %s -p tblastn\n" % (evalue))
    if "no" in KO.lower():
        with open("./ko_blast.sh", "w") as wr:
            wr.write(
                "/ifs4/BC_PUB/biosoft/pipeline/RNA/RNA_RNAseq/RNA_RNAseq_2017a/TF/../software/diamond blastp --evalue 1e-5 --threads 5 --outfmt 6 -d %s/%s.fa -q ./transcription_all.fasta -o all_transcription_ko.blast.out --seg no --max-target-seqs 1 --more-sensitive -b 0.5 --salltitles" % (
                    NR))







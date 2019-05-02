for i in `ls *fasta`; do /ifs4/BC_PUB/biosoft/pipeline/RNA/RNA_RNAdenovo/RNA_RNAdenovo_2015a/software/diamond makedb --in $i -d $i; done

#*coding=utf-8
#by chenweitian@genomics.cn
#Date: Thu Oct 27 11:04:30 HKT 2016
from __future__ import division
import optparse
import sys,re,os
import commands

usage="""\n
Author: chenweitian@genomics.cn
Date: Thu Oct 27 11:04:30 HKT 2016
Function: filter string database
=====================================================================================================
python %s -h
=====================================================================================================
"""%(sys.argv[0])
option = optparse.OptionParser(usage)
option.add_option('','--m6',help='blast out',default='NA' )
option.add_option('','--fa',help='fa',default='NA' )
option.add_option('','--db',help='database',default='' )
option.add_option('','--protein_list',help='unigene which map to multi protein database ',default='' )
option.add_option('','--diff_list',help='different expression list',default='' )
option.add_option('','--result',help='result',default='')
option.add_option('','--bin',help='software bin path',default='')
option.add_option('','--mem',help='memory,default:3(mean:3G)',default='3')

(opts, args) = option.parse_args()

m6_opt = opts.m6
fa_opt = opts.fa
db_opt = opts.db
protein_list_opt = opts.protein_list
diff_list_opt = opts.diff_list
result_opt = opts.result
bin_opt = opts.bin
mem_opt = float(opts.mem)/6

result_dir = os.path.dirname(result_opt)

def blast(fa):
    blast_shell = """
%s/diamond   blastp  --evalue  1e-8  --threads 5 --outfmt  6  -d  %s  -q  %s -o  %s/blast_m6 --more-sensitive -b %s \n
"""%(bin_opt,db_opt,fa_opt,result_dir,mem_opt)
    #print blast_shell
    status = os.system(blast_shell)
    #status, blast_out = commands.getstatusoutput(qc_shell)

def main(M6,DB,RESULT):
    gene_str = {}#string datbase relation
    result = open(RESULT,'w')
    best_gene = {}#get best result from m6
    result.write("protein1\tprotein2\tprotein_cluster1\tprotein_cluster2\tscore\n")

    srtdb = {}
    protein_list = []#store unigene id which map to all database
    for line in open(protein_list_opt,'r'):
        if line.startswith('Unigene\tNr'):continue
        #if re.search('NA',line):continue
        array=line.strip().split('\t')
        if "Protein" in array[0]:

            protein_list.append(array[0].replace("_Protein",""))
        elif "mRNA" in array[0]:

            protein_list.append(array[0].replace("_mRNA",""))
    open(protein_list_opt,'r').close()
    #===============it had read protein_list_opt
    candidate_dict = {}
    for line in open(diff_list_opt,'r'):
        line = line.strip().split("\t")
        if line[0] in protein_list:
            candidate_dict[line[0]] = line[1] #unigene foldchange
    #===============it had read diff_list_opt
    for line in open(M6,'r'):
        line = line.strip().split("\t")
        if line[0] not in best_gene:
            best_gene[line[0]] = 1
            if line[0] in candidate_dict:#only store candidate gene
                gene_str.setdefault(line[2],[]).append(line[0])#394.NGR c10170:[unigene1,unigene2]
    #===============it had read M6
    ##self_relation = {}#multi unigene map in same STRING protein sequence
    ##for line in gene_str:
    ##  for index,left in enumerate(gene_str[line]):
    ##      for right in gene_str[line][index+1:]:
    ##          #relation = "%s\t%s\t%s\t%s"%(i,j,line,line)
    ##          result.write("%s\t%s\t%s\t%s\t%s\n"%(left,right,line,line,line))
    #=============== self relation\nstart to read STRING DATABASE"
    os.system("date")
    for line in open(DB,'r'):
        #if line.startswith('group1'):continue
        line = line.strip().split("\t")
        if  gene_str.has_key(line[0]) and gene_str.has_key(line[1]):
            for left in gene_str[line[0]]:
                for right in gene_str[line[1]]:
                    result.write("%s\t%s\t%s\t%s\t%s\n"%(left,right,line[0],line[1],line[2]))
    result.close()
    os.system("date")   
if __name__ == '__main__':
    if len(sys.argv) < 5:
        os.system("python %s -h"%(sys.argv[0]))
        sys.exit(1)
    if m6_opt == "NA" and fa_opt == "NA":
        os.system("give a input please : python %s --m6  or python %s --fa"%(sys.argv[0],sys.argv[0]))
        sys.exit(1)
    if m6_opt == "NA" and fa_opt != "NA":
        blast(fa)
        m6_opt = "%s/blast_m6"%(result_dir)
        RESULT = result_opt
        DB = db_opt
        M6 = m6_opt
        main(M6,DB,RESULT)
    if m6_opt != "NA" and fa_opt == "NA":
        RESULT = result_opt
        DB = db_opt
        M6 = m6_opt
        main(M6,DB,RESULT)
    else:
        os.system("give a input please : python %s --m6  or python %s --fa"%(sys.argv[0],sys.argv[0]))
        sys.exit(1)
        

import json
import os
import math

####################################################################
##########The purpose of this function is to volcano map############
####################################################################
if __name__ == '__main__':
    myfile = open("correlation_config.json", 'r')
    result = json.load(myfile)
    group = result["Basis_Information"]["Comparison_Group"]
    protein_fold = result["Filter Parameters"]["ProteinFoldChange"]
    protein_fold=math.log(float(protein_fold), 2)
    gene_fold = result["Filter Parameters"]["GeneFoldChange"]
    gene_fold = math.log(float(gene_fold), 2)
    protein_p = result["Filter Parameters"]["Protein p value Threshold"]
    gene_p = result["Filter Parameters"]["Gene p value Threshold"]
    protein_p=float(protein_p)
    gene_p=float(gene_p)
    home = result["Basis_Information"]["Correlation analysis process server path"]
    R_HOME_PATH = result["Basis_Information"]["R_HOME_PATH"]
    array_group = group.split(",")
    wg= open("./Quantitative_volcano.sh", "w")
    while True:
        if os.path.exists("./Data_Analysis"):
            for index in array_group:
                protein_three1=0
                protein_three2 = 0
                gene_three1=0
                gene_three2 = 0
                correlation_id=[]
                wr=open("./Data_Analysis/%s/Quantitative/Association_volcano.txt"%index,"w")
                root = "./Data_Analysis/%s/Quantitative/" % index
                with open("%sAssociation.txt"%root) as fh:
                    n=0
                    for line in fh.readlines():
                        if n==0:
                            wr.write(line)
                            n+=1
                            continue
                        else:
                            line = line.strip()
                            array = line.split("\t")
                            correlation_id.append(array[1])
                            if array[4]=="None" :
                                if float(array[3]) <protein_p :
                                    protein_three1 = 1
                                    array[4]="None(p_value<%s)"%protein_p
                                if float(array[3]) >= protein_p:
                                    protein_three2=1
                                    array[4] = "None(p_value>%s)"%protein_p
                            if array[7] == "None":
                                if float(array[6]) < gene_p:
                                    gene_three1 = 1
                                    array[7] = "None(p_value<%s)"%gene_p
                                if float(array[6]) >= gene_p:
                                    gene_three2=1
                                    array[7] = "None(p_value>%s)"%gene_p
                            wr.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%(array[0],array[1],array[2],array[3],array[4],array[5],array[6],array[7]))
                wr.close()
                with open("./Data_Analysis/%s/Quantitative/correlation_scatter_plot.txt" % index, "w") as wr:
                    wr.write("Gene_ID\tlog10_C_Expression\tlog10_T_Expression\tGene_group\n")
                    with open("./%s/Transcription/%s.GeneDiffExp.xls"%(index,index),"r") as fh:
                        error = 0
                        n = 0
                        Id = -1
                        pvalue = -1
                        Description = -1
                        Ratio = -1
                        Regulation = -1

                        for line in fh.readlines():
                            line = line.strip()
                            array = line.split("\t")
                            if n == 0:

                                for i in range(len(array)):

                                    if array[i] == "GeneID":
                                        Id = i
                                    if "Description" in array[i]:
                                        Description = i
                                    if "log2" in array[i]:
                                        Ratio = i
                                    if "Up" in array[i] and "Down" in array[i]:
                                        Regulation = i
                                    if "value" in array[i]:
                                        pvalue = i

                                n += 1
                                if Id == -1:
                                    error = 1
                                    print(
                                        "error:transcription of title id is not found!Please modify your transcription id as Id")
                                if Regulation == -1:
                                    error = 1
                                    print(
                                        "error:transcription of title Regulation is not found!Please modify your transcription Regulation as Up-Down-Regulation")
                                if pvalue == -1:
                                    print(
                                        "warning:transcription of title pvalue is not found!Please modify your transcription pvalue as p-value")
                                if Description == -1:
                                    print(
                                        "warning:transcription of title Description is not found!Please modify your transcription Description as Description")
                                if Ratio == -1:
                                    error = 1
                                    print(
                                        "error:transcription of title Mean Ratio is not found!Please modify your transcription Mean Ratio as Mean_Ratio_[sample of your name]")
                                if error == 1:
                                    print("Please correct the error before proceeding")
                                    break
                                continue

                            else:
                                if array[2] != "NA" and array[3] != "NA":
                                    if array[0] in correlation_id:
                                        if float(array[2])!=0 and float(array[3])!=0  :
                                            wr.write("%s\t%s\t%s\tRNA-Seq+proteomics\n"%(array[0],math.log(float(array[2]), 10),math.log(float(array[3]), 10)))
                                    else:
                                        if float(array[2]) != 0 and float(array[3]) != 0:
                                            wr.write("%s\t%s\t%s\tRNA-Seq-proteomics\n" % (array[0], math.log(float(array[2]), 10), math.log(float(array[3]), 10)))
                wr.close()
                if protein_three1==1 and protein_three2==1:
                    wg.write("%s/Rscript %smodule/Quantitative_association_analysis/volcano_protein1.R ./Data_Analysis/%s/Quantitative/Association_volcano.txt ./Data_Analysis/%s/Quantitative/volcano_protein.png %s %s\n"%(R_HOME_PATH,home,index,index,protein_fold,protein_p))
                else:
                    wg.write(
                        "%s/Rscript %smodule/Quantitative_association_analysis/volcano_protein2.R ./Data_Analysis/%s/Quantitative/Association_volcano.txt ./Data_Analysis/%s/Quantitative/volcano_protein.png %s %s\n" % (
                        R_HOME_PATH, home, index, index, protein_fold, protein_p))
                if gene_three1 == 1 and gene_three2==1:
                    wg.write("%s/Rscript %smodule/Quantitative_association_analysis/volcano_transcription1.R ./Data_Analysis/%s/Quantitative/Association_volcano.txt ./Data_Analysis/%s/Quantitative/volcano_transcription.png %s %s \n"%(R_HOME_PATH,home,index,index,gene_fold,gene_p))
                else:
                    wg.write(
                        "%s/Rscript %smodule/Quantitative_association_analysis/volcano_transcription2.R ./Data_Analysis/%s/Quantitative/Association_volcano.txt ./Data_Analysis/%s/Quantitative/volcano_transcription.png %s %s \n" % (
                        R_HOME_PATH, home, index, index, gene_fold, gene_p))
                wg.write(
                    "%s/Rscript %smodule/Quantitative_association_analysis/volcano_correlation.R ./Data_Analysis/%s/Quantitative/correlation_scatter_plot.txt ./Data_Analysis/%s/Quantitative/correlation_scatter_plot.png\n" % (
                    R_HOME_PATH, home,index, index))
            wg.close()
            break


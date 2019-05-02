import os
import json
import re
##########################################################################################
##########The purpose of this function is to draw KEGG_DEPs_DEGs map######################
##########################################################################################
if __name__ == '__main__':
    home=os.getcwd()
    myfile = open("correlation_config.json", 'r')
    result = json.load(myfile)
    List=os.getcwd()
    group = result["Basis_Information"]["Comparison_Group"]
    R_HOME_PATH = result["Basis_Information"]["R_HOME_PATH"]
    Species = result["Annotation"]["NR_Species_type"]
    array_group = group.split(",")
    for index in array_group:
        DEPs_DEGs=[]
        root = "./Data_Analysis/%s/Function/" % index
        with open("./%s/Transcription/%s.GeneDiffExp.xls" % (index, index), "r") as fh:
            Id = -1
            pvalue = -1
            Description = -1
            Ratio = -1
            Regulation = -1
            Sequence = -1
            n = 0
            error = 0
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

                if array[Regulation]=="Up" or array[Regulation]=="Down":
                    DEPs_DEGs.append(array[Id]+"_mRNA")
        with open("./%s/protein/%s_Up.xls"%(index,index),"r") as fh :
            n = 0
            for line in fh.readlines():
                if n == 0:
                    n += 1
                    continue
                line = line.strip()
                array = line.split("\t")
                DEPs_DEGs.append(array[1] + "_Protein")
        with open("./%s/protein/%s_Down.xls"%(index,index),"r") as fh :
            n = 0
            for line in fh.readlines():
                if n == 0:
                    n += 1
                    continue
                line = line.strip()
                array = line.split("\t")
                DEPs_DEGs.append(array[1] + "_Protein")

        os.chdir(root)
        wr=open("./pro_mRNA_DEPs_DEGs.ko","w")
        with open("pro_mRNA.ko","r") as fh:
            for line in fh.readlines():
                t = line.strip()
                array = t.split("\t")
                name = re.sub("\(.*\)", "", array[0])
                if name in DEPs_DEGs:
                    wr.write(line)
        wr.close()
        wr = open("./glist/DEPs_DEGs.glist", "w")
        with open("./glist/all.glist","r") as fh:
            for line in fh.readlines():
                t = line.strip()
                array = t.split("\t")
                name = re.sub("\(.*\)", "", array[0])

                if name in DEPs_DEGs:
              
                    wr.write(line)
        wr.close()
        with open("./KEGG_DEPs_DEGs.sh", "w") as wz:
            wz.write(
                "sh /zfssz3/SP_MSI/Pipeline/FuctionalAnalysis/bin/function_all_new_pathway_cor.sh -i ./pro_mRNA_DEPs_DEGs -d DEPs_DEGs -k %s -g -c -w -u 1>FunLogt 2>FunLoge" % (
                     Species))
        os.system("sh KEGG_DEPs_DEGs.sh")
        os.chdir(home)



from matplotlib import pyplot as plt
from matplotlib_venn import venn2
import json
import os
####################################################################
##########The purpose of this function is to venn map###############
####################################################################
def vene(a,b,c,output):
    plt.switch_backend('agg')
    plt.figure(figsize=(5,5))
    v=venn2(subsets=(a,b,c),set_labels = ('Protein','Transcription'))
    if a!=0:
        v.get_patch_by_id('10').set_color("#00ba38")
    if b!=0:
        v.get_patch_by_id('01').set_color("#619cff")
    if c!=0:
        v.get_patch_by_id('11').set_color("#f8766d")
    plt.savefig(output)
if __name__ == '__main__':
    myfile = open("correlation_config.json", 'r')
    result = json.load(myfile)
    group = result["Basis_Information"]["Comparison_Group"]
    array_group = group.split(",")
    while True:
        if os.path.exists("./Data_Analysis"):
            for index in array_group:
                a1=0
                a2=0
                a3=0
                a4=0
                a5=0
                a6=0
                pro=[]
                trans=[]
                correlation={}
                root = "./Data_Analysis/%s/Quantitative/" % index

                with open("%sAssociation.txt" % root) as fh:
                    n=0
                    for line in fh.readlines():
                        if n==0:
                            n+=1
                            continue
                        line=line.strip()
                        array=line.split("\t")
                        if array[4]!="None":
                            if array[7]!="None":
                                a6+=1

                        correlation[array[0]]=0

                        pro.append(array[0])
                        trans.append(array[1])
                a3=len(correlation.keys())
                with open("./%s/protein/%s.xls" % (index,index)) as fh:
                    error = 0
                    n = 0
                    Id = -1

                    for line in fh.readlines():
                        line = line.strip()
                        array = line.split("\t")
                        if n==0:
                            for i in range(len(array)):
                                if array[i] == "Protein_ID":
                                    Id = i

                            n += 1

                            if Id == -1:
                                print(
                                    "error:transcription of title id is not found!Please modify your protein id as Protein_ID")
                                error = 1

                            if error == 1:
                                print("Please correct the error before proceeding")
                                break
                            continue

                        if array[Id] not in pro:
                            a1+=1
                with open("./%s/protein/%s_Up.xls" % (index, index)) as fh:
                    error = 0
                    n = 0
                    Id = -1

                    for line in fh.readlines():
                        line = line.strip()
                        array = line.split("\t")
                        if n == 0:
                            for i in range(len(array)):
                                if array[i] == "Protein_ID":
                                    Id = i

                            n += 1

                            if Id == -1:
                                print(
                                    "error:transcription of title id is not found!Please modify your protein id as Protein_ID")
                                error = 1

                            if error == 1:
                                print("Please correct the error before proceeding")
                                break
                            continue

                        if array[Id] not in pro:
                            a4 += 1
                with open("./%s/protein/%s_Down.xls" % (index, index)) as fh:
                    error = 0
                    n = 0
                    Id = -1

                    for line in fh.readlines():
                        line = line.strip()
                        array = line.split("\t")
                        if n == 0:
                            for i in range(len(array)):
                                if array[i] == "Protein_ID":
                                    Id = i

                            n += 1

                            if Id == -1:
                                print(
                                    "error:transcription of title id is not found!Please modify your protein id as Protein_ID")
                                error = 1

                            if error == 1:
                                print("Please correct the error before proceeding")
                                break
                            continue

                        if array[Id] not in pro:
                            a4 += 1
                with open("./%s/Transcription/%s.GeneDiffExp.xls" % (index,index)) as fh:
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

                        if array[Id] not in trans:
                            a2+=1
                            if "up" in array[Regulation].lower() or "Down" in array[Regulation]:
                                a5 += 1
                vene(a1, a2, a3,"%svenn_all.png"%root)
                vene(a4, a5, a6, "%svenn_DEPs_DEGs.png"%root)
                wr=open("%spdf_1.txt"%root,"w")
                wr.write("%s\tprotein\ttranscription\tcorrelation\n"%index)
                wr.write("all\t%s\t%s\t%s\n"%(a1+a3,a2+a3,a3))
                wr.write("diff\t%s\t%s\t%s\n" % (a4 + a6, a5 + a6, a6))
            break



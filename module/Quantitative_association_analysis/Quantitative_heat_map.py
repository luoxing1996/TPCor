import json
import os
import math
import numpy as np
from math import sqrt
from shutil import copyfile
def multiply(a,b):
    #a,b两个列表的数据一一对应相乘之后求和
    sum_ab=0.0
    for i in range(len(a)):
        temp=a[i]*b[i]
        sum_ab+=temp
    return sum_ab

def cal_pearson(x,y):
    n=len(x)
    #求x_list、y_list元素之和
    sum_x=sum(x)
    sum_y=sum(y)
    #求x_list、y_list元素乘积之和
    sum_xy=multiply(x,y)
    #求x_list、y_list的平方和
    sum_x2 = sum([pow(i,2) for i in x])
    sum_y2 = sum([pow(j,2) for j in y])
    molecular=sum_xy-(float(sum_x)*float(sum_y)/n)
    #计算Pearson相关系数，molecular为分子，denominator为分母
    denominator=sqrt((abs(sum_x2-float(sum_x**2)/n))*(abs(sum_y2-float(sum_y**2)/n)))
    if denominator==0:
        return 0
    else:

        return molecular/denominator

####################################################################
##########The purpose of this function is to cluster and heat map###
####################################################################
def person(a,b):
    np.array([])
if __name__ == '__main__':
    protein={}
    trans={}
    myfile = open("correlation_config.json", 'r')
    result = json.load(myfile)
    home = result["Basis_Information"]["Correlation analysis process server path"]
    group = result["Basis_Information"]["Comparison_Group"]
    R_HOME_PATH = result["Basis_Information"]["R_HOME_PATH"]
    array_group = group.split(",")
    wg= open("Quantitative_heat.sh" , "w")
    while True:
        if os.path.exists("./Data_Analysis"):
            for index in array_group:
                protein[index]={}
                trans[index]={}
                root = "./Data_Analysis/%s/Quantitative/" % index
                #Create a heat map analysis text for the difference group
                fh = open("./%s/protein/%s_Down.xls"%(index,index), "r")
                error = 0
                n = 0
                Id = -1
                Pvalue = -1
                Description = -1
                Ratio = -1
                Sequence = -1

                for line in fh.readlines():
                    line = line.strip()
                    array = line.split("\t")

                    if n == 0:

                        for i in range(len(array)):
                            if array[i] == "Protein_ID":
                                Id = i
                            if array[i] == "Description":
                                Description = i
                            if "Mean_Ratio_" in array[i]:
                                Ratio = i
                            elif "Ratio_" in array[i] and Ratio == -1:
                                Ratio = i

                            if "Pvalue_" in array[i]:
                                Pvalue = i
                            if "Qvalue_" in array[i]:
                                Pvalue = i
                            if array[i] == "Protein_Sequence":
                                Sequence = i
                        n += 1

                        if Id == -1:
                            print("error:protein of title id is not found!Please modify your protein id as Protein_ID")
                            error = 1
                        if Pvalue == -1:
                            print(
                                "error:protein of title Pvalue is not found!Please modify your protein Pvalue as Pvalue_[sample_name]")
                            error = 1
                        if Description == -1:
                            error = 1
                            print(
                                "error:protein of title Description is not found!Please modify your protein Description as Description")
                        if Ratio == -1:
                            error = 1
                            print(
                                "error:protein of title Mean Ratio is not found!Please modify your protein Mean Ratio as Mean_Ratio_[sample of your name]")
                        if Sequence == -1:
                            error = 1
                            print(
                                "error:protein of title Sequence is not found!Please modify your protein Sequence as Protein_Sequence")
                        if error == 1:
                            print("Please correct the error before proceeding")
                            break
                        continue
                    protein[index][array[Id]] = math.log(float(array[Ratio]), 2)
                fh = open("./%s/protein/%s_Up.xls" % (index, index), "r")
                error = 0
                n = 0
                Id = -1
                Pvalue = -1
                Description = -1
                Ratio = -1
                Sequence = -1

                for line in fh.readlines():
                    line = line.strip()
                    array = line.split("\t")

                    if n == 0:

                        for i in range(len(array)):
                            if array[i] == "Protein_ID":
                                Id = i
                            if array[i] == "Description":
                                Description = i
                            if "Mean_Ratio_" in array[i]:
                                Ratio = i
                            elif "Ratio_" in array[i] and Ratio == -1:
                                Ratio = i

                            if "Pvalue_" in array[i]:
                                Pvalue = i
                            if "Qvalue_" in array[i]:
                                Pvalue = i
                            if array[i] == "Protein_Sequence":
                                Sequence = i
                        n += 1

                        if Id == -1:
                            print("error:protein of title id is not found!Please modify your protein id as Protein_ID")
                            error = 1
                        if Pvalue == -1:
                            print(
                                "error:protein of title Pvalue is not found!Please modify your protein Pvalue as Pvalue_[sample_name]")
                            error = 1
                        if Description == -1:
                            error = 1
                            print(
                                "error:protein of title Description is not found!Please modify your protein Description as Description")
                        if Ratio == -1:
                            error = 1
                            print(
                                "error:protein of title Mean Ratio is not found!Please modify your protein Mean Ratio as Mean_Ratio_[sample of your name]")
                        if Sequence == -1:
                            error = 1
                            print(
                                "error:protein of title Sequence is not found!Please modify your protein Sequence as Protein_Sequence")
                        if error == 1:
                            print("Please correct the error before proceeding")
                            break
                        continue
                    protein[index][array[Id]] = math.log(float(array[Ratio]), 2)
                fh = open("./%s/Transcription/%s.GeneDiffExp.xls" % (index, index), "r")
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
                    if array[Regulation]=="Up" or array[Regulation]=="Down":
                        trans[index][array[Id]]=-float(array[Ratio])
            protein_interset=[]
            for i in protein:
                if protein_interset!=[]:
                    protein_interset=list(set(protein_interset).intersection(set(list(protein[i].keys()))))
                else:
                    protein_interset=list(protein[i].keys())
            trans_interset = []

            for i in trans:
                if trans_interset != []:
                    trans_interset=list(set(trans_interset).intersection(set(list(trans[i].keys()))))
                else:
                    trans_interset = list(trans[i].keys())
            protein_array={}
            protein_id="\t"
            n=0
            for i in protein_interset:
                protein_id+=i+"\t"
                for index in array_group:
                    if i not in protein_array.keys():

                        protein_array[i]=[protein[index][i]]
                    else:
                        protein_array[i].append(protein[index][i])
            trans_array = {}
            for i in trans_interset:
                for index in array_group:
                    if i not in trans_array.keys():
                        trans_array[i] = [trans[index][i]]
                    else:
                        trans_array[i].append(trans[index][i])
            cor_result={}
            for i in protein_interset:
                for j in trans_interset:
                    if i not in cor_result.keys():
                        cor_result[i]={}

                    cor_result[i][j]=cal_pearson(list(protein_array[i]),list(trans_array[j]))
            wr = open("diff_heat.txt" , "w")
            wr.write(protein_id+"\n")
            for i in trans_interset:
                wr.write("%s"%i)
                for j in protein_interset:
                    wr.write("\t%s"%cor_result[j][i])
                wr.write("\n")
            wr.close()
            wg = open("Quantitative_heat.sh", "w")

            wg.write("%s/Rscript %smodule/Quantitative_association_analysis/heat.R ./diff_heat.txt ./heat_DEGs_DEPs.jpeg\n" % (R_HOME_PATH, home))
            wg.close()
            os.system("sh Quantitative_heat.sh")
            for index in array_group:
                while True:
                    if os.path.exists("./diff_heat.txt") and os.path.exists("./heat_DEGs_DEPs.jpeg"):
                        if os.path.getsize("./diff_heat.txt") and os.path.getsize(
                                "./heat_DEGs_DEPs.jpeg"):
                            copyfile('./diff_heat.txt', './Data_Analysis/%s/Quantitative/diff_heat.txt'%index)
                            copyfile('./heat_DEGs_DEPs.jpeg', './Data_Analysis/%s/Quantitative/heat_DEGs_DEPs.jpeg' % index)
                            break


            break



#coding=utf-8
from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from matplotlib import pyplot as plt
from matplotlib_venn import venn2
import os
import json
import math
import numpy as np
import scipy
from scipy.stats import chisquare
import numpy
import scipy
from scipy.stats import chisquare
import pandas as pd
import seaborn as sns
def violin(pokemon):
    #flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
    plt.switch_backend('agg')
    plt.figure(figsize=(10, 8))
    plt.tick_params(labelsize=8)


    plt.yticks(fontsize=15)
    plt.xlabel('Transcription factor superfamily', fontsize=20)
    plt.ylabel('log2_ratio', fontsize=20)
    sns.violinplot(y='log2_ratio',x='TF',data=pokemon,hue='Group',split=True,scale="width",inner="stick",scale_hue=False)
    plt.savefig('TF_violinplot.png')
def colorful(id,trans,pro,root):
    t = np.arange(1,len(trans)+1)
    s1 = trans
    s2 = pro
    colors=["#FF0000","#FF3300","#FF6600","#FF9900","#FFFF00","#CCFF00","#00FF00","#00FF99","#00FFCC","#00FFFF","#00CCFF","#0099FF","#0033FF","#6600FF","#9900FF","#CC00FF","#FF00FF","#FF0066","#FF0033","#DD2248","#BB445C","#916F76","#875EA2","#614DB3","#4D4DB3"]
    colors=colors[0:len(t)]
    plt.switch_backend('agg')
    plt.figure(figsize=(8, 10))
    ax1 = plt.subplot(211)
    if len(t)<15:
        plt.bar(t,s1,color=colors,width=0.5)
    else:
        plt.bar(t, s1, color=colors)
    plt.xticks(t, id,fontsize=5)

    plt.title("transcription",fontsize=20)
    plt.tick_params(width=0)#Coordinate scale width is 0
    plt.setp(ax1.get_xticklabels(), fontsize=5)
    # share x only
    ax2 = plt.subplot(212, sharex=ax1)
    if len(t)<15:
        plt.bar(t,s2,color=colors,width=0.5)
    else:
        plt.bar(t, s2, color=colors)
    plt.tick_params(labelsize=12)
    ax2.set_xlabel('protein',fontsize=20)
    plt.ylim(max(s2)+1,0)
    plt.tick_params(width=0)#Coordinate scale width is 0
    # make these tick labels invisible

    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.savefig("%sTF_colorful.png"%root)
def bar(id,array_pro,array_trans,array_correlation,output):
    x1=[]
    x2=[]
    x3=[]

    plt.switch_backend('agg')
    for i in range(0,len(id)*3,3):
        x1.append(i*1)
    for i in range(0,len(id)*3,3):
        x2.append(0.8+i*1)
    for i in range(0,len(id)*3,3):
        x3.append(1.6+i*1)
    plt.figure(figsize=(10, 6))

    plt.barh(x3,array_pro,color='#f8766d',label="protein")
    plt.barh(x2,array_trans,color="#619cff",label="transcription")
    plt.barh(x1,array_correlation,color="#00ba38",label="correlation")
    plt.yticks(x2, id)
    plt.legend(loc='upper right')
    plt.tick_params(labelsize=1)  # 坐标轴刻度大小
    plt.title("Number of transcription factors identified by each superfamily", fontsize=15)
    plt.savefig(output)
def venn(a,b,c,output,title):
    plt.switch_backend('agg')
    plt.figure(figsize=(5,5))
    v=venn2(subsets=(a,b,c),set_labels = ('Protein','Transcription'))
    if a!=0:
        v.get_patch_by_id('10').set_color("#00ba38")
    if b!=0:
        v.get_patch_by_id('01').set_color("#619cff")
    if c!=0:
        v.get_patch_by_id('11').set_color("#f8766d")
    plt.title(title, fontsize=10)
    plt.savefig(output)
def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]
def method(a,b,c,d):
    n=a+b+c+d
    a1=(a+b)*(a+c)/n
    b1 = (a + b) * (b+d) / n
    c1 = (a + c) * (d + c) / n
    d1 = (d + b) * (d + c) / n
    T=[a1,b1,c1,d1]
    t=min(T)
    if t>=5 and n>=40:
        return "Chisquare"
    else:
        return "Fisher"
if __name__ == '__main__':
    myfile = open("correlation_config.json", 'r')
    result = json.load(myfile)
    group = result["Basis_Information"]["Comparison_Group"]
    language = result["Basis_Information"]["Language"]
    perl = result["Basis_Information"]["perl_HOME_PATH"]
    TF = result["Transcription factor"]["TF_Species_Name"]
    home = result["Basis_Information"]["Correlation analysis process server path"]
    R_HOME_PATH = result["Basis_Information"]["R_HOME_PATH"]
    array_group = group.split(",")
    for index in array_group:
        Id = -1
        pvalue=-1
        Description = -1
        Ratio = -1
        Regulation=-1
        root="./Data_Analysis/%s/TF/"%index
        ratio = {}
        group_protein_id=[]
        group_transcription_id=[]
        uniq_pro=[]
        uniq_trans=[]
        for seq_record in SeqIO.parse("./Data_Analysis/%s/Quantitative/protein.fasta"%index, "fasta"):
            group_protein_id.append(str(seq_record.id))
        for seq_record in SeqIO.parse("./Data_Analysis/%s/Quantitative/transcription.fasta"%index, "fasta"):
            group_transcription_id.append(str(seq_record.id))
        wr1=open("%sTF_transcription_filter_result.txt"%root,"w")
        wr2 = open("%sTF_protein_filter_result.txt" % root,"w")
        with open("./TF_transcription_all_filter_result.txt","r") as fh:
            for line in fh.readlines():
                t=line.strip()
                array=t.split("\t")
                if array[0] in group_transcription_id and array[0] not in uniq_trans:
                    wr1.write(line)
                    uniq_trans.append(array[0])
        with open("./TF_protein_all_filter_result.txt","r") as fh:
            for line in fh.readlines():
                t=line.strip()
                array=t.split("\t")
                if array[0] in group_protein_id and array[0] not in uniq_pro:
                    wr2.write(line)
                    uniq_pro.append(array[0])
        wr1.close()
        wr2.close()
        while True:
            if os.path.exists("%sTF_protein_filter_result.txt" % root) and os.path.exists(
                    "%sTF_transcription_filter_result.txt" % root):

                with open("./%s/protein/%s.xls" % (index, index), "r") as fh:
                    n = 0
                    protein = []
                    Id = -1
                    Pvalue = -1
                    Description = -1
                    Ratio = -1
                    Sequence = -1
                    n = 0
                    error = 0
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
                                if "KEGG" in array[i]:
                                    KEGG = i
                            if Id == -1:
                                print(
                                    "error:transcription of title id is not found!Please modify your protein id as Protein_ID")
                                error = 1
                            if Pvalue == -1:
                                print(
                                    "error:transcription of title Pvalue is not found!Please modify your protein Pvalue as Pvalue_[sample_name]")
                                error = 1
                            if Description == -1:
                                error = 1
                                print(
                                    "error:protein of title Description is not found!Please modify your protein Description as Description")
                            if Ratio == -1:
                                error = 1
                                print(
                                    "error:protein of title Mean Ratio is not found!Please modify your protein Mean Ratio as Mean_Ratio_[sample of your name]")
                            if error == 1:
                                print("Please correct the error before proceeding")
                                break
                            n += 1
                            continue
                        if array[Ratio]!="-" and "n" not in array[Ratio].lower() and "a" not in array[Ratio].lower():
                            if float(array[Ratio])!=0:
                                ratio[array[Id]]=math.log(float(array[Ratio]),2)
                with open("./%s/protein/%s_Up.xls" % (index, index), "r") as fh:
                    n = 0
                    protein = []
                    for line in fh.readlines():
                        array = line.split("\t")
                        line = line.strip()
                        if n == 0:
                            for i in range(len(array)):
                                if array[i] == "Protein_ID":
                                    Id = i
                                if "Description" in array[i]:
                                    Description = i
                                if "Mean_Ratio" in array[i]:
                                    Ratio = i
                            n += 1
                            continue
                        protein.append(array[Id])
                with open("./%s/protein/%s_Down.xls" % (index, index), "r") as fh:
                    n = 0
                    protein = []
                    for line in fh.readlines():
                        line = line.strip()
                        array = line.split("\t")
                        if n == 0:
                            for i in range(len(array)):
                                if array[i] == "Protein_ID":
                                    Id = i
                                if "Description" in array[i]:
                                    Description = i
                                if "Mean_Ratio" in array[i]:
                                    Ratio = i
                            n += 1
                            continue
                        protein.append(array[Id])
                with open("./%s/Transcription/%s.GeneDiffExp.xls" % (index, index),
                          "r") as fh:
                    Id = -1
                    pvalue = -1
                    Description = -1
                    Ratio = -1
                    Regulation = -1
                    Sequence = -1
                    n = 0
                    error = 0
                    transcription = []
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

                        ratio[array[Id]]=array[Ratio]
                        if "up" == array[Regulation].lower() or "down" == array[Regulation]:
                            transcription.append(array[Id])
                correlation_id = {}
                with open("./Data_Analysis/%s/Quantitative/Association.txt" % index, "r") as fh:
                    n = 0
                    for line in fh.readlines():
                        if n == 0:
                            n += 1
                            continue
                        line = line.strip()
                        array = line.split("\t")
                        correlation_id[array[0]] = array[1]
                TF_protein = []
                TF_DEG_num=0
                TF_DEG_DEP_num=0
                TF_DEP_num = 0
                dic={}
                TF_transcription = []
                TF_correlation=[]
                with open("%sTF_violin_correlation.csv" % root, "w") as we:
                    we.write("Group,TF,log2_ratio\n")

                    n1 = 0

                    while True:
                        if n1!=0:
                            with open("%sTF_protein_filter_result.txt" % root, "r") as fh2:
                                n2 = 0
                                n3=0
                                for line in fh2.readlines():
                                    line = line.strip()
                                    array = line.split("\t")

                                    if array[0] in ratio:
                                        if "na" not in str(ratio[array[0]]).lower() and "-" not in str(ratio[array[0]]).lower():
                                            we.write("protein,%s,%s\n" % (array[2], ratio[array[0]]))
                                    if array[2] not in dic.keys():
                                        dic[array[2]]=[1,0,0]
                                    else:
                                        dic[array[2]][0]+=1
                                    if array[0] in correlation_id :
                                        if correlation_id[array[0]] in TF_transcription:
                                            if array[0] in protein and correlation_id[array[0]] in transcription:
                                                TF_DEG_DEP_num+=1
                                            n3 += 1
                                            dic[array[2]][2]+=1
                                            TF_correlation.append(array[0])
                                    if array[0] in protein:
                                        TF_DEP_num+=1


                                    TF_protein.append(array[0])
                                    n2 += 1
                                TF_protein_num = n2

                            break
                        else:
                            with open("%sTF_transcription_filter_result.txt" % root, "r") as fh1:
                                for line in fh1.readlines():
                                    n1 += 1
                                    line = line.strip()
                                    array = line.split("\t")
                                    if array[0] in ratio:
                                        if "na" not in str(ratio[array[0]]).lower()  and "-" not in str(ratio[array[0]]).lower():
                                            we.write("transcription,%s,%s\n" % (array[2], ratio[array[0]]))
                                    if array[0] in transcription:
                                        TF_DEG_num += 1
                                    if array[2] not in dic.keys():
                                        dic[array[2]] = [0, 1, 0]
                                    else:
                                        dic[array[2]][1] += 1
                                    TF_transcription.append(array[0])
                                TF_transcription_num = n1
                            dic_ratio_protein = {}
                TF_correlation_num = n3

                venn(TF_protein_num-TF_correlation_num,  TF_transcription_num-TF_correlation_num,TF_correlation_num, "%sTF_venn.png" % root,"Number of identified transcription factors")
                venn(TF_DEP_num - TF_DEG_DEP_num, TF_DEG_num - TF_DEG_DEP_num, TF_DEG_DEP_num,
                     "%sTF_DEG_DEP_venn.png" % root, "Number of identified transcription factors in DEGs and DEPs")
                id=[]
                TF_Superfamily_pro=[]
                TF_Superfamily_trans=[]
                TF_Superfamily_correlation=[]
                dic_top20 = {}
                top=0
                if len(dic.keys()) > 20:
                    top=1
                    array_top20 = []
                    cor = []

                    for tt in dic.keys():
                        dic_top20[tt] = dic[tt][2]
                        cor.append(dic[tt][2])
                    cor = set(sorted(cor)[(len(cor) - 20):])
                    for u in cor:
                        array_top20.append(get_key(dic_top20, u))
                    n=0
                    for oo in array_top20:
                        if n == 20:
                            break
                        for tt in oo:
                            n+=1
                            if n == 20:
                                break

                            id.append(tt)
                            TF_Superfamily_pro.append(dic[tt][0])
                            TF_Superfamily_trans.append(dic[tt][1])
                            TF_Superfamily_correlation.append(dic[tt][2])
                else:
                    for tt in dic.keys():
                        id.append(tt)
                        TF_Superfamily_pro.append(dic[tt][0])
                        TF_Superfamily_trans.append(dic[tt][1])
                        TF_Superfamily_correlation.append(dic[tt][2])

                colorful(id,TF_Superfamily_trans,TF_Superfamily_pro,root)
                break

        while True:
            if os.path.exists("%sTF_violin_correlation.csv"%root):
                root = "./Data_Analysis/%s/TF/" % index
                main_directory=os.getcwd()
                os.chdir(root)
                if top==1:

                    we=open("TF_violin_correlation_top20.csv","w")
                    with open("TF_violin_correlation.csv","r") as fh:
                        n=0
                        top_20_family={}
                        for line in fh.readlines():
                            t = line.strip()
                            array = t.split(",")
                            if n==0:
                                n+=1
                                continue
                            if array[1] not in top_20_family:
                                top_20_family[array[1]]=1
                            else:
                                top_20_family[array[1]]+=1
                    family_num_array=set(sorted(list(top_20_family.values()))[(len(cor) - 20):])
                    family_id_array=[]
                    for family_index in family_num_array:
                        family_id_array.append(get_key(top_20_family, family_index))
                    n = 0
                    family_id=[]
                    for oo in family_id_array:
                        if n == 20:
                            break
                        for tt in oo:
                            n += 1
                            if n == 20:
                                break
                            family_id.append(tt)

                    with open("TF_violin_correlation.csv", "r") as fh:
                        n = 0
                        top_20_family = {}
                        for line in fh.readlines():
                            t = line.strip()
                            array = t.split(",")
                            if n == 0:
                                we.write(line)
                                n += 1
                                continue
                            if array[1] in family_id:
                                we.write(line)
                    we.close()
                    while True:
                        if os.path.exists("TF_violin_correlation_top20.csv"):


                            pokemon = pd.read_csv("./TF_violin_correlation_top20.csv")
                            violin(pokemon)
                            while True:
                                if os.path.exists("./TF_violinplot.png"):
                                    os.popen("rm ./TF_violin_correlation_top20.csv")
                                    break
                            break
                else:
                    pokemon = pd.read_csv("TF_violin_correlation.csv")
                    violin(pokemon)
                os.chdir(main_directory)
                break
        a=TF_DEP_num
        b=TF_DEG_num
        c=TF_protein_num-TF_DEP_num
        d=TF_transcription_num-TF_DEG_num
        method_id=method(a,b,c,d)
        if method_id=="Chisquare":

            array=numpy.array([a,b,c,d])

            p = scipy.stats.chisquare(array).pvalue
            print (p)
        elif method_id=="Fisher":
            array = numpy.array([[a, b], [c, d]])
            p = scipy.stats.fisher_exact(array)[1]
        with open("%spdf_2.txt" % root, "w",encoding='utf-8') as wr:
            wr.write("%s\tprotein\ttranscription\n"%index)
            wr.write(
                "TF_nodiff\t%s\t%s\n" % (TF_protein_num - TF_DEP_num, TF_transcription_num - TF_DEG_num))
            wr.write("TF_diff\t%s\t%s\n" % (TF_DEP_num, TF_DEG_num))

            if "chinese" in language.lower():
                if p<=0.05:
                    wr.write("%s检验\tp值为%s\t该比较组两个组学鉴定到的转录因子个数与表达差异相关"%(method_id,round(p,4)))
                else:
                    wr.write("%s检验\tp值为%s\t该比较组两个组学鉴定到的转录因子个数与表达差异无关" % (method_id,round(p,4)))
            if "english" in language.lower():
                if p<=0.05:
                    wr.write("Using %s method\tp-value is %s\tindicating the number of transcription factors detected by the comparison group proteome and the transcriptome is related to the difference in expression."%(method_id,p))
                else:
                    wr.write("Using %s method\tp-value is %s\tindicating the number of transcription factors detected by the comparison group proteome and the transcriptome is not related to the difference in expression." % (method_id,p))




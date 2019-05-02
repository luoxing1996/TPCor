"""
import numpy as np
import os
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import colors
###########################################################################
##########The purpose of this function is to draw a bubble graph###########
###########################################################################
def list_Normalized(list):
    a=min(list)
    new=[]
    for i in list:
        new.append((i-a+0.1)*5)
    return new
def DrawBubble(id,pro_enrich ,trans_enrich ,pro_size,trans_size,pro_p_value,trans_p_value,title,output):#气泡图
    plt.switch_backend('agg')
    sns.set(style = "whitegrid")#设置样式
    cm = plt.cm.get_cmap('RdYlBu')
    fig, ax = plt.subplots(figsize=(10, len(id)/2))
    norm=colors.Normalize(vmin=0, vmax=0.1)
    bubble1 = ax.scatter(pro_enrich, range(1,len(id)+1) , s = list_Normalized(pro_size), c = pro_p_value,marker='D',cmap = cm,norm=norm,linewidth = 0.5, alpha = 0.5)
    ax.scatter(trans_enrich, range(1, len(id) + 1), s=list_Normalized(trans_size), c=trans_p_value, marker='o',
                         cmap=cm, norm=norm, linewidth=0.5, alpha=0.5)
    ax.grid()
    fig.colorbar(bubble1)
    plt.yticks(range(1,len(id)+1), id)
    plt.title(title, fontsize=20)
    plt.xlim(0, 1.2)
    plt.xlabel(u'Enrichment factor', fontsize=16)
    plt.legend(["protein","transcription"],loc="upper right",markerscale=0.5)
    plt.savefig(output)
def file_array(file):
    id=[]
    pro_enrich1=[]
    trans_enrich1=[]
    pro_size1=[]
    trans_size1=[]
    pro_p_value1=[]
    trans_p_value1=[]
    pro_enrich2=[]
    trans_enrich2=[]
    pro_size2=[]
    trans_size2=[]
    pro_p_value2=[]
    trans_p_value2=[]
    with open(file, "r") as fh:
        n = 0
        for line in fh.readlines():
            if n == 0:
                n += 1
                continue
            line = line.strip()
            array = line.split("\t")
            if float(array[4]) < 0.05 or float(array[5]) < 0.05:
                id.append("%s(%s)"%(array[0],array[3]))
                pro_enrich.append(float(array[7]))
                trans_enrich.append((float(array[8])))
                pro_size.append(int(array[1]))
                trans_size.append(int(array[2]))
                if float(array[4])<=0.05:
                    pro_p_value.append(0)
                else:
                    pro_p_value.append(1)
                if float(array[5]) <= 0.05:
                    trans_p_value.append(0)
                else:
                    trans_p_value.append(1)
    return id,pro_enrich ,trans_enrich ,pro_size,trans_size,pro_p_value,trans_p_value
if __name__ == '__main__':
    myfile = open("correlation_config.json", 'r')
    result = json.load(myfile)
    group = result["Basis_Information"]["Comparison_Group"]
    R_HOME_PATH = result["Basis_Information"]["R_HOME_PATH"]
    array_group = group.split(",")
    while True:
        if os.path.exists("./Data_Analysis"):
            for index in array_group:
                root="./Data_Analysis/%s/Function/"%index
                id,pro_enrich ,trans_enrich ,pro_size,trans_size,pro_p_value,trans_p_value=file_array("%sGO_C.txt" % root)
                DrawBubble(id,pro_enrich ,trans_enrich ,pro_size,trans_size,pro_p_value,trans_p_value,"Cellular Component","%sbubble_C.png"%root)
                root="./Data_Analysis/%s/Function/"%index

                id,pro_enrich ,trans_enrich ,pro_size,trans_size,pro_p_value,trans_p_value=file_array("%sGO_F.txt" % root)
                DrawBubble(id,pro_enrich ,trans_enrich ,pro_size,trans_size,pro_p_value,trans_p_value,"Molecular Function","%sbubble_F.png"%root)
                root="./Data_Analysis/%s/Function/"%index
                id,pro_enrich ,trans_enrich ,pro_size,trans_size,pro_p_value,trans_p_value=file_array("%sGO_P.txt" % root)
                DrawBubble(id,pro_enrich ,trans_enrich ,pro_size,trans_size,pro_p_value,trans_p_value,"Biological Process","%sbubble_P.png"%root)
                root="./Data_Analysis/%s/Function/"%index
                id,pro_enrich ,trans_enrich ,pro_size,trans_size,pro_p_value,trans_p_value=file_array("%sPathway.txt" % root)
                DrawBubble(id,pro_enrich ,trans_enrich ,pro_size,trans_size,pro_p_value,trans_p_value,"KEGG Pathway","%sbubble_Pathway.png"%root)

            break
"""
import numpy as np
import os
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import colors
def list_Normalized(list):
    if list==[]:
        return list
    a=min(list)
    new=[]
    for i in list:
        new.append((i-a+1)*5)
    return new


def DrawBubble(array1, array2, brray1, brray2, crray1, crray2, drray1, drray2, idarray,title,output):#气泡图
    #1:p>0.05 2:p<=0.05 array,brray:size  crray,drray:enrich_factor array,crray:protein brray,drray:transcription
    plt.switch_backend('agg')
    sns.set(style = "whitegrid")
    cm = plt.cm.get_cmap('rainbow')

    fig, ax = plt.subplots(figsize=(10, len(idarray)/2))
    norm = colors.Normalize(vmin=0, vmax=1)
    length=len(array1.keys())
    x=[1]*length
    y=list(array1.keys())
    bubble1 = ax.scatter(x, y , s = list_Normalized(list(array1.values())), c = list(crray1.values()),marker='o',cmap = cm,norm=norm,linewidth = 0.5, alpha = 0.5)
    length = len(array2.keys())
    x = [1] * length
    y = list(array2.keys())
    ax.scatter(x, y, s=list_Normalized(list(array2.values())), c=list(crray2.values()), marker='D', cmap=cm, linewidth=0.5, alpha=0.5)
    ax.grid()
    length=len(brray1.keys())
    x=[1.5]*length
    y=list(brray1.keys())
    ax.scatter(x, y , s = list_Normalized(list(brray1.values())), c = list(drray1.values()),marker='o',cmap = cm,linewidth = 0.5, alpha = 0.5)
    length = len(brray2.keys())
    x = [1.5] * length
    y = list(brray2.keys())
    ax.scatter(x, y, s=list_Normalized(list(brray2.values())), c=list(drray2.values()), marker='D', cmap=cm, linewidth=0.5, alpha=0.5)

    fig.colorbar(bubble1)
    plt.xticks([1,1.5], ["protein","transcription"])
    plt.yticks(range(0,len(list(idarray.keys()))), list(idarray.values()))
    plt.xlim(0.8, 2)
    plt.title(title, fontsize=30)
    plt.tick_params(labelsize=15)
    plt.legend(["p value>0.05","p value<=0.05"])
    plt.savefig(output,bbox_inches='tight')

def file_array(file):
    array1={}
    array2={}
    brray1={}
    brray2={}
    crray1={}
    crray2={}
    drray1={}
    drray2={}
    idarray={}

    with open(file, "r") as fh:
        n = -1
        for line in fh.readlines():
            if n == -1:
                n += 1
                continue
            line = line.strip()
            array = line.split("\t")
            idarray[n]="%s(%s)"%(array[0],array[3])
            if float(array[4])<=0.05:
                array1[n]=int(array[1])
                crray1[n] = float(array[7])
            else:
                array2[n]=int(array[1])
                crray2[n] = float(array[7])
            if float(array[5])<=0.05:
                brray1[n]=int(array[2])
                drray1[n] = float(array[8])
            else:
                brray2[n]=int(array[2])
                drray2[n] = float(array[8])
            n+=1
    return array1,array2,brray1,brray2,crray1,crray2,drray1,drray2,idarray
if __name__ == '__main__':
    myfile = open("correlation_config.json", 'r')
    result = json.load(myfile)
    group = result["Basis_Information"]["Comparison_Group"]
    R_HOME_PATH = result["Basis_Information"]["R_HOME_PATH"]
    array_group = group.split(",")
    while True:
        if os.path.exists("./Data_Analysis"):
            for index in array_group:
                root="./Data_Analysis/%s/Function/"%index
                path = os.getcwd()






                while True:
                    if os.path.exists("%sGO_P.txt"%root) and os.path.exists("%sGO_C.txt"%root)and os.path.exists("%sGO_F.txt"%root):
                        break
                with open("%sGO_P.txt"%root, "r") as fh:
                    t = 0
                    for line in fh.readlines():
                        if t == 0:
                            line1=line

                        t+=1
                if t>21:

                    wr = open("./Data_Analysis/%s/Function/GO_P_TOP20.txt" % index, "w")
                    wr.write(line1)
                    os.chdir("./Data_Analysis/%s/Function/" % index)
                    os.system("  sed -n '2,$p' GO_P.txt|sort -nrk4 -t $'\t' |sed -n 1,20p>>GO_P_TOP20.txt")
                    os.chdir(path)
                    sucess = 0
                    while True:#over
                        with open("%sGO_P_TOP20.txt"%root, "r") as fh:
                            n = 0
                            for line in fh.readlines():
                                n += 1
                                if n == 2:
                                    sucess = 1
                                    break
                        if sucess == 1:
                            break
                    array1, array2, brray1, brray2, crray1, crray2, drray1, drray2, idarray = file_array(
                        "%sGO_P_TOP20.txt" % root)
                else:
                    array1, array2, brray1, brray2, crray1, crray2, drray1, drray2, idarray = file_array(
                        "%sGO_P.txt" % root)

                DrawBubble(array1, array2, brray1, brray2, crray1, crray2, drray1, drray2, idarray,"Biological Process","%sbubble_P.png"%root)








                with open("%sGO_C.txt"%root, "r") as fh:
                    t = 0
                    for line in fh.readlines():
                        if t == 0:
                            line1 = line

                        t += 1
                if t > 21:
                    wr = open("./Data_Analysis/%s/Function/GO_C_TOP20.txt" % index, "w")
                    wr.write(line1)
                    os.chdir("./Data_Analysis/%s/Function/" % index)
                    os.popen(" sed -n '2,$p' GO_C.txt|sort -nrk4 -t $'\t' |sed -n 1,20p>>GO_C_TOP20.txt")
                    os.chdir(path)
                    sucess = 0
                    while True:  # over
                        with open("%sGO_C_TOP20.txt"%root, "r") as fh:
                            n = 0
                            for line in fh.readlines():
                                n += 1
                                if n == 2:
                                    sucess = 1
                                    break
                        if sucess == 1:
                            break
                    array1, array2, brray1, brray2, crray1, crray2, drray1, drray2, idarray = file_array(
                        "%sGO_C_TOP20.txt" % root)
                else:
                    array1, array2, brray1, brray2, crray1, crray2, drray1, drray2, idarray = file_array(
                        "%sGO_C.txt" % root)


                DrawBubble(array1, array2, brray1, brray2, crray1, crray2, drray1, drray2, idarray,
                           "Cellular Component",
                           "%sbubble_C.png" % root)








                with open("%sGO_F.txt"%root, "r") as fh:
                    t = 0
                    for line in fh.readlines():
                        if t == 0:
                            line1 = line

                        t += 1
                if t > 21:
                    wr = open("./Data_Analysis/%s/Function/GO_F_TOP20.txt" % index, "w")
                    wr.write(line1)
                    os.chdir("./Data_Analysis/%s/Function/" % index)
                    os.popen(" sed -n '2,$p' GO_F.txt|sort -nrk4 -t $'\t' |sed -n 1,20p>>GO_F_TOP20.txt")
                    os.chdir(path)
                    sucess = 0
                    while True:  # over
                        with open("%sGO_F_TOP20.txt"%root, "r") as fh:
                            n = 0
                            for line in fh.readlines():
                                n += 1
                                if n == 2:
                                    sucess = 1
                                    break
                        if sucess == 1:
                            break
                    array1, array2, brray1, brray2, crray1, crray2, drray1, drray2, idarray = file_array(
                        "%sGO_F_TOP20.txt" % root)
                else:
                    array1, array2, brray1, brray2, crray1, crray2, drray1, drray2, idarray = file_array(
                        "%sGO_F.txt" % root)


                DrawBubble(array1, array2, brray1, brray2, crray1, crray2, drray1, drray2, idarray,
                           "Mlecular Function",
                           "%sbubble_F.png" % root)









                with open("%sPathway.txt"%root, "r") as fh:
                    t = 0
                    for line in fh.readlines():
                        if t == 0:
                            line1 = line

                        t += 1
                if t > 21:
                    wr = open("./Data_Analysis/%s/Function/Pathway_TOP20.txt" % index, "w")
                    wr.write(line1)
                    os.chdir("./Data_Analysis/%s/Function/" % index)
                    os.popen(" sed -n '2,$p' Pathway.txt|sort -nrk4 -t $'\t' |sed -n 1,20p>>Pathway_TOP20.txt")
                    os.chdir(path)
                    sucess = 0
                    while True:  # over
                        with open("%sPathway_TOP20.txt"%root, "r") as fh:
                            n = 0
                            for line in fh.readlines():
                                n += 1
                                if n == 2:
                                    sucess = 1
                                    break
                        if sucess == 1:
                            break
                    array1, array2, brray1, brray2, crray1, crray2, drray1, drray2, idarray = file_array(
                        "%sPathway_TOP20.txt" % root)
                else:
                    array1, array2, brray1, brray2, crray1, crray2, drray1, drray2, idarray = file_array(
                        "%sPathway.txt" % root)


                DrawBubble(array1, array2, brray1, brray2, crray1, crray2, drray1, drray2, idarray,
                           "KEGG Pathway",
                           "%sbubble_Pathway.png" % root)
            break

from PIL import Image
import os
import json
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#####################################################################################
##########The purpose of this function is to draw a correlation_function graph#######
#####################################################################################
def function_heat(function_array,output,term_id,title):
    plt.switch_backend('agg')
    if len(term_id)<=3:
        fig, ax = plt.subplots(figsize=(10, 6))
    elif len(term_id)<10 and len(term_id)>3:
        fig, ax = plt.subplots(figsize = (9,len(term_id)*3/4 ))
    else:
        fig, ax = plt.subplots(figsize=(9, len(term_id) /2))
    sns.heatmap(pd.DataFrame(np.round(function_array,2),columns = ['Up-Up', 'Down-Down', 'Up-None','Down-None','None-Up','None-Down'], index = range(1,len(function_array)+1)),
                     vmax=1,vmin = 0, xticklabels= True, yticklabels= True, square=True, cmap="YlOrRd")
    ax.set_yticklabels(term_id, fontsize = 9, rotation = 360, horizontalalignment='right')
    ax.set_xticklabels(['Up-Up', 'Down-Down','Up-None','Down-None', 'None-Down','None-Up'],fontsize = 6, horizontalalignment='center')
    plt.title(title,verticalalignment="bottom",fontsize=20)
    plt.tick_params(width=0)#Coordinate scale width is 0
    plt.savefig(output)

def blend_two_images(head,foot,output,length):
    im1 = Image.open(head)
    im2 = Image.open(foot)
    width1, height1 = im1.size
    width2, height2 = im2.size
    if length>15:
        im2.paste(im1, box=(220, (length-20)*2))
        im2.save(output)
    else:
        result = Image.new(im1.mode, (width2, height1 + height2), "white")
        result.paste(im1, box=(220, 0))
        result.paste(im2, box=(0, height1))
        result.save(output)
    return
def correlation_function_map(file,correlation_dic,output):
    wr=open(output,"w")
    wr.write("term\tUp-Up\t Down-Down\tUp-None\tDown-None\tNone-Down\tNone-Up\n")
    with open(file, "r") as fh:
        n = 0
        empty=0
        matrix=[]
        term_id=[]
        for line in fh.readlines():
            if n == 0:
                n += 1
                continue
            line = line.strip()
            array = line.split("\t")
            Probability_row = []
            if len(array)==9:
                protein_ID=array[6].split(",")
                row_court=[0,0,0,0,0,0]
                length=len(protein_ID)
                term_id.append("%s(%s)"%(array[0],array[3]))
                for index in protein_ID:
                    if index in correlation_dic.keys():
                        if correlation_dic[index]==0:
                            row_court[0]+=1
                        if correlation_dic[index]==1:
                            row_court[1]+=1
                        if correlation_dic[index]==2:
                            row_court[2]+=1
                        if correlation_dic[index]==3:
                            row_court[3]+=1
                        if correlation_dic[index]==4:
                            row_court[4]+=1
                        if correlation_dic[index]==5:
                            row_court[5]+=1

                wr.write("%s(%s)\t%s\t%s\t%s\t%s\t%s\t%s\n"%(array[0],array[3],row_court[0],row_court[1],row_court[2],row_court[3],row_court[4],row_court[5]))
            else:
                continue


            empty=1
            for i in row_court:
                Probability_row.append(i/length)
            matrix.append(Probability_row)
        if empty==0:
            return [],[]
        else:
            return np.array(matrix),term_id
if __name__ == '__main__':
    myfile = open("correlation_config.json", 'r')
    result = json.load(myfile)
    group = result["Basis_Information"]["Comparison_Group"]
    home = result["Basis_Information"]["Correlation analysis process server path"]
    R_HOME_PATH = result["Basis_Information"]["R_HOME_PATH"]
    array_group = group.split(",")
    while True:
        if os.path.exists("./Data_Analysis"):
            for index in array_group:
                correlation_id=[]
                root = "./Data_Analysis/%s/Quantitative/" % index
                correlation_dic={}
                with open("%sAssociation.txt" % root, "r") as fh:
                    n = 0
                    for line in fh.readlines():
                        if n == 0:
                            n += 1
                            continue
                        line = line.strip()
                        array = line.split("\t")
                        if array[4]=="Up" and array[7]=="Up":
                            correlation_dic[array[0]]=0
                        if array[4]=="Down" and array[7]=="Down":
                            correlation_dic[array[0]]=1
                        if array[4]=="Up" and array[7]=="None":
                            correlation_dic[array[0]]=2
                        if array[4]=="Down" and array[7]=="None":
                            correlation_dic[array[0]]=3
                        if array[4]=="None" and array[7]=="Up":
                            correlation_dic[array[0]]=4
                        if array[4]=="None" and array[7]=="Down":
                            correlation_dic[array[0]]=5
                ####################cellular component##########################
                matrix,term_id=correlation_function_map("./Data_Analysis/%s/Function/GO_C.txt"%index,correlation_dic,"./Data_Analysis/%s/Function/correlation_function_GO_C.txt"%index)
                if matrix != []:
                    function_heat(matrix, "./Data_Analysis/%s/Function/foot_C.png"%index,term_id,"cellular component")
                    blend_two_images("%slib/head.png"%home, "./Data_Analysis/%s/Function/foot_C.png" % index,"./Data_Analysis/%s/Function/correlation_function_map_C.png"%index,len(term_id) )
                ####################Molecular Function##########################
                matrix, term_id = correlation_function_map("./Data_Analysis/%s/Function/GO_F.txt" % index, correlation_dic,"./Data_Analysis/%s/Function/correlation_function_GO_F.txt"%index)
                if matrix != []:

                    function_heat(matrix, "./Data_Analysis/%s/Function/foot_F.png" % index, term_id, "Molecular Function")
                    blend_two_images("%slib/head.png"%home,
                                     "./Data_Analysis/%s/Function/foot_F.png" % index,
                                     "./Data_Analysis/%s/Function/correlation_function_map_F.png" % index,len(term_id))
                ####################biological process##########################
                if os.path.exists("./Data_Analysis/%s/Function/GO_P_TOP20.txt" % index):
                    matrix, term_id = correlation_function_map("./Data_Analysis/%s/Function/GO_P_TOP20.txt" % index, correlation_dic,"./Data_Analysis/%s/Function/correlation_function_GO_P.txt"%index)
                else:
                    matrix, term_id = correlation_function_map("./Data_Analysis/%s/Function/GO_P.txt" % index,
                                                               correlation_dic,
                                                               "./Data_Analysis/%s/Function/correlation_function_GO_P.txt" % index)
                if matrix != []:
                    function_heat(matrix, "./Data_Analysis/%s/Function/foot_P.png" % index, term_id, "biological process")
                    blend_two_images("%slib/head.png"%home,
                                     "./Data_Analysis/%s/Function/foot_P.png" % index,
                                     "./Data_Analysis/%s/Function/correlation_function_map_P.png" % index,len(term_id))

            break



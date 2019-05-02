import numpy as np
import os
import json
import matplotlib.pyplot as plt
import pandas as pd
import math
from matplotlib.backends.backend_pdf import PdfPages
####################################################################
##########The purpose of this function is to correlation map########
####################################################################
def spearman_distance(vector1, vector2):
    df = pd.DataFrame({'protein':np.array(vector1),
         'transcription':np.array(vector2)})
    return float(df.corr('spearman')['protein']['transcription'])
def Least_squares(x,y,length):
    x_ = x.mean()
    y_ = y.mean()
    m = np.zeros(1)
    n = np.zeros(1)
    for i in np.arange(length-1):
        k = (x[i]-x_)* (y[i]-y_)
        m += k
        p = np.square( x[i]-x_ )
        n = n + p
    a = m/n
    b = y_ - a* x_
    return a,b
def correlation_map(protein_ratio,transcription_ratio,title,output,labeling):
    plt.switch_backend('agg')
    plt.figure(figsize=(10, 10), facecolor='w')
    if  protein_ratio!=[] and transcription_ratio!=[]:
        row = max(protein_ratio) / 1.3
        col = max(transcription_ratio) / 1.2
        length=len(protein_ratio)
        R=spearman_distance(protein_ratio,transcription_ratio)
        x=np.array(protein_ratio)
        y=np.array(transcription_ratio)
        a, b = Least_squares(x, y,length)
        y1 = a * x + b

        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['left'].set_position(('data', 0))
        plt.plot(x, y, 'ro', label=labeling, lw=2, markersize=4,c="#f8766d")
        plt.tick_params(labelsize=15)
        plt.legend(loc='upper left')
        plt.plot(x, y1, 'r-', lw=2, markersize=4)
        plt.text(row, col, "$y=%.3f*x+%.3f$\nR(Spearman)=%.3f"%(float(a),float(b),R), fontsize=20, style='oblique', ha='center', va='top', wrap=True)

        plt.text(row, -0.3, "Protein Log2(Ratio)" , fontsize=15, style='oblique',
                 ha='left', va='top', wrap=True)
        plt.text(0.1, col+0.8, "Transcription Log2(Ratio)", fontsize=15, style='oblique',
                 ha='left', va='top', wrap=True)
        plt.title(title,fontsize=30)
        plt.savefig(output)
    else:
        plt.title(title, fontsize=30)

        plt.savefig(output)
def correlation_allmap(dic,title,output):
    plt.switch_backend('agg')
    plt.figure(figsize=(10, 10), facecolor='w')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    plt.plot(dic["NDEPs_NDEGs"][0], dic["NDEPs_NDEGs"][1], 'ro', label="NDEPs_NDEGs", lw=2, markersize=4,c="#89A1B2")
    plt.plot(dic["DEPs_NDEGs"][0], dic["DEPs_NDEGs"][1], 'ro', label="DEPs_NDEGs", lw=2, markersize=4,c="#619CFF")
    plt.plot(dic["NDEPs_DEGs"][0], dic["NDEPs_DEGs"][1], 'ro', label="NDEPs_DEGs", lw=2, markersize=4,c="#00BA38")
    plt.plot(dic["DEPs_DEGs"][0], dic["DEPs_DEGs"][1], 'ro', label="DEPs_DEGs", lw=2, markersize=4,c="#f8766d")
    protein_ratio=dic["NDEPs_NDEGs"][0]+dic["DEPs_NDEGs"][0]+dic["NDEPs_DEGs"][0]+dic["DEPs_DEGs"][0]
    transcription_ratio=dic["NDEPs_NDEGs"][1]+dic["DEPs_NDEGs"][1]+dic["NDEPs_DEGs"][1]+dic["DEPs_DEGs"][1]
    row = max(protein_ratio) / 1.3
    col = max(transcription_ratio) / 1.2
    length=len(protein_ratio)
    R=spearman_distance(protein_ratio,transcription_ratio)
    x=np.array(protein_ratio)
    y=np.array(transcription_ratio)
    a, b = Least_squares(x, y,length)
    y1 = a * x + b
    plt.legend(loc='upper left')
    plt.tick_params(labelsize=15)

    plt.plot(x, y1, 'r-', lw=2, markersize=4)
    plt.text(row, col, "$y=%.3f*x+%.3f$\nR(Spearman)=%.3f"%(float(a),float(b),R), fontsize=20, style='oblique', ha='center', va='top', wrap=True)
    plt.text(row, -0.3, "Protein Log2(Ratio)" , fontsize=15, style='oblique',
             ha='left', va='top', wrap=True)
    plt.text(0.1, col+0.8, "Transcription Log2(Ratio)", fontsize=15, style='oblique',
             ha='left', va='top', wrap=True)
    plt.title(title,fontsize=30)
    plt.savefig(output)

if __name__ == '__main__':
    myfile = open("correlation_config.json", 'r')
    result = json.load(myfile)
    group = result["Basis_Information"]["Comparison_Group"]
    R_HOME_PATH = result["Basis_Information"]["R_HOME_PATH"]
    array_group = group.split(",")
    while True:
        if os.path.exists("./Data_Analysis"):
            for index in array_group:
                root="./Data_Analysis/%s/Quantitative/"%index
                correlation_dictionary={}
                correlation_all={}
                correlation_all["NDEPs_NDEGs"]=[[],[]]
                correlation_all["DEPs_NDEGs"] = [[], []]
                correlation_all["NDEPs_DEGs"] = [[], []]
                correlation_all["DEPs_DEGs"] = [[], []]
                correlation_dictionary["sametrend"]=[[],[]]
                correlation_dictionary["opposite"] = [[], []]
                correlation_dictionary["difference"]=[[],[]]
                with open("./Data_Analysis/%s/Quantitative/Association.txt" % index, "r") as fh:
                    n=0
                    for line in fh.readlines():
                        if n==0:
                            n+=1
                            continue
                        line=line.strip()
                        array=line.split("\t")
                        if array[4] !="Up" and array[4] !="Down" :
                            if array[7] != "Up" and array[7] != "Down":
                                correlation_all["NDEPs_NDEGs"][0].append(float(array[2]))
                                correlation_all["NDEPs_NDEGs"][1].append(float(array[5]))
                        if array[4] =="Up" or array[4] =="Down" :
                            if array[7] != "Up" and array[7] != "Down":
                                correlation_all["DEPs_NDEGs"][0].append(float(array[2]))
                                correlation_all["DEPs_NDEGs"][1].append(float(array[5]))
                        if array[4] != "Up" and array[4] != "Down":
                            if array[7] == "Up" or array[7] == "Down":
                                correlation_all["NDEPs_DEGs"][0].append(float(array[2]))
                                correlation_all["NDEPs_DEGs"][1].append(float(array[5]))
                        if array[4] == "Up" or array[4] == "Down":
                            if array[7] == "Up" or array[7] == "Down":
                                correlation_all["DEPs_DEGs"][0].append(float(array[2]))
                                correlation_all["DEPs_DEGs"][1].append(float(array[5]))
                                correlation_dictionary["difference"][0].append(float(array[2]))
                                correlation_dictionary["difference"][1].append(float(array[5]))
                        if array[4] =="Up" and array[7] =="Down":
                            correlation_dictionary["opposite"][0].append(float(array[2]))
                            correlation_dictionary["opposite"][1].append(float(array[5]))
                        if array[7] =="Up" and array[4] =="Down":
                            correlation_dictionary["opposite"][0].append(float(array[2]))
                            correlation_dictionary["opposite"][1].append(float(array[5]))
                        if array[4] =="Up" and array[7] =="Up":
                            correlation_dictionary["sametrend"][0].append(float(array[2]))
                            correlation_dictionary["sametrend"][1].append(float(array[5]))
                        if array[7] =="Down" and array[4] =="Down":
                            correlation_dictionary["sametrend"][0].append(float(array[2]))
                            correlation_dictionary["sametrend"][1].append(float(array[5]))
                correlation_map(correlation_dictionary["sametrend"][0], correlation_dictionary["sametrend"][1],
                                "Correlation of DEGs and DEPs(sametrend)","%sDEPs_DEGs_SameTrend.png"%root,"sametrend")
                correlation_map(correlation_dictionary["opposite"][0], correlation_dictionary["opposite"][1],
                                "Correlation of DEGs and DEPs(opposite)", "%sDEPs_DEGs_Opposite.png"%root,"opposite")
                correlation_map(correlation_dictionary["difference"][0], correlation_dictionary["difference"][1],
                                "Correlation of DEGs and DEPs(all)", "%scorrelation_DEPs_DEGs.png"%root,"all DEGs and DGPs")
                correlation_allmap(correlation_all,"Correlation of proteome and transcriptome", "%scorrelation_all.png" % root)
            break








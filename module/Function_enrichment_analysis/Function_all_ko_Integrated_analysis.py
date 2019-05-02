import os
import json
import math
import re
##########################################################################################
##########The purpose of this function is to draw KEGG_all map############################
##########################################################################################
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
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
        trans_id = {}
        pro_id = {}
        root = "./Data_Analysis/%s/Function/" % index
        with open("./%s/protein/%s.xls"%(index,index),"r") as fh :
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
                        if array[i] == "Protein_Sequence":
                            Sequence = i
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
                    if Sequence == -1:
                        error = 1
                        print(
                            "error:protein of title Sequence is not found!Please modify your protein Sequence as Protein_Sequence")
                    if error == 1:
                        print("Please correct the error before proceeding")
                        break

                    n += 1
                    continue

                if is_number(array[Ratio]):
                    if float(array[Ratio])==0:
                        pro_id[array[Id] + "_Protein"]=9999
                    else:

                        pro_id[array[Id]+"_Protein"]=math.log(float(array[Ratio]), 2)


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

                if is_number(array[Ratio]):
                    trans_id[array[Id]+"_mRNA"] = -1*float(array[Ratio])
        wz = open("%sglist/all.glist" % root, "w")
        with open("%spro_mRNA.ko" % root, "r") as fh:
            for line in fh.readlines():
                line = line.strip()
                array = line.split("\t")
                name=re.sub("\(.*\)","",array[0])
                if name in pro_id:
                    wz.write("%s\t%s\n" % (array[0], pro_id[name]))
                if name in trans_id:
                    wz.write("%s\t%s\n" % (array[0], trans_id[name]))
        while True:
            if os.path.exists("%sglist" % root):
                os.chdir(root)
                with open("./KEGG_all.sh" , "w") as wz:
                    wz.write( "sh /zfssz3/SP_MSI/Pipeline/FuctionalAnalysis/bin/function_all_new_pathway_cor.sh -i ./pro_mRNA -d all -k %s -g -c -w -u 1>FunLogt 2>FunLoge" % (
                          Species))
                os.system("sh KEGG_all.sh" )
                os.chdir(home)
                break


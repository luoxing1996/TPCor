import os
import json
##########################################################################################
##########The purpose of this function is to draw a volcano graph about function##########
##########################################################################################
if __name__ == '__main__':
    myfile = open("correlation_config.json", 'r')
    result = json.load(myfile)
    home = result["Basis_Information"]["Correlation analysis process server path"]
    group = result["Basis_Information"]["Comparison_Group"]
    R_HOME_PATH = result["Basis_Information"]["R_HOME_PATH"]
    array_group = group.split(",")
    wg= open("./Function_volcano.sh" , "w")
    while True:
        if os.path.exists("./Data_Analysis"):

            for index in array_group:
                root = "./Data_Analysis/%s/Function/" % index
                while True:
                    if os.path.exists("%sGO_P_all.txt"%root) and os.path.exists("%sGO_C_all.txt"%root)and os.path.exists("%sGO_F_all.txt"%root):
                        break
                root="./Data_Analysis/%s/Function/"%index

                wg.write(
                    "%s/Rscript %smodule/Function_enrichment_analysis/Function_volcano.R ./Data_Analysis/%s/Function/GO_C_all.txt ./Data_Analysis/%s/Function/volcano_C.png 'cellular_component'\n" % (
                    R_HOME_PATH,home, index, index))
                wg.write(
                    "%s/Rscript %smodule/Function_enrichment_analysis/Function_volcano.R ./Data_Analysis/%s/Function/GO_F_all.txt ./Data_Analysis/%s/Function/volcano_F.png 'Molecular_Function'\n" % (
                    R_HOME_PATH,home, index, index))
                wg.write(
                    "%s/Rscript %smodule/Function_enrichment_analysis/Function_volcano.R ./Data_Analysis/%s/Function/GO_P_all.txt ./Data_Analysis/%s/Function/volcano_P.png 'Biological_Process'\n" % (
                        R_HOME_PATH,home, index, index))
                wg.write(
                    "%s/Rscript %smodule/Function_enrichment_analysis/Function_volcano.R ./Data_Analysis/%s/Function/Pathway_all.txt ./Data_Analysis/%s/Function/volcano_Pathway.png 'KEGG_Pathway'\n" % (
                        R_HOME_PATH,home, index, index))
            wg.close()
            break

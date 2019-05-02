import json
import os
import re
import sys
root=sys.argv[1]
ppi={}
all=[]
cluster={}
protein={}
with open("%sppi_network_relation.xls"%root,"r") as fh:
    n=0
    for line in fh.readlines():

        if n==0:
            theme=line.strip()
            n+=1
            continue
        array=line.strip().split("\t")
        if float(array[4])<600:
            continue
        else:
            if array[0] not in protein.keys():

                protein[array[0]]=[array[1]]
            else:
                if array[1] not in protein[array[0]]:
                    protein[array[0]].append(array[1])
            if array[1] not in protein.keys():

                protein[array[1]] = [array[0]]
            else:
                if array[0] not in protein[array[1]]:
                    protein[array[1]].append(array[0])
            if ppi=={}:
                cluster[array[0]]=1
                ppi[array[0]]=[array[0], array[1]]


            else:
                inter=""

                for num in list(ppi.keys()):

                    if array[0] in ppi[num]:

                        if array[1] not in ppi[num]:

                            if inter!="":
                                ppi[inter]=list(set(ppi[inter]).union(set(ppi[num])))
                                del ppi[num]
                                del cluster[num]
                            else:

                                inter=num
                                ppi[num].append(array[1])
                                cluster[num] += 1
                        else:
                            inter = num

                    elif array[1] in ppi[num]:

                        if array[0] not in ppi[num]:

                            if inter!="":
                                ppi[inter]=list(set(ppi[inter]).union(set(ppi[num])))
                                del ppi[num]
                                del cluster[num]
                            else:

                                inter=num
                                ppi[num].append(array[0])
                                cluster[num] += 1
                        else:
                            inter = num
                if inter=="":
                    cluster[array[0]]=1
                    ppi[array[0]]=[array[0],array[1]]
def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]
protein_num_dic={}
wr=open("%sppi_network_protein_filter.xls"%root,"w")
wr.write("protein_ID\tcorrelation_num\tcorrelation_protein_group\n")

for index in protein.keys():
    protein_num_dic[index]=len(protein[index])
length = list(set(protein_num_dic.values()))
length=sorted(length,reverse=True)
for u in length:
    urray = get_key(protein_num_dic, u)
    for t in urray:
        wr.write("%s\t%s\t%s\n"%(t,protein_num_dic[t],",".join(protein[t])))



for i in list(cluster.keys()):
    if cluster[i]< 5:
        del(cluster[i])
        del (ppi[i])
    else:
        for t in ppi[i]:
            all.append(t)

wr=open("%sppi_network_relation_filter.xls"%root,"w")
wr.write(theme+"\n")

if all !=[]:
    sentence=[]
    with open("%sppi_network_relation.xls"%root,"r") as fh:
        n=0
        for line in fh.readlines():
            if n==0:
                n+=1
                continue
            array=line.strip().split("\t")
            if float(array[4])<600:
                continue
            elif array[0] in all:
                wr.write(line)
                sentence.append(line.strip())
    wr=open("%sppi_network_relation_cluster.xls"%root,"w")
    wr.write("%s\tcluster\n" % theme)
    length = list(set(cluster.values()))
    length=sorted(length,reverse=True)
    n = 0
    for u in length:
        urray=get_key(cluster,u)
        for t in urray:
            n += 1
            for z in ppi[t]:
                for sen in sentence[:]:
                    if z in sen:
                        wr.write("%s\t%s\n" % (sen, n))
                        sentence.remove(sen)


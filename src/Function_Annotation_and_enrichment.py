3
.p/\OH  �               @   sv  d dl Z d dlZd dlZedk�rre j� Zedd�Zeje�Z	e j� Z
e	d d Ze	d d Ze	d d	 Ze	d d
 Ze	d d Ze	d d Ze	d d Zejd�Zdej� ks�dej� k�rr�x�eD �]�Zedeef d�Zedeef d����ZdDZdEZdFZdGZdHZd Zd Z�x�ej� D �]�Z e j!� Z e jd�Z"ed k�r�x�e#e$e"��D ]�Z%e"e% dk�rbe%Ze"e% dk�rte%Zde"e% k�r�e%Znde"e% k�r�edIk�r�e%Zde"e% k�r�e%Zde"e% k�r�e%Ze"e% dk�r�e%Zde"e% k�rLe%Z&�qLW edJk�re'd� dZedKk�re'd� dZedLk�r4dZe'd� edMk�rJdZe'd � edNk�r`dZe'd!� edk�rte'd"� P ed7 Z�qe"e d#k�rej(d$e"e ej)e*e"e �d%�f � �qW W dQ R X ej+�  ed&eef d�Zed'eef d����ZdOZdPZ,dQZdRZdSZ-dTZd Zd Z�x�ej� D �]|Z e j!� Z e jd�Z"ed k�rped k�rpx~e#e$e"��D ]nZ%e"e% d(k�rpe%Zde"e% k�r�e%Zd)e"e% k�r�e%Zd*e"e% k�r�d+e"e% k�r�e%Z-d,e"e% k�rZe%Z,�qZW ed7 ZedUk�r�dZe'd-� e-dVk�r dZe'd.� e,dWk�rdZe'd/� edXk�r,dZe'd0� edYk�rBdZe'd1� edZk�rXdZe'd2� edk�r e'd"� P �q e"e d3k�r ej(d$e"e e*e"e �f � �q W W dQ R X ej+�  dej� k�r�e j.d4e � d5eef Z/e/j0d6e�Z/d7e Z1e/e1 Z2ed8d�Zej(e2� ej+�  e j3d9eef � d:eef Z4e4j0d6e�Z4d;Z5e5j0d6e�Z5e4e5 Z6ed<d�Zej(e6� ej+�  e j3d=eef � e j.e� dej� kr�e j.d>e � d?eef Z/e/j0d6e�Z/d@e Z1e/e1 Z2ed8d�Zej(e2� ej+�  e j3d9eef � dAeef Z4e4j0d6e�Z4dBZ5e5j0d6e�j0dCe�Z5e4e5 Z6ed<d�Zej(e6� ej+�  e j3d=eef � e j.e� q�W dS )[�    N�__main__zcorrelation_config.json�rZBasis_Information�SGEQueueZ
AnnotationZAnnotationMemoryZComparison_Group�R_HOME_PATHZNR_Species_typez5Whether to do transcriptome annotation and enrichmentz0Whether to do proteome annotation and enrichment�,�yesz%s/protein/%s.glist�wz./%s/protein/%s.xls�   �	Z
Protein_ID�DescriptionZMean_Ratio_ZRatio_ZPvalue_ZQvalue_ZProtein_Sequence�KEGGzXerror:transcription of title id is not found!Please modify your protein id as Protein_IDzjerror:transcription of title Pvalue is not found!Please modify your protein Pvalue as Pvalue_[sample_name]zeerror:protein of title Description is not found!Please modify your protein Description as Descriptionzxerror:protein of title Mean Ratio is not found!Please modify your protein Mean Ratio as Mean_Ratio_[sample of your name]zderror:protein of title Sequence is not found!Please modify your protein Sequence as Protein_Sequencez*Please correct the error before proceeding�-z%s	%s
�   z%s/Transcription/%s.glistz%./%s/Transcription/%s.GeneDiffExp.xlsZGeneIDZlog2ZUpZDown�valuezVerror:transcription of title id is not found!Please modify your transcription id as Idzverror:transcription of title Regulation is not found!Please modify your transcription Regulation as Up-Down-Regulationzcerror:transcription of title pvalue is not found!Please modify your transcription pvalue as p-valuezqerror:transcription of title Description is not found!Please modify your transcription Description as Descriptionz�error:transcription of title Mean Ratio is not found!Please modify your transcription Mean Ratio as Mean_Ratio_[sample of your name]z{error:transcription of title Regulation is not found!Please modify your transcription Regulation as Up-Down-Regulation(T/C)z-NAz./%s/proteinu	  
#/bin/bash 
#step1 将鉴定到蛋白序列与nr哺乳动物数据库进行blast比对,拿到proteinID与assessionID号
/opt/bio/ncbi/bin/blastall -i ../../Data_Analysis/%s/Quantitative/protein.fasta -d /zfssz3/SP_MSI/Pipeline/FuctionalAnalysis/database/nr/nr_20170924/20170924//%s.fa -o Homo_sapiens.fa.1.blastout.nr -p blastp -F F -m 7 -e 1e-5 -b 10 -v 10 -a 5
#将xml文件转换为tabular文件
/share/app/python-2.7.10/bin/python2.7 /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/xml2tabular.py -c std -o Homo_sapiens.fa.1.blastout.nr.tab Homo_sapiens.fa.1.blastout.nr
#step2  通过assessionID 找到相应的go number
/share/app/python-2.7.10/bin/python2.7 /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/BLAST3GO.py --NR_tab Homo_sapiens.fa.1.blastout.nr.tab --Accession_go /zfssz3/SP_MSI/Pipeline/FuctionalAnalysis/database/go/20171220/20171220/accession2go --output Homo_sapiens.fa.blastnr.annot
sort -u Homo_sapiens.fa.blastnr.annot >Homo_sapiens.fa.blastnr.annot.uniq
#step3 这步将分别得到go ontology层面信息的对应的go number.生成的文件为Homo_sapiens.fa.C，Homo_sapiens.fa.F Homo_sapiens.fa.P，C.conf，F.conf，P.conf
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/annot2goa.pl Homo_sapiens.fa.blastnr.annot.uniq Homo_sapiens.fa
#step4 #Convert annot file from Blast3GO to wego file，也就是把同一个蛋白对应go number 放在同一行
/share/app/python-2.7.10/bin/python2.7 /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/anno2wego.py --infile Homo_sapiens.fa.blastnr.annot.uniq --outfile Homo_sapiens.fa.blastnr.wego
#step5 通过go number 找到go.class对应的注释信息，生成的文件：Homo_sapiens.fa.GO2protein.xls
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/drawGO_modi.pl -gglist Homo_sapiens.fa.blastnr.wego -go /zfssz3/SP_MSI/Pipeline/FuctionalAnalysis/database/go/20171220/20171220/go.class -output Homo_sapiens.fa
#step6 得到go ontology 各种层面的信息和go number
cp Homo_sapiens.fa.blastnr.wego Homo_sapiens.fa.protein2GO.xls 
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/get_go.pl Homo_sapiens.fa.protein2GO.xls >Homo_sapiens.fa_GO_detail.xls

                
                ZHomo_sapiensa�  
        #!/bin/bash
        # go enrichment analysis
        export PERL5LIB=/zfssz3/SP_MSI/Pipeline/software/perl/perl-5.14.2/lib/site_perl/5.14.2/x86_64-linux:/zfssz3/SP_MSI/Pipeline/software/perl/perl-5.14.2/lib/5.14.2:/zfssz3/SP_MSI/Pipeline/software/perl/perl-5.10.1/locallib/lib/perl5/
        /zfssz3/SP_MSI/Pipeline/software/perl/perl-5.14.2/bin/perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/go_nodiff.pl -gldir ./ -sdir ./ -species %s -outdir ./ 
        
                zgo.shzFqsub -clear -cwd -l vf=%s,num_proc=5  -binding linear:5 -q %s  ./go.shu�  
#/bin/bash
#step1 blast between Homo_sapiens.fa and animal.fa (将鉴定到的蛋白序列与kegg数据库中的animal参考序列进行blast,得到蛋白对应的kegg数据库的基因ID号)
/opt/bio/ncbi/bin/blastall -i ../../Data_Analysis/%s/Quantitative/protein.fasta -d /zfssz3/SP_MSI/Pipeline/FuctionalAnalysis/database/kegg/87/87.0//%s.fa -o Homo_sapiens.fa.1.blastout.kegg -p blastp -F F -m 8 -e 1e-5 -b 10 -v 10 -a 5
#step2 blast2ko，blast→ko   通过kegg基因ID号，找到kegg pathway通路中的ko号。
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/blast2ko_v81.pl -input Homo_sapiens.fa -blastout Homo_sapiens.fa.1.blastout.kegg -type blastout -output Homo_sapiens.ko
#step3 通过kegg数据库的ko号，找到ko相应的pathway通路。
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/pathfind81.pl -fg Homo_sapiens.ko -output Homo_sapiens.path -k /zfssz3/SP_MSI/Pipeline/FuctionalAnalysis/database/kegg/87/87.0/ko_map.tab

                u�  
#!/bin/bash
#01 get diff_protein ko 拿到差异蛋白的ko号
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/get_diff_ko.pl Homo_sapiens.ko MSC-VS-C.glist MSC-VS-C.diff.ko
#02 pathfind 找到差异蛋白ko number对应的pathway通路
if [[ $pvalue == 1 ]]
then
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/pathfind81.pl -bg Homo_sapiens.ko -fg MSC-VS-C.diff.ko -output ./MSC-VS-C.diff.path -k Homo_sapiens -qvalue
else
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/pathfind81.pl -bg Homo_sapiens.ko -fg MSC-VS-C.diff.ko -output ./MSC-VS-C.diff.path -k Homo_sapiens 
fi

                z
pathway.shzKqsub -clear -cwd -l vf=%s,num_proc=5  -binding linear:5 -q %s  ./pathway.shz./%s/Transcriptionu	  
#/bin/bash 
#step1 将鉴定到蛋白序列与nr哺乳动物数据库进行blast比对,拿到transcriptionID与assessionID号
/opt/bio/ncbi/bin/blastall -i ../../Data_Analysis/%s/Quantitative/transcription.fasta -d /zfssz3/SP_MSI/Pipeline/FuctionalAnalysis/database/nr/nr_20170924/20170924//%s.fa -o Homo_sapiens.fa.1.blastout.nr -p blastp -F F -m 7 -e 1e-5 -b 10 -v 10 -a 5
#将xml文件转换为tabular文件
/share/app/python-2.7.10/bin/python2.7 /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/xml2tabular.py -c std -o Homo_sapiens.fa.1.blastout.nr.tab Homo_sapiens.fa.1.blastout.nr
#step2  通过assessionID 找到相应的go number
/share/app/python-2.7.10/bin/python2.7 /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/BLAST3GO.py --NR_tab Homo_sapiens.fa.1.blastout.nr.tab --Accession_go /zfssz3/SP_MSI/Pipeline/FuctionalAnalysis/database/go/20171220/20171220/accession2go --output Homo_sapiens.fa.blastnr.annot
sort -u Homo_sapiens.fa.blastnr.annot >Homo_sapiens.fa.blastnr.annot.uniq
#step3 这步将分别得到go ontology层面信息的对应的go number.生成的文件为Homo_sapiens.fa.C，Homo_sapiens.fa.F Homo_sapiens.fa.P，C.conf，F.conf，P.conf
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/annot2goa.pl Homo_sapiens.fa.blastnr.annot.uniq Homo_sapiens.fa
#step4 #Convert annot file from Blast3GO to wego file，也就是把同一个蛋白对应go number 放在同一行
/share/app/python-2.7.10/bin/python2.7 /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/anno2wego.py --infile Homo_sapiens.fa.blastnr.annot.uniq --outfile Homo_sapiens.fa.blastnr.wego
#step5 通过go number 找到go.class对应的注释信息，生成的文件：Homo_sapiens.fa.GO2transcription.xls
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/drawGO_modi.pl -gglist Homo_sapiens.fa.blastnr.wego -go /zfssz3/SP_MSI/Pipeline/FuctionalAnalysis/database/go/20171220/20171220/go.class -output Homo_sapiens.fa
#step6 得到go ontology 各种层面的信息和go number
cp Homo_sapiens.fa.blastnr.wego Homo_sapiens.fa.transcription2GO.xls 
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/get_go.pl Homo_sapiens.fa.transcription2GO.xls >Homo_sapiens.fa_GO_detail.xls

    
                        a�  
#!/bin/bash
# go enrichment analysis
export PERL5LIB=/zfssz3/SP_MSI/Pipeline/software/perl/perl-5.14.2/lib/site_perl/5.14.2/x86_64-linux:/zfssz3/SP_MSI/Pipeline/software/perl/perl-5.14.2/lib/5.14.2:/zfssz3/SP_MSI/Pipeline/software/perl/perl-5.10.1/locallib/lib/perl5/
/zfssz3/SP_MSI/Pipeline/software/perl/perl-5.14.2/bin/perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/go_nodiff.pl -gldir ./ -sdir ./ -species %s -outdir ./ 

                        u  
#/bin/bash
#step1 blast between Homo_sapiens.fa and animal.fa (将鉴定到的蛋白序列与kegg数据库中的animal参考序列进行blast,得到蛋白对应的kegg数据库的基因ID号)
/opt/bio/ncbi/bin/blastall -i ../../Data_Analysis/%s/Quantitative/transcription.fasta -d /zfssz3/SP_MSI/Pipeline/FuctionalAnalysis/database/kegg/87/87.0//%s.fa -o Homo_sapiens.fa.1.blastout.kegg -p blastx -F F -m 8 -e 1e-5 -b 10 -v 10 -a 5
#step2 blast2ko，blast→ko   通过kegg基因ID号，找到kegg pathway通路中的ko号。
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/blast2ko_v81.pl -input Homo_sapiens.fa -blastout Homo_sapiens.fa.1.blastout.kegg -type blastout -output Homo_sapiens.ko
#step3 通过kegg数据库的ko号，找到ko相应的pathway通路。
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/pathfind81.pl -fg Homo_sapiens.ko -output Homo_sapiens.path -k /zfssz3/SP_MSI/Pipeline/FuctionalAnalysis/database/kegg/87/87.0/ko_map.tab

                        u�  
#!/bin/bash
#01 get diff_transcription ko 拿到差异蛋白的ko号
perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/get_diff_ko.pl Homo_sapiens.ko MSC-VS-C.glist MSC-VS-C.diff.ko
#02 pathfind 找到差异蛋白ko number对应的pathway通路
if [[ $pvalue == 1 ]]
then
    perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/pathfind81.pl -bg Homo_sapiens.ko -fg MSC-VS-C.diff.ko -output ./MSC-VS-C.diff.path -k Homo_sapiens -qvalue
else
    perl /ldfssz1/SP_MSI/Pipeline/Pipeline/iTRAQ/iTRAQ_2017b/module/subroutine/pathfind81.pl -bg Homo_sapiens.ko -fg MSC-VS-C.diff.ko -output ./MSC-VS-C.diff.path -k Homo_sapiens 
fi
mv MSC-VS-C.diff.ko MSC-VS-C.ko
mv MSC-VS-C.diff.path MSC-VS-C.path
                        zMSC-VS-C�����r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   )7�osZjsonZmath�__name__�getcwd�home�openZmyfile�load�resultZListr   Zmemory�groupr   ZSpeciesZtransZpro�splitZarray_group�lower�indexZwzZfhZIdZPvaluer   ZRatio�Sequence�n�error�	readlines�line�stripZarray�range�len�ir   �print�write�log�float�closeZpvalueZ
Regulation�chdirZgo_annotation�replaceZgo_enrichmentZgo�popenZpathway_annotationZpathway_enrichmentZpathway� r-   r-   �R/ldfssz1/SP_MSI/Pipeline/Pipeline/TP_Cor/src/Function_Annotation_and_enrichment.py�<module>   sb  












6










.











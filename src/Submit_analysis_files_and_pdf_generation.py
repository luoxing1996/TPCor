3
�?�\#�  �               @   s�  d dl Z d dlZd dlZd dlmZ d dlmZ d dlmZ e	dd�Z
eje
�Zed d Zed	 d
 Zed	 d Zed	 d Zed	 d Zed	 d Zed d Zed d Zed d Zejd�ZdZdeeeeef ZdZee e ZdZdZdZdZdd� Z dd� Z!e"dk�r�e j#� Z$d Z%d Z&�x�eD �]�Z'd!ej(� k�r4e j)d"� xVe j*d#�D ]H\Z+Z,Z-x:e-D ]2Z.d$e.k�rhd%e.k�rhd&e.k�rhe j)d'e. � �qhW �qXW e j#� Z$e j/d(e' � e j)d)� e j/e$� e j/d*e' � e j)d+� e j/e$� e j/d,e' � e j)d-� e j/e$� e j/d.e' � e j)d/� e j/e$� e j)d0� d1e' Z0e j/e0� xFe j*d#�D ]8\Z+Z,Z-x*e-D ]"Z1d2e1k�rld3e1k�rle e1� �qlW �q\W e j/e$� d4e' Z2e j/e2� xFe j*d#�D ]8\Z+Z,Z-x*e-D ]"Z1d2e1k�r�d3e1k�r�e e1� �q�W �q�W e j/e$� d5e' Z3e j/e3� xFe j*d#�D ]8\Z+Z,Z-x*e-D ]"Z1d2e1k�r4d3e1k�r4e e1� �q4W �q$W e j/e$� d6e' Z4e j/e4� xZe j*d#�D ]L\Z+Z,Z-d7e-k�s�d8e-k�r�x*e-D ]"Z1d2e1k�r�d3e1k�r�e e1� �q�W �q�W e j/e$� e!e'�\Z5Z6e%e57 Z%e&e67 Z&�q.W e	d9d:�Z7d!ej(� k�r6ee% e e e& e Z8nd;ej(� k�rTee% e e Z8e7j9e8� e j)d<�Z:e:j;� Z<e:j=�  e<d k�r�e j#� jd=�d> Z>xNe j)d?� e j)d@e> � e j)dAee>f � e j?j@dBe> ��r�e jAdC� P �q�W dS )D�    N)�portrait)�canvas)�Imagezcorrelation_config.json�rZBasis_InformationZComparison_GroupzFilter ParametersZProteinFoldChangeZGeneFoldChangezProtein p value ThresholdzGene p value ThresholdZBlastEvaluez(Correlation analysis process server pathzTranscription factorz+Whether to do transcription factor analysisz!Whether to empty the process file�,u�  
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>华大基因蛋白质组与转录组关联分析结题报告</title>
<link href="css/report.css" rel="stylesheet" type="text/css">
<script language="javascript" src="js/jquery.js"></script>
<script language="javascript" src="js/report.js"></script>
<style type="text/css">
html{
	overflow:auto;
}
body{
	position:relative;
}
</style>
</head>
<body>
	<div class=seq_cn1>
		<div class="top_btn"></div>
		<h1><a name="1"></a>1 关联分析概述</h1>
		<h2><a name="1.1"></a>1.1 多组学联合分析概述</h2>
			<p>对复杂生物性状遗传基础的研究是众多学者的重要研究内容。生物性状多样性的主要遗传基础是基因表达多样性，并且受多层级复杂而精细的遗传调控。基因表达调控主要表现在以下层面：在基因组水平存在单核苷酸多态性（SNP）、拷贝数变异（CNV）、杂合性丢失（LOH）和基因组重排（易位）等；在表观基因组水平存在DNA甲基化修饰、组蛋白修饰、转录因子结合以及micRNA作用等；在转录水平存在可变剪切，蛋白水平存在翻译后加工与修饰等。
			<p>随着实验技术的进步，对生物系统中的基因组，表观基因组，转录组，蛋白质组和代谢组等数据的测量成为可能。此外，测量样品从全血或组织发展到了单细胞。生物性状是遗传因素和环境因素共同作用的结果。已有多种技术研究基因的表达对表型的影响。长期以来，对各个组学的数据都是进行独立的分析来研究该组学数据与生物学过程的关系。通过单一组学数据的分析，目前已经对部分物种的遗传信息和代谢通路进行了阐释。但是，仅用单一组学数据很难对复杂性状的遗传病原学和生物网络调控进行解释。因此，为了研究复杂生物性状，基于多组学的系统生物学快速发展起来。整合多组学数据进行分析可以弥补单一组学数据分析时数据缺失、噪音等因素带来的数据问题。多组学数据资源之间可以进行相互验证，减少单一组学分析带来的假阳性。重要的是多组学数据联合分析更有利于对生物学模型进行表型与遗传过程调控机制的研究[1]。
		<h2><a name="1.2"></a>1.2 蛋白质组与转录组关联分析概述</h2>
			<p>细胞内蛋白质的产生和蛋白浓度的维持需要一系列紧密相关的生物学过程，包括基因的转录，mRNA加工、降解、翻译，蛋白质的加工、修饰和转运等。在基因表达过程中，蛋白质丰度的变化动态的反映了这一过程中的各级调控。然而，研究人员往往用mRNA的表达量来预测对应蛋白的表达量，因此对于基因表达各级调控的机理研究一直是研究的难点。DNA测序技术和质谱技术的进步为获取mRNA和蛋白质表达丰度提供了可能。目前对于单一的细胞过程所受到的调控有较为深入的研究，但对基因表达所涉及的整个过程及其调控了解还很少[2]。通过蛋白质组学和转录组学数据关联分析有利于研究基因表达过程的多级调控[3]。
			<p>分子生物学的中心法则解释了基因表达信息流的传递过程（gene->mRNA->protein）。基因在表达的过程中受到受多层次的调控，目前多数文献报道mRNA与相应的蛋白质之间的表达一致性不是很高，因此将蛋白质组和转录组进行联合分析，有助于发现基因表达调控情况[4]。Mary Muers在nature上发表论述，指出mRNA和相应的蛋白关联程度不高，约为百分之二十七到百分之四十，但各个组学水平的定量信息是基因表达调控研究的基础[5]。Bouchal P等人采用转录组与蛋白组关联分析寻找轻度乳腺癌转移的潜在biomarkers，用于后续判定轻度乳腺癌患者中存在转移的高风险个体，对于后续随访和治疗起到针对性的作用[6]。Petersen HO等人利用转录组和蛋白组/磷酸化蛋白组关联分析研究水螅头部重生的分子机制。Wnts和转变生长因子TGF，β-相关因子等信号分析被激活参与随后的重生反应；同时表明干细胞及其神经元等衍生物未参与水螅头部重生[7]。Wang J等人采用转录组与蛋白组关联分析研究苏云金杆菌孢子的代谢调控与半孢晶体形成机制[8]。
		<h1><a name="2"></a>2 关联分析流程</h1>
		<h2><a name="2.1"></a>2.1 蛋白质组与转录组关联分析流程</h2>
			<p>蛋白质组与转录组关联分析基本原理为中心法则，基于基因表达信息流情况，在mRNA和蛋白水平进行组学测序，将两组学数据进行整合分析，观测基因表达过程。基于数据不同分类和关联层次的不同，关联分析流程如图2-1。
			<p> <div class="tc"><img width=100% src="./images/flow_chart.png" /></div>
			<p><b>图2-1 蛋白组与转录组关联分析流程图</b>  蛋白组与转录组关联分析流程图,具体项目根据情况进行相应内容分析。
		<h2><a name="2.2"></a>2.2 蛋白质组与转录组关联分析参数</h2>
			<p>关联过程中需对转录组和蛋白组数据进行不同的处理与整合，本次关联分析数据筛选及差异定义如表2-1
			<center><b>表2-1 关联分析主要参数一览表</b></center>
				<div>
					<table>
a�  
                        <tr><th>Type</th><th>Value</th></tr>
						<tr><td>Protein_FoldChange</td><td>%s</td></tr>
						<tr><td>Gene_FoldChange</td><td>%s</td></tr>
						<tr><td>Protein p value  Threshold</td><td>%s</td></tr>
						<tr><td>Gene p value Threshold</td><td>%s</td></tr>
						<tr><td>Blast_Evalue</td><td>%s</td></tr>
						<tr><td>GO_Significant</td><td><0.05</td></tr>
						<tr><td>Pathway_Significant</td><td><0.05</td></tr>	
						<tr><td>Top_number</td><td>20</td></tr>

u�  
					</table>
					<br>
			<p><b>表注：</b> 关联分析主要参数表 详细释义如下：Protein_UniquePeptide:蛋白质定量采用的特有肽段数量，Protein_FoldChange：定义差异蛋白所用倍数，Protein_Significant：蛋白显著性水平阀值，Gene_FoldChange：定义差异基因所用倍数，Gene_Significant：基因显著性水平阀值，GO_Significant：GO富集显著性阀值，Pathway_Significant：Pathway富集分析显著性阀值，Top_number：GO和Pathway富集关联分析图片展示的条目数。如果采用了BLAST分析，则 BlastIdentity：Blast一致性过滤水平，BlastEvalue：Blast期望值水平。参数一栏如果出现“NA”则表示本次关联分析未采用此参数，或此参数无意义。
		<h1><a name="3"></a>3 定量的关联分析</h1>
		<h2><a name="3.1"></a>3.1 关联数量统计</h2>
			<p>转录组与蛋白质组是检测一定状态下特定的生物个体、组织、细胞或细胞器的mRNA和蛋白质表达水平。关联分析时，首先得到特定时空下的个体、组织、细胞或细胞器的转录组和蛋白质组数据，当某一个蛋白质在转录组水平有表达量时，被认为关联到。在鉴定、定量和显著差异3个层面，关联到的蛋白质和基因数量关系如下表3-1。
			<center><b>表3-1 在定量、显著差异2个范围中，能关联到的蛋白质和基因数量关系</b></center>
				<div>
					<table>

u�v  
                    </table>
					<br>
			<p>分别对定量和差异两个层面关联数量进行统计并画韦恩图，定量层面韦恩图见图3-1-1,3-1,2。定量和差异关联Venn图具体见分析数据。
			<p> <div class="tc"><img width=50% src="./material/venn_all.png" /></div>
			<p><b>图3-1-1 所有蛋白质组与转录组在鉴定层面关联数量venn图</b>  
			<p>输出文件：
			<p><a href="./material/venn_ALL.txt" target="_blank">Quantitative_association_analysis_result/Association.txt</a>
			<p><a href="./material/venn_ALL.png" target="_blank">Quantitative_association_analysis_result/venn_ALL.png</a>
			<p><a href="./material/venn_ALL.pdf" target="_blank">Quantitative_association_analysis_result/venn_ALL.pdf</a>
			<p> <div class="tc"><img width=50% src="./material/venn_DEPs_DEGs.png" /></div>
			<p><b>图3-1-2 差异蛋白质组与转录组在鉴定层面关联数量venn图</b>  
			<p>输出文件：
			<p><a href="./material/venn_DEGs_and_DEPs.txt" target="_blank">Quantitative_association_analysis_result/Association.txt</a>
			<p><a href="./material/venn_DEGs_and_DEPs.png" target="_blank">Quantitative_association_analysis_result/venn_DEPs_DEGs.png</a>
			<p><a href="./material/enn_DEGs_and_DEPs.pdf" target="_blank">Quantitative_association_analysis_result/venn_DEGs_and_DEPs.pdf</a>
			<br>
			<br>
		<h2><a name="3.2"></a>3.2 蛋白质组差异分析</h2>
			<p>对蛋白质的比较组的差异进行分类，结果如图3-2
			<p> <div class="tc"><img width=80% src="./material/volcano_protein.png" /></div>
			<p><b>图3-2 蛋白质组的火山图</b>  红点为上调蛋白，绿点为下调蛋白，蓝点为p-value/< 0.05的非差异蛋白，灰点为p-value>0.05的非差异蛋白
			<p>输出文件：
			<p><a href="./material/volcano_protein.txt" target="_blank">Quantitative_association_analysis_result/Association_volcano.txt</a>
			<p><a href="./material/volcano_protein.png" target="_blank">Quantitative_association_analysis_result/volcano_protein.png</a>
			<p><a href="./material/volcano_protein.pdf" target="_blank">Quantitative_association_analysis_result/volcano_protein.pdf</a>
			<br>
			<br>
		<h2><a name="3.3"></a>3.3 转录组差异分析</h2>
			<p>对蛋白质的比较组的差异进行分类，结果如图3-3
			<p> <div class="tc"><img width=80% src="./material/volcano_transcription.png" /></div>
			<p><b>图3-3 转录组的火山图</b>  红点为上调基因，绿点为下调基因，蓝点为p-value/< 0.05的非差异基因，灰点为p-value>0.05的非差异基因
			<p>输出文件：
			<p><a href="./material/volcano_correlation.txt" target="_blank">Quantitative_association_analysis_result/Association_volcano.txt</a>
			<p><a href="./material/volcano_correlation.png" target="_blank">Quantitative_association_analysis_result/volcano_transcription.png</a>
			<p><a href="./material/volcano_correlation.pdf" target="_blank">Quantitative_association_analysis_result/volcano_transcription.pdf</a>

			<br>
			<br>
		<h1><a name="4"></a>4 表达的关联分析</h1>
		<h2><a name="4.1"></a>4.1 非关联与关联的表达量分析</h2>
			<p>在转录组中，对是否关联上的基因的表达量的差异情况进行分析，可以看出分布差异，从而指导后续对比较组mRNA转录后的调控机制的分析。
			<p> <div class="tc"><img width=80% src="./material/correlation_scatter_plot.png" /></div>
			<p><b>图4-1 是否关联上的基因的表达量的差异情况的散点图</b>  图为是否关联上的基因的表达量的差异情况，横坐标为对照组的表达量，纵坐标为实验组的表达量。其中红点为关联上的基因，蓝点为没有关联上的基因。
			<p>输出文件：
			<p><a href="./material/correlation_scatter_plot.txt" target="_blank">Quantitative_association_analysis_result/correlation_scatter_plot.txt</a>
			<p><a href="./material/correlation_scatter_plot.png" target="_blank">Quantitative_association_analysis_result/correlation_scatter_plot.png</a>
			<p><a href="./material/correlation_scatter_plot.pdf" target="_blank">Quantitative_association_analysis_result/correlation_scatter_plot.pdf</a>
			<br>
			<br>

		<h2><a name="4.2"></a>4.2 表达关联分类</h2>
			<p>据文献报道mRNA与其蛋白在表达量上呈现较为复杂的非线性关系[1-8]，以下分析中，将基于mRNA水平和蛋白质水平的表达结果，根据不同的关联类型，分别讨论。
			<p>1）DEPs_DEGs_SameTrend:蛋白表达上调、基因表达上调或蛋白表达下调、基因表达下调
			<p>2）DEPs_DEGs_Opposite:蛋白表达上调、基因表达下调或蛋白表达下调、基因表达上调
			<p>3）DEPs_NDEGs:蛋白表达有差异、基因表达无差异
			<p>4）NDEPs_DEGs:蛋白表达无差异、基因表达有差异
			<p>5）NDEPs_NDEGs:蛋白表达无差异、基因表达无差异
			<p>将蛋白水平和转录组水平关联到的所有表达数据进行关联分析，计算Spearman相关系数[9]。多数文献报道，表达量相关性呈适度的相关性，除实验过程和数据类型的不同导致相关性没有呈现高度一致性，基因表达过程中复杂的调控机制对其也有重要的影响[10]。
		<h3><a name="4.2.1"></a>4.2.1 DEPs_DEGs_all</h3>
			<p>图4-2-1 所有定量蛋白质和基因的表达关联图 图为两个样品蛋白质和基因定量值的关联分析图，横坐标为蛋白质的表达量，纵坐标为基因的表达量。黑点表示mRNA和蛋白都无显著性差异，红点表示mRNA无显著性差异，蛋白显著性差异，绿点表示mRNA显著差异，蛋白无显著差异，蓝点表示mRNA和蛋白都显著性差异。
			<p> <div class="tc"><img width=80% src="./material/correlation_all.png" /></div>
			<p>输出文件：
			<p><a href="./material/Association.txt" target="_blank">Quantitative_association_analysis_result/Association.txt</a>
			<p><a href="./material/correlation_all.png" target="_blank">Quantitative_association_analysis_result/correlation_all.png</a>
			<p><a href="./material/correlation_all.pdf" target="_blank">Quantitative_association_analysis_result/correlation_all.pdf</a>
			<br>
			<br>

		<h3><a name="4.2.2"></a>4.2.2 DEPs_DEGs</h3>
			<p>图4-2-2 显著差异蛋白质和显著差异基因表达关联图
			图为两个样品显著蛋白质和显著差异基因的关联分析图，横坐标为蛋白质的表达量，纵坐标为基因的表达量。
			<p> <div class="tc"><img width=80% src="./material/correlation_DEPs_DEGs.png" /></div>
			<p>输出文件：
			<p><a href="./material/Association.txt" target="_blank">Quantitative_association_analysis_result/Association.txt</a>
			<p><a href="./material/correlation_DEPs_DEGs.png" target="_blank">Quantitative_association_analysis_result/correlation_DEPs_DEGs.png</a>
			<p><a href="./material/correlation_DEPs_DEGs.pdf" target="_blank">Quantitative_association_analysis_result/correlation_DEPs_DEGs.pdf</a>
			<br>
			<br>
		<h3><a name="4.2.3"></a>4.2.3 DEPs_DEGs_SameTrend</h3>
			<p>蛋白组与转录组从两个不同的层面反映了基因表达的情况，联合分析的目的是实现数据互补，获取生物体更加完整的表达信息。对显著差异表达趋势相同的蛋白质和mRNA信息进行分析，有助于相互印证测序结果和解释基因表达调控等情况[11-13]。根据蛋白质水平和mRNA水平表达趋势，对变化趋势相同的mRNA和蛋白进行相关性分析，如图4-2-3所示。
			<p> <div class="tc"><img width=80% src="./material/DEPs_DEGs_SameTrend.png" /></div>
			<p><b>图4-2-3 表达变化趋势相同蛋白质和基因表达关联图</b>  
			<p>输出文件：
			<p><a href="./material/Association.txt" target="_blank">Quantitative_association_analysis_result/Association.txt</a>
			<p><a href="./material/DEPs_DEGs_SameTrend.png" target="_blank">Quantitative_association_analysis_result/DEPs_DEGs_SameTrend.png</a>
			<p><a href="./material/DEPs_DEGs_SameTrend.pdf" target="_blank">Quantitative_association_analysis_result/DEPs_DEGs_SameTrend.pdf</a>
			<br>
			<br>
		<h3><a name="4.2.4"></a>4.2.4 DEPs_DEGs_Opposite</h3>
			<p>蛋白质与转录组测序数据从两个不同的层面反映了基因表达的情况，将两组学数据进行联合分析可实现数据差异比较。从表达变化趋势相反的蛋白质和mRNA信息中可分析mRNA转录后的调控机制，蛋白翻译效率等情况[14-16],结果见图4-2-4。
			<p> <div class="tc"><img width=80% src="./material/DEPs_DEGs_Opposite.png" /></div>
			<p>输出文件：
			<p><a href="./material/Association.txt" target="_blank">Quantitative_association_analysis_result/Association.txt</a>
			<p><a href="./material/DEPs_DEGs_Opposite.png" target="_blank">Quantitative_association_analysis_result/DEPs_DEGs_Opposite.png</a>
			<p><a href="./material/DEPs_DEGs_Opposite.png" target="_blank">Quantitative_association_analysis_result/DEPs_DEGs_Opposite.pdf</a>
			<br>
			<br>


		<h1><a name="5"></a>5 GO富集关联分析</h1>
		<h2><a name="5.1"></a>5.1 GO富集关联分析概述</h2>
			<p>随着高通量测序和质谱技术的进步，在转录组水平和蛋白质组水平上积累了大量的组学数据。但基因表达受多层次的表达调控，mRNA和蛋白之间表达情况的复杂性成为解读组学数据的主要障碍。
			<p>在传统的分子生物学研究中，认为一个基因表达一个蛋白，一个蛋白有一个结构，一个结构完成一个功能，也就是遵从由序列到结构再到功能这样一个思维方式。对单个基因及蛋白的研究，有利于深入研究基因及其产物在细胞中的功能，但细胞的增殖、衰老、病变及修复往往处于生物系统调控网络中，对于单个基因及蛋白的研究有以下不足：①忽略了细胞过程中与其他基因及蛋白的相互作用；②不同的生理条件或细胞同一基因或蛋白检测的可重复性不理想；③单个基因及蛋白的功能难以解释某种生物表型或是生物特征。现在越来越多的事实说明，一个基因的单独表达往往不能主宰一个生物学事件的发生，一个事件的发生是一组基因的同时表达，是一组蛋白质的协同作用。因此，实际上更真实表现生物学功能的，应当是一组相关基因、一组相互作用的蛋白质，这些相互作用着的蛋白质就必然构成一个网络。所以真正能更真实说明生物学功能的应该是一组组相互作用的生物大分子形成的网络，这就是系统生物学所带来的思维上的变化和研究思路的变化[17]。为了克服单基因分析的诸多不足，国外的生物数据分析学者于2005年提出了基于已定义的基因集(gene set)进行分析的方法—基因富集分析(gene set enrichmentanalysis，GSEA)”。基因集的定义基于统一的先验生物学知识，如已发表的有关生物通路，基因共表达信息等。一个基因集具有相同生物学功能或位于同一生物学通路中的基因。目前常用的定义基因集的基因注释数据库有Gene Ontology(GO)、KEGG等[18-19]。对于多组学数据，从转录组水平和蛋白质组水平分别进行GO及代谢通路上进行富集分析，并将两组学的数据进行整合分析，有利于从基因集共表达层面研究基因表达调控[20-23]。
			<p>GO功能显著性富集分析给出与所有鉴定到的蛋白质(或该物种基因)背景相比，差异蛋白质（或差异基因）中显著富集的GO功能条目，从而给出差异蛋白质（或差异基因）与哪些生物学功能显著相关。该分析首先把所有差异蛋白质（或差异基因）向Gene Ontology数据库（http://www.geneontology.org/)的各个term映射，计算每个term的蛋白质（或基因）数目，然后应用超几何检验，找出与所有蛋白质（或该物种基因）背景相比，在差异蛋白质（或差异基因）中显著富集的GO条目。其计算公式为：<div class="tc"><img src="./images/GO_enrichment.png" /></div>
			<p>其中N为所有蛋白（或该物种基因）中具有GO注释信息的蛋白（或基因）数目，n为N中差异蛋白（或差异基因）的数目，M为所有蛋白（或基因）中注释到某个GO条目的蛋白（或基因）数目，m为注释到某个GO条目的差异蛋白（或差异基因）数目。计算得到P-value值，以P-value≤0.05为阈值，满足此条件的GOterm定义为在差异蛋白质（或差异基因）中显著富集的GO term。通过GO显著性分析能确定差异蛋白（或基因）行使的主要生物学功能。

		<h2><a name="5.2"></a>5.2 GO富集关联分析</h2>
			<p>Gene Ontology（简称GO）是一个国际标准化的基因功能分类体系，提供了一套动态更新的标准词汇表（Controlled Vocabulary）来全面描述生物体中基因和基因产物的属性。GO总共有三个本体（Ontology），分别描述基因的分子功能（Molecular Function）、所处的细胞位置（Cellular Component）、参与的生物过程（Biological Process）。
			<p>基因产物可能分别具有分子生物学上的功能、生物学途径和在细胞中的组件作用。当然，它们也可能在某一个方面有多种性质。如细胞色素C，在分子功能上体现为电子传递活性，在生物学途径中与氧化磷酸化和细胞凋亡有关，在细胞中存在于线粒体质中和线粒体内膜上。
			<p>对转录组差异表达基因和蛋白质组差异表达蛋白在GO条目上的注释及富集情况进行分析，并将相同的GO功能条目中注释到的基因和蛋白进行整合分析，同一GO条目上的基因和蛋白在功能上相似，对环境因素的反馈可能存在共调控或是共表达等情况。有利于从基因集的层面研究基因表达调控。
		<h3><a name="5.2.1"></a>5.2.1 GO富集关联相关性分析</h3>
			<p>通过超几何检验对基因和蛋白分别进行富集分析，并将两个组学的富集条目进行关联分析，得到两个组学层面上的富集情况,按照“GO富集关联数量统计”中描述的三类分类情况，统计各个GO条目在蛋白质组与转录组中的富集显著性，结果分布如图5-2-1。结果文件中*html文件对每个富集的GO条目与GO数据库进行了链接，可通过链接查询该条目的详细信息。
			<p> <div class="tc"><img width=80% src="./material/volcano_P.png" /></div>
			<p><b>图5-2-1 GO富集关联分析显著性分布图</b>
			<p>输出文件：
			<p><a href="./material/GO_C_all.txt" target="_blank">Function_enrichment_analysis_result/GO_C_all.txt</a>
			<p><a href="./material/GO_F_all.txt" target="_blank">Function_enrichment_analysis_result/GO_F_all.txt</a>
			<p><a href="./material/GO_P_all.txt" target="_blank">Function_enrichment_analysis_result/GO_P_all.txt</a>
			<p><a href="./material/volcano_C.png" target="_blank">Function_enrichment_analysis_result/volcano_C.png</a>
			<p><a href="./material/volcano_F.png" target="_blank">Function_enrichment_analysis_result/volcano_F.png</a>
			<p><a href="./material/volcano_P.png" target="_blank">Function_enrichment_analysis_result/volcano_P.png</a>
			<p><a href="./material/volcano_C.pdf" target="_blank">Function_enrichment_analysis_result/volcano_C.pdf</a>
			<p><a href="./material/volcano_F.pdf" target="_blank">Function_enrichment_analysis_result/volcano_F.pdf</a>
			<p><a href="./material/volcano_P.pdf" target="_blank">Function_enrichment_analysis_result/volcano_P.pdf</a>
			<br>
			<br>
		<h3><a name="5.2.2"></a>5.2.2 GO关联数量及富集因子分析</h3>
			<p>将两个组学的富集条目进行关联分析，得到两个组学层面上的富集情况,按照“GO富集关联数量统计”中描述的三类分类情况，统计各个GO条目在蛋白质组与转录组中关联数目与富集因子，其中Y轴为各个GO条目，并且统计了该条目所关联的蛋白数量，两列分别为转录组与蛋白质组，气泡大小代表富集数量，颜色代表富集因子，圆圈代表转录组（蛋白质组）p值大于等于0.05,钻石形代表转录组（蛋白质组）p值小于0.05,结果分布如图5-2-2。
			<p> <div class="tc"><img width=100% src="./material/bubble_P.png" /></div>
			<p><b>图5-2-2 GO关联数量及富集因子分析四维气泡图</b>
			<p>输出文件：
			<p><a href="./material/GO_C.txt" target="_blank">Function_enrichment_analysis_result/GO_C.txt</a>
			<p><a href="./material/GO_F.txt" target="_blank">Function_enrichment_analysis_result/GO_F.txt</a>
			<p><a href="./material/GO_P.txt" target="_blank">Function_enrichment_analysis_result/GO_P.txt</a>
			<p><a href="./material/bubble_C.png" target="_blank">Function_enrichment_analysis_result/bubble_C.png</a>
			<p><a href="./material/bubble_F.png" target="_blank">Function_enrichment_analysis_result/bubble_F.png</a>
			<p><a href="./material/bubble_P.png" target="_blank">Function_enrichment_analysis_result/bubble_P.png</a>
			<p><a href="./material/bubble_C.pdf" target="_blank">Function_enrichment_analysis_result/bubble_C.pdf</a>
			<p><a href="./material/bubble_F.pdf" target="_blank">Function_enrichment_analysis_result/bubble_F.pdf</a>
			<p><a href="./material/bubble_P.pdf" target="_blank">Function_enrichment_analysis_result/bubble_P.pdf</a>
			<br>
			<br>
		<h3><a name="5.2.3"></a>5.2.3 GO关联上的差异分析概率热图</h3>
			<p>将两个组学的富集条目进行关联分析，得到两个组学层面上的富集情况,按照“GO富集关联数量统计”中描述的三类分类情况，统计各个GO条目在6种差异的分布情况，其中X轴代表蛋白质组与转录组在同上调，同下调，只蛋白质组上调，只蛋白质组下调，只转录组上调，只转录组下调的6种情况。其中Y轴为各个GO条目，并且统计了该条目所关联的蛋白数量，热图颜色代表该情况在该GO条目关联上的蛋白中所占的比例，结果分布如图5-2-3。
			<p> <div class="tc"><img width=100% src="./material/correlation_function_map_P.png" /></div>
			<p><b>图5-2-3 GO关联数量及富集因子分析气泡图</b>
			<p>输出文件：
			<p><a href="./material/correlation_function_GO_C.txt" target="_blank">Function_enrichment_analysis_result/correlation_function_GO_C.txt</a>
			<p><a href="./material/correlation_function_GO_F.txt" target="_blank">Function_enrichment_analysis_result/correlation_function_GO_F.txt</a>
			<p><a href="./material/correlation_function_GO_P.txt" target="_blank">Function_enrichment_analysis_result/correlation_function_GO_P.txt</a>
			<p><a href="./material/correlation_function_map_C.png" target="_blank">Function_enrichment_analysis_result/correlation_function_map_C.png</a>
			<p><a href="./material/correlation_function_map_P.png" target="_blank">Function_enrichment_analysis_result/correlation_function_map_P.png</a>
			<p><a href="./material/correlation_function_map_F.png" target="_blank">Function_enrichment_analysis_result/correlation_function_map_F.png</a>
			<p><a href="./material/correlation_function_map_C.pdf" target="_blank">Function_enrichment_analysis_result/correlation_function_map_C.pdf</a>
			<p><a href="./material/correlation_function_map_P.pdf" target="_blank">Function_enrichment_analysis_result/correlation_function_map_P.pdf</a>
			<p><a href="./material/correlation_function_map_F.pdf" target="_blank">Function_enrichment_analysis_result/correlation_function_map_F.pdf</a>
			<br>
			<br>
		<h1><a name="6"></a>6 Pathway功能富集分析</h1>
		<h2><a name="6.1"></a>6.1 Pathway富集关联分析概述</h2>
			<p>Pathway显著性富集分析方法同Pathway功能富集分析，是以KEGG Pathway为单位，应用超几何检验，找出与所有鉴定到蛋白（或该物种基因）背景相比，在差异蛋白（或差异基因）中显著性富集的Pathway。通过Pathway显著性富集能确定差异蛋白（或差异基因）参与的最主要生化代谢途径和信号转导途径。
		<h2><a name="6.2"></a>6.2 Pathway富集关联分析</h2>
			<p>在生物体内，不同蛋白相互协调行使其生物学行为，基于Pathway的分析有助于更进一步了解其生物学功能。KEGG是有关Pathway的主要公共数据库（Kanehisa，2008），通过Pathway分析能确定蛋白质参与的最主要生化代谢途径和信号转导途径。
		<h3><a name="6.2.1"></a>6.2.1 Pathway富集关联相关性分析</h3>
			<p>通过超几何检验对基因和蛋白分别进行富集分析，并将两个组学的富集条目进行关联分析，得到两个组学层面上的富集情况,按照“Pathway富集关联数量统计”中描述的三类分类情况，统计各个Pathway条目在蛋白质组与转录组中的富集显著性，结果分布如图6-2-1。结果文件中*html文件对每个富集的Pathway条目与Pathway数据库进行了链接，可通过链接查询该条目的详细信息。
			<p> <div class="tc"><img width=80% src="./material/volcano_Pathway.png" /></div>
			<p><b>图6-2-1 Pathway富集关联分析显著性分布图</b>
			<p>输出文件：
			<p><a href="./material/Pathway_all.txt" target="_blank">Function_enrichment_analysis_result/Pathway_all.txt</a>
			<p><a href="./material/volcano_Pathway.png" target="_blank">Function_enrichment_analysis_result/volcano_Pathway.png</a>
			<p><a href="./material/volcano_Pathway.pdf" target="_blank">Function_enrichment_analysis_result/volcano_Pathway.pdf</a>
			<br>
			<br>
		<h3><a name="6.2.2"></a>6.2.2 Pathway关联数量及富集因子分析</h3>
			<p>将两个组学的富集条目进行关联分析，得到两个组学层面上的富集情况,按照“Pathway富集关联数量统计”中描述的三类分类情况，统计各个Pathway条目在蛋白质组与转录组中关联数目与富集因子，其中Y轴为各个Pathway条目，并且统计了该条目所关联的蛋白数量，两列分别为转录组与蛋白质组，气泡大小代表富集数量，颜色代表富集因子，圆圈代表转录组（蛋白质组）p值大于等于0.05,钻石形代表转录组（蛋白质组）p值小于0.05,结果分布如图6-2-2。
			<p> <div class="tc"><img width=100% src="./material/bubble_Pathway.png" /></div>
			<p><b>图6-2-2 Pathway关联数量及富集因子分析四维气泡图</b>
			<p>输出文件：
			<p><a href="./material/Pathway.txt" target="_blank">Function_enrichment_analysis_result/Pathway.txt</a>
			<p><a href="./material/bubble_Pathway.png" target="_blank">Function_enrichment_analysis_result/bubble_Pathway.png</a>
			<p><a href="./material/bubble_Pathway.pdf" target="_blank">Function_enrichment_analysis_result/bubble_Pathway.pdf</a>
			<br>
			<br>

		<h2><a name="6.3"></a>6.3 差异蛋白与差异基因整合分析结果</h2>
			<p>对本次鉴定到的差异蛋白与测序得到的差异基因同时向KEGG数据库进行代谢通路分析，结果如图6-3。
			<p> <div class="tc"><img width=80% src="./images/map.DIFF.png" /></div>
			<p><b>图6-3 差异蛋白与差异基因Pathway代谢通路整合分析图</b>  蓝色框即为本次基因注释到的代谢通路靶点，红框为蛋白注释到的代谢通路靶点。将转录组和蛋白质组数据同时向代谢通路中进行注释，有利于形成基因表达在通路中的全景图。（上图为示意图，并非本次分析结果）
			<p>输出文件：
			<p><a href="./material/DEPs_DEGs_CorMap/DEPs_DEGs_CorMap.htm" target="_blank">Function_enrichment_analysis_result/DEPs_DEGs_CorMap/DEPs_DEGs.htm</a>
			<p><a href="./material/DEPs_DEGs_CorMap/DEPs_DEGs_CorMap.ko" target="_blank">Function_enrichment_analysis_result/DEPs_DEGs_CorMap/DEPs_DEGs.ko</a>
			<p><a href="./material/DEPs_DEGs_CorMap/DEPs_DEGs_CorMap.path" target="_blank">Function_enrichment_analysis_result/DEPs_DEGs_CorMap/DEPs_DEGs.path</a>
			<br>
			<br>

		<h1><a name="7"></a>7 多组学网络的关联分析</h1>
		<h2><a name="7.1"></a>7.1 蛋白互作网络分析概述</h2>
			<p>蛋白质 - 蛋白质相互作用（PPI）对细胞中的几乎每个过程都是必不可少的，因此理解PPI对于理解正常和疾病状态下的细胞生理学至关重要。蛋白互作网络分析有助于从系统的角度研究分子机制、发现新靶点等等。蛋白质 - 蛋白质相互作用是瞬态和稳定的交互，例如：蛋白质复合物（例如核糖体，血红蛋白）中形成稳定的相互作用。瞬时相互作用是修饰或携带蛋白质的短暂相互作用，导致进一步改变（例如蛋白酶激化，协助物质进入核孔）。它们构成了生物体中最具活力的部分。蛋白质互作网络是由单独蛋白通过彼此之间的相互作用构成，来参与生物信号传递、基因表达调节、能量和物质代谢及胞周期调控等生命过程的各个环节。系统分析大量蛋白在生物系统中的相互作用关系，对于了解生物系统中蛋白质的工作原理，了解疾病等特殊生理状态下生物信号和能量物质代谢的反应机制，以及了解蛋白之间的功能联系都有重要意义。
			<p>在科研中，蛋白质互作网络有着广泛的应用，例如：在蛋白质鉴定中，我们可以用蛋白互作网络来发现一些未知的蛋白质; 在信号通路中,我们可以通过蛋白互作网络添加细粒度;当我们想研究多分子复合物（例如蛋白酶体）时，同样可以运行互作网络找到蛋白质之间的表征关系。


            <p>在临床上，蛋白互作网络同样有着广泛的运用。新药的开发依赖于科学家理解疾病的生物学细节的能力，以及新分子药物可以用来治愈疾病或缓解症状的方式。一种非常重要的生物学机制是一种蛋白质识别并结合另一种蛋白质以调节其功能的方式。这种蛋白质 - 蛋白质相互作用的功能调节是活细胞中大多数生物活性的基础，但我们不了解蛋白质的哪些特性允许它与另一种蛋白质结合，我们也不了解如何设计分子来预防或增强这种相互作用。获得这样的理解将是一个巨大的进步。据估计，在每个人细胞中存在大约650,000种类型的特定蛋白质 - 蛋白质相互作用。这意味着可能有650,000个目标通过使用药物来改变生物功能。基本上生物过程的每个部分以及每种疾病，原则上都可以通过药物来解决。尽管想要做到这一点仍超出了目前的科技水平，但其中的某些蛋白质网络互作关系已经收录于String数据库中，供研究者使用。
            <p>随着科学技术的发展以及大规模PPI筛选技术的问世，特别是高通量亲和纯化结合质谱和酵母双杂交分析，已经引起PPI数据量的井喷式增长和更复杂，更完整的蛋白相互作用网络组的正在构建。
            <p> <div class="tc"><img width=60% src="./images/ppi.png" /></div>
            <p><b>图7-1 人类的401种蛋白质的
            高度可信的相互作用网络图。。来自于Cell, Vol. 122, 957–968, September 23, 2005, Copyright ?2005 by Elsevier Inc. DOI 10.1016/j.cell.2005.08.029. </b>  

        <h2><a name="7.2"></a>7.2 Pathway富集网络分析</h2>
        <p>本流程针对转录层面Pathway的p小于0.05或者蛋白层面Pathway的p小于0.05的通路进行分析，以Pathway level 1为中心，将鉴定到的差异蛋白与差异进行Pathway网络图构建。结果如图7-2。
        <p> <div class="tc"><img width=50% src="./material/Pathway_network.png" /></div>
        <p><b>图7-2 Pathway富集网络图</b>  图中为转录层面Pathway的p小于0.05或者蛋白层面Pathway的p小于0.05的所有通路的差异基因与差异蛋白。其中大球代表不同level 1的通路，不同颜色代表不同通路，小球代表关联上的基因，圆形代表没有关联上的基因，正方形代表没有关联上的蛋白。红色代表上调，蓝色代表下调。
        <p>输出文件：
			<p><a href="./material/network.glist" target="_blank">Interaction_network_association_analysis_result/network.glist</a>
			<p><a href="./material/network.path" target="_blank">Interaction_network_association_analysis_result/network.path</a>
			<p><a href="./material/network.path" target="_blank">Interaction_network_association_analysis_result/ppi_network_relation_cluster.xls</a>
			<p><a href="./material/network.path" target="_blank">Interaction_network_association_analysis_result/ppi_network_protein_filter.xls</a>
			<p><a href="./material/Pathway_network.png" target="_blank">Interaction_network_association_analysis_result/Pathway_network.png</a>
			<p><a href="./material/Pathway_network.pdf" target="_blank">Interaction_network_association_analysis_result/Pathway_network.pdf</a>
			<br>
			<br>
		<h2><a name="7.3"></a>7.3 差异蛋白互作网络图</h2>
        <p>针对上图中的所有差异蛋白，通过与STRING蛋白互作数据
        库比对，对差异表达蛋白进行互作分析绘制了网络互作图，结果如图7-3。
        <p> <div class="tc"><img width=50% src="./material/ppi_network.png" /></div>
        <p><b>图7-3 差异蛋白网络互作图</b>  图中显示了转录层面Pathway的p小于0.05或者蛋白层面Pathway的p小于0.05的所有通路的差异蛋白的网络互作关系。其中球的大小代表网络贡献度大小，线的粗细代表蛋白之间的关系强度，紫色的线代表蛋白之间的关系大于0.4，黑色的线代表蛋白之间的关系小于0.4，球代表在转录组关联上的蛋白，正方形代表在转录组没有关联上的蛋白，其中红色代表上调，蓝色代表下调。
        <p>输出文件：
			<p><a href="./material/network.glist" target="_blank">Interaction_network_association_analysis_result/network.glist</a>
			<p><a href="./material/ppi_network.relation.xls" target="_blank">Interaction_network_association_analysis_result/ppi_network_relation_cluster.xls</a>
			<p><a href="./material/ppi_network.relation.xls" target="_blank">Interaction_network_association_analysis_result/ppi_network_protein_filter.xls</a>
			<p><a href="./material/ppi_network.png" target="_blank">Interaction_network_association_analysis_result/ppi_network.png</a>
			<p><a href="./material/ppi_network.pdf" target="_blank">Interaction_network_association_analysis_result/ppi_network.pdf</a>
			<br>
			<br>

uL  
		<h1><a name="8"></a>8 转录因子的关联分析</h1>
		<h2><a name="8.1"></a>8.1 转录因子概述</h2>
			<p>转录因子(Tranion factor，TF)是一群能与基因5`端上游特定序列专一性结合，从而保证目的基因以特定的强度、时间、空间去表达的蛋白质分子。真核生物的RNA聚合酶不能直接识别启动子，需要转录因子。转录因子可以调控核糖核酸聚合酶（RNA聚合酶）与DNA模板的结合。转录因子一般有不同的功能区域，如DNA结合结构域与效应结构域。转录因子不单与基因上游的启动子区域结合，也可以和其它转录因子形成转录因子复合体来影响基因的转录。如图8-1-1<div class="tc"><img width=80% src="./images/TF.png" /></div>
			<p>图8-1-1 转录因子行使功能
			<p>根据转录因子的作用特点可分为二类；第一类转录因子为组织细胞特异性转录因子，这些TF是在特异的组织细胞或是受到一些类固醇激素生长因子或其它刺激后，开始表达某些特异蛋白质分子时，才需要的一类转录因子。第二类为普遍转录因子,它们与RNA聚合酶Ⅱ共同组成转录起始复合体时，转录才能在正确的位置开始。除TFⅡD以外，还发现TFⅡA，TFⅡB，TFⅡF，TFⅡE，TFⅡH等，它们在转录起始复合体组装的不同阶段起作用。如图8-1-2<div class="tc"><img src="./images/TF_type.png" /></div>
			<p>8-1-2 普遍转录因子和RNA聚合酶Ⅱ组成的转录起始复合体以及普遍转录因子常见分类
			<p>转录因子在动植物的生长发育及其对外界环境的反应中起着重要的调控作用，它已经成为现在生物学研究领域的热点。转录因子常见的分析方法如下：我们可通过表达量的差异分析，筛选出关注生物学问题过程中起主要调控作用的一些转录因子。然后我们可以通过转录因子的功能注释，得到相应转录因子的功能，或者，通过WGCNA分析发现基因表达模块，筛选关键转录因子在基因模块中是否为hub gene。另外，我们还可以预测转录因子的靶基因（MEME，http://meme-suite.org/tools/fimo），筛选出基因模块中的靶基因，建立以转录因子为hub gene的调控网络。 该流程只对转录因子表达量进行差异分析，你可以从中筛选出你更感兴趣的转录因子进行进一步分析
			<p>我们通过统计检验来验证蛋白质组与转录组检测到的转录因子是否与基因或者蛋白差异表达相关：
			<p> （1）当T（最小理论频数）>= 5, n>= 40 时，直接用Pearson 卡方检验； 
			<p>	（2）当n = 40 时，需要用连续性校正公式做卡方检验。这是因为卡方分布为连续型分布，而2*2列联表资料是分类资料，所以样本量较小时要进行连续性校正；
			<p>	（3）当T< 1 , 或者 n < 40, 或做卡方检验后所得的P值接近检验水准a 时，用Fisher's exact检验 。
			<p>	其中是否差异与组学之间的列联表为：<div  class="tc"><img width=50% src="./images/form.png" /></div>
			<p>	Fisher's exact检验计算公式为：<div  class="tc"><img width=50% src="./images/Fisher.png" /></div>
			<p>	Pearson卡方检验计算公式为：<div  class="tc"><img width=30% src="./images/Pearson.png" /></div>
		<h2><a name="8.2"></a>8.2 转录因子关联分析</h2>
		<h3><a name="8.2.1"></a>8.2.1 各组学转录因子鉴定个数</h3>
			<p>蛋白质与转录组中鉴定到的转录因子个数，结果如图8-3
			<p> <div class="tc"><img width=50% src="./material/TF_venn.png" /></div>
			<p><b>图8-3 各组学转录因子鉴定个数</b>
		<p>输出文件：
			<p><a href="./material/TF_protein_filter_result.txt" target="_blank">Transcription_factor_correlation_analysis_result/TF_protein_result.txt</a>
			<p><a href="./material/TF_transcription_filter_result.txt" target="_blank">Transcription_factor_correlation_analysis_result/TF_trasncription_result.txt</a>
			<p><a href="./material/TF_venn.png" target="_blank">Transcription_factor_correlation_analysis_result/TF_venn.png</a>
			<p><a href="./material/TF_venn.pdf" target="_blank">Transcription_factor_correlation_analysis_result/TF_venn.pdf</a>
			<br>
			<br>
		<h3><a name="8.2.2"></a>8.2.2 各组学差异表达的转录因子鉴定个数</h3>
			<p>鉴定到的差异蛋白与差异基因中的转录因子的个数，结果如图8-2-2
			<p> <div class="tc"><img width=50% src="./material/TF_DEG_DEP_venn.png" /></div>
			<p><b>图8-2-2 各组学差异表达的转录因子鉴定个数</b> 
		<p>输出文件：
			<p><a href="./material/TF_protein_filter_result.txt" target="_blank">Transcription_factor_correlation_analysis_result/TF_protein_filter_result.txt</a>
			<p><a href="./material/TF_transcription_filter_result.txt" target="_blank">Transcription_factor_correlation_analysis_result/TF_trasncription_filter_result.txt</a>
			<p><a href="./material/TF_DEG_DEP_venn.png" target="_blank">Transcription_factor_correlation_analysis_result/TF_DEG_DEP_venn.png</a>
			<p><a href="./material/TF_DEG_DEP_venn.pdf" target="_blank">Transcription_factor_correlation_analysis_result/TF_DEG_DEP_venn.pdf</a>
			<br>
			<br>  
		<h2><a name="8.3"></a>8.3 转录因子超家族分类</h2>
			<p>在两个组学层面上，差异基因中鉴定到的各个TF超家族的转录因子个数，结果如图8-3
			<p> <div class="tc"><img width=80% src="./material/TF_colorful.png" /></div>
			<p><b>图8-3 各个TF超家族转录因子鉴定到的个数</b> 
		<p>输出文件：
			<p><a href="./material/TF_protein_result.txt" target="_blank">Transcription_factor_correlation_analysis_result/TF_protein_filter_result.txt</a>
			<p><a href="./material/TF_transcription_result.txt" target="_blank">Transcription_factor_correlation_analysis_result/TF_trasncription_filter_result.txt</a>
			<p><a href="./material/TF_colorful.png" target="_blank">Transcription_factor_correlation_analysis_result/TF_colorful.png</a>
			<p><a href="./material/TF_colorful.pdf" target="_blank">Transcription_factor_correlation_analysis_result/TF_colorful.pdf</a>
			<br>
			<br>
		<h2><a name="8.4"></a>8.4 转录因子各组学表达量差异分析</h2>
			<p>在鉴定到的转录因子中，转录组学与蛋白质组学的表达量差异分布，结果如图8-4
			<p> <div class="tc"><img width=80% src="./material/TF_violinplot.png" /></div>
			<p><b>图8-4 转录因子表达量小提琴图</b> 
		<p>输出文件：
			<p><a href="./material/TF_violin_correlation.csv" target="_blank">Transcription_factor_correlation_analysis_result/TF_violin_correlation.csv</a>
			<p><a href="./material/TF_violinplot.png" target="_blank">Transcription_factor_correlation_analysis_result/TF_violinplot.png</a>
			<p><a href="./material/TF_violinplot.pdf" target="_blank">Transcription_factor_correlation_analysis_result/TF_violinplot.pdf</a>
			<br>
			<br>
		<h2><a name="8.5"></a>8.5 关联数量统计</h2>
			<p>利用统计检验看蛋白质组与转录组检测到的转录因子是否与基因或者蛋白差异表达相关
			<center><b>表8-5 在差异与非差异情况下，蛋白质组与转录组检测到转录因子的个数</b></center>
				<div>
					<table>
u1  
</table>	
			<br>
			<br>
		<h1><a name="9"></a>9 参考文献</h1>
		<h2><a name="9.1"></a>9.1 参考文献</h2>
			<p>[1]Ritchie MD , et al.Methods of integrating data to uncover genotype–phenotype interactions. Nat Rev Genet. 2015 Feb;16(2):85-97.
			<p>[2]Schwanh?usser B , et al. Global quantification of mammalian gene expression control. Nature.2013 Mar 7;495(7439):126-7.
			<p>[3]Vogel C, Marcotte EM. Insights into the regulation of protein abundance from proteomic and transcriptomic analyses . Nat Rev Genet. 2012 Mar13;13(4):227-32 .
			<p>[4]Maier T, Güell M, Serrano L. Correlation of mRNA and protein in complex biological samples FEBS Letters 583 (2009) 3966–3973.
			<p>[5]Mary Muers.Transcriptome to proteome and back to genome. Nature Reviews Genetics ,2011.
			<p>[6]Bouchal P., et al.Combined proteomics and transcriptomics identifies carboxypeptidase B1 and NF-κB associated proteins as putative biomarkers of metastasis in low grade breast cancer. Mol Cell Proteomics. 2015 Apr 22.
			<p>[7]Petersen HO, H?ger SK, Looso M，et al. A Comprehensive Transcriptomic and Proteomic Analysis of Hydra Head Regeneration. Mol Biol Evol. 2015 .
			<p>[8]Wang J, Mei H, Zheng C, et al. The metabolic regulation of sporulation and parasporal crystal formation in Bacillus thuringiensis revealed by transcriptomics and proteomics. Mol Cell Proteomics. 2013 May;12(5):1363-76.
			<p>[9]B. FUTCHER, et al.A Sampling of the Yeast Proteome MOLECULAR AND CELLULAR BIOLOGY,Nov. 1999, 7357–7368.
			<p>[10]吴松峰，朱云平，贺福初. 转录组与蛋白质组比较研究进展.生物化学与生物物理进展.2005,3（2）.
			<p>[11]Lan P, Li W, Schmidt W. Complementary proteome and transcriptome profiling in phosphate-deficient Arabidopsis roots reveals multiple levels of gene regulation. Molecular & Cellular Proteomics. 2012 Nov;11(11):1156-66.
			<p>[12]Dyhrman ST, Jenkins BD, Rynearson TA, Saito MA, Mercier ML, et al. The Transcriptome and Proteome of the Diatom Thalassiosira pseudonana Reveal a Diverse Phosphorus Stress Response. PLoS ONE 7(3),2012.
			<p>[13]Lackner DH, Schmidt MW, Wu S, Wolf DA, B?hler J. Regulation of transcriptome, translation, and proteome in response to environmental stress in fission yeast. Genome Biology. 2012,13:R25.
			<p>[14]Gonzalez, LMG,et al.Integrated transcriptomic and proteomic profiling of white spruce stems during the transition from active growth to dormancy .Plant Cell Environ. 2012 Apr;35(4):682-701.
			<p>[15]Kuss C , Gan CS , Gunalan K , Bozdech Z , Sze SK , Preiser PR. Quantitative proteomics reveals new insights into erythrocyte invasion by Plasmodium falciparum .Mol Cell Proteomics. 2012 ,11(2).
			<p>[16]Kocharunchitt C, King T, Gobius K, Bowman JP, Ross T. Integrated Transcriptomic and proteomic Analysis of the Physiological Response of Escherichia coli O157:H7 Sakai to steady-state conditions of cold and water activity stress. Molecular & Cellular Proteomics. 2012 .
			<p>[17]陈润生.关于非编码RNA 研究的一些思考.生命科学.第22卷第7期.2010.7(594-597).
			<p>[18]曹文君等.基因表达谱富集分析方法研究进展.生物技术通讯.2008.
			<p>[19]Croken et al.Gene Set Enrichment Analysis (GSEA) of Toxoplasma gondii expression datasets links cell cycle progression and the bradyzoite developmental program. BMC Genomics .2014, 15:515.
			<p>[20]Wang SH, You ZY, Ye LP, et al. Quantitative proteomic and transcriptomic analyses of molecular mechanisms associated with low silk production in silkworm Bombyx mori. J Proteome Res. 2014 Feb 7;13(2):735-51.
			<p>[21]Chen Q, Guo W, Feng L, et al.Transcriptome and proteome analysis of Eucalyptus infected with Calonectria pseudoreteaudii. J Proteomics. 2015 Feb 6;115:117-31.
			<p>[22]Trevisan S, Manoli A, Ravazzolo L, et al.Nitrate sensing by the maize root apex transition zone: a merged transcriptomic and proteomic survey. J Exp Bot. 2015 Apr 23. pii: erv165.
			<p>[23]Ghazalpour A, Bennett B, Petyuk VA, Orozco L, Hagopian R, Mungrue IN, et al. Comparative Analysis of Proteome and Transcriptome Variation in Mouse.PLoS Genet 7(6).2011.
	</div>
</body>
<html>
u  
		<h1><a name="8"></a>8 参考文献</h1>
		<h2><a name="8.1"></a>8.1 参考文献</h2>
			<p>[1]Ritchie MD , et al.Methods of integrating data to uncover genotype–phenotype interactions. Nat Rev Genet. 2015 Feb;16(2):85-97.
			<p>[2]Schwanh?usser B , et al. Global quantification of mammalian gene expression control. Nature.2013 Mar 7;495(7439):126-7.
			<p>[3]Vogel C, Marcotte EM. Insights into the regulation of protein abundance from proteomic and transcriptomic analyses . Nat Rev Genet. 2012 Mar13;13(4):227-32 .
			<p>[4]Maier T, Güell M, Serrano L. Correlation of mRNA and protein in complex biological samples FEBS Letters 583 (2009) 3966–3973.
			<p>[5]Mary Muers.Transcriptome to proteome and back to genome. Nature Reviews Genetics ,2011.
			<p>[6]Bouchal P., et al.Combined proteomics and transcriptomics identifies carboxypeptidase B1 and NF-κB associated proteins as putative biomarkers of metastasis in low grade breast cancer. Mol Cell Proteomics. 2015 Apr 22.
			<p>[7]Petersen HO, H?ger SK, Looso M，et al. A Comprehensive Transcriptomic and Proteomic Analysis of Hydra Head Regeneration. Mol Biol Evol. 2015 .
			<p>[8]Wang J, Mei H, Zheng C, et al. The metabolic regulation of sporulation and parasporal crystal formation in Bacillus thuringiensis revealed by transcriptomics and proteomics. Mol Cell Proteomics. 2013 May;12(5):1363-76.
			<p>[9]B. FUTCHER, et al.A Sampling of the Yeast Proteome MOLECULAR AND CELLULAR BIOLOGY,Nov. 1999, 7357–7368.
			<p>[10]吴松峰，朱云平，贺福初. 转录组与蛋白质组比较研究进展.生物化学与生物物理进展.2005,3（2）.
			<p>[11]Lan P, Li W, Schmidt W. Complementary proteome and transcriptome profiling in phosphate-deficient Arabidopsis roots reveals multiple levels of gene regulation. Molecular & Cellular Proteomics. 2012 Nov;11(11):1156-66.
			<p>[12]Dyhrman ST, Jenkins BD, Rynearson TA, Saito MA, Mercier ML, et al. The Transcriptome and Proteome of the Diatom Thalassiosira pseudonana Reveal a Diverse Phosphorus Stress Response. PLoS ONE 7(3),2012.
			<p>[13]Lackner DH, Schmidt MW, Wu S, Wolf DA, B?hler J. Regulation of transcriptome, translation, and proteome in response to environmental stress in fission yeast. Genome Biology. 2012,13:R25.
			<p>[14]Gonzalez, LMG,et al.Integrated transcriptomic and proteomic profiling of white spruce stems during the transition from active growth to dormancy .Plant Cell Environ. 2012 Apr;35(4):682-701.
			<p>[15]Kuss C , Gan CS , Gunalan K , Bozdech Z , Sze SK , Preiser PR. Quantitative proteomics reveals new insights into erythrocyte invasion by Plasmodium falciparum .Mol Cell Proteomics. 2012 ,11(2).
			<p>[16]Kocharunchitt C, King T, Gobius K, Bowman JP, Ross T. Integrated Transcriptomic and proteomic Analysis of the Physiological Response of Escherichia coli O157:H7 Sakai to steady-state conditions of cold and water activity stress. Molecular & Cellular Proteomics. 2012 .
			<p>[17]陈润生.关于非编码RNA 研究的一些思考.生命科学.第22卷第7期.2010.7(594-597).
			<p>[18]曹文君等.基因表达谱富集分析方法研究进展.生物技术通讯.2008.
			<p>[19]Croken et al.Gene Set Enrichment Analysis (GSEA) of Toxoplasma gondii expression datasets links cell cycle progression and the bradyzoite developmental program. BMC Genomics .2014, 15:515.
			<p>[20]Wang SH, You ZY, Ye LP, et al. Quantitative proteomic and transcriptomic analyses of molecular mechanisms associated with low silk production in silkworm Bombyx mori. J Proteome Res. 2014 Feb 7;13(2):735-51.
			<p>[21]Chen Q, Guo W, Feng L, et al.Transcriptome and proteome analysis of Eucalyptus infected with Calonectria pseudoreteaudii. J Proteomics. 2015 Feb 6;115:117-31.
			<p>[22]Trevisan S, Manoli A, Ravazzolo L, et al.Nitrate sensing by the maize root apex transition zone: a merged transcriptomic and proteomic survey. J Exp Bot. 2015 Apr 23. pii: erv165.
			<p>[23]Ghazalpour A, Bennett B, Petyuk VA, Orozco L, Hagopian R, Mungrue IN, et al. Comparative Analysis of Proteome and Transcriptome Variation in Mouse.PLoS Genet 7(6).2011.
	</div>
</body>
<html>
c             C   sP   t j| �j\}}| jdd�}tj|t||f�d�}|j| dd||� |j�  d S )N�pngZpdf)Zpagesizer   )	r   �open�size�replacer   ZCanvasr   Z	drawImageZsave)�fileZmaxwZmaxh�name�c� r   �X/ldfssz1/SP_MSI/Pipeline/Pipeline/TP_Cor/src/Submit_analysis_files_and_pdf_generation.py�imgtopdf�  s
    r   c             C   s�  d|  }t d| d���x}d}x�|j� D ]t}|j� }|jd�}|dkrP|d7 }q(|dkrz|d7 }|d }|d }|d }q(|dkr(|d }	|d }
|d }q(q(W d	| ||||	|
|f }t d
|  d���}d}x�|j� D ]�}|j� }|jd�}|dkr�|d7 }q�|dk�r |d7 }|d }|d }q�|dk�rD|d7 }|d }|d }q�|dkr�|d }|d }|d }q�q�W W d Q R X d| |||||||f }W d Q R X ||fS )Nz ./Data_Analysis/%s/Quantitative/z%spdf_1.txtr   r   �	�   �   �   a  
        <tr><th>%s</th><th>Number of Proteins</th><th>Number of Genes</th><th>Number of Correlations</th></tr>
						<tr><td>Quantitative</td><td>%s</td><td>%s</td><td>%s</td></tr>
						<tr><td>Differentially expressed</td><td>%s</td><td>%s</td><td>%s</td></tr>
        z./Data_Analysis/%s/TF/pdf_2.txtz�
        <tr><td>%s</td><th>Number of Proteins</th><th>Number of Genes</th></tr>
						<tr><th>difference</th><td>%s</td><td>%s</td></tr>
						<tr><th>No differnce</th><td>%s</td><td>%s</tr>
						<tr><th>%s</th><td>%s</td><td>%s</td></tr>

        )r   �	readlines�strip�split)�index�rootZfh�n�lineZarrayZprotein_allZtranscription_allZcorrelation_allZprotein_diffZtranscription_diffZcorrelation_diff�excel1ZTF__protein_diffZTF_transcription_diffZTF_protein_nodiffZTF_transcription_nodiff�method�pZdescription�excel2r   r   r   �
html_excel�  s`    



r    �__main__� �yesz2rm *.sh.* *.nhr *.nin *.nsq formatdb.log error.logz./ZshZrunZdealzrm %sz./Data_Analysis/%s/Quantitativezrm  *.shz./Data_Analysis/%s/TFzrm  *.sh *.sh.*z./Data_Analysis/%s/Networkzrm  -r *.shz./Data_Analysis/%s/Functionzrm -r KEGG* foot*zrm *.pdfz ./Data_Analysis/%s/Quantitative/z.png�mapz./Data_Analysis/%s/Function/z./Data_Analysis/%s/TF/z./Data_Analysis/%s/Network/Zppi_network_filesZPathway_network_filesz./submit/pdf/content.html�w�nozfc-list :lang=zh�/�   zexport LANG = en_US.UTF-8zmkdir -p /home/%s/.fontsz+cp %s/lib/wqy-microhei.ttc /home/%s/.fonts/z /home/%s/.fonts/wqy-microhei.ttczfc-cache -fv)B�osZtimeZjsonZreportlab.lib.pagesizesr   Zreportlab.pdfgenr   ZPILr   r   Zmyfile�load�result�groupZprotein_foldZ	gene_foldZ	protein_pZgene_pZblast_evalueZcor_rootZtf�clearr   Zarray_groupZ
section1_1Z
section1_2Z
section1_3Zsection1Zsection2Zsection3Zsection4Zsection5r   r    �__name__�getcwdr   Z
excel1_allZ
excel2_allr   �lower�popen�walk�parentZdirnames�	filenamesr   �chdirZroot1r   Zroot2Zroot3Zroot4r   r   ZweZhtml�writeZprocess�read�output�close�user�path�exists�systemr   r   r   r   �<module>   s�   


( mA!>































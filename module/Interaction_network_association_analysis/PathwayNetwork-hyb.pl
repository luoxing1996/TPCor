
use strict;
use Getopt::Long;
use FindBin '$Bin';

my($path,$list,$genecol,$UpDowncol,$symbol,$outdir,$help,$network,$convert);
GetOptions(
	"pathway:s" => \$path,
	"list:s" => \$list,
	"genecol:i" => \$genecol,
	"UpDowncol:i" => \$UpDowncol,
	"symbol:s" => \$symbol,
	"outdir:s" => \$outdir,
	"help|?" => \$help,
);

&usage if(!$path || !$list || $help);
$genecol ||= 1; $UpDowncol ||= 3;
print "Network profile is on the way......\n";

$outdir ||= "."; `mkdir -p $outdir`;
$network ||= "$Bin/network.py";
$convert ||= "convert";
my %shape;
#根据GO关系和GO结果转换成Network输入列表
my %diff;
open LIST,"$list" or die $!;

while(<LIST>){
	chomp();
	my @a=split;
	$shape{$a[0]}='square' if($a[2] eq 'uniq_protein');
	$shape{$a[0]}='sphere' if($a[2] eq 'correlation');
	$shape{$a[0]}='circle' if($a[2] eq 'uniq_transcription');
	$diff{$a[$genecol-1]}=$a[$UpDowncol-1];
	$diff{$a[$genecol-1]}=$a[$UpDowncol-1];
	
} 
close LIST;

my %symb;
if($symbol && -f $symbol){
	open SY,"$symbol";
	while(<SY>){
		chomp();
		my @a=split;
		$symb{$a[0]}="$a[0]:$a[1]"; #geneID:symbol的格式展示
#		$symb{$a[0]}=$a[1];	#只展示symbol 有重复的symbol导致无法画
	}
}

#######边属性
my($from,$to,$color,$width,$lty,$arrowsize,$arrowwidth,$arrowmode,$label,$labelfont,$labelcex,$labelcolor,%color);
#$color="#696969";	#边颜色
$color="#FF4500";	#边颜色
$width=0.02;	#宽度
$lty="solid";	#线条类型
$arrowsize=0.1;	
$arrowwidth=0.5;
$arrowmode=0;	#箭头类型,[0]没有箭头,[1]<,<-[2]>,->[3]<>,<->
$labelfont=3;
$labelcex=0.15;
$labelcolor="black";

# 紫 #B822DD  橙 #FF4500  亮绿 #90EE90  绿 #4DAF4A #53B603  粉红 #FF1493  红 #E41A1C 浅蓝 7B68EE
#######点属性
my($pathsize,$genesize,$pathshape,$geneshape,$pathcolor,$genecolor,$pathframecolor,$geneframecolor,$pathlabelfont,$genelabelfont,$pathlabelcex,$genelabelcex,$pathlabelcolor,$genelabelcolor,%pathcolor,%pathlabelcex);
my $n=0;
$pathsize=16;			$genesize=5;
$pathshape="sphere";		$geneshape="sphere";	#circle 圆  sphere 球 rectangle 长方形
$pathcolor="#B822DD";		$genecolor="";		#gene颜色在后面判断设置
$pathframecolor="ivory";	$geneframecolor="NA";#顶点的外圈颜色,默认[black]-->NA
$pathlabelfont=2;		$genelabelfont=1;	#1纯文本 2加粗 3斜体 4加粗斜体 5指定符号字体
$pathlabelcex=0.45;		$genelabelcex=0.1;
$pathlabelcolor="black";	$genelabelcolor="black";

my $name=`basename $path`;
$name=~s/.path.xls//;
chomp($name);
my %significant;
my %gene;
open EDGE,">$outdir/Pathway_network.edges.xls";
print EDGE "from\tto\tcolor\twidth\tlty\n";
open IN,"$path";<IN>;

while(<IN>){
	chomp();
	$n++;
	my @a=split /\t/,$_;
	if($n < 11){
		
		$color{$a[0]}='#B822DD';
		$pathcolor{$a[0]}='#90EE90' if($a[3] eq 'Cellular Processes');
		$pathcolor{$a[0]}='#FF1493' if($a[3] eq 'Environmental Information Processing');
		$pathcolor{$a[0]}='#4DAF4A' if($a[3] eq 'Genetic Information Processing');
		$pathcolor{$a[0]}='#984EA3' if($a[3] eq 'Human Diseases');
		$pathcolor{$a[0]}='#FF7F00' if($a[3] eq 'Metabolism');
		$pathcolor{$a[0]}='#FFE528' if($a[3] eq 'Organismal Systems');
		$pathcolor{$a[0]}='#A65628' if($a[3] eq 'Drug Development');
		$significant{$a[0]}=$pathsize; #pathway节点大小
		$pathsize=$pathsize*0.9;
		$pathlabelcex{$a[0]}=$pathlabelcex;
		$pathlabelcex=$pathlabelcex*0.95;
		my @gene=split /\;/,$a[4];

		$from = $a[0];
		foreach my $to(@gene){
			if($symbol && -f $symbol && exists $symb{$to}){
				print EDGE "$from\t$symb{$to}\t$color{$from}\t$width\t$lty\n";
			}else{
				print EDGE "$from\t$to\t$color{$from}\t$width\t$lty\n";
			}
			if($diff{$to}){
				if($diff{$to}=~/Up/i){ ; #gene 颜色(上下调)
				#	$gene{$to}="#E41A1C";
					$gene{$to}="#FF0000";
				#	$gene{$to}="#FF1493";
				}elsif($diff{$to}=~/Down/i){
				#	$gene{$to}="#90EE90";
					$gene{$to}="#1E90FF";
				}
			}else{	$gene{$to}="#D1D1D1"; }
		}
	}
}


$genesize=300/(keys %gene);
$genelabelcex=20/(keys %gene);
$genesize=($genesize >10)?10:$genesize;
$genelabelcex=($genelabelcex >0.67)?0.67:$genelabelcex;

open NODE,">$outdir/Pathway_network.nodes.xls";
print NODE "name\tsize\tshape\tcolor\tframe.color\tlabel.font\tlabel.cex\tlabel.color\n";
foreach my $pathway(keys %significant){
	print NODE "$pathway\t$significant{$pathway}\t$pathshape\t$pathcolor{$pathway}\t$pathframecolor\t$pathlabelfont\t$pathlabelcex{$pathway}\t$pathlabelcolor\n";
}
foreach my $gene(keys %gene){
	if($symbol && -f $symbol && exists $symb{$gene}){
		
		print NODE "$symb{$gene}\t$genesize\t$shape{$gene}\t$gene{$gene}\t$geneframecolor\t$genelabelfont\t$genelabelcex\t$genelabelcolor\n";
	}else{

		print NODE "$gene\t$genesize\t$shape{$gene}\t$gene{$gene}\t$geneframecolor\t$genelabelfont\t$genelabelcex\t$genelabelcolor\n";
	}
}
close NODE;

sub usage {
        print  << "USAGE";
Description: Create Pathway-NetWork
Author: licong\@genomics.cn
Release Date: 2017.5.15
Usage: perl $0  [options]
Options:
        -pathway	<path>*         pathway result
        -list		<path>*         gene list with Up or Down infomation
		-genecol			gene id col [1]
		-UpDowncol			UpDown col [3]
		-symbol		<path>		gene2symbol file
        -outdir		<path>          output dir, default current (should be absolute path)
        -help|?:	                print help information

e.g1.:
perl $0 -pathway /ifs4/BC_PUB/biosoft/pipeline/RNA/RNA_RNAref/RNA_RNAref_2016a/example/result/Transcriptome_Resequencing_Report/BGI_result/4.Quantify/DifferentiallyExpressedGene/KeggPathwayEnrichment/HBRR1-VS-UHRR1.PossionDis_Method.path -list /ifs4/BC_PUB/biosoft/pipeline/RNA/RNA_RNAref/RNA_RNAref_2016a/example/result/process/Pathway_Hypergeometric/tmp_file/HBRR1-VS-UHRR1.PossionDis_Method.glist.temp  -outdir \$PWD/result

e,g2.:
perl $0 -pathway /ifs4/BC_PUB/biosoft/pipeline/RNA/RNA_RNAref/RNA_RNAref_2016a/example/result/Transcriptome_Resequencing_Report/BGI_result/4.Quantify/DifferentiallyExpressedGene/KeggPathwayEnrichment/HBRR1-VS-UHRR1.PossionDis_Method.path -list /ifs4/BC_PUB/biosoft/pipeline/RNA/RNA_RNAref/RNA_RNAref_2016a/example/result/process/Pathway_Hypergeometric/tmp_file/HBRR1-VS-UHRR1.PossionDis_Method.glist.temp  -outdir \$PWD/result -symbol /ifs4/BC_PUB/biosoft/pipeline/RNA/RNA_RNAref/RNA_RNAref_version5.0_beta/Database/hg19/human.gene2symbol.txt
USAGE
        exit 0;
}

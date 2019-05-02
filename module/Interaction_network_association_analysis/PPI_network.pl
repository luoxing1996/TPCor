#!/usr/bin/perl -w
use strict;
use Getopt::Long;
use FindBin '$Bin';

my($relation,$codefile,$outdir,$help,$network,$convert,$path);
GetOptions(
	"list:s" => \$relation,
	"path:s" => \$path,
	"code:s" => \$codefile,
	"outdir:s" => \$outdir,
	"help|?" => \$help,
);

&usage if(!$relation || !$codefile || $help);
$outdir ||= "."; `mkdir -p $outdir`;
$network ||= "$Bin/network.py";
$convert ||= "convert";

	

#根据GO关系和GO结果转换成Network输入列表
#######边属性
my($from,$to,$color,$width,$lty,$arrowsize,$arrowwidth,$arrowmode,$label,$labelfont,$labelcex,$labelcolor,%color);
#$color="#696969";	#边颜色
$color="black";	#边颜色
$width=0.5;	#宽度
$lty="solid";	#线条类型
$arrowsize=0.1;	
$arrowwidth=0.5;
$arrowmode=0;	#箭头类型,[0]没有箭头,[1]<,<-[2]>,->[3]<>,<->
$labelfont=1;
$labelcex=0.15;
$labelcolor="black";

# 紫 #B822DD  橙 #FF4500  亮绿 #90EE90  绿 #4DAF4A #53B603  粉红 #FF1493  红 #E41A1C 浅蓝 7B68EE
#######点属性
=a
my($pathsize,$genesize,$pathshape,$geneshape,$pathcolor,$genecolor,$pathframecolor,$geneframecolor,$pathlabelfont,$genelabelfont,$pathlabelcex,$genelabelcex,$pathlabelcolor,$genelabelcolor,%pathcolor,%pathlabelcex);
my $n=0;
$pathsize=16;			$genesize=5;
$pathshape="sphere";		$geneshape="sphere";	#circle 圆  sphere 球 rectangle 长方形
$pathcolor="#B822DD";		$genecolor="";		#gene颜色在后面判断设置
$pathframecolor="ivory";	$geneframecolor="NA";#顶点的外圈颜色,默认[black]-->NA
$pathlabelfont=1;		$genelabelfont=1;	#1纯文本 2加粗 3斜体 4加粗斜体 5指定符号字体
$pathlabelcex=0.45;		$genelabelcex=0.1;
$pathlabelcolor="black";	$genelabelcolor="black";
=cut
my %width;
my %line_color;
my $bestscore;
open IN,"$relation" or die "$!\n";
while (<IN>) {
	chomp;

	my @line= split("\t",$_);

	if ($.==1) {
	}
	elsif ($.==2) {
		$bestscore=$line[4];
		if ($line[4]>700){
                $line_color{$line[0]}{$line[1]}="#B822DD";

                }else {
                $line_color{$line[0]}{$line[1]}="black";

}
	} else {
	if ($line[4]>400){
		$width{$line[0]}{$line[1]}= ($line[4]/$bestscore)*$width*0.5;
		if ($line[4]>700){
                $line_color{$line[0]}{$line[1]}="#B822DD";
  
                }else {
                $line_color{$line[0]}{$line[1]}="black";
}
	}
}
}
my $name=`basename $relation`;
$name=~s/ppi_network_relation.xls.*//;
chomp($name);
my %significant;
my %gene;
open EDGE,">$path/ppi_network_edges.xls";
print EDGE "from\tto\tcolor\twidth\tlty\n";
open IN,"$relation" or die "$!\n";
while(<IN>){
	chomp();
	my @a= split("\t",$_);

	if ($a[4] eq "score") {

	}
	else{

	if ($a[4]>400){
	if (exists $line_color{$a[0]}{$a[1]}){
	print EDGE "$a[0]\t$a[1]\t$line_color{$a[0]}{$a[1]}\t$width{$a[0]}{$a[1]}\t$lty\n";
	}
	else{

	}
}
}
}
close IN;
open NODE,">$path/ppi_network_nodes.xls";
print NODE "name\tsize\tshape\tcolor\tframe.color\tlabel.font\tlabel.cex\tlabel.color\n";
open IN2,"$codefile";
while(<IN2>){
	chomp();
	my @a=split /\t/,$_;
	my $size=log($a[1])/log(10)*2.8+2;
	my $color=($a[2] eq "Up")?'#E41A1C':'#377EB8';
	if ("uniq_protein" eq $a[3]){
	print NODE "$a[0]\t$size\tsquare\t$color\tivory\t1\t0.2\tblack\n";
	}
        elsif ("correlation" eq $a[3]){
		print NODE "$a[0]\t$size\tsphere\t$color\tivory\t1\t0.2\tblack\n";
}
	elsif ("uniq_transcription" eq $a[3]){
		print NODE "$a[0]\t$size\tcircle\t$color\tivory\t1\t0.2\tblack\n";
}



}
close NODE;


sub usage {
	print "perl $0 -list /ifshk7/BC_RD/PROJECT/P17Z12200N0121/RNAseq2017a/New_HK/RNAseq/result.SE2/process/PPI_Interaction/HBRR1-VS-UHRR1.DEGseq_Method.network.relation.xls.100 -code /ifshk7/BC_RD/PROJECT/P17Z12200N0121/RNAseq2017a/New_HK/RNAseq/result.SE2/process/PPI_Interaction/HBRR1-VS-UHRR1.DEGseq_Method.network.relation.xls.100.fd -outdir /ifshk7/BC_RD/PROJECT/P17Z12200N0121/RNAseq2017a/New_HK/RNAseq/result.SE2/process/PPI_Interaction";
        exit 0;
}

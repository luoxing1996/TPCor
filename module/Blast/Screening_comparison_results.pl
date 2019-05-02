#!/usr/bin/perl
#===============================================================================
#
#         FILE:  sort_u.pl
#
#        USAGE:  perl sort_u.pl inputfile outputfile
#
#  DESCRIPTION:  当ID相同时候，取对应的evalue更小的那一列
#
#      OPTIONS:  
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:  heyanbin
#      COMPANY:
#      VERSION:  1.0
#      CREATED:  31/05/2016 09:15 PM
#     REVISION:  ---
#===============================================================================
#usege: perl sort_u.pl inputfile outputfile

#use strict;
use warnings;
my $in=shift;
my $out=shift;
open IN, "<","$in" or die "$!\n";
open OUT,">", "$out";
my %map;
while(<IN>){
	chomp;
	my @F=split (/\t/,$_);
	my $id=$F[0];
	my $score=$F[11];
	if(exists $map{$F[0]}){
		my @tem=@{$map{$F[0]}};#数组解引用 
		if($tem[10] > $score){
			$map{$F[0]}=\@F;
			}
		else{
			next;
			}
		}
	else{
		$map{$F[0]}=\@F; #数组引用
		}
}
close IN;
foreach  my $id (keys %map){
	my @tmp=@{$map{$id}};
	foreach (@tmp){
		print OUT "$_\t";
		}
	print OUT "\n";
}

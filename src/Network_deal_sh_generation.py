3
$v\~  �               @   s  d dl Z d dlZd dlZedk�redd�Ze je�Zed d Zed d Z	ed d Z
ed	 d
 Zed	 d Zdeef Ze	jd�Z�xveD �]lZej� Zde Zdee
eeee
eee
eeef Zde
eeeef Zde
eeeee
eeeee
eee
eeef Zede d�Zede d���Zd Zx�ej� D ]vZej� Zejd�Zed k�rdeje� ed7 Z�q.ej dded  �ed < e!e�dk�r.ejded  ed f � �q.W W dQ R X ej"�  ede d�Z#e#jee � e#j"�  ede d�Z#e#je� e#j"�  q�W dS )�    N�__main__zcorrelation_config.json�rZBasis_InformationZperl_HOME_PATHZComparison_Groupz(Correlation analysis process server pathZNetworkZroot_databaseZString_Species_typez%s/uniq.protein.links.txt.%s�,z./Data_Analysis/%s/Network/a  
%sperl %smodule/Interaction_network_association_analysis/PathwayNetwork-hyb.pl -pathway=%snetwork.path -list=%snetwork.glist -genecol=1 -UpDowncol=2 -outdir=%s
/share/app/python-2.7.10/bin/python %smodule/Interaction_network_association_analysis/network.py --nodes %sPathway_network.nodes.xls --edges %sPathway_network.edges.xls --config %smodule/Interaction_network_association_analysis/Pathwaynetwork.conf --output_prefix %sPathway_network
convert -density 300 -resize 30%% %sPathway_network.pdf %sPathway_network.png
        z�
/share/app/python-2.7.10/bin/python %smodule/Interaction_network_association_analysis/PPI_relation.py --m6 ./all_diff_ppi.blast.out --protein_list %sall.glist --diff_list %snetwork.glist  --db %s   --result %sppi_network_relation.xls

        a�  
        /share/app/python-2.7.10/bin/python %smodule/Interaction_network_association_analysis/PPI_fd_relation.py %sppi_network_relation_filter.xls %snetwork.glist %sppi_network_relation.xls.fd
        %sperl %smodule/Interaction_network_association_analysis/PPI_network.pl -list %sppi_network_relation_filter.xls -code %sppi_network_relation.xls.fd -path %s -outdir %sPPI_network
        /share/app/python-2.7.10/bin/python %smodule/Interaction_network_association_analysis/network.py --nodes %sppi_network_nodes.xls --edges %sppi_network_edges.xls --config %smodule/Interaction_network_association_analysis/Pathwaynetwork.conf --output_prefix %sppi_network
        convert -density 300 -resize 30%% %sppi_network.pdf %sppi_network.png  

                z%sall.glist�wz+./Data_Analysis/%s/Function/glist/all.glist�	�   z\(.*\)� �   z%s	%s
z%s_network.shz%s_network_filter.sh)$Zjson�os�re�__name__�openZmyfile�load�resultZperl�group�homeZstring_rootZ	link_typeZ	link_root�splitZarray_group�index�getcwd�rootZnetwork_rootZpathway_networkZppi_networkZppi_network_filterZweZfh�n�	readlines�line�strip�tZarray�write�sub�len�close�wr� r    r    �J/ldfssz1/SP_MSI/Pipeline/Pipeline/TP_Cor/src/Network_deal_sh_generation.py�<module>   sP   



 


*

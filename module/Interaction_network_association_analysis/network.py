#!/usr/bin/env python
#*coding=utf-8
#
#

import sys
import optparse
import os
import ConfigParser

usage="""\n
Author: chenweitian@genomics.cn
Date: Sun May  7 23:11:09 CST 2017
Function: draw  network  picture
=====================================================================================================
[python %s -h]
[python %s --example yes] run it to see nodes file and edges file  's detailed configuration
[python %s --nodes nodes.xls --edges edges.xls ]
[python %s --nodes nodes.xls --edges edges.xls --config conf --output_prefix ./network]
=====================================================================================================
"""%(sys.argv[0],sys.argv[0],sys.argv[0],sys.argv[0])

option = optparse.OptionParser(usage)
option.add_option('','--nodes',help='***Must be provided,graph nodes file***',default='NA' )
option.add_option('','--edges',help='***Must be provided,graph edges file***',default='NA' )
#option.add_option('','--conf',help='Optional,a conf file to  set more attributes for netowrk',default='NA' )
option.add_option('','--example',help='Optional,show the example',default='' )
#option.add_option('','--method',help='run igraph or dynamic picture or both[igraph|visnetwork|both]',default='both' )
#后面再加
option.add_option('','--config',help='use a conf or not',default='NA' )
option.add_option('','--output_prefix',help='Optional,output prefix,default[./network]',default='./network' )
option.add_option('','--layout',help='Optional,define layout yourself ',default='NA' )

(opts, args) = option.parse_args()
nodes_opt = opts.nodes
edges_opt = opts.edges
example_opt = opts.example
#method_opt = opts.method
conf_opt = opts.config
output_prefix_opt = opts.output_prefix
layout_opt = opts.layout

Bin="%s"%('/zfssz3/SP_MSI/Pipeline/software/R/R-devel/bin')

dict_conf={}
def setconf():
    class cConfParser:  
        def __init__(self, conf_path):  
            self.fpath = conf_path
            self.cf = ConfigParser.ConfigParser()
            self.cf.read(self.fpath)
        def get(self, s, o):  
            return self.cf.get(s, o)
        def sections(self):  
            return self.cf.sections()
        def items(self, s):  
            return self.cf.items(s)
        def options(self, s):  
            return self.cf.options(s) 
    if conf_opt:
        config_file = conf_opt 
        cp = cConfParser(config_file)
        for section_i in cp.sections():
            for options_i in cp.options(section_i):
                if len(cp.get(section_i, options_i))<1:
                    continue
                else:
                    dict_conf[options_i]=cp.get(section_i,options_i)
#        print dict_conf
                        

        



        
        
def usage_example():
    visnetwork='''
************************************************************************************************************************
=============
==nodes vis==
=============
[id]                点的id
[label]             点的名称
[group]             分组
[value]             大小
[shape]             形状["square", "triangle", "box", "circle", "dot", "star", "ellipse", "database", "text", "diamond"]
[title]             
[color]             颜色
[shadow]            是否有阴影FALSE/TRUE
=============
==edge vis===
=============

*[shape]:"circle","crectangle","csquare","none","pie","raster","rectangle","sphere","square","vrectangle"
*[layout]:布局默认用:"layout_nicely"   推荐:layout_nicely/layout_with_fr/layout_in_circle
        layouts <- grep("^layout_", ls("package:igraph"), value=TRUE)[-1]
        # [1] "layout_as_bipartite"  "layout_as_star"       "layout_as_tree"      
        # [4] "layout_components"    "layout_in_circle"     "layout_nicely"       
        # [7] "layout_on_grid"       "layout_on_sphere"     "layout_randomly"     
        #[10] "layout_with_dh"       "layout_with_drl"      "layout_with_fr"      
        #[13] "layout_with_gem"      "layout_with_graphopt" "layout_with_kk"      
        #[16] "layout_with_lgl"      "layout_with_mds"      "layout_with_sugiyama"
*[color]:
colours=colorRampPalette(c("#E41A1C","#377EB8","#4DAF4A","#984EA3","#FF7F00","#FFE528","#A65628","#F781BF","#999999"))(9)[1:9]
colours2=colorRampPalette(c("#A2A2A2","#D184AE","#79AC6C","#F5BF76","#EB643F","#8DC2E9"))(6)[1:6]
#灰色,暗粉红,绿色,黄色,朱红,蓝色

vis[color.background] label的颜色
vis[color.highlight.background] 选中时的背景颜色
edges1<-read.table('edges.xls',sep="\t",check.names=1,header=T,comment.char = "",quote="")

visNetwork:
*****nodes*******
*[shape]:"square", "triangle", "box", "circle", "dot", "star","ellipse", "database", "text", "diamond"
==========
===edge===
==========
[from]                          边的起点
[to]                            边的终点
[color]                         边的颜色，默认是起点的颜色
[width]                         边的宽度
#[lty]                           边的形状
[arrows_enabled]                是否有箭头[TRUE/FALSE]
[arrow_size]                    箭头大小[2]
[label]                         边的名称
type:
dashes:TRUE/NO (dotted/solid)
[font.size]                     边的字体大小
[font.color]                    边的字体颜色
arrows_enabled = FALSE




    please set "--example no " and rerun again

'''
    igraph='''
问题请联系:chenweitian@genomics.cn
************************************************************************************************************************
nodes文件配置,--nodes选项必选, "name"列必须提供，其他属性都是可选
edges文件配置,--edges 必选,edges文件 "from","to"两列必须提供,其他属性都是可选
conf文件配置,--config可选,配置更多属性
[python %s --show_example yes] 运行此命令，产生nodes,edges,conf文件例子,结果一个pdf图,一个网页动态图
************************************************************************************************************************'''%(sys.argv[0])
    igraph1='''
nodes文件配置,--nodes选项必选, "name"列必须提供，其他属性都是可选

[name]             node的名称
[group]            分组,例如[1,1,1,2,3,2,4,3,4]相同的分组会用置信区间圈起来,更多聚类算法请在配置文件中配置
[size]             node大小 (value),默认根据点的多少设置大小
[shape]            形状[circle]圆形,[sphere]球形,[rectangle]长方形,[triangle]三角形,[star]星形
                   "crectangle","csquare","none","pie","raster","rectangle","square","vrectangle"
[color]            顶点的颜色,默认:SkyBlue2
                   set1色卡:"#E41A1C","#377EB8","#4DAF4A","#984EA3","#FF7F00","#FFE528","#A65628","#F781BF","#999999"
                   "#A2A2A2","#D184AE","#79AC6C","#F5BF76","#EB643F","#8DC2E9"
                   #灰色,暗粉红,绿色,黄色,朱红,蓝色

[frame.color]      顶点的外圈颜色,默认[black]-->NA
[frame.width]      顶点的外圈大小，1
[label.font]       [1]纯文本, [2]加粗,[3]斜体,[4]加粗斜体,[5]指定符号字体,默认[1]
[label.cex]        label的大小
[label.dist]       字体离标签的距离,默认0
[label.degree]     标签与label的偏离方向,默认[-pi/4],[pi]左,[-pi/2]上,[pi/2]下,[zero]右
[label.color]      标签的颜色,默认[black]
=======================================================================================================================
edges文件配置,--edges 必选,edges文件 "from","to"两列必须提供,其他属性都是可选

[width]            边的粗细，默认[1]
[color]            边的颜色，默认[darkgrey]
[lty]              边的类型，实线[solid],dashed,虚线[dotted],dotdash,longdash,twodash，默认[solid]
[arrow_size]       箭头大小,默认1
[arrow.width]      箭头的宽度
[label]            label名字
[label.family]     label字体
[label.font]       label front,粗细等等,参考nodes
[label.cex]        label大小,默认[1]
[label.color]      label颜色
[curved]           zero curvature means straight edges, negative values means the edge bends clockwise,
positive values the opposite. TRUE means curvature 0.5, FALSE means curvature zero
[arrow.mode]        箭头类型,[0]没有箭头,[1]<,<-[2]>,->[3]<>,<->
[label.x]          x
[label.y]          y
=========================================================================================================================
conf文件配置,--config可选,配置更多属性

[layout =]
布局默认用      layout_nicely
推荐            [layout_nicely][layout_with_fr][layout_in_circle]中的一种
all选项会画出多种layout的pdf例子
"layout_as_bipartite","layout_as_star","layout_as_tree","layout_components","layout_in_circle"
"layout_nicely","layout_on_grid","layout_on_sphere","layout_randomly","layout_with_dh","layout_with_drl"
"layout_with_fr","layout_with_gem","layout_with_graphopt" "layout_with_kk","layout_with_lgl"
"layout_with_mds","layout_with_sugiyama"

[gradient = qvalue--"red","green"]
qvalue--"red","green"使用qvalue列的值用于点的颜色渐变,渐变颜色从红到绿
[degree = 6]
是否根据边的多少设置nodes的大小,不设置放空,基数的值为正数,公式log(最大节点的边数+1)*1.8+基数
[alpha = 0.01 ]
nodes中的group选项,分组的置信区间的透明度0-1
==========================================================================================================================
'''
    '''
更多信息请查看
http://igraph.org/r/doc/

edges1<-read.table('edges1.xls',sep="\t",header=T,comment.char = "",quote="")
g <- graph_from_data_frame(edges1, directed=TRUE, vertices=nodes1)
layouts <- grep("^layout_", ls("package:igraph"), value=TRUE)[-1]
http://igraph.org/r/doc/vertex.shape.pie.html

#=====
vis
"square", "triangle", "box", "circle", "dot", "star",
  "ellipse", "database", "text", "diamond"
color = list(background = "lightblue", 
                        border = "darkblue",
                        highlight = "yellow")

'''
    #toVisNetworkData(net)
    #visIgraph(net)
    print ("%s%s"%(igraph,igraph1))
#http://igraph.org/r/doc/shapes.html 
#https://datastorm-open.github.io/visNetwork/edges.html
def generate_rcode():
    igraph_shell='''library ("igraph")\nlibrary("visNetwork")\noptions(stringsAsFactors=F)
#add shape
#nil: no shape
add_shape("nil")
#add triangle

mytriangle <- function(coords, v=NULL, params) {
    vertex.color <- params("vertex", "color")
    if (length(vertex.color) != 1 && !is.null(v)) {
        vertex.color <- vertex.color[v]
    }

    vertex.frame.color <- params("vertex", "frame.color")
    if (length(vertex.frame.color) != 1 && !is.null(v)) {
    vertex.frame.color <- vertex.frame.color[v]
    }

    vertex.size <- 1/200 * params("vertex", "size")
    if (length(vertex.size) != 1 && !is.null(v)) {
        vertex.size <- vertex.size[v]*1.5
    }
    symbols(x=coords[,1], y=coords[,2], bg=vertex.color,fg=vertex.frame.color,
        stars=cbind(vertex.size, vertex.size, vertex.size),
        add=TRUE, inches=FALSE)
    }
# clips as a circle
add_shape("triangle", clip=shapes("circle")$clip,plot=mytriangle)
# generic star vertex shape, with a parameter for number of rays
mystar <- function(coords, v=NULL, params) {
    
    vertex.color <- params("vertex", "color")
    if (length(vertex.color) != 1 && !is.null(v)) {
        vertex.color <- vertex.color[v]
    }


    vertex.frame.color <- params("vertex", "frame.color")
    if (length(vertex.frame.color) != 1 && !is.null(v)) {
    vertex.frame.color <- vertex.frame.color[v]
    }
    vertex.size  <- 1/200 * params("vertex", "size")
    if (length(vertex.size) != 1 && !is.null(v)) {
        vertex.size <- vertex.size[v]*1.5
    }
    norays <- params("vertex", "norays")
    if (length(norays) != 1 && !is.null(v)) {
        norays <- norays[v]
    }

    vertex.frame.color <- params("vertex", "frame.color")
    if (length(vertex.frame.color) != 1 && !is.null(v)) {
    vertex.frame.color <- vertex.frame.color[v]
    }

    mapply(coords[,1], coords[,2], vertex.color, vertex.frame.color,vertex.size, norays,
        FUN=function(x, y, bg, fg,size, nor) {
            symbols(x=x, y=y, bg=vertex.color,fg=vertex.frame.color,
                stars=matrix(c(size,size/2), nrow=1, ncol=nor*2),
                add=TRUE, inches=FALSE)
        })
    }
   add_shape("star", clip=shape_noclip,plot=mystar, parameters=list(vertex.norays=5))

'''

    gradient_shell=""
    if 'gradient' in dict_conf :
        gra_column=dict_conf['gradient'].split('--')[0]
        gra_color="%s"%(dict_conf['gradient'].split('--')[1])
        gradient_shell+='''\
gra_color<-colorRampPalette(c(%s))(100)
df<-!is.na(as.numeric(nodes$%s))
nodes[df,]$color<-gra_color[cut(as.numeric(nodes[df,]$%s),breaks = 100)]
'''%(gra_color,gra_column,gra_column)
    #set alpha
    if 'alpha' not in dict_conf:
            alpha = 0.5
    else:
            alpha = dict_conf['alpha']

    if nodes_opt and edges_opt:
        igraph_shell+='''\
nodes<-read.table('%s',sep="\\t",header=T,comment.char = "",quote="")
edges <- read.table('%s',sep="\\t",header=T,comment.char = "",quote="")
'''%(nodes_opt,edges_opt)
        igraph_shell+=gradient_shell
        #set group color alpha

        igraph_shell+='''\
if (is.null(nodes$shape)){nodes$shape<-c('sphere')}
if (is.null(nodes$size)){ifelse(length(unique(nodes$name))>200,nodes$size<-c(1),ifelse(length(unique(nodes$name))<50,nodes$size<-c(10),nodes$size<-c(6)))}
if (is.null(nodes$color)){nodes$color<-c("SkyBlue2")}
if (is.null(nodes$frame.color)){nodes$frame.color<-c("NA")}

if (is.null(edges$color)){edges$color<-c('black')}
if (is.null(edges$width)){edges$width<-c(0.2)}
if (is.null(edges$lty)){edges$lty<-c('solid')}
if (is.null(edges$arrow.size)){edges$arrow.size<-c(0)}
#pie
#if (nodes$shape=="pie" & !is.null(nodes$pie) & !is.null(nodes$pie.color)){
#nodes$pie[!is.na(nodes$pie)]<-list(nodes$pie[!is.na(nodes$pie)])
#nodes$pie.color[!is.na(nodes$pie.color)]<-list(nodes$pie.color[!is.na(nodes$pie.color)])
#
#}



mark_list<-NULL
color_key<-c("#E41A1C","#377EB8","#4DAF4A","#984EA3","#FF7F00","#FFE528","#A65628","#F781BF","#999999")
mark_col<-color_key
mark_col1<-color_key
cat (nodes$group)
if (!is.null(nodes$group)){
   a<-nodes[!is.na(nodes$group),]
   paste_R<-"list(c(a[a$group==names(table(a$group))[1],]$name)"
    for (i in 2:length(table(a$group))){
        #a1<-"rownames(a[a$group==names(table(a$group))[i],])"
        a1<-paste0("c(a[a$group==names(table(a$group))[",i,"],]$name)")
        paste_R<-paste(paste_R, a1,sep=",")
    }
    color_key<-c("#E41A1C","#377EB8","#4DAF4A","#984EA3","#FF7F00","#FFE528","#A65628","#F781BF","#999999")
    mark_col1<-colorRampPalette(color_key)(length(table(a$group)))
    mark_col<-adjustcolor(mark_col1, alpha.f = %s)
    paste_R<- paste(paste_R,")")
    mark_list<-eval(parse(text=paste_R))
}
g <- graph_from_data_frame(edges,vertices=nodes)
#write.table(nodes,'nodes_temp.xls',sep="\t",quote=F,row.names = F)
'''%(alpha)

    if 'degree' in dict_conf:
        degree = dict_conf['degree']
        igraph_shell+='''\
if(%s){
    V(g)$size<-log(degree(g)*1.8+1)+%s   
    #cat(nodes$size)
    if(length(V(g))>500){
        V(g)$size<-log(degree(g)*1.8+1)+1
    }
}
'''%(degree,degree)

    if 'layout' not in dict_conf:
        dict_conf['layout']='layout_nicely'
    if 'layout' in dict_conf:
        #title(main="test layout", sub="%s", cex.main = 3, cex.sub = 2)    
        if dict_conf['layout'] == 'all':
            all="layout_as_star,layout_as_tree,layout_components,layout_in_circle,layout_nicely,layout_on_grid,layout_on_sphere,layout_randomly,layout_with_dh,layout_with_drl,layout_with_fr,layout_with_gem,layout_with_graphopt,layout_with_kk,layout_with_lgl,layout_with_mds"
            igraph_shell+='''\
par(mfrow=c(4,5),new=TRUE)
pdf("%s.all_layout.pdf")
'''%(output_prefix_opt)
            for layout_i in all.split(','):
                igraph_shell+='''plot(g,layout=%s,mark.groups=mark_list,mark.col=mark_col,mark.border=mark_col1)
title(main="%s")
'''%(layout_i,layout_i)
            igraph_shell+='''\
dev.off()
'''        
        if dict_conf['layout'] != 'all':
            if 'cluster' in dict_conf:
                if dict_conf['cluster'] == "all":
                    cluster_list=['cluster_edge_betweenness','cluster_label_prop','cluster_fast_greedy','cluster_leading_eigen','cluster_louvain','cluster_optimal','cluster_spinglass','cluster_walktrap']
                    #cluster_fast_greedy
                    igraph_shell+='''\
par(mfrow=c(4,5),new=TRUE)
pdf("%s.all_cluster.pdf")
'''%(output_prefix_opt)
                    for layout_i in cluster_list:
                        igraph_shell+='''clp <- %s(g)
plot(clp,g)
title(main="%s")
'''%(layout_i,layout_i)
                    #out of for
                    igraph_shell+='''\
dev.off()
''' 
                else:
                    igraph_shell+='''\
pdf("%s.pdf")
clp <- %s(g)
plot(clp,g)
dev.off()
'''%(output_prefix_opt,dict_conf['cluster'])

            else:
                #自定义layout
                if layout_opt != "NA":
                    igraph_shell+='''\
mylayout2<-read.table("%s",header=T,row.names=1,sep="\t",quote="")
V(g)[row.names(mylayout2)]$x=mylayout2$x
V(g)[row.names(mylayout2)]$y=mylayout2$y
if(! is.null(mylayout2$z)){
V(g)[row.names(mylayout2)]$z=mylayout2$z
}
pdf("%s.pdf")
plot(g,mark.groups=mark_list,mark.col=mark_col,mark.border=mark_col1)
dev.off()
'''%(layout_opt,output_prefix_opt)
                else:

                   igraph_shell+='''\
pdf("%s.pdf")
plot(g,layout=%s,mark.groups=mark_list,mark.col=mark_col,mark.border=mark_col1)
dev.off()
'''%(output_prefix_opt,dict_conf['layout'])

                igraph_shell+='''\
visg<-toVisNetworkData(g)
#title<-paste0("<p>", visg$nodes$label,"<br>Tooltip !</p>")
ifelse(!is.null(visg$nodes$label),visg$nodes$title<-visg$nodes$label,ifelse(!is.null(visg$nodes$id),'1=1',visg$nodes$title<-visg$nodes$id))

#if(!is.null(visg$edges$label)){
#visg$edges$title<-visg$nodes$label
#}

visg$nodes$color.background <-visg$nodes$color
#visg$nodes$color<-"#4DAF4A"
#visg$nodes$color<-"firebrick1"不支持,黑色
visg$nodes$highlight.background <-visg$nodes$color
visg$nodes$shape[visg$nodes$shape=="circle"]<-"dot"
#按名称长度改成点
#ifelse(max(nchar(visg$nodes$label)>20),visg$nodes$shape[visg$nodes$shape=="sphere"]<-"dot",visg$nodes$shape[visg$nodes$shape=="sphere"]<-"ellipse")
#球与圆圈全部改成点
visg$nodes$shape[visg$nodes$shape=="sphere"]<-"dot"
visg$edges$dashes<-FALSE
visg$edges$dashes[visg$edges$lty=="dotdash"]<-TRUE
if(!is.null(visg$nodes$size)){
visg$nodes$size[visg$nodes$shape=="dot"]<- visg$nodes$size[visg$nodes$shape=="dot"]*5+10
visg$nodes$size[visg$nodes$shape=="star"]<- visg$nodes$size[visg$nodes$shape=="star"]*3+25
visg$nodes$size[visg$nodes$shape=="triangle"]<- visg$nodes$size[visg$nodes$shape=="triangle"]*6+25
visg$nodes$size[visg$nodes$shape=="square"]<- visg$nodes$size[visg$nodes$shape=="square"]*3+25
}
#visg$nodes$font.color<-NULL
#visg$nodes$label.color<-NULL
#visg$edges$color<-"yellow"#边的颜色
#visg$edges$font.color<-"green"#边的字体颜色
if(!is.null(visg$edges$arrow.size)|!is.null(visg$edges$arrow.width)){visg$edges$arrows[edges$arrow.size>0]<-"to"}

layout=ifelse(length(unique(nodes$name))<30,'layout_in_circle','layout_with_fr')
network<-visNetwork(visg$nodes, visg$edges,height = "1000px",width='1500px') %>%
#visIgraphLayout(layout = "layout_in_circle") %>%
visIgraphLayout(layout = layout) %>%
visIgraphLayout()%>%
visOptions(highlightNearest = list(enabled = T, hover = T), 
             nodesIdSelection = T) %>%
visInteraction(dragNodes = TRUE, 
                 dragView = TRUE, 
                 zoomView = TRUE,
                 keyboard = TRUE, tooltipDelay = 0
                )
'''
                igraph_shell+='''\
#skip the error output
#write.table(visg$nodes,'visg_nodes.xls',sep="\t",quote=F,row.names = F)
#write.table(visg$edges,'visg_edges.xls',sep="\t",quote=F,row.names = F)
#tryCatch(visSave(network,'%s.html'), error = function(err){cat("***cluster is too old to use PANDOC, just ignore the pandoc error,sign by chenweitian,use high version glibc to slove it.***")})
cwd = getwd()
visSave(network,paste(cwd,'%s.html',sep="/"),selfcontained=F)
'''%(output_prefix_opt,output_prefix_opt)
    temp_R=open('temp.R','w')
    temp_R.write("%s"%(igraph_shell))
    temp_R.close()

    #print "%s/Rscript temp.R"%(Bin)
    #2>/dev/null
    os.system("%s/Rscript temp.R \necho 'Still_waters_run_deep' 2>/dev/null \nrm temp.R"%(Bin))
    #os.system("%s/Rscript temp.R \necho 'Still_waters_run_deep' 2>/dev/null "%(Bin))

    R_shell='''\
'''
    to='''
visLayout(randomSeed = 123)
#skip the error
library(htmlwidgets)
my.saveWidget<-function (widget, file, selfcontained = TRUE, libdir = NULL, 
    background = "white", knitrOptions = list()) 
{
    html <- toHTML(widget, standalone = TRUE, knitrOptions = knitrOptions)
    if (is.null(libdir)) {
        libdir <- paste(tools::file_path_sans_ext(basename(file)), 
            "_files", sep = "")
    }
    htmltools::save_html(html, file = file, libdir = libdir, 
        background = background)
    if (selfcontained) {
        if (!pandoc_available()) {
            cat("Saving a widget with selfcontained = TRUE requires pandoc. For details see:\n", 
                "https://github.com/rstudio/rmarkdown/blob/master/PANDOC.md")
        }
        pandoc_self_contained_html(file, file)
        unlink(libdir, recursive = TRUE)
    }
    invisible(NULL)
}
#skip the error output
#trace(saveWidget,edit=TRUE)
#htmlwidgets::saveWidget
unlockBinding("saveWidget", as.environment("package:htmlwidgets"))
assign("saveWidget", my.saveWidget, as.environment("package:htmlwidgets"))
lockBinding("saveWidget", as.environment("package:htmlwidgets"))

visEdges(arrows = "from") %>% 
  visHierarchicalLayout() # same as   visLayout(hierarchical = TRUE) 

'''
    #print igraph_shell


    def pdf(mod):
        if mod=='all':
            #layouts <- grep("^layout_", ls("package:igraph"), value=TRUE)[-1]
            pass 
                
        
    Rcode_3=r'''
    
    network<-visNetwork(nodes, edges, height = "500px", width = "100%",main = "A really simple example")
    network %>%'''
    Rcode4=r''' visSave(file = "%s")'''%('network.html')
    #print Rcode3+Rcode4









def example():
    
    edges_example='''\

'''





















if __name__ == '__main__':
    if len(sys.argv) < 2:
        os.system("python %s -h"%(sys.argv[0]))
        sys.exit(1)
    if example_opt == "yes":
        usage_example()
        sys.exit(1)
    else:
        #generate_rcode()
        setconf()
        generate_rcode()
        #print dict_conf
















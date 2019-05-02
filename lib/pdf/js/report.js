var timeout,hv_obj,goTop,scroll_time,seq_cn_wid,seq_cn_hg,clazz;



$(function(){
	goTopEx();
	top_icon();	
	cnt_hg_adj();	
	$(window).scroll(function(){
		cnt_hg_adj();
	  });
	$(window).resize(function(){
		cnt_hg_adj();
	  }); 
    $("ul.seq_ul span").click(function(){
	   $(this).parent().find("ul:first").slideToggle(300);
	   if($(this).hasClass("click"))
	   $(this).removeClass("click");
	   else
	   $(this).addClass("click");
	});  
    $(".nav_ul > li").not(".line").hover(function(){
		    hv_obj=this;
		    timeout=setTimeout(function(){
				$(hv_obj).addClass("li_hv");
				$(hv_obj).find(".nav_drop").slideDown(300);					
			  },300);			
		  },function(){
			clearTimeout(timeout);				  
			$(hv_obj).removeClass("li_hv");
			$(hv_obj).find(".nav_drop").slideUp(300);					
    });
	$(".nav_drop li").hover(function(){
		 $(this).addClass("li_hv");
		},function(){
		 $(this).removeClass("li_hv");
	  });
	$(".seq_ctl_top:first").css("display","block");
	if($(".seq_ctl_top:first").next().is("ul")){
		$(".seq_ctl_top:first").next().css("display","block");
		}		
	$(".nav_ul li").not(".line").click(function(){
		var drop_text=$.trim($(this).find("a:first").text());		
		$(".seq_ctl_top",window.frames["left_page"].document).each(function(){
			var ctl_text=$.trim($(this).text());
			if(drop_text==ctl_text){
				 $(".seq_ctl_top",window.frames["left_page"].document).css("display","none");
				 $(".seq_ul",window.frames["left_page"].document).css("display","none");
				 $(this).css("display","block");
				 if($(this).next().is("ul")){
					 $(this).next().css("display","block");
				   }
				 return false;
				}
			});		
	  });
	$(".seq_contentc").click(function(){
		if($(this).hasClass("seq_contentc1")){
			var seq_cn_wid=$(".seq_cn").width() - 247;
			$(this).removeClass("seq_contentc1");
			$(".seq_contentl").css("display","block");
			$(".seq_cn").css("width",seq_cn_wid);			
		  }else{
			var seq_cn_wid=$(".seq_cn").width() + 247;
			$(this).addClass("seq_contentc1");
			$(".seq_contentl").css("display","none");
			$(".seq_cn").css("width",seq_cn_wid);			  
		 }
	 });	
	$(".seq_top").click(function(){
		if($(this).hasClass("seq_top1")){
			var seq_cn_hg=$(".seq_cn").height() - 76 + "px";
			$(this).removeClass("seq_top1");
			$(".header").css("display","block");
			$(".seq_cn").css("height",seq_cn_hg);
			$(".seq_contentl").css("height",seq_cn_hg);			
		  }else{
			var seq_cn_hg=$(".seq_cn").height() + 76 + "px";
			$(this).addClass("seq_top1");
			$(".header").css("display","none");
            $(".seq_contentl").css("height",seq_cn_hg);	
			$(".seq_cn").css("height",seq_cn_hg);		
		 }
	 });
	 $("div[class^='top_btn']").hover(function(){
		  clazz=$(this).attr("class");		 
		  $(this).addClass(clazz + "_hv");
		 },function(){
		  $(this).removeClass(clazz + "_hv");
	  }); 
});
function cnt_hg_adj(){
	var win_wid=$(window).width();
	var win_hg=$(window).height();
	if($(".seq_contentl").css("display")=="block"){
		seq_cn_wid=win_wid - 257 + "px";
		}else{
		seq_cn_wid=win_wid - 10 + "px";	
	  }
	if($(".header").css("display")=="block"){
	    seq_cn_hg=win_hg - 143 + "px";		
		}else{
		seq_cn_hg=win_hg - 67 + "px";	
	 }
	$(".seq_cn").css({"width":seq_cn_wid,"height":seq_cn_hg});
	$(".seq_contentl").css({"height":seq_cn_hg});
  }
function goTopEx(){	
    $("div[class^='top_btn']").click(function(){
		goTop=setInterval(scrollMove,10);	        	
		return false;						
     });
}
function top_icon(){
	if(scroll_time)clearTimeout(scroll_time);
	getScrollTop()>0 ? $("div[class^='top_btn']").css("visibility","visible"):$("div[class^='top_btn']").css("visibility","hidden");
	scroll_time=setTimeout("top_icon()",300);
}
function getScrollTop(){	
       return $(document).scrollTop();
    }
function setScrollTop(value){
       $(document).scrollTop(value);
    } 
function scrollMove(){
        setScrollTop(getScrollTop()/1.3);
        if(getScrollTop()<1)clearInterval(goTop);
    }
window.onload = function(){
document.getElementById("group_id1").innerHTML="C-VS-T";
document.getElementById("group_id2").innerHTML="C-VS-T";
document.getElementById("protein_all").innerHTML="1846";
document.getElementById("transcription_all").innerHTML="2528";
document.getElementById("correlation_all").innerHTML="1830";
document.getElementById("protein_diff").innerHTML="563";
document.getElementById("transcription_diff").innerHTML="392";
document.getElementById("correlation_diff").innerHTML="282";
document.getElementById("TF_protein_diff").innerHTML="15";
document.getElementById("TF_transcription_diff").innerHTML="19";
document.getElementById("TF_protein_nodiff").innerHTML="6";
document.getElementById("TF_transcription_nodiff").innerHTML="3";
document.getElementById("p").innerHTML="0.28";
document.getElementById("p_description").innerHTML="该比较组蛋白质组与转录组检测到的转录因子个数与表达差异无关";
};
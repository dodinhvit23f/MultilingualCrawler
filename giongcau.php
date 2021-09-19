<?php
	$i = 1;
	
	$line = 0;
	$lim = 10 + $line;
	$last = ($line > 10) ? 0: $lim - 10;
	
 ?>
<!DOCTYPE html>
<html>
<head>
	<title>Thực hiện gióng hàng</title>
	<meta charset='UTF-8'>
	<link href="bootstrap-4.5.3-dist\css\bootstrap.min.css">
</head>
<body>
<iframe id="download_iframe" style="display:none;"><head> <meta charset="UTF-8"> </head></iframe>
<div style="width: 100%;height:100px;background:#gray;" align="center">
	<h1 style="color: #304499;">Công cụ hỗ trợ soạn thảo ngữ liệu song ngữ</h1>
</div>
<div style="width: 100%;height: 50px;background:gray;">
	<ul style="display: inline-block;"class="menu">
		<li style="list-style: none;float: left;height: 50px;width: 100px;text-align: center;margin-top: -15px;"><a href="demo01.html" style="text-decoration: none;line-height: 50px;color: white;">Trang Chủ</a></li>
		<li style="list-style: none;float: left;height: 50px;width: 150px;text-align: center;margin-top: -15px;"><a href="solieuthongke.html" style="text-decoration: none;line-height: 50px;color: white;">Thống kê ngữ liệu</a></li>
		<li style="list-style: none;float: left;height: 50px;width: 150px;text-align: center;margin-top: -15px;"><a href="gionghangvb.html" style="text-decoration: none;line-height: 50px;color: white;">Gióng hàng văn bản</a></li>
		<li style="list-style: none;float: left;height: 50px;width: 150px;text-align: center;margin-top: -15px;"><a href="gionghangcau.html" style="text-decoration: none;line-height: 50px;color: white;">Gióng hàng câu</a></li>

	</ul>
		<style type="text/css">.menu li:hover{
			background: #A0A0A0;
		}
	.menu li a:hover{
		color: blue;
	}
	table {
    width: 100%;
    height: auto;       
    font-family: arial, sans-serif;
    border:1px solid #ddd;
}
th, td {
    padding: 8px;
    text-align: left;
    border-top: 1px solid #dee2e6;
    text-align: center;
}
    tbody tr:nth-child(odd) {
    background-color: #f2f2f2;
}
.detele{
	width: 60%;
	height: 30px;
	font-size: 16px;
	margin-left: 10px;
}
.detele-gh{
	width: auto;height: 30px;
	font-size: 16px;
	}
.content{
	width: 100%;height: auto;margin-top: 2%;
}
.content-1{
	width: 60%;height: auto;margin-left: 10%;border: 2px solid #ddd;;padding-left: 15%;border-radius: 

}
.website{
	margin-right: 10px;
	margin-left: 10px;
	font-size: 18px;
}
.leangue{
	width: 15%;
	height:30px;
	margin-right: 20px;
}
.modal{
margin: 0% 3% 0% 3%; width: 100%;
}
.modal-table{
	width: 90%;height: auto;text-align: center;font-size: 18px;margin-top: 15px;
}
.phantrang{margin-left:20px; width: 90%; height: auto;margin: 0% 3% 0% 3%;}
.input1{width: 70px; height: 30px; text-align: center; margin-right: 15px;}
.skip{width: 100px; height: 32px;}
.extract{
	width: 10%;
	height: 40px;
	}
.phan{float:right;margin-top: 10px;}
.pvg{list-style: none;float:left;}
.export-data{
	width: 5%;
	height: 40px;
	float:right;
	margin-right: 54px;
}
.url{
	width: 20%;
	height: 26px;
}
body,html{
	margin: 0;
	padding: 0;
	}

.export-data {
  background-color: #808080;
  width: auto;
  border: none;
  color: #ffffff;
  cursor: pointer;
  display: inline-block;
  font-family: 'BenchNine', Arial, sans-serif;
  font-size: 1em;
  font-size: 18px;
  line-height: 1em;
  margin: 10px 35px;
  outline: none;
  padding: 12px 30px 10px;
  position: relative;
  text-transform: uppercase;
  font-weight: 700;
}

.export-data:before,
.export-data:after {
  border-color: transparent;
  -webkit-transition: all 0.25s;
  transition: all 0.25s;
  border-style: solid;
  border-width: 0;
  content: "";
  height: 24px;
  position: absolute;
  width: 24px;
}

.export-data:before {
  border-color: #808080;
  border-top-width: 2px;
  left: 0px;
  top: -5px;
}

.export-data:after {
  border-bottom-width: 2px;
  border-color: #808080;
  bottom: -5px;
  right: 0px;
}

.export-data:hover,
.export-data.hover {
  background-color: #808080;
}

.export-data:hover:before,
.export-data.hover:before,
.export-data:hover:after,
.export-data.hover:after {
  height: 100%;
  width: 100%;
}

.export{
  background-color: #808080;
  width: auto;
  border: none;
  color: #ffffff;
  cursor: pointer;
  display: inline-block;
  font-family: 'BenchNine', Arial, sans-serif;
  font-size: 1em;
  font-size: 18px;
  line-height: 1em;
  margin: 10px 35px;
  outline: none;
  padding: 12px 30px 10px;
  position: relative;
  text-transform: uppercase;
  font-weight: 700;
}

.export:before,
.export:after {
  border-color: transparent;
  -webkit-transition: all 0.25s;
  transition: all 0.25s;
  border-style: solid;
  border-width: 0;
  content: "";
  height: 24px;
  position: absolute;
  width: 24px;
}

.export:before {
  border-color: #808080;
  border-top-width: 2px;
  left: 0px;
  top: -5px;
}

.export:after {
  border-bottom-width: 2px;
  border-color: #808080;
  bottom: -5px;
  right: 0px;
}

.export:hover,
.export.hover {
  background-color: #808080;
}

.export:hover:before,
.export.hover:before,
.export:hover:after,
.export.hover:after {
  height: 100%;
  width: 100%;
}
.btncon{
  background-color: #808080;
  width: 50%;
  border: none;
  color: #ffffff;
  cursor: pointer;
  display: inline-block;
  font-family: 'BenchNine', Arial, sans-serif;
  font-size: 1em;
  font-size: 18px;
  line-height: 1em;
  outline: none;
  position: relative;
  text-transform: uppercase;
  font-weight: 700;
}

.btncon:before,
.btncon:after {
  border-color: transparent;
  -webkit-transition: all 0.25s;
  transition: all 0.25s;
  border-style: solid;
  border-width: 0;
  content: "";
  height: 24px;
  position: absolute;
  width: 24px;
}

.btncon:before {
  border-color: #808080;
  border-top-width: 2px;
  left: 0px;
  top: -5px;
}

.btncon:after {
  border-bottom-width: 2px;
  border-color: #808080;
  bottom: -5px;
  right: 0px;
}

.btncon:hover,
.btncon.hover {
  background-color: #808080;
}

.btncon:hover:before,
.btncon.hover:before,
.btncon:hover:after,
.btncon.hover:after {
  height: 100%;
  width: 100%;
}
.btncon-gh{
  background-color: #808080;
  width: auto;
  height: 15%;
  border: none;
  color: #ffffff;
  cursor: pointer;
  display: inline-block;
  font-family: 'BenchNine', Arial, sans-serif;
  font-size: 1em;
  font-size: 18px;
  line-height: 1em;
  outline: none;
  position: relative;
  text-transform: uppercase;
  font-weight: 700;
}

.btncon-gh:before,
.btncon-gh:after {
  border-color: transparent;
  -webkit-transition: all 0.25s;
  transition: all 0.25s;
  border-style: solid;
  border-width: 0;
  content: "";
  height: 24px;
  position: absolute;
  width: 24px;
}

.btncon-gh:before {
  border-color: #808080;
  border-top-width: 2px;
  left: 0px;
  top: -5px;
}

.btncon-gh:after {
  border-bottom-width: 2px;
  border-color: #808080;
  bottom: -5px;
  right: 0px;
}

.btncon-gh:hover,
.btncon-gh.hover {
  background-color: #808080;
}

.btncon-gh:hover:before,
.btncon-gh.hover:before,
.btncon-gh:hover:after,
.btncon-gh.hover:after {
  height: 100%;
  width: 100%;
}
.modal-dialog{
	margin-left: 15%;
}
.modal-content
{
	margin-left: 15%;
	height: 500px;
}
</style>
</div>
<div class="content">
	<!-- 
	<div class="content-1">
	<p>
		<input type="radio"  id="dlcs" onclick="chonDLgoc()" checked="true" />
			<label for="age1" style="font-size: 18px">Dữ Liệu Có Sẵn</label>
		<input type="radio"  id="dlcs1" onclick="chonDLkhac()"/>
			<label for="age2" style="font-size: 18px">Dữ Liệu Khác</label>
	</p>
	<p>
		<span style="font-size: 18px">Nguồn Dữ Liệu</span>
		<select name="web" id="data-exsit" style="width: 10%;height: 30px;">
			<option></option>
			<option>VOV</option>
			<option>Wikipedia</option>
			<option>Ted talk</option>
			<option>Subtitle</option>
			<option>Paracrawl</option>
		</select>
		<span class="website"> Link Website</span>
		<input id="urlnn1" type="text"  style="margin-right: 10px;" class="url" disabled="true">
		<input id="urlnn2" type="text"  class="url" disabled="true">
	</p>
	<p>
		<span style="font-size: 18px">Cặp Ngôn Ngữ</span>
		<select name="src_lang" id="src_lang"class="leangue">
			<option></option>
			<option value="vi">Vietnamese</option>
			<option value="km">Khmer</option>
			<option value="zh">Chinese</option>
			<option value="lo">Laos</option>
			<option value="en">English</option>
		</select>
		<span>
			<select name="tgt_lang" id="tgt_lang"  class="leangue">
				<option></option>
				<option value="en">English</option>
				<option value="lo">Laos</option>
				<option value="zh">Chinese</option>
				<option value="km">Khmer</option>
				<option value="vi">Vietnamese</option>
			</select>
		</span>
	</p>
	-->
	
	
</div>
	<div style="margin: 1% 3% 0% 3%; width: 100%;" id="modal_cau">
		<table style="width: 90%;height: auto;text-align: center;font-size: 18px;margin-top: 15px;">
			<tr>				
				<th style="width: 3%;"><input id="btncheck_vb" type="checkbox" name=""></th>
				<th style="width: 35%;"><?php echo $_REQUEST['src_lang']; ?></th>
				<th style="width: 35%;"><?php echo $_REQUEST['tgt_lang']; ?></th>
				<th style="width: 5%;">Độ đo</th>
				<th style="width: 10%;">Edit</th>
				
			</tr>
			
			<?php
				$align_files = $_REQUEST['file'];
				//echo(getcwd());
				if(!isset($align_files)){
					return;
				}
				
				$file = fopen($align_files, "r") or die("Unable to open file!");
				
				while(!feof($file)): 
				
				$str = explode("\t",fgets($file));
				if(!isset($str[0])){
					continue;
				}
				
				if(!isset($str[1])){
					continue;
				}
			
				?>
				<tr id="line_<?php echo $i;?>" class="line">
					<td><input id="check_all" type="checkbox" name="name"></td>
					
					<td style="text-align:left;"> 
							<span id="src_line_<?php echo $i;?>" class="content_line" ><?php   echo $str[0] ; ?></span>
					<td style="text-align:left;"> 
							<span  id="tgt_line_<?php echo $i;?>" class="content_line" ><?php  echo $str[1]; ?></span>				
					</td>
					<td>0.5</td>
					<td><button style="width: 40%;height: 30px;" id="detele"class="btncon" onclick="remove('line_<?php echo $i;?>')">Xoá</button>
						<button style="width: 40%;height: 30px;margin-left:10px;"id="edit"onclick="popupOpen(<?php echo $i++; ?>)"class="btncon">Edit</button>
					</td>
				<tr>
			<?php if(!isset($file)){
					return;
				}
				endwhile;
				fclose($file);
			?>
	</table>
	<div class="phantrang" >
		<p>      
			<button id="previ" style="font-weight: bold; width: 150px;text-decoration: none; " onclick="paging(0,10)">
				<span aria-hidden="true" id="">←</span> Trước
			</button>
			<button id="next"  style="font-weight: bold; width: 150px;text-decoration: none;" onclick="paging(10,20)">Sau
				<span aria-hidden="true">→</span>
			</button>
			
			<button class="export-data" id="export-data" onclick="getAllContent('content_line')"> Export Data</button>
			<button class="export-data" id="export-all" onclick="getAllContent('content_line')">Save All</button>
			<button type="submit" class="export-data">Checks Exist</button>
		</p>              
	</div>         
	</div>
	</div>
</div>
	<div class="modal-dialog" id="popup" style="top:100px; display:none;position:fixed;z-index:100;width:55%;background-color: #BDBDBD" onload="paging(true)">
					<div class="modal-content" style="position:relative">
						<div class="modal-header" style="height: 100px; ">
							<button type="button" onclick="popupClose()" data-dismiss="modal" style="margin-top: 3px;margin-left:-90px;margin-bottom: 30px;  position:relative ;">×</button>
							<!-- <h4 class="modal-title">Chỉnh sửa ngữ liệu song ngữ</h4> -->
							<h4 class="modal-title" style="font-size: 16px;margin-top: -1%;">
								<div class="row">
									<div class="col-md-5">
										<label for="field4">
											<span>Status:
												<span class="required"></span>
											</span>
											<select name="select_status_ctmL6RA47mkLvRFaT" style="padding: 5px; width: 195px;">
												<option value="sure">Sure</option>
												<option value="notSure">Not Sure</option>
												<option value="needReview">Need Review</option>
												<option value="veryNeedReview">Really Need Review</option>
											</select>									
										</label>
										
										<label for="field4" style="margin-top: 5px">
											<span>Topic:
												<span class="required"></span>
											</span>
											<select name="select_topic_ctmL6RA47mkLvRFaT" style="padding: 5px; margin-left: 7px; width: 195px">
											<option value="">None</option>
											
											</select>
										</label>
										
									</div>
									<div class="col-md-3">
										<label for="field4">
											Edit count:  0 
										</label>
									</div>
									<div class="col-md-4" style="width: 220px;">
										<label for="field4">
											
										</label>
									</div>
								</div>
							</h4>
						</div>
						<div class="modal-body" style="margin-top: 2%;">
							<div class="row">
								
								<div class="col-sm-6" style="position:absolute;left:-120px;">
									<div class="col-sm-6" >
										<div class="col-sm-12" style="font-weight: bold; font-size: 18px; "><?php echo $_REQUEST['src_lang']; ?></div>
										<div class="col-sm-12">
											<label for="field2">
												<!-- <textarea rows="10" cols="49.8" 
												style="max-width: 100%; color: black;" 
												name="vietnamese_sentence_{{_id}}">{{#if vnSentenceEdited}}{{vnSentenceEdited}}{{else}}{{vietnamese_sentence}}{{/if}}</textarea> -->
												<div><input id="line" type="hidden" value="" /></div>
												<!-- comment to remove redundant spaces -->
												<div id="vietnamese_sentence_ctmL6RA47mkLvRFaT" style="width:380px; max-width: 100%; color: black; border: 1px solid black; height: 206px; font-weight: normal; padding: 5px; overflow-y: auto;" contenteditable="true"><!--
												--><!-- 
													--><!-- 
														--><!--
															--><span id="src_line" style="color: black;"></span><!--
														--><!-- 
													--><!-- 
												--><!--
											 --></div>
											</label>
										</div>
									</div>				
								</div>
								<div class="col-sm-6" style="position:absolute; left:50%;">
										<div class="col-sm-12" >
										<div class="col-sm-12" style="font-weight: bold; font-size: 18px; "><?php echo $_REQUEST['tgt_lang']; ?></div>
											<label for="field2">
												<!-- <textarea rows="10" cols="49.8" 
												style="max-width: 100%; color: black;" 
												name="japanese_sentence_{{_id}}">{{#if jpSentenceEdited}}{{jpSentenceEdited}}{{else}}{{japanese_sentence}}{{/if}}</textarea> -->
												
												<!-- comment to remove redundant spaces -->
												<div id="japanese_sentence_ctmL6RA47mkLvRFaT" style="width:380px; max-width: 100%; color: black; border: 1px solid black; height: 206px; font-weight: normal; padding: 5px; overflow-y: auto;" contenteditable="true"><!--
												--><!-- 
													--><!-- 
														--><!--
															--><span id="tgt_line" style="color: black;"></span><!--
														--><!-- 
													--><!-- 
												--><!--
											 --></div>																																	
											</label>
										</div>
									</div>
							</div>
							<div class="row" style="position:absolute; bottom:20px; left:27%; height:40px">
								<div class="col-md-8">
									<button type="button" id="Save_Edit" class="btn-save-edit btn btn-primary btn-lg center-block" data-dismiss="modal" style="width: 200px; margin-top: 25px; 
											   margin-right: 45px; float: right;">Save Editing</button>
								</div>								
								<div class="col-md-4">
									
								</div>
							</div>
						</div>
						<!-- <div class="modal-footer">
								<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
							</div> -->
					</div>
				</div>
</div>
	<script>
	
	function paging(start,end){
		var lines = document.getElementsByClassName('line');
				
		for(var line = 0; line < lines.length; line++){
			
			
			if(line >= start && line < end){
				lines[line].style.display = "table-row";
				continue;
			}
			
			lines[line].style.display = "none";
		}
		
		var startN = 0;
		var endN = 10;
		
		if(end + 10 < lines.length){
			startN = start + 10;
			endN = end + 10;	
		}else{
			
			startN = start;
			
			if(end <	 lines.length){
				//alert(endN);
				//alert(lines.length);
				startN = lines.length - (lines.length - end);
			}	
			endN = lines.length;			
			
		}
		//alert("paging\(true,"+start+","+end+"\)");
		
		document.getElementById("next").setAttribute("onclick","paging\("+startN+","+endN+"\)");	
		
		var startL = 0;
		var endL = 10;
		
		if(endN != lines.length){
			if(start - 10 > 0){
				startL = start - 10;
				endL = end - 10;
				
			} else{
				if(start - 10 == 0){
					startL = 0;
					endL = 10;
				}
			}
		}
		else{
			startL = startN - 10;
			endL = startN;
		}
			//alert("paging(true,"+start+","+end")");
			
		
		
			
				
		
	
		document.getElementById("previ").setAttribute("onclick","paging\("+startL+","+endL+"\)");
		
	}
	
	function remove(id){
		document.getElementById(id).remove();
	}
	
	function chonDLgoc (){
		document.getElementById("dlcs1").checked = false;
		//document.getElementById("data-exsit").disabled = false;
		document.getElementById("urlnn1").disabled = true;
		document.getElementById("urlnn2").disabled = true;
	}
	function chonDLkhac (){
		document.getElementById("dlcs").checked = false;
		//document.getElementById("data-exsit").disabled = true;
		document.getElementById("urlnn1").disabled = false;
		document.getElementById("urlnn2").disabled = false;
	}
	
	/*
	document.getElementById("btncheck").onclick = function(){

		var checkboxes = document.getElementsByName('name');
		if (document.getElementById("btncheck").checked == false) 
		{
			for (var i = 0; i < checkboxes.length; i++){
                    checkboxes[i].checked = false;
                }
		}
		else if(document.getElementById("btncheck").checked == true)
		{
			for (var i = 0; i < checkboxes.length; i++){
                    checkboxes[i].checked = true;
                }
		}
	}*/
	
	document.getElementById("btncheck_vb").onclick = function(){

		var checkboxes = document.getElementsByName('name2');
		if (document.getElementById("btncheck_vb").checked == false) 
		{
			for (var i = 0; i < checkboxes.length; i++){
                    checkboxes[i].checked = false;
                }
		}
		else if(document.getElementById("btncheck_vb").checked == true)
		{
			for (var i = 0; i < checkboxes.length; i++){
                    checkboxes[i].checked = true;
                }
		}
	}
	
	function popupOpen(id) {
	
	document.getElementById("popup").style.display = "block";	
	document.getElementById("src_line").innerHTML = document.getElementById("src_line_"+id).innerHTML;
	document.getElementById("tgt_line").innerHTML = document.getElementById("tgt_line_"+id).innerHTML;
	document.getElementById("line").value = id;
	
	}
	
	function saveRecordLine(){
		var id = document.getElementById("line").value;
		if(id != ""){
			document.getElementById("src_line_"+id).innerHTML = document.getElementById("src_line").innerHTML;
			document.getElementById("tgt_line_"+id).innerHTML = document.getElementById("tgt_line").innerHTML;
		}
		
	}
	
	document.getElementById("Save_Edit").onclick = function(){
		popupClose();
		saveRecordLine();
	}	
	
		
	function popupClose() {
		
	document.getElementById("popup").style.display = "none";	
	
		
	}
	
	function getAllContent(_class){
		var content = document.getElementsByClassName(_class);
		var frame = document.getElementById('download_iframe');
	
		var contents = "";
		for (var i = 0; i < content.length; i+= 2){
			contents += content[i].innerHTML +'\t'+ content[i + 1].innerHTML;
			//alert(content[i].innerHTML +'\t'+ content[i + 1].innerHTML);
		}
		//alert(contents);
		var xhr = new XMLHttpRequest();
		xhr.onreadystatechange = function(){
			if (xhr.readyState === 4) {
				//respoce recived
				
				var res = xhr.responseText;
				
				if(res != ' ' || res != ''){
					
					var link = document.createElement('a');
					link.style.display = "none";
					link.setAttribute('download','');
					link.href=res;
					
					link.click();
					link.remove();
				}
			
            }
			
		}
        xhr.open("POST",'luufile.php',true);
		xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
		
		xhr.send(JSON.stringify({"name":'<?php echo $_REQUEST['file']; ?>',"data":contents }));
	}
	
</script>

</body>
</html>

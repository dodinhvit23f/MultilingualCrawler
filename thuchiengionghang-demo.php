<?php
	#error_reporting(0);
	//date_default_timezone_set('Asia/Ho_Chi_Minh');
	
	//echo $today;
 ?>
<!DOCTYPE html>
<html>
<head>
	<title>Thực hiện gióng hàng</title>
	<meta charset='UTF-8'>
	<script>
	
		function dowload_file(item, tag, uri){
					var string = item.value.split("&")
					tag.href = uri;
					tag.click();
					setTimeout(function(){
					console.log("Download slowly");	
		}, 1500);
		}
		
		function dowload_all_file(child_class, _case){
			var checkboxes = document.getElementsByClassName(child_class);
			
			var link = document.createElement("a");
			link.style.display = "none";	
			link.setAttribute('download', '');
			
			document.body.appendChild(link);			
			for(var i = 0; i < checkboxes.length; i++){
				if(_case == 1){
					var string = checkboxes[i].value.split("&")
					dowload_file(checkboxes[i],link,string[0]);
					dowload_file(checkboxes[i],link,string[1]);
				} 
				if(_case == 0){
					//alert(checkboxes[i].value);
					dowload_file(checkboxes[i], link, checkboxes[i].value);
				}
			}
			
			link.remove();
		}
	
		function download_file_checked(child_class, _case){
			var checkboxes = document.getElementsByClassName(child_class);
			/*var frame = document.getElementById("download_iframe");
			var xhr = new XMLHttpRequest();
			xhr.responseType = 'blob';
				for(var i = 0; i < checkboxes.length; i++){
					if(checkboxes[i].checked){
						var string = checkboxes[i].value.split("&")
						xhr.open('GET',"./crawl_ted_talk_success_TH2/" + string[0],true);
						xhr.send();
						
						xhr.open('GET',"./crawl_ted_talk_success_TH2/" + string[1],true);
						xhr.send();
						//alert(checkboxes[i].value);
					}
				}
				*/
			var link = document.createElement("a");
			link.style.display = "none";	
			link.setAttribute('download', '');
			
			document.body.appendChild(link);			
			for(var i = 0; i < checkboxes.length; i++){
				if(checkboxes[i].checked){
					if(_case == 1){
								
						var string = checkboxes[i].value.split("&")
						dowload_file(checkboxes[i],link, string[0]);
						dowload_file(checkboxes[i],link, string[1]);
					} 
					
					if(_case == 0){
						dowload_file(checkboxes[i],link,"./" + checkboxes[i].value);
					}
				}
			}
			
			link.remove();
		}
		
		
		function setCheckedCheckBox(item){
			if(item != null){
				item.checked = true;
			}
		}
		
		function checkAllCheckBox(id,child_class){
			
			var checkAllButton = document.getElementById(id);
			
			if(checkAllButton.checked){
				
				var checkboxes = document.getElementsByClassName(child_class);
				var lim = checkboxes.length;
				
				for(var i = 0; i < lim; i++){
					checkboxes[i].checked = true;
					
					//setCheckedCheckBox(checkboxes[i]);
				}
				
			}
			
		}
		
		
	
	</script>
</head>
<body>
<iframe id="download_iframe" style="display:none;"><head> <meta charset="UTF-8"> </head></iframe>
<div style="width: 100%;height:100px;background:#gray;" align="center">
	<h1 style="color: #304499;">Công cụ hỗ trợ soạn thảo ngữ liệu song ngữ</h1>
</div>
<div style="width: 100%;height: 50px;background:gray;">
	<ul style="display: inline-block;"class="menu">
		<li style="list-style: none;float: left;height: 50px;width: 100px;text-align: center;margin-top: -15px;"><a href="index.html" style="text-decoration: none;line-height: 50px;color: white;">Trang Chủ</a></li>
		<li style="list-style: none;float: left;height: 50px;width: 150px;text-align: center;margin-top: -15px;"><a href="solieuthongke.html" style="text-decoration: none;line-height: 50px;color: white;">Thống kê ngữ liệu</a></li>
		<li style="list-style: none;float: left;height: 50px;width: 150px;text-align: center;margin-top: -15px;"><a href="gionghangvb.html" style="text-decoration: none;line-height: 50px;color: white;">Gióng hàng văn bản</a></li>
		<li style="list-style: none;float: left;height: 50px;width: 150px;text-align: center;margin-top: -15px;"><a href="gionghangcau.html" style="text-decoration: none;line-height: 50px;color: white;">Gióng hàng câu</a></li>
	</ul>
<style type="text/css">
.menu li:hover{
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
	<div style="margin-left: 29%;">
		<button class="export" id="extract-vb" onclick="">Extract Văn Bản</button>
		<button class="export" id="extract-cau" onclick="">Extract Câu song ngữ</button>
	</div>
	
</div>

	<div class="modal" id="modal_ghvb">
		<table class="modal-table">
			<tr>
				<th style="width: 3%;"><input id="btncheck_vb" type="checkbox" onclick="checkAllCheckBox('btncheck_vb','checkbox_child_1')" name=""></th>
				<th style="width: 35%;"><?php echo $_POST['src_lang']; ?></th>
				<th style="width: 35%;"><?php echo $_POST['tgt_lang']; ?></th>
				<th style="width: 5%;">Độ đo</th>
				<th style="width: 10%;">Edit</th>
				<th style="width: 10%;">Gióng Hàng</th>
			</tr>
			<?php
				
				$hadFile = true;
				
				if(!isset($_REQUEST['file'])){
					
					$hadFile = false;
					
				}
				
				
					
				if($hadFile):
					
					$files = $_REQUEST['file'];	
					foreach ($files as  $file ): ?>
					
					<tr>
						
						<td><input class="checkbox_child_1 ckb_child" type="checkbox" value="<?php print($file[0]);
						echo "&";
						echo $file[2]; ?>" name="name2"></td>
						<td style="text-align:left;"> 
							<a href="<?php echo $file[0]; ?>" download>
								<?php echo $file[1]; ?>
							</a> 
						</td>
						<td style="text-align:left;">  <a href="./<?php echo $file[2]; ?>" download>
								<?php echo $file[3]; ?>
								</a> 
						</td>
						<td>0.2</td>
						<td><button style="width: 40%;height: 30px;" id="detele"class="btncon">Xoá</button>
							<button style="width: 40%;height: 30px;margin-left:10px;"id="edit" onclick="popupOpen()" class="btncon">Edit</button>
						</td>
						<td><button class="btncon-gh" id="gionghang1" class="btncon">Gióng hàng</button></td>
					</tr>
				<?php 
					endforeach;
				endif
				
				?>
		</table>
		<div class="phantrang">
		<p>
			<input type="text" placeholder="1 - 2"  class="input1">       
				<a  href="xuly.php?web=<?php echo $_REQUEST['web']; ?>&src_lang=<?php echo $_REQUEST['src']; ?>&tgt_lang=<?php echo $_REQUEST['tgt']; ?>&page=<?php echo $_REQUEST['prev_page'];?>" style="font-weight: bold; width: 150px;text-decoration: none; ">
					<span aria-hidden="true" id="">←</span> Trước
				</a>
				<a href="xuly.php?web=<?php echo $_REQUEST['web']; ?>&src_lang=<?php echo $_REQUEST['src']; ?>&tgt_lang=<?php echo $_REQUEST['tgt']; ?>&page=<?php echo $_REQUEST['next_page'];?>" style="font-weight: bold; width: 150px;text-decoration: none;">Sau
					<span aria-hidden="true">→</span>
				</a>
				<button class="export-data" id="export-data" onclick="download_file_checked('checkbox_child_1',1)" > Export Data</button>
				<button class="export-data" id="export-all" onclick="dowload_all_file('checkbox_child_1',1) ">Save All</button>
		</p>           
	</div>
	</div>
	<div style="margin: 1% 3% 0% 3%; width: 100%;display: none;" id="modal_cau">
		<table style="width: 90%;height: auto;text-align: center;font-size: 18px;margin-top: 15px;">
			<tr>				
				<th style="width: 3%;"><input id="btncheck_cau" class="checkbox_child" type="checkbox" onclick="checkAllCheckBox('btncheck_cau','checkbox_child')" name=""></th>
				<th colspan='2' style="width: 35%;"><?php echo $_POST['src_lang']; ?></th>
				
				<th style="width: 5%;">Độ đo</th>
				<th style="width: 10%;">Edit</th>
				
			</tr>
			
			<?php
				$align_files = $_REQUEST['align_file'];
								
				if(!isset($align_files)){
					return;
				}
				foreach ($align_files as  $file_path=> $file_name ): 
			?>
			<tr>
				<td><input class="checkbox_child ckb_child" type="checkbox" value="<?php echo $file_path; ?>" name="name2"></td>
				<td colspan="2" style="text-align:left;"> 
					<a href="giongcau.php?file=<?php echo $file_path;?>&src_lang=<?php echo $_POST['src_lang']; ?>&tgt_lang=<?php echo $_POST['tgt_lang']?>" target="_blank">
						<?php echo $file_name; ?>
					</a> 
				</td>
				
				<td>0.2</td>
				<td>
					<button style="width: 40%;height: 30px;" id="detele"class="btncon">Xoá</button>
					<button style="width: 40%;height: 30px;margin-left:10px;"id="edit"onclick="popupOpen()"class="btncon">Edit</button>
				</td>
				
			<tr>
			<?php if(!isset($align_files)){
					return;
				}
				endforeach 
			?>
	</table>
	<div class="phantrang">
		<p>
			<input type="text" placeholder="1 - 2"  class="input1">        
				<a  href="xuly.php?web=<?php echo $_REQUEST['web']; ?>&src_lang=<?php echo $_REQUEST['src']; ?>&tgt_lang=<?php echo $_REQUEST['tgt']; ?>&page=<?php echo $_REQUEST['prev_page'];?>" style="font-weight: bold; width: 150px;text-decoration: none; ">
					<span aria-hidden="true" id="">←</span> Trước
				</a>
				<a href="xuly.php?web=<?php echo $_REQUEST['web']; ?>&src_lang=<?php echo $_REQUEST['src']; ?>&tgt_lang=<?php echo $_REQUEST['tgt']; ?>&page=<?php echo $_REQUEST['next_page'];?>" style="font-weight: bold; width: 150px;text-decoration: none;">Sau
					<span aria-hidden="true">→</span>
				</a>
				<button class="export-data" id="export-data" onclick="download_file_checked('checkbox_child',0)" > Export Data</button>
				<button class="export-data" id="export-all" onclick="dowload_all_file('checkbox_child',0) ">Save All</button>
				<button class="export-data">Checks Exist</button>
		</p>           
	</div>         
	</div>
	</div>
</div>
	<div class="modal-dialog" id="popup" style="top:100px;display:none;position:fixed;z-index:100;width:70%;background-color: #BDBDBD">
					<div class="modal-content">
						<div class="modal-header" style="height: 100px;">
							<button type="button" onclick="popupClose()" data-dismiss="modal" style="margin-top: 3px;margin-bottom: 30px;">×</button>
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
											<option value="tourism">Tourism</option>
											<option value="law_commercial">Commercial law</option>
											<option value="ja_culture">Japanese culture</option>
											<option value="law_investiment">Investment law</option>
											<option value="law_tourism">Tourism law</option>
											<option value="other_topic">Other topics</option>
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
								<div class="col-md-6">
									<div class="row" style="font-weight: bold; font-size: 18px;">Vietnamese</div>
									<div class="row">
										<label for="field2">
											<!-- <textarea rows="10" cols="49.8" 
											style="max-width: 100%; color: black;" 
											name="vietnamese_sentence_{{_id}}">{{#if vnSentenceEdited}}{{vnSentenceEdited}}{{else}}{{vietnamese_sentence}}{{/if}}</textarea> -->

											<!-- comment to remove redundant spaces -->
											<div id="vietnamese_sentence_ctmL6RA47mkLvRFaT" style="width: 465px; max-width: 100%; color: black; border: 1px solid black; height: 206px; font-weight: normal; padding: 5px; overflow-y: auto;" contenteditable="true"><!--
											--><!-- 
												--><!-- 
													--><!--
														--><span style="color: black;">Tiếp tục khắc phục hậu quả bão lũ ở các tình miền Trung.</span><!--
													--><!-- 
												--><!-- 
											--><!--
										 --></div>
										</label>
									</div>
								</div>

								<div class="col-md-6">
									<div class="row" style="font-weight: bold; font-size: 18px;">Khmer</div>
									<div class="row">
										<label for="field2">
											<!-- <textarea rows="10" cols="49.8" 
											style="max-width: 100%; color: black;" 
											name="japanese_sentence_{{_id}}">{{#if jpSentenceEdited}}{{jpSentenceEdited}}{{else}}{{japanese_sentence}}{{/if}}</textarea> -->
											
											<!-- comment to remove redundant spaces -->
											<div id="japanese_sentence_ctmL6RA47mkLvRFaT" style="width: 465px; max-width: 100%; color: black; border: 1px solid black; height: 206px; font-weight: normal; padding: 5px; overflow-y: auto;" contenteditable="true"><!--
											--><!-- 
												--><!-- 
													--><!--
														--><span style="color: black;">បន្តសកម្មភាពជំនះពុះពារនូវផលវិបាកបណ្តាមកពីព្យុះនិងទឹកជំនន់នៅតំបន់ភាគកណ្តាលវៀតណាម</span><!--
													--><!-- 
												--><!-- 
											--><!--
										 --></div>																																	
										</label>
									</div>
								</div>
							</div>
							<div class="row">
								<div class="col-md-8">
									<button type="submit" class="btn-save-edit btn btn-primary btn-lg center-block" data-dismiss="modal" style="width: 200px; margin-top: 25px; 
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
	function chonDLgoc (){
		document.getElementById("dlcs1").checked = false;
		document.getElementById("data-exsit").disabled = false;
		document.getElementById("urlnn1").disabled = true;
		document.getElementById("urlnn2").disabled = true;
	}
	function chonDLkhac (){
		document.getElementById("dlcs").checked = false;
		document.getElementById("data-exsit").disabled = true;
		document.getElementById("urlnn1").disabled = false;
		document.getElementById("urlnn2").disabled = false;
	}
	document.getElementById("extract-vb").onclick = function(){
		document.getElementById("modal_ghvb").style.display = "block";
		document.getElementById("modal_cau").style.display = "none";
		
	}
	document.getElementById("extract-cau").onclick = function(){
		document.getElementById("modal_ghvb").style.display = "none";
		document.getElementById("modal_cau").style.display = "block";
		
	}
	/*
	document.getElementById("btncheck").onclick = function(){

		var checkboxes = document.getElementsByName('name[]');
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
	}
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
	 function popupOpen() {
	
	document.getElementById("popup").style.display = "block";
		
	document.getElementById("overlay").style.display = "block";
		
	}
		
	// Popup Close
		
	function popupClose() {
		
	document.getElementById("popup").style.display = "none";
		
	document.getElementById("overlay").style.display = "none";
		
	}
	*/
	
</script>
</body>
</html>

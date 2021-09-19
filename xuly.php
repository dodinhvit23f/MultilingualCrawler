
<?php 
	#error_reporting(0);
	
	function findFileWithArrayString($output, $cdir,$path_){
		$array = array();
		foreach($cdir as $key => $value){
			//echo $key ;
			if(strcmp($value,".")==0){
				continue;
			}
			
			if(strcmp($value,"..")==0){
				continue;
			}
			
			foreach($output as $path){
				
				if((!is_int(strpos($value, $path))) === false ){
					array_push( $array, sprintf("%s%s",$path_,$value) );
					break;						
				}	
			}
			
		}		
		return $array; 		
	}
	
	function FindAllFileInFolder($folder, &$file , $start, $end , & $current){
		
		$array_folder = array();
		if($handle = opendir($folder)){
					
			while (false != ($entry = readdir($handle))) {
				#print($entry);
				array_push($array_folder,$entry);

				if($entry != "." && $entry != ".."){
					
					if(strpos($entry, ".txt") != false){
						
						
						if($start <= $current && $current < $end){
							$file["$folder/$entry"] = $entry;
							
						}
						
						$current = $current + 1;
					}else{					
						FindAllFileInFolder("$folder/$entry", $file, $start, $end , $current);						
					}
					
					
				}
				
			}
			closedir($handle);
	
			#print_r($folders);
			
			foreach ( $array_folder as $f){
				$f = trim($f);
				if ($f == "" || $f == " "){
					continue;
				}
							
				if($f != "." && $f != ".."){
					
					
					if(strpos($f, ".txt") != false){
						
						
						if($start <= $current && $current < $end){
							$file["$folder/$f"] = $f;
							#echo($f);
							#echo("<br>");
						}
						
						$current = $current + 1;
					}else{	
						if ($f != "" || $f != " "){
							FindAllFileInFolder("$folder/$f", $file, $start, $end , $current);
						} 
												
					}
					
					
				}
			}
		}
		
	}
	
	function AlignFile($dictionary, $src_lang ){
		
		$array_src = array();
		$array_tgt = array();
		
		
		foreach ($dictionary as $file_path => $file_name){
			#print_r($dictionary);
			#print("<br/>");
			if(strpos($file_name, "$src_lang.txt") != false){
				$array_src[$file_path] = $file_name;
			}else{
				$array_tgt[$file_path] = $file_name;			
			}
			
		}
		
		$file = array();
		
		foreach ($array_src as $src_file_path => $src_file_name){
			
			$name = str_replace("$src_lang.txt","",$src_file_name);
			
			foreach ($array_tgt as $tgt_file_path => $tgt_file_name){
				
				if( strpos($tgt_file_name, $name) !== false ){
					#print($tgt_file_name);
					#print(" ");
					#print(strpos($tgt_file_name, $name));
					#print("<br/>");
					array_push($file, array($src_file_path, $src_file_name, $tgt_file_path, $tgt_file_name) );
					break;
				}
			}
		}
		return $file;
	}
	
	function VovCase($src_lang, $tgt_lang, $start, $end , &$cur){
		
		$document = sprintf("Data/crawler_success/Vov/%s-%s/Document/",$src_lang,$tgt_lang);
		$sentence = sprintf("Data/crawler_success/Vov/%s-%s/Sentence/",$src_lang,$tgt_lang);
		
		$files_document = array();
		$cur = 0;
		FindAllFileInFolder($document, $files_document, $start, $end , $cur);
		
		if (!is_dir($document)) {
			print("Ngôn Ngữ Tìm Kiếm Không Tồn Tại") ;
			return;
		}
		
		if(!isset($files_document)){
			FindAllFileInFolder($document, $files_document, $start, $end , $cur);
		}
		
		$files_document =  AlignFile($files_document, $src_lang);
		#print_r($files_document);
		$cur = 0;
		$files_align = array();
		FindAllFileInFolder($sentence,$files_align, $start, $end, $cur);
		
		return array($files_document, $files_align);		
	}
	
	function TedCase($src_lang, $tgt_lang, $start, $end, $cur){
		$file = array();
		$align_file = array();
		
		$output = null;
		#echo "python crawl_ted_transcript.py --src_lang ".'"'.$src_lang.'"'." --tgt_lang ".'"'.$tgt_lang.'"'." 2>&1";
		#exec("python VovCrawl.py --src_lang ".'"'.$src_lang.'"'." --tgt_lang ".'"'.$tgt_lang.'"'." 2>&1",$output);
		
		$document = sprintf("Data/crawler_success/TedTalk/%s-%s/Document/",$src_lang,$tgt_lang);
		$sentence = sprintf("Data/crawler_success/TedTalk/%s-%s/Sentence/",$src_lang,$tgt_lang);
		
		if (!is_dir($document)) {
			print("Ngôn Ngữ Tìm Kiếm Không Tồn Tại");
			return;
		}
		
		$files_document = array();
		$cur = 0;
		FindAllFileInFolder($document, $files_document, $start, $end , $cur);
		
		if(!isset($files_document)){
			exec("python crawl_ted_transcript.py --src_lang ".'"'.$src_lang.'"'." --tgt_lang ".'"'.$tgt_lang.'"'." 2>&1",$output);
			FindAllFileInFolder($document, $files_document, $start, $end , $cur);
		}
		
		$files_document =  AlignFile($files_document, $src_lang);
		$cur = 0;
		$files_align = array();
		FindAllFileInFolder($sentence,$files_align, $start, $end, $cur);
		
		return array($files_document, $files_align);				
		
	}
	
	function VnanetCase($src_lang, $tgt_lang , $start, $end, $cur){
		$file = array();
		$align_file = array();
		
		$output = null;
		#echo "python crawl_ted_transcript.py --src_lang ".'"'.$src_lang.'"'." --tgt_lang ".'"'.$tgt_lang.'"'." 2>&1";
		#exec("python crawl_ted_transcript.py --src_lang ".'"'.$src_lang.'"'." --tgt_lang ".'"'.$tgt_lang.'"'." 2>&1",$output);
		
		$document = sprintf("Data/crawler_success/Vnanet/%s-%s/Document/",$src_lang,$tgt_lang);
		$sentence = sprintf("Data/crawler_success/Vnanet/%s-%s/Sentence/",$src_lang,$tgt_lang);
		
		if (!is_dir($document)) {
			return;
		}
		
		$files_document = array();
		$cur = 0;
		FindAllFileInFolder($document, $files_document, $start, $end , $cur);
		
		if(!isset($files_document)){
			exec("python VnanetCrawl.py --src_lang ".'"'.$src_lang.'"'." --tgt_lang ".'"'.$tgt_lang.'"'." 2>&1",$output);
			FindAllFileInFolder($document, $files_document, $start, $end , $cur);
		}
		
		$files_document =  AlignFile($files_document, $src_lang);
		$cur = 0;
		$files_align = array();
		FindAllFileInFolder($sentence,$files_align, $start, $end, $cur);
		
		return array($files_document, $files_align);				
		
	}
	
	function VietNamPlusCase($src_lang, $tgt_lang){
		$file = array();
		$align_file = array();
		
		$output = null;
		#echo "python crawl_ted_transcript.py --src_lang ".'"'.$src_lang.'"'." --tgt_lang ".'"'.$tgt_lang.'"'." 2>&1";
		#exec("python crawl_ted_transcript.py --src_lang ".'"'.$src_lang.'"'." --tgt_lang ".'"'.$tgt_lang.'"'." 2>&1",$output);
		
		$document = sprintf("Data/crawler_success/VietNamPlus/%s-%s/Document/",$src_lang,$tgt_lang);
		$sentence = sprintf("Data/crawler_success/VietNamPlus/%s-%s/Sentence/",$src_lang,$tgt_lang);
		
		if (!is_dir($document)) {
			print("Ngôn Ngữ Tìm Kiếm Không Tồn Tại");
			return;
		}
		
		$files_document = array();
		$cur = 0;
		FindAllFileInFolder($document, $files_document, $start, $end , $cur);
		
		if(!isset($files_document)){
			FindAllFileInFolder($document, $files_document, $start, $end , $cur);
		}
		
		$files_document =  AlignFile($files_document, $src_lang);
		$cur = 0;
		$files_align = array();
		FindAllFileInFolder($sentence,$files_align, $start, $end, $cur);
		
		return array($files_document, $files_align);				
		
	}
	
	function CoVietCase(){
		$file = array();
		$align_file = array();
		
		$output = null;
		#echo "python crawl_ted_transcript.py --src_lang ".'"'.$src_lang.'"'." --tgt_lang ".'"'.$tgt_lang.'"'." 2>&1";
		#exec("python crawl_ted_transcript.py --src_lang ".'"'.$src_lang.'"'." --tgt_lang ".'"'.$tgt_lang.'"'." 2>&1",$output);
		
		$sentence = sprintf("Data/crawler_success/CoViet/");
		
		$cur = 0;
		$files_align = array();
		FindAllFileInFolder($sentence,$files_align, 0, 10, $cur);
		
		return array(array(), $files_align);				
		
	}
	
	function KhmerboiCase(){
		$file = array();
		$align_file = array();
		
		$output = null;
		#echo "python crawl_ted_transcript.py --src_lang ".'"'.$src_lang.'"'." --tgt_lang ".'"'.$tgt_lang.'"'." 2>&1";
		#exec("python crawl_ted_transcript.py --src_lang ".'"'.$src_lang.'"'." --tgt_lang ".'"'.$tgt_lang.'"'." 2>&1",$output);

		$sentence = sprintf("Data/crawler_success/Khmerboi/");
		
		
		$cur = 0;
		$files_align = array();
		FindAllFileInFolder($sentence,$files_align, 0, 10, $cur);
		
		return array( array() , $files_align);				
		
	}

	if(isset($_REQUEST)){
		
		
		
		$src_lang = $_REQUEST['src_lang'];
		$tgt_lang = $_REQUEST['tgt_lang'];
		
		$src = $_REQUEST['src_lang'];
		$tgt = $_REQUEST['tgt_lang'];
		
		$web = $_REQUEST['web'];
		
		$page = isset($_REQUEST['page'])? $_REQUEST['page'] - 1: 0;
		
		if($page < 0){
			return;
		}
		
		$number_of_record = 20;
		$start = $page * $number_of_record;
		$end = $start + $number_of_record;
		$cur = 0 ;
		
		if(empty($src_lang)){
			header('Location:index.html');
			exit();
		}
		
		if(empty($tgt_lang)){
			header('Location:index.html');
			exit();
		}
		
		if(empty($web)){
			header('Location:index.html');
			exit();
		}
		
		date_default_timezone_set("Asia/Ho_Chi_Minh");
		$output = null;
		
		$file = array();
		$align_file = array();
		
		$today = date("dmyyHis"); 
		
		if(strcmp($web,"ted")==0){
			
			$array = TedCase($src_lang, $tgt_lang, $start, $end, $cur);
			
			$file = $array[0];
			$align_file = $array[1];
		}
		
		
		if(strcmp($web,"vov")==0){
			
			$array = VovCase($src_lang, $tgt_lang, $start, $end, $cur);
			
			$file = $array[0];
			$align_file = $array[1];
		}
		
		
		if(strcmp($web,"para")==0){
			echo "chức năng hiện đang bảo trì";
		}
		
		if(strcmp($web,"vnanet")==0){
			$array = VnanetCase($src_lang, $tgt_lang, $start, $end, $cur);
			
			$file = $array[0];
			$align_file = $array[1];
		}
		
		if(strcmp($web,"vietnamplus")==0){
			$array = VietNamPlusCase($src_lang, $tgt_lang, $start, $end, $cur);
			
			$file = $array[0];
			$align_file = $array[1];
		}
		
		if(strcmp($web,"khmerboi")==0){
			$array = KhmerboiCase();
			
			$file = $array[0];
			
			$align_file = $array[1];
			
		}
		
		if(strcmp($web,"coviet")==0){
			$array = CoVietCase($src_lang, $tgt_lang, $start, $end, $cur);
			
			$file = $array[0];
			$align_file = $array[1];
		}
		//print_r($file['sir_ken_robinson_bring_on_the_learning_revolution-vi']);
		
		if(empty($align_file)){
			header('Location:index.html');
			exit();
		}
		
		switch ($src_lang){
			case "lo":
				$src_lang = "Lào";
				break;
			case "zh":
				$src_lang = "Trung Quốc";
				break;
			case "km":
				$src_lang = "Khnmer";
				break;
			case "kh":
				$src_lang = "Khnmer";
				break;	
			case "vi":
				$src_lang = "Việt Nam";
				break;
			case "en":
				$src_lang = "Tiếng Anh";
				break;				
		}
		
		
		
		switch ($tgt_lang){
			case "lo":
				$tgt_lang = "Lào";
				break;
			case "zh":
				$tgt_lang = "Trung Quốc";
				break;
			case "km":
				$tgt_lang = "Khnmer";
				break;
			case "kh":
				$tgt_lang = "Khnmer";
				break;		
			case "vi":
				$tgt_lang = "Việt Nam";
				break;
			case "en":
				$tgt_lang = "Tiếng Anh";	
				break;
		}
		
		$max_page = ($cur / $number_of_record) + 1 ;
		
		
		
		if($page < $max_page){
		
			$next_page = $page + 2;
		}
		else{
			$next_page = $page + 1;
		}
		
		if($page <= 0){
			$prev_page  = 1;
		}else{
			$prev_page = $page;
		}
		
		
		
		$foldername = explode("/",$_SERVER['REQUEST_URI'])[1];	
		$url= "http://". $_SERVER['SERVER_NAME'].":$_SERVER[SERVER_PORT]"."/".$foldername .'/thuchiengionghang-demo.php';
		
		
		
		$data = array('file' => $file
						,'align_file' => $align_file
						,'src_lang' => $src_lang
						,'tgt_lang'=> $tgt_lang
						,'next_page' => $next_page
						,'prev_page' => $prev_page
						,'max_page' => $max_page
						,'src' => $src
						,'tgt' => $tgt
						,'web' => $web);

		
		$options = array(
			'http' => array(
				'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
				'method'  => 'POST',
				'content' => http_build_query($data)
			)
		);
		
		$context  = stream_context_create($options);
		$result = file_get_contents($url, false, $context);
		if ($result === FALSE) { 
			echo "khong co trang ";
		}
		
		echo($result);
		
	}
?>
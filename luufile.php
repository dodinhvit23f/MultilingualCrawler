<?php
	if(isset($_POST)){
		$inputJSON = file_get_contents('php://input');
		
		if(!empty($inputJSON)){
			$input = json_decode($inputJSON,true);
			if (file_exists($input['name'])) {
				
				$array = explode("/",$input['name']);
				
				$filename = sprintf("%s/%d-%s",$array[0],time(),$array[1]);
				
				$myfile = fopen($filename, "a");
				fwrite($myfile,$input['data']);
				fclose($myfile);
				echo $filename;
				
				//echo readfile ($input['name']);
				exit;
			}
		}
	}
	
?>
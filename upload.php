<?php
	$target_dir = "./_evaluator/uploads/";
	if (!file_exists($target_dir)) {
		mkdir($target_dir, 0777, true);
	}

	$base_filename = $_FILES["targetFile"]["name"][0];
	$base_file = $target_dir . basename($base_filename);
	$base_pptxFileType = strtolower(pathinfo($base_file, PATHINFO_EXTENSION));

	$modified_filename = $_FILES["targetFile"]["name"][1];
	$modified_file = $target_dir . basename($modified_filename);
	$modified_pptxFileType = strtolower(pathinfo($modified_file, PATHINFO_EXTENSION));

	$uploadOk = 1;

	// Check if file already exists
	// if (file_exists($target_file)) {
	// 	echo "Sorry, file already exists.<br>";
	// 	$uploadOk = 0;
	// }

	// Check file size
	if ($_FILES["targetFile"]["size"][0] > 500000 && $_FILES["targetFile"]["size"][1] > 500000) {
		echo "Sorry, either or both your files are too large.<br>";
		$uploadOk = 0;
	}

	// Allow certain file formats
	if($base_pptxFileType != "pptx" && $modified_pptxFileType != "pptx") {
		echo "Sorry, only PPTX files is allowed.<br>";
		$uploadOk = 0;
	}

	// Check if $uploadOk is set to 0 by an error
	if ($uploadOk == 0) {
		echo "Sorry, your file was not uploaded.<br>";
	}

	// if everything is ok, try to upload file
	else {
		if (move_uploaded_file($_FILES["targetFile"]["tmp_name"][0], $base_file)) { echo "The file ". basename($base_filename). " has been uploaded.<br>"; }
		else { echo "Sorry, there was an error uploading ".basename($_FILES["targetFile"]["name"]).".<br>"; }

		if (move_uploaded_file($_FILES["targetFile"]["tmp_name"][1], $modified_file)) { echo "The file ". basename($modified_filename). " has been uploaded.<br>"; }
		else { echo "Sorry, there was an error uploading ".basename($_FILES["targetFile"]["name"]).".<br>"; }

		//echo "cmd$: ".("/Library/Frameworks/Python.framework/Versions/3.7/bin/python3 ./_evaluator/main.py --unpack \"".$base_filename.":".$modified_filename."\" --texts --colors --images --videos --animations <br>");
		$output_unpack = shell_exec("/Library/Frameworks/Python.framework/Versions/3.7/bin/python3 ./_evaluator/main.py --unpack \"".$base_filename.":".$modified_filename."\" --texts --colors --images");
		echo ($output_unpack."<br>");

		// Check if the Modified PPT is following the guideline using the computation for checking.
		$checked_color = json_decode(file_get_contents("./_evaluator/scores/colors-checker-v3.json"), true);
		$checked_image = json_decode(file_get_contents("./_evaluator/scores/images-checker-v3.json"), true);
		$checked_text = json_decode(file_get_contents("./_evaluator/scores/texts-checker-v3.json"), true);
		
		// Checking computation: ‘Use bold, italics, or underline sparingly’.
		if ($checked_text['used_bold_italic_underlined_sparingly_all'] == false) {
			echo "<br><b>Error: Use bold, italics, and underline sparingly.<b>";
			echo "<script>window.location.href = 'error-used_bold_italic_underlined_sparingly_all.php'</script>";
		}
		else if ($checked_color['use_additional_color_for_emphasis_all'] == false || $checked_color['used_contrasting_colors_between_text_and_background'] == false) {
			echo "<br><b>Error: Use additional color in text for emphasis. Use contrasting colors.<b>";
			echo "<script>window.location.href = 'error-use_additional_color_for_emphasis_all.php'</script>";
		}
		else if ($checked_image['used_no_more_than_2_images_per_slide'] == false) {
			echo "<br><b>Error: Use no more than 2 images per slide.<b>";
			echo "<script>window.location.href = 'error-used_no_more_than_2_images_per_slide.php'</script>";
		}
		else if (strpos($output_unpack, 'DONE') > 0) {
			// proceed with summarize trigger
			$output_summarize = shell_exec("/Library/Frameworks/Python.framework/Versions/3.7/bin/python3 ./_evaluator/main.py --summarize \"".$base_filename.":".$modified_filename."\"");
			echo ($output_summarize."<br>");
			if (strpos($output_summarize, 'DONE') > 0) {
				echo "<br>redirect to <a href=\"results.php\">results</a> page";
				echo "<script>window.location.href = 'results.php'</script>";
			}
			else
			echo "<script>window.location.href = 'error.php'</script>";

		}
	}
?>
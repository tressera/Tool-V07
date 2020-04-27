<!DOCTYPE html>
<html lang="en">

<head>

<?php include('imports/head.php') ?>

</head>

<body>

    <!--*******************
        Preloader start
    ********************-->

    <!--
    <div id="preloader">
        <div class="loader"></div>
    </div>
    -->

    <!--*******************
        Preloader end
    ********************-->


    <!--**********************************
        Main wrapper start
    ***********************************-->
    <div id="main-wrapper">

        <!--**********************************
            Nav header start
        ***********************************-->



        <!--**********************************
            Nav header end
        ***********************************-->

        <!--**********************************
            Header start
        ***********************************-->

        <!--**********************************
            Header end ti-comment-alt
        ***********************************-->

        <!--**********************************
            Sidebar start
        ***********************************-->



        <!--**********************************
            Sidebar end
        ***********************************-->

        <!--**********************************
            Content body start
        ***********************************-->
        <div class="content-body c-body-1">


            <div class="container-fluid">

                <div class="row">

                    <div class="col-12">
                    <!--<span class="brand-title"><b><img src="../assets/images/Logo.png" width="375px;" height="175px;"></b></span>-->
                    </div>

                </div>

                <div class="row justify-content-between mb-3 header-01">
					<div class="card-body col-12 text-center">
						<h2 class="page-heading-01">Learning Improvement Prediction Tool</h2>
						<h5 class="p-header">A tool that will predict learning improvement based on the Powerpoint Presesentation design enhancements.
                        </h5>
					</div>
                </div>

                <div class="col-xl-6 col-xxl-12 pads-4-left-right-2-top-bottom">
                    <div class="card ">
                        <div class="card-header pads-top-left">
                        <h3 class="text-center font-g">RESULTS</h3>


                        </div>
                        <div class="card-body">
                            <div class="row">

                                <div class="col-lg-4 mb-4 pads-2-left-right-2-top-bottom">
                                    <img src="assets/images/lipt-font.png" class="center-img">
                                    <h5 class="text-center font-g">
                                        <br>Font
                                    </h5>
                                    <?php
                                        $texts_scores = file_get_contents("./_evaluator/scores/texts-checker-v3.json");
                                        $json_a = json_decode($texts_scores, true);
                                    ?>
                                    
                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["used_large_fonts_all"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Used large fonts.
                                    </p>
                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["used_3_font_sizes_only"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Used 3 sizes at most
                                    </p>
                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["used_sans_serif_all"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Used sanserif fonts
                                    </p>
                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["used_2_fonts_only"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Used one or two fonts at most
                                    </p>
                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["used_bold_italic_underlined_sparingly_all"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Used bold, italics, or underlines sparingly
                                    </p>
                                    
                                </div>

                                    

                                <div class="col-lg-4 mb-4 pads-2-left-right-2-top-bottom">
                                    <img src="assets/images/lipt-color.png" class="center-img">
                                    <h5 class="text-center font-g">
                                        <br>Color
                                    </h5>
                                    <?php
                                        $texts_scores = file_get_contents("./_evaluator/scores/colors-checker-v3.json");
                                        $json_a = json_decode($texts_scores, true);
                                    ?>

                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["used_3-to-4_colors_only"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Used not more than 4 colors
                                    </p>
                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["used_contrasting_colors_between_text_and_background"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Used contrasting colors between text and background
                                    </p>
                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["use_additional_color_for_emphasis_all"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Used additional color in text for emphasis
                                    </p>
                                    <!--***
                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["avoided_vibrating_color_combinations"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Avoided vibrating color combinations
                                    </p>
                                    **!-->

                                </div>

                                <div class="col-lg-4 mb-4 pads-2-left-right-2-top-bottom">
                                    <img src="assets/images/lipt-image.png" class="center-img">
                                    <h5 class="text-center font-g">
                                        <br>Image
                                    </h5>
                                    <?php
                                        $texts_scores = file_get_contents("./_evaluator/scores/images-checker-v3.json");
                                        $json_a = json_decode($texts_scores, true);
                                    ?>

                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["used_images"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Used images
                                    </p>
                                    <!--***
                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["used_clear_and_high_quality_image"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Used clear and high-quality, relevant images
                                    </p>
                                    **!-->
                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["used_png_or_jpg_images"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Used png or jpg images.
                                    </p>
                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["used_no_more_than_2_images_per_slide"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Used 2 images per slide at most
                                    </p>
                                    <p class="text-left font-g">
                                        <?php
                                            if ($json_a["balanced_image_w_text_els"] == true) { echo '&#9989;'; }
                                            else { echo '&#10060;'; }
                                        ?> Balanced image (size) with text elements.
                                    </p>
                                </div>

                                

                            </div>

                            
                            

                            


                        </div>
                    </div>
                </div>
                <div class="card-body">
                    <div class="row">

                        <div class="col-3">
                        </div>

                        <div class="col-lg-3 mb-4 ">
                            <div class="text-center">
                                <a href="index.php"><button class="btn btn-lipt mb-2 btnp-01">HOME</button></a>
                            </div>
                        </div>
                        <div class="col-lg-3 mb-4 ">
                            <div class="text-center">
                                <a href="check.php"><button class="btn btn-lipt mb-2 btnp-01">CHECK ANOTHER PPT</button></a>
                            </div>
                        </div>

                        <div class="col-3">
                        </div>

                    </div>

                </div>

            </div>

        </div>

        <!-- Modal -->

        <!--**********************************
            Content body end
        ***********************************-->


        <!--**********************************
            Footer start
        ***********************************-->

        <?php include('imports/footer.php') ?>

        <!--**********************************
            Footer end
        ***********************************-->


        <!--**********************************
            Right sidebar start
        ***********************************-->

        <!--**********************************
        ***********************************-->

        <!--**********************************
            Right sidebar end
        ***********************************-->
    </div>
    <!--**********************************
        Main wrapper end
    ***********************************-->

    <!--**********************************
        Scripts
    ***********************************-->

    <?php include('imports/scripts.php') ?>

</body>

</html>